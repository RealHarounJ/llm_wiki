#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏆 AMSR Gold Auto-Trader for MetaTrader 5 (Demo/Paper Trading Mode)
--------------------------------------------------------------------------------
Questo script gestisce l'esecuzione automatica in tempo reale del modello AMSR
(Gold Speculator) su conti di test / demo di MetaTrader 5.
Funzioni principali:
1. Si connette a MT5 e scarica le ultime 100 candele Daily reali dell'Oro (XAUUSD).
2. Calcola la media SMA 20, SMA 50 e lo Z-Score robusto basato su MAD.
3. Scrape delle news RSS per modulare la soglia di ingresso tramite il sentiment.
4. Calcola la dimensione del lotto dinamico per rischiare esattamente $200 per trade.
5. Invia ordini automatici completi di Stop Loss e Take Profit sul server MT5.
6. Esegue un controllo continuo (Kill-Switch) per bloccare tutto se il drawdown
   giornaliero supera la soglia di sicurezza ($1.500 per challenge da $50k).
--------------------------------------------------------------------------------
"""

import os
import sys

# Forza la codifica UTF-8 per l'output sulla console Windows per evitare crash con emoji
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import json
import math
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import MetaTrader5 as mt5

# ==============================================================================
# CONFIGURAZIONE PARAMETRI OPERATIVI
# ==============================================================================
MT5_LOGIN = 10011042813          # ID del conto di trading (demo/reale)
MT5_PASSWORD = "_6XmOxUc"        # Password del conto di trading
MT5_SERVER = "MetaQuotes-Demo"  # Server del broker MT5

SYMBOL = "XAUUSD"               # Simbolo attivo: XAUUSD (Oro spot)
RISK_PER_TRADE_USD = 200.0      # Rischio fisso per trade ($200, pari al 10% del buffer)
KILLSWITCH_LOSS_USD = 1500.0    # Soglia di blocco di sicurezza (4% del conto o $1.500 su challenge da $50k)
MAGIC_NUMBER = 888168           # Magic Number unico per tracciare le posizioni del bot AMSR

# NOTIFICHE TELEGRAM (FACOLTATIVE)
# Per attivare, crea un bot con @BotFather e ottieni il tuo Chat ID da @userinfobot
TELEGRAM_TOKEN = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"              # Token del bot Telegram dell'utente
TELEGRAM_CHAT_ID = "715100445"            # Chat ID di Telegram dell'utente

Z_THRESHOLD = 1.0               # Soglia di Z-Score base
robust_period = 20

# Liste sentiment quantitativo
BULLISH_WORDS = ["inflation", "recession", "crisis", "cut", "cuts", "war", "geopolitical", "uncertainty", "stimulus", "safe-haven"]
BEARISH_WORDS = ["recovery", "growth", "hike", "hikes", "hawkish", "tightening", "strong", "usd", "yields", "dollar"]

# ==============================================================================
# GESTIONE STATO PERSISTENTE (PRODUCTION-GRADE)
# ==============================================================================
STATE_FILE = "data/amsr_bot_state.json"

def load_bot_state():
    default_state = {
        "last_updated": "",
        "daily_date": "",
        "daily_pnl": 0.0,
        "daily_trades_count": 0,
        "last_trade_time": 0.0,
        "active_trade_ticket": None
    }
    # Crea la directory data se non esiste
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    if not os.path.exists(STATE_FILE):
        save_bot_state(default_state)
        return default_state
    try:
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            state = json.load(f)
            # Reset delle statistiche giornaliere al cambio di data
            today_str = datetime.now().strftime("%Y-%m-%d")
            if state.get("daily_date") != today_str:
                state["daily_date"] = today_str
                state["daily_pnl"] = 0.0
                state["daily_trades_count"] = 0
                save_bot_state(state)
            return state
    except Exception as e:
        print(f"⚠️ Errore nel caricamento dello stato locale: {e}. Uso lo stato predefinito.")
        return default_state

def save_bot_state(state):
    try:
        state["last_updated"] = datetime.now().isoformat()
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=4)
    except Exception as e:
        print(f"❌ Errore nel salvataggio dello stato locale: {e}")

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = json.dumps({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }).encode('utf-8')
    req = urllib.request.Request(
        url, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception as e:
        print(f"⚠️ Impossibile inviare notifica Telegram: {e}")
        return False

# ==============================================================================
# 1. FUNZIONI DI INGESTIONE DATI E SENTIMENT
# ==============================================================================
def fetch_sentiment_rss():
    keyword = "bitcoin" if "BTC" in SYMBOL.upper() or "BIT" in SYMBOL.upper() else "gold"
    query = f"{keyword}+inflation+recession+crisis+fed"
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            root = ET.fromstring(response.read())
            scores = []
            for item in root.findall('.//item')[:30]:
                title = item.find('title').text.lower()
                bull = sum(1 for w in BULLISH_WORDS if w in title)
                bear = sum(1 for w in BEARISH_WORDS if w in title)
                if (bull + bear) > 0:
                    scores.append((bull - bear) / (bull + bear))
            return sum(scores) / len(scores) if scores else 0.0
    except Exception as e:
        print(f"⚠️ Errore nel caricamento notizie RSS per {keyword}: {e}. Sentiment impostato a 0.0 (Neutro).")
        return 0.0

# ==============================================================================
# 2. CALCOLO INDICATORI QUANTITATIVI DA MT5
# ==============================================================================
def get_amsr_indicators():
    # Scarica le ultime 100 candele daily con un loop di riprova per permettere a MT5 di sincronizzare i dati storici
    rates = None
    for attempt in range(10):
        rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_D1, 0, 100)
        if rates is not None and len(rates) >= 55:
            break
        print(f"\r🔄 Sincronizzazione candele storiche per {SYMBOL} in corso (tentativo {attempt+1}/10)...", end="", flush=True)
        time.sleep(1.5)
        
    if rates is None or len(rates) < 55:
        print(f"\n❌ Errore nel recupero delle candele storiche per {SYMBOL} da MT5 (Dati non sincronizzati o simbolo inattivo).")
        return None
        
    closes = [r['close'] for r in rates]
    
    # SMA 50 (Trend Filter)
    sma_50 = sum(closes[-50:]) / 50.0
    
    # SMA 20
    window_20 = closes[-20:]
    sma_20 = sum(window_20) / 20.0
    
    # MAD 20 (Median Absolute Deviation)
    sorted_20 = sorted(window_20)
    median_20 = sorted_20[10]
    abs_deviations = [abs(c - median_20) for c in window_20]
    mad = sorted(abs_deviations)[10]
    std_mad = mad * 1.4826 if mad > 0 else 1e-6
    
    # Robust Z-Score corrente
    current_price = closes[-1]
    z_score = (current_price - sma_20) / std_mad
    trend = 1 if sma_20 > sma_50 else -1
    
    return {
        "price": current_price,
        "sma_20": sma_20,
        "sma_50": sma_50,
        "std_mad": std_mad,
        "z_score": z_score,
        "trend": trend
    }

# ==============================================================================
# 3. GESTIONE ORDINI E KILL-SWITCH SU MT5
# ==============================================================================
def check_emergency_killswitch():
    acct = mt5.account_info()
    if acct is None:
        return False
        
    floating_pnl = acct.equity - acct.balance
    if floating_pnl < 0 and abs(floating_pnl) >= KILLSWITCH_LOSS_USD:
        print(f"\n🚨🚨🚨 KILL-SWITCH ATTIVATO! Perdita corrente di ${abs(floating_pnl):.2f} supera il limite di sicurezza di ${KILLSWITCH_LOSS_USD:.2f}.")
        close_all_bot_positions()
        
        # Invia notifica Telegram
        msg_kill = (
            f"🚨🚨🚨 <b>KILL-SWITCH ATTIVATO!</b> 🚨🚨🚨\n"
            f"• Perdita fluttuante di <code>${abs(floating_pnl):.2f}</code> supera il limite di sicurezza di <code>${KILLSWITCH_LOSS_USD:.2f}</code>.\n"
            f"• Tutte le posizioni attive del bot sono state <b>chiuse immediatamente</b>."
        )
        send_telegram_message(msg_kill)
        return True
    return False

def close_all_bot_positions():
    positions = mt5.positions_get(magic=MAGIC_NUMBER)
    if positions:
        for pos in positions:
            tick = mt5.symbol_info_tick(pos.symbol)
            trade_type = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask
            
            req = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": pos.symbol,
                "volume": pos.volume,
                "type": trade_type,
                "position": pos.ticket,
                "price": price,
                "deviation": 20,
                "magic": MAGIC_NUMBER,
                "comment": "KILL-SWITCH CLOSE",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILL_IOC
            }
            res = mt5.order_send(req)
            if res.retcode != mt5.TRADE_RETCODE_DONE:
                print(f"Impossibile chiudere la posizione {pos.ticket}: {res.comment}")
            else:
                print(f"Chiusa con successo la posizione {pos.ticket}.")

def modify_position_sl(ticket, new_sl):
    positions = mt5.positions_get(ticket=ticket)
    if not positions:
        return False
    pos = positions[0]
    
    request = {
        "action": mt5.TRADE_ACTION_SLTP,
        "symbol": pos.symbol,
        "position": pos.ticket,
        "sl": round(new_sl, 2),
        "tp": round(pos.tp, 2), # Mantiene il TP originale intatto
        "magic": MAGIC_NUMBER
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Impossibile modificare SL per la posizione {pos.ticket}. Codice: {result.retcode} ({result.comment})")
        return False
        
    print(f"🔄 Trailing Stop Loss aggiornato per la posizione {pos.ticket}: Nuovo SL a ${new_sl:.2f}")
    return True

def run_paper_trader():
    # Inizializza MT5 con le credenziali del conto demo configurate in alto
    # Prova prima a lanciare automaticamente MT5 dal percorso standard rilevato
    mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
    initialized = False
    
    if os.path.exists(mt5_path):
        print(f"🤖 Rilevato MetaTrader 5 installato in: {mt5_path}")
        print("🔄 Tentativo di avvio automatico di MetaTrader 5 e connessione...")
        initialized = mt5.initialize(path=mt5_path, login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
    
    if not initialized:
        # Fallback generico se già aperto o se installato in un percorso personalizzato
        print("🔄 Tentativo di connessione generica (assicurati che MT5 sia già aperto)...")
        initialized = mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
        
    if not initialized:
        print("❌ Inizializzazione di MetaTrader 5 fallita.")
        print("👉 Soluzione: Apri manualmente il programma desktop 'MetaTrader 5' sul tuo PC, poi riavvia questo script.")
        return
        
    print("\n" + "="*80)
    print("🤖 AVVIO BOT AUTOMATICO AMSR ORO IN MODALITÀ DEMO/PAPER TRADING")
    print("="*80)
    
    # Verifica informazioni conto di test
    acct = mt5.account_info()
    if acct is None:
        print("Impossibile recuperare le informazioni del conto. Verifica la connessione a MT5.")
        mt5.shutdown()
        return
        
    print(f"• Conto Connesso: {acct.login} (Broker: {acct.company})")
    print(f"• Saldo Corrente: ${acct.balance:,.2f}  |  Equity: ${acct.equity:,.2f}")
    print(f"• Kill-Switch Perdita Giornaliera: ${KILLSWITCH_LOSS_USD:.2f}")
    
    # Seleziona e abilita il simbolo in Market Watch (fondamentale per permettere a MT5 di scaricare i dati storici)
    if not mt5.symbol_select(SYMBOL, True):
        print(f"❌ Errore: Impossibile abilitare il simbolo {SYMBOL} in Market Watch. Verifica se il broker lo supporta.")
        mt5.shutdown()
        return
    else:
        print(f"• Simbolo Attivo: {SYMBOL} (Abilitato con successo in Market Watch)")
    
    # Carica lo stato persistente locale
    state = load_bot_state()
    
    # Sincronizzazione automatica all'avvio se c'è già una posizione aperta su MT5
    active_positions = mt5.positions_get(magic=MAGIC_NUMBER)
    if active_positions:
        current_ticket = active_positions[0].ticket
        if state["active_trade_ticket"] != current_ticket:
            print(f"• ⚠️ Sincronizzazione: Trovata posizione attiva su MT5 (Ticket {current_ticket}). Aggiorno lo stato locale.")
            state["active_trade_ticket"] = current_ticket
            save_bot_state(state)
            
    print(f"• Stato Bot Caricato. Trade di oggi: {state['daily_trades_count']} | PnL odierno: ${state['daily_pnl']:+.2f}")
    if state["active_trade_ticket"] is not None:
        print(f"• ⚠️ Rilevata posizione attiva salvata nello stato: Ticket {state['active_trade_ticket']}")
        
    # Invia notifica Telegram di avvio
    msg_startup = (
        f"🤖 <b>AMSR Gold Bot Avviato!</b>\n"
        f"• Simbolo: <code>{SYMBOL}</code>\n"
        f"• Conto: <code>{acct.login}</code>\n"
        f"• Saldo: <code>${acct.balance:,.2f}</code>\n"
        f"• PnL Odierno: <code>${state['daily_pnl']:+.2f}</code>\n"
        f"• Trade Oggi: <code>{state['daily_trades_count']}</code>"
    )
    send_telegram_message(msg_startup)
        
    # Loop operativo
    try:
        while True:
            # 1. Verifica Kill-Switch di sicurezza
            if check_emergency_killswitch():
                print("Operatività bloccata dal sistema di sicurezza drawdown.")
                time.sleep(300) # Dorme 5 minuti prima di ricontrollare
                continue
                
            # 2. Scarica dati e calcola indicatori
            indicators = get_amsr_indicators()
            if indicators is None:
                time.sleep(60)
                continue
                
            # 3. Scarica il sentiment
            sentiment = fetch_sentiment_rss()
            
            # Calcola la soglia sentiment-adjusted
            adjusted_z = Z_THRESHOLD - (sentiment * 0.3)
            z_score = indicators["z_score"]
            trend = indicators["trend"]
            price = indicators["price"]
            std_mad = indicators["std_mad"]
            
            # Controlla posizioni aperte dal bot
            positions = mt5.positions_get(magic=MAGIC_NUMBER)
            
            # Riconciliazione dello stato locale se la posizione attiva è stata chiusa (SL, TP o manuale)
            if not positions and state["active_trade_ticket"] is not None:
                time.sleep(1.0) # Delay per permettere a MT5 di registrare il deal nei server storici
                history = mt5.history_deals_get(position=state["active_trade_ticket"])
                trade_pnl = 0.0
                if history:
                    for deal in history:
                        if deal.entry in [mt5.DEAL_ENTRY_OUT, mt5.DEAL_ENTRY_OUT_BY]:
                            trade_pnl += deal.profit + deal.commission + deal.swap
                    print(f"\n📈 POSIZIONE CHIUSA! Ticket: {state['active_trade_ticket']} | PnL finale: ${trade_pnl:+.2f}")
                else:
                    print(f"\n⚠️ Posizione {state['active_trade_ticket']} chiusa esternamente (non trovo deal storici).")
                
                # Invia notifica Telegram prima di azzerare lo stato locale
                msg_closed = (
                    f"📈 <b>Posizione Chiusa!</b>\n"
                    f"• Simbolo: <code>{SYMBOL}</code>\n"
                    f"• Ticket: <code>{state['active_trade_ticket']}</code>\n"
                    f"• PnL Trade: <code>${trade_pnl:+.2f}</code>\n"
                    f"• PnL Giornaliero Accumulato: <code>${state['daily_pnl'] + trade_pnl:+.2f}</code>"
                )
                send_telegram_message(msg_closed)
                
                state["daily_pnl"] += trade_pnl
                state["active_trade_ticket"] = None
                save_bot_state(state)
            
            print(f"\r[{datetime.now().strftime('%H:%M:%S')}] {SYMBOL}: ${price:.2f} | Trend: {'🟢' if trend == 1 else '🔴'} | Z-Score: {z_score:+.2f} | Sent: {sentiment:+.2f} | Posizioni: {len(positions)}", end="", flush=True)
            
            if not positions:
                # ── LOGICA DI INGRESSO (NESSUN TRADE APERTO) ──────────────────────────
                # Recupera le informazioni del simbolo per calcolare i lotti in modo dinamico
                symbol_info = mt5.symbol_info(SYMBOL)
                contract_size = symbol_info.trade_contract_size if symbol_info is not None else 1.0
                
                # LONG Entry (Trend rialzista e Z-Score ipervenduto)
                if trend == 1 and z_score < -adjusted_z:
                    # Calcolo parametri SL/TP
                    stop_loss_points = 2.0 * std_mad
                    take_profit_points = 3.5 * std_mad
                    
                    # Calcolo Lotti dinamici per rischiare esattamente $200 basato su contract_size
                    lots = RISK_PER_TRADE_USD / (stop_loss_points * contract_size)
                    lots = round(max(0.01, min(lots, 1.0)), 2) # Limita a max 1.0 lotto e min 0.01 lotto
                    
                    print(f"\n🚀 SEGNALE LONG RILEVATO! Prezzo: ${price:.2f}, Z-Score: {z_score:.2f}, Sentiment: {sentiment:.2f}")
                    print(f"📊 Calcolo Size: {lots} Lotti (Rischio: ${RISK_PER_TRADE_USD:.2f}, SL: ${stop_loss_points:.2f} Punti, Contratto: {contract_size})")
                    
                    # Invio ordine Buy
                    ticket = send_market_order("BUY", price, lots, stop_loss_points, take_profit_points)
                    if ticket is not None:
                        state["active_trade_ticket"] = ticket
                        state["daily_trades_count"] += 1
                        state["last_trade_time"] = time.time()
                        save_bot_state(state)
                        
                        # Invia notifica Telegram
                        msg_entry = (
                            f"🚀 <b>Segnale LONG Rilevato! (BUY)</b>\n"
                            f"• Simbolo: <code>{SYMBOL}</code>\n"
                            f"• Prezzo d'Ingresso: <code>${price:.2f}</code>\n"
                            f"• Dimensione: <code>{lots} Lotti</code>\n"
                            f"• Stop Loss: <code>${price - stop_loss_points:.2f}</code>\n"
                            f"• Take Profit: <code>${price + take_profit_points:.2f}</code>\n"
                            f"• Rischio Stimato: <code>${RISK_PER_TRADE_USD}</code>"
                        )
                        send_telegram_message(msg_entry)
                    
                # SHORT Entry (Trend ribassista e Z-Score ipercomprato)
                elif trend == -1 and z_score > adjusted_z:
                    stop_loss_points = 2.0 * std_mad
                    take_profit_points = 3.5 * std_mad
                    
                    lots = RISK_PER_TRADE_USD / (stop_loss_points * contract_size)
                    lots = round(max(0.01, min(lots, 1.0)), 2)
                    
                    print(f"\n📉 SEGNALE SHORT RILEVATO! Prezzo: ${price:.2f}, Z-Score: {z_score:.2f}, Sentiment: {sentiment:.2f}")
                    print(f"📊 Calcolo Size: {lots} Lotti (Rischio: ${RISK_PER_TRADE_USD:.2f}, SL: ${stop_loss_points:.2f} Punti, Contratto: {contract_size})")
                    
                    ticket = send_market_order("SELL", price, lots, stop_loss_points, take_profit_points)
                    if ticket is not None:
                        state["active_trade_ticket"] = ticket
                        state["daily_trades_count"] += 1
                        state["last_trade_time"] = time.time()
                        save_bot_state(state)
                        
                        # Invia notifica Telegram
                        msg_entry = (
                            f"📉 <b>Segnale SHORT Rilevato! (SELL)</b>\n"
                            f"• Simbolo: <code>{SYMBOL}</code>\n"
                            f"• Prezzo d'Ingresso: <code>${price:.2f}</code>\n"
                            f"• Dimensione: <code>{lots} Lotti</code>\n"
                            f"• Stop Loss: <code>${price + stop_loss_points:.2f}</code>\n"
                            f"• Take Profit: <code>${price - take_profit_points:.2f}</code>\n"
                            f"• Rischio Stimato: <code>${RISK_PER_TRADE_USD}</code>"
                        )
                        send_telegram_message(msg_entry)
            
            else:
                # ── GESTIONE POSIZIONI APERTE (TRAILING STOP & INVERSIONE TREND) ──────────
                for pos in positions:
                    # 1. Trailing Stop Loss Dinamico basato su Volatilità (MAD)
                    tick = mt5.symbol_info_tick(SYMBOL)
                    if tick is not None:
                        current_price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask
                        # Distanza di sicurezza SL calibrata sulla volatilità MAD
                        sl_distance = 2.0 * std_mad
                        
                        if pos.type == mt5.ORDER_TYPE_BUY:
                            new_sl = round(current_price - sl_distance, 2)
                            # Sposta lo SL solo verso l'alto ed evita micro-modifiche (soglia minima di 0.5 * std_mad)
                            if new_sl > pos.sl + (0.5 * std_mad):
                                if modify_position_sl(pos.ticket, new_sl):
                                    msg_trailing = (
                                        f"🔄 <b>Trailing Stop Aggiornato! (BUY)</b>\n"
                                        f"• Simbolo: <code>{SYMBOL}</code>\n"
                                        f"• Ticket: <code>{pos.ticket}</code>\n"
                                        f"• Nuovo Stop Loss: <code>${new_sl:.2f}</code>\n"
                                        f"• Prezzo Corrente: <code>${current_price:.2f}</code>"
                                    )
                                    send_telegram_message(msg_trailing)
                                    
                        elif pos.type == mt5.ORDER_TYPE_SELL:
                            new_sl = round(current_price + sl_distance, 2)
                            # Sposta lo SL solo verso il basso ed evita micro-modifiche (soglia minima di 0.5 * std_mad)
                            if pos.sl == 0.0 or new_sl < pos.sl - (0.5 * std_mad):
                                if modify_position_sl(pos.ticket, new_sl):
                                    msg_trailing = (
                                        f"🔄 <b>Trailing Stop Aggiornato! (SELL)</b>\n"
                                        f"• Simbolo: <code>{SYMBOL}</code>\n"
                                        f"• Ticket: <code>{pos.ticket}</code>\n"
                                        f"• Nuovo Stop Loss: <code>${new_sl:.2f}</code>\n"
                                        f"• Prezzo Corrente: <code>${current_price:.2f}</code>"
                                    )
                                    send_telegram_message(msg_trailing)
                    
                    # 2. Uscita di emergenza per Inversione Trend
                    if pos.type == mt5.ORDER_TYPE_BUY and trend == -1:
                        print(f"\n⚠️ Inversione Trend a ribassista rilevata. Chiusura anticipata posizione LONG {pos.ticket}.")
                        close_all_bot_positions()
                    elif pos.type == mt5.ORDER_TYPE_SELL and trend == 1:
                        print(f"\n⚠️ Inversione Trend a rialzista rilevata. Chiusura anticipata posizione SHORT {pos.ticket}.")
                        close_all_bot_positions()
            
            # Attende 60 secondi prima del prossimo controllo
            time.sleep(60)
            
    except KeyboardInterrupt:
        print("\n🤖 Monitoraggio automatico arrestato manualmente dall'utente.")
    finally:
        mt5.shutdown()

def send_market_order(action, price, lots, sl_points, tp_points):
    symbol_info = mt5.symbol_info(SYMBOL)
    if not symbol_info.visible:
        # Se non visibile, lo aggiungiamo a MarketWatch
        mt5.symbol_select(SYMBOL, True)
        
    tick = mt5.symbol_info_tick(SYMBOL)
    order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL
    entry_price = tick.ask if action == "BUY" else tick.bid
    
    sl_price = entry_price - sl_points if action == "BUY" else entry_price + sl_points
    tp_price = entry_price + tp_points if action == "BUY" else entry_price - tp_points
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": float(lots),
        "type": order_type,
        "price": entry_price,
        "sl": round(sl_price, 2),
        "tp": round(tp_price, 2),
        "deviation": 20,
        "magic": MAGIC_NUMBER,
        "comment": "AMSR Gold Paper-Trader",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILL_IOC
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"❌ Ordine non eseguito. Codice errore: {result.retcode} ({result.comment})")
        return None
        
    print(f"✅ Ordine {action} eseguito con successo! Ticket: {result.order} | SL: ${sl_price:.2f} | TP: ${tp_price:.2f}")
    return result.order

if __name__ == "__main__":
    run_paper_trader()
