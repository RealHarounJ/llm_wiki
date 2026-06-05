#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏆 AMSR AI Human-Like Adaptive Trading Bot (Hedge Fund Multi-Asset Multi-Strategy Model v4)
--------------------------------------------------------------------------------
Assets: XAUUSD (Gold), NAS100 (Nasdaq), US500 (S&P 500), EURUSD (Forex)
Architecture:
  - Layer 1: Knowledge Base Scraper (data/knowledge_base.json)
  - Layer 2: Human Variable Engine (47 variables calculated in real-time)
  - Layer 3: Signal Fusion Engine (dynamic weights based on market regime)
  - Layer 4: ML Adaptive Model (Random Forest / Pure-NumPy Logistic Regression fallback)
  - Layer 5: Risk & Execution Engine (Kill-Switches, Covariance Risk Parity)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import time
import urllib.request
from datetime import datetime, timezone, timedelta
import MetaTrader5 as mt5
import numpy as np

# Aggiungi wiki/Script al path di importazione
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importa i Layer custom
import human_variable_engine as hve
import signal_fusion_engine as sfe
import ml_model as ml

# ==============================================================================
# CONFIGURAZIONE STRATEGICA E PARAMETRI OPERATIVI
# ==============================================================================
MT5_LOGIN = 1513562873
MT5_PASSWORD = "Q?5X*?1m8S1"
ALT_PASSWORD = ""
MT5_SERVER = "FTMO-Demo"

# Asset Allocations (Espanso come da task list)
ASSETS = [
    "XAUUSD", "US100.cash", "US500.cash", "EURUSD", "BTCUSD", 
    "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", 
    "GBPJPY", "EURJPY", "AAPL", "AMZN", "GOOG", "META", 
    "MSFT", "NVDA", "TSLA"
]

PORTFOLIO_RISK_LIMIT_USD = 40.0   # Sotto-limite di rischio ridotto per massimizzare la sicurezza
DAILY_KILLSWITCH_USD = 450.0      # Kill-Switch giornaliero ($450 < limite FTMO $500)
TOTAL_KILLSWITCH_USD = 900.0      # Kill-Switch totale ($900 < limite FTMO $1000)
INITIAL_BALANCE = 10000.0         # Saldo iniziale del conto challenge
MAGIC_NUMBER = 999888             # Magic Number unico per il bot v4

# Timeframe Strategici (Pure Scalping Configuration: H1 / M15 / M5)
TF_LONG = mt5.TIMEFRAME_H1       # Filtro trend lungo termine
TF_MEDIUM = mt5.TIMEFRAME_M15    # Timeframe Z-Score, ADX, e Features
TF_SHORT = mt5.TIMEFRAME_M5      # Execution (Donchian, RSI, ATR)

# Impostazioni Soglie
CONFLUENCE_THRESHOLD = 75       # Soglia di confluenza per il trigger dei segnali
MAX_CONCURRENT_POSITIONS = 3    # Massimo numero di posizioni aperte contemporaneamente
TRAILING_STOP_ATR_MULT = 2.0    # Moltiplicatore ATR per Trailing Stop
TRAIL_PROFIT_GATE_ATR = 1.0     # Attivazione trail dopo 1.0x ATR di profitto

STATE_FILE = "data/amsr_ai_brain_state.json"
DASHBOARD_FILE = "data/dashboard_data.json"
CONTROL_FILE = "data/bot_control.json"

def load_bot_control():
    default_control = {
        "trading_enabled": True,
        "confluence_threshold": CONFLUENCE_THRESHOLD,
        "portfolio_risk_limit_usd": PORTFOLIO_RISK_LIMIT_USD,
        "manual_close_tickets": [],
        "emergency_stop": False
    }
    os.makedirs(os.path.dirname(CONTROL_FILE), exist_ok=True)
    if not os.path.exists(CONTROL_FILE):
        try:
            with open(CONTROL_FILE, 'w', encoding='utf-8') as f:
                json.dump(default_control, f, indent=4)
        except Exception:
            pass
        return default_control
    try:
        with open(CONTROL_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default_control

def save_bot_control(control):
    try:
        with open(CONTROL_FILE, 'w', encoding='utf-8') as f:
            json.dump(control, f, indent=4)
    except Exception as e:
        print(f"[ERROR] Impossibile salvare il controllo bot: {e}")


FEATURE_KEYS = [
    "price", "sma20", "sma50", "trend", "atr", "z_score", "donchian_high", "donchian_low",
    "fomo_index", "capitulation_idx", "stop_hunt_prob", "round_num_prox", "herding_signal",
    "spread_ratio", "liquidity_proxy", "price_efficiency", "delta_imbalance", "absorption_signal",
    "intermarket_corr", "fear_greed_idx", "risk_regime", "trend_quality", "momentum_persist",
    "false_breakout_risk", "frac_diff", "entropy", "vol_regime", "hurst_exponent",
    "session_quality", "prop_pressure", "overfit_guard"
]

# ==============================================================================
# GESTIONE STATO PERSISTENTE
# ==============================================================================
def load_bot_state():
    default_state = {
        "last_updated": "",
        "daily_date": "",
        "daily_pnl": 0.0,
        "daily_trades_count": 0,
        "active_tickets": [],       # Lista di ticket aperti dal bot
        "ticket_features": {},      # Salva le feature calcolate all'apertura del ticket
        "last_trained_date": ""
    }
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    if not os.path.exists(STATE_FILE):
        save_bot_state(default_state)
        return default_state
    try:
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            state = json.load(f)
            today_str = datetime.now().strftime("%Y-%m-%d")
            if state.get("daily_date") != today_str:
                state["daily_date"] = today_str
                state["daily_pnl"] = 0.0
                state["daily_trades_count"] = 0
                try:
                    acct = mt5.account_info()
                    if acct is not None:
                        state["day_start_balance"] = acct.balance
                except Exception:
                    pass
                save_bot_state(state)
            return state
    except Exception as e:
        print(f"[WARN] Impossibile caricare lo stato locale: {e}. Uso lo stato predefinito.")
        return default_state

def save_bot_state(state):
    try:
        state["last_updated"] = datetime.now().isoformat()
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=4)
    except Exception as e:
        print(f"[ERROR] Impossibile salvare lo stato locale: {e}")

def send_telegram_message(message):
    token = "8215784991:AAE-78OdQk3pZZVSY22CfqnXBlyZjT-q1dA"
    chat_id = "715100445"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = json.dumps({
        "chat_id": chat_id,
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
        print(f"[WARN] Notifica Telegram fallita: {e}")
        return False

# ==============================================================================
# RISOLUZIONE COVARIANZA E DYNAMIC RISK PARITY SIZING
# ==============================================================================
def calculate_portfolio_weights():
    asset_returns = []
    for symbol in ASSETS:
        rates = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, 30)
        if rates is None or len(rates) < 20:
            n_assets = len(ASSETS)
            return np.ones(n_assets) / n_assets
        closes = np.array([r['close'] for r in rates])
        rets = np.diff(closes) / closes[:-1]
        asset_returns.append(rets)
        
    min_len = min(len(r) for r in asset_returns)
    aligned_returns = np.array([r[-min_len:] for r in asset_returns])
    
    cov_matrix = np.cov(aligned_returns)
    variances = np.diag(cov_matrix)
    inv_variances = 1.0 / (variances + 1e-8)
    weights = inv_variances / np.sum(inv_variances)
    return weights

# ==============================================================================
# INTERMARKET & MACRO DYNAMICS
# ==============================================================================
def get_intermarket_changes():
    """Rileva i cambiamenti percentuali su base M15 per DXY, Gold, Bond."""
    try:
        # USDCHF come proxy DXY
        rates_dxy = mt5.copy_rates_from_pos("USDCHF", TF_MEDIUM, 0, 2)
        # XAUUSD come Gold
        rates_gold = mt5.copy_rates_from_pos("XAUUSD", TF_MEDIUM, 0, 2)
        # EURUSD come EUR
        rates_eur = mt5.copy_rates_from_pos("EURUSD", TF_MEDIUM, 0, 2)
        
        chg_dxy = (rates_dxy[-1]['close'] - rates_dxy[0]['close']) / rates_dxy[0]['close'] if rates_dxy is not None and len(rates_dxy) >= 2 else 0.0
        chg_gold = (rates_gold[-1]['close'] - rates_gold[0]['close']) / rates_gold[0]['close'] if rates_gold is not None and len(rates_gold) >= 2 else 0.0
        chg_eur = (rates_eur[-1]['close'] - rates_eur[0]['close']) / rates_eur[0]['close'] if rates_eur is not None and len(rates_eur) >= 2 else 0.0
        
        return chg_dxy, chg_gold, chg_eur
    except Exception:
        return 0.0, 0.0, 0.0

# ==============================================================================
# ENGINE GESTIONE ORDINI E NOTIFICHE
# ==============================================================================
def get_day_start_balance(acct, state):
    today_str = datetime.now().strftime("%Y-%m-%d")
    if state.get("daily_date") == today_str and "day_start_balance" in state:
        return state["day_start_balance"]
    return acct.balance

def check_emergency_killswitch():
    acct = mt5.account_info()
    if acct is None:
        return False
        
    state = load_bot_state()
    day_start_balance = state.get("day_start_balance")
    if day_start_balance is None:
        day_start_balance = acct.balance
        state["day_start_balance"] = day_start_balance
        save_bot_state(state)
        
    daily_drawdown = day_start_balance - acct.equity
    total_loss = INITIAL_BALANCE - acct.equity
    
    if daily_drawdown >= DAILY_KILLSWITCH_USD:
        print(f"\n[ALERT] KILL-SWITCH GIORNALIERO ATTIVATO! Perdita di ${daily_drawdown:.2f}")
        close_all_positions()
        msg = (
            f"🚨🚨🚨 <b>KILL-SWITCH GIORNALIERO ATTIVATO!</b> 🚨🚨🚨\n"
            f"• Perdita giornaliera: <code>${daily_drawdown:.2f}</code> (Limite: <code>${DAILY_KILLSWITCH_USD:.2f}</code>)\n"
            f"• Equity: <code>${acct.equity:.2f}</code>\n"
            f"• Tutte le posizioni chiuse ed trading sospeso per oggi."
        )
        send_telegram_message(msg)
        return True
    
    if total_loss >= TOTAL_KILLSWITCH_USD:
        print(f"\n[ALERT] KILL-SWITCH TOTALE ATTIVATO! Perdita di ${total_loss:.2f}")
        close_all_positions()
        msg = (
            f"🚨🚨🚨 <b>KILL-SWITCH TOTALE ATTIVATO!</b> 🚨🚨🚨\n"
            f"• Perdita totale: <code>${total_loss:.2f}</code> (Limite: <code>${TOTAL_KILLSWITCH_USD:.2f}</code>)\n"
            f"• Equity: <code>${acct.equity:.2f}</code>\n"
            f"• BOT COMPLETAMENTE ARRESTATO."
        )
        send_telegram_message(msg)
        return True
    
    return False

def close_all_positions():
    positions = mt5.positions_get()
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
                "comment": "QUANTUM KILLSWITCH",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC
            }
            res = mt5.order_send(req)
            if res.retcode != mt5.TRADE_RETCODE_DONE:
                print(f"[ERROR] Impossibile chiudere posizione {pos.ticket}: {res.comment}")
            else:
                print(f"[OK] Chiusa posizione {pos.ticket} su {pos.symbol}.")

def execute_order(symbol, order_type, volume, price, sl, tp, comment):
    req = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": round(volume, 2),
        "type": order_type,
        "price": price,
        "sl": round(sl, 2),
        "tp": round(tp, 2),
        "deviation": 20,
        "magic": MAGIC_NUMBER,
        "comment": comment[:31], # Commento troncato a 31 char per MT5
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC
    }
    result = mt5.order_send(req)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"[ERROR] Ordine fallito su {symbol}. Codice: {result.retcode} ({result.comment})")
        return None
    print(f"[OK] Ordine eseguito con successo! Ticket: {result.order}")
    return result.order

# ==============================================================================
# GESTIONE TRAILING STOP DINAMICO (ATR-BASED)
# ==============================================================================
def manage_trailing_stops():
    positions = mt5.positions_get(magic=MAGIC_NUMBER)
    if not positions:
        return
        
    for pos in positions:
        symbol = pos.symbol
        # Recupera ATR corrente per l'asset
        rates = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, 20)
        if rates is None or len(rates) < 15:
            continue
            
        tr_list = []
        for k in range(1, len(rates)):
            h = rates[k]['high']
            l = rates[k]['low']
            pc = rates[k-1]['close']
            tr = max(h - l, abs(h - pc), abs(l - pc))
            tr_list.append(tr)
        atr = sum(tr_list[-14:]) / 14.0
        
        tick = mt5.symbol_info_tick(symbol)
        if not tick:
            continue
            
        trail_dist = atr * TRAILING_STOP_ATR_MULT
        gate_dist = atr * TRAIL_PROFIT_GATE_ATR
        
        if pos.type == mt5.ORDER_TYPE_BUY:
            profit_points = tick.bid - pos.price_open
            # Controlla se siamo in profitto oltre il gate
            if profit_points >= gate_dist:
                new_sl = tick.bid - trail_dist
                # Sposta lo stop-loss verso l'alto
                if new_sl > pos.sl and new_sl < tick.bid:
                    req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "symbol": symbol,
                        "position": pos.ticket,
                        "sl": round(new_sl, 2),
                        "tp": pos.tp
                    }
                    res = mt5.order_send(req)
                    if res.retcode == mt5.TRADE_RETCODE_DONE:
                        print(f"[TRAIL] Spostato SL BUY per {symbol} a {new_sl:.2f}")
                        
        elif pos.type == mt5.ORDER_TYPE_SELL:
            profit_points = pos.price_open - tick.ask
            if profit_points >= gate_dist:
                new_sl = tick.ask + trail_dist
                # Sposta lo stop-loss verso il basso
                if (pos.sl == 0.0 or new_sl < pos.sl) and new_sl > tick.ask:
                    req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "symbol": symbol,
                        "position": pos.ticket,
                        "sl": round(new_sl, 2),
                        "tp": pos.tp
                    }
                    res = mt5.order_send(req)
                    if res.retcode == mt5.TRADE_RETCODE_DONE:
                        print(f"[TRAIL] Spostato SL SELL per {symbol} a {new_sl:.2f}")

# ==============================================================================
# MAIN BOT OPERATIVO LOOP
# ==============================================================================
def run_quantum_bot_v4():
    mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
    initialized = False
    
    if os.path.exists(mt5_path):
        print(f"[INFO] Avvio di MetaTrader 5 da: {mt5_path}")
        initialized = mt5.initialize(path=mt5_path, login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
        if not initialized and ALT_PASSWORD:
            initialized = mt5.initialize(path=mt5_path, login=MT5_LOGIN, password=ALT_PASSWORD, server=MT5_SERVER)
            
    if not initialized:
        initialized = mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
        if not initialized and ALT_PASSWORD:
            initialized = mt5.initialize(login=MT5_LOGIN, password=ALT_PASSWORD, server=MT5_SERVER)
            
    if not initialized:
        print("[ERROR] Connessione a MetaTrader 5 fallita.")
        return
        
    print("\n" + "="*80)
    print("[RUN] AVVIO BOT AMSR AI BRAIN v4 (ADAPTIVE ML SYSTEM)")
    print("="*80)
    
    acct = mt5.account_info()
    if acct is None:
        print("[ERROR] Impossibile connettersi al conto demo.")
        mt5.shutdown()
        return
        
    print(f"- Conto Connesso: {acct.login} (Broker: {acct.company})")
    print(f"- Saldo Iniziale: ${acct.balance:,.2f}  |  Equity: ${acct.equity:,.2f}")
    
    # Abilita tutti gli asset nel Market Watch
    for sym in ASSETS:
        mt5.symbol_select(sym, True)
    
    print("[INFO] Attesa di 5 secondi per la sincronizzazione del server...")
    time.sleep(5)
        
    state = load_bot_state()
    
    # Inizializza Modello ML
    ml_model = ml.AdaptiveMLModel(FEATURE_KEYS)
    
    # Primo training se dati storici sono presenti
    ml_model.train()
    
    # Sincronizzazione active_tickets con le posizioni reali del conto all'avvio
    active_positions = mt5.positions_get(magic=MAGIC_NUMBER)
    if active_positions:
        updated = False
        for pos in active_positions:
            if pos.ticket not in state["active_tickets"]:
                print(f"[INFO] Trovata posizione attiva sul conto: Ticket {pos.ticket} ({pos.symbol}). Aggiunta allo stato.")
                state["active_tickets"].append(pos.ticket)
                updated = True
        if updated:
            save_bot_state(state)
            
    # Notifica di startup
    msg_startup = (
        f"🧠 <b>AMSR AI Brain Bot v4 Avviato!</b>\n"
        f"• Conto: <code>{acct.login}</code>\n"
        f"• Asset Caricati: <code>{len(ASSETS)}</code>\n"
        f"• Risk Target: <code>${PORTFOLIO_RISK_LIMIT_USD:.2f}</code>\n"
        f"• Daily Max Loss: <code>${DAILY_KILLSWITCH_USD:.2f}</code>\n"
        f"• ML Model Status: <code>{'Trained' if ml_model.is_trained else 'Awaiting Data'}</code>"
    )
    send_telegram_message(msg_startup)
    
    try:
        while True:
            # 1. Ricarica lo stato e i controlli remoti
            state = load_bot_state()
            control = load_bot_control()
            
            # Applica override dinamici
            current_confluence_threshold = control.get("confluence_threshold", CONFLUENCE_THRESHOLD)
            current_portfolio_risk_limit = control.get("portfolio_risk_limit_usd", PORTFOLIO_RISK_LIMIT_USD)
            trading_enabled = control.get("trading_enabled", True)
            
            # Gestione Emergency Stop
            if control.get("emergency_stop", False):
                print("\n[ALERT] EMERGENZA RILEVATA DA PANNELLO REMOTO! Chiusura di tutte le posizioni...")
                close_all_positions()
                control["emergency_stop"] = False
                control["trading_enabled"] = False
                save_bot_control(control)
                send_telegram_message("⚠️ <b>EMERGENCY STOP RILEVATO!</b> Tutte le posizioni sono state chiuse e il trading è stato disabilitato.")
                
            # Gestione Chiusure Manuali
            manual_close_tickets = control.get("manual_close_tickets", [])
            if manual_close_tickets:
                positions = mt5.positions_get(magic=MAGIC_NUMBER)
                for pos in (positions or []):
                    if pos.ticket in manual_close_tickets:
                        print(f"\n[INFO] Chiusura manuale richiesta da remoto per Ticket: {pos.ticket}")
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
                            "comment": "MANUAL CLOSE REMOTE",
                            "type_time": mt5.ORDER_TIME_GTC,
                            "type_filling": mt5.ORDER_FILLING_IOC
                        }
                        res = mt5.order_send(req)
                        if res.retcode == mt5.TRADE_RETCODE_DONE:
                            print(f"[OK] Posizione remota {pos.ticket} chiusa.")
                            send_telegram_message(f"⏹️ <b>Chiusura Manuale da Remoto!</b>\n• Asset: <code>{pos.symbol}</code>\n• Ticket: <code>{pos.ticket}</code>")
                
                control["manual_close_tickets"] = []
                save_bot_control(control)
            
            # 2. Controllo Kill-Switch
            if check_emergency_killswitch():
                time.sleep(300)
                continue
                
            # 3. Gestione trailing stop
            manage_trailing_stops()
            
            # 4. Controllo re-training settimanale (Domenica)
            now_local = datetime.now()
            if now_local.weekday() == 6: # Domenica
                today_str = now_local.strftime("%Y-%m-%d")
                if state.get("last_trained_date") != today_str:
                    print("\n[ML] Avvio sessione di re-training settimanale automatico...")
                    if ml_model.train():
                        state["last_trained_date"] = today_str
                        save_bot_state(state)
                        send_telegram_message("🔄 <b>ML Model Retrained!</b>\nModello riaddestrato con successo sulle nuove feature.")
            
            # 5. Calcolo pesi di portafoglio basati su Covarianza
            weights = calculate_portfolio_weights()
            
            # 6. Ciclo operativo per ogni asset
            active_positions = mt5.positions_get(magic=MAGIC_NUMBER)
            n_active = len(active_positions) if active_positions else 0
            
            symbol_watchlist_stats = {}
            features = None
            
            for idx, symbol in enumerate(ASSETS):
                # Filtro orario azioni
                is_stock = symbol in ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]
                if is_stock:
                    local_now = datetime.now()
                    current_time_val = local_now.hour + local_now.minute / 60.0
                    if current_time_val < 15.75 or current_time_val > 21.5:
                        continue
                        
                # Recupera storico barre per calcolo indicatori su TF_MEDIUM (M15)
                rates = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, 150)
                if rates is None or len(rates) < 100:
                    continue
                closes = np.array([r['close'] for r in rates], dtype=float)
                highs = np.array([r['high'] for r in rates], dtype=float)
                lows = np.array([r['low'] for r in rates], dtype=float)
                
                # Calcolo ATR su TF_SHORT (M5) per sizing e stop-loss
                atr_rates = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, 20)
                if atr_rates is None or len(atr_rates) < 15:
                    continue
                tr_list = []
                for k in range(1, len(atr_rates)):
                    h = atr_rates[k]['high']
                    l = atr_rates[k]['low']
                    pc = atr_rates[k-1]['close']
                    tr = max(h - l, abs(h - pc), abs(l - pc))
                    tr_list.append(tr)
                atr = sum(tr_list[-14:]) / 14.0
                if atr <= 0:
                    atr = closes[-1] * 0.001
                
                sym_info = mt5.symbol_info(symbol)
                tick = mt5.symbol_info_tick(symbol)
                if not sym_info or not tick:
                    continue
                
                # Calcola le variazioni macro/intermarket in tempo reale
                chg_dxy, chg_gold, chg_eur = get_intermarket_changes()
                
                # Calcola le 47 variabili umane
                features = hve.compute_all_human_variables(
                    symbol=symbol,
                    closes=closes,
                    highs=highs,
                    lows=lows,
                    atr=atr,
                    symbol_info=sym_info,
                    daily_pnl=state["daily_pnl"],
                    total_pnl=INITIAL_BALANCE - acct.equity,
                    n_signals_today=state["daily_trades_count"],
                    daily_kill=DAILY_KILLSWITCH_USD,
                    total_kill=TOTAL_KILLSWITCH_USD,
                    initial_balance=INITIAL_BALANCE
                )
                
                if features is None:
                    continue
                
                # Sovrascrivi i cambiamenti intermarket corretti
                features["risk_regime"] = hve.calc_risk_regime(chg_dxy, chg_gold, chg_eur)
                
                # Fonde le variabili usando pesi dinamici basati sul regime
                fusion_results = sfe.fuse_signals(features)
                buy_score = fusion_results["buy_score"]
                sell_score = fusion_results["sell_score"]
                regime = fusion_results["regime"]
                confidence = fusion_results["confidence"]
                
                # Predizione ML
                ml_pred = ml_model.predict(features)
                ml_probs = ml_model.predict_probability(features)
                
                # Salva statistiche per la dashboard
                symbol_watchlist_stats[symbol] = {
                    "price": float(closes[-1]),
                    "buy_score": float(buy_score),
                    "sell_score": float(sell_score),
                    "regime": regime,
                    "confidence": float(confidence),
                    "ml_pred": int(ml_pred),
                    "ml_probs": [float(p) for p in ml_probs]
                }
                
                # Logica di ingresso a Confluenza & ML Alignment
                if trading_enabled and n_active < MAX_CONCURRENT_POSITIONS:
                    # Controlla se abbiamo posizioni già aperte su questo simbolo
                    already_open = False
                    if active_positions:
                        for p in active_positions:
                            if p.symbol == symbol:
                                already_open = True
                                break
                    
                    if not already_open:
                        # ──────────────────────────────────────────────────────
                        # SEGNALE BUY
                        # ──────────────────────────────────────────────────────
                        if buy_score >= current_confluence_threshold:
                            # ML Alignment Check: l'ML deve supportare il segnale (non deve predire -1)
                            if ml_pred >= 0:
                                # Calcolo lot size con Risk Parity e Covarianza
                                weight = weights[idx]
                                risk_usd = current_portfolio_risk_limit * weight
                                
                                # SL a 2.5x ATR
                                sl_dist = atr * 2.5
                                # Calcola valore pip per dimensionare l'ordine
                                point_value = sym_info.trade_tick_value / sym_info.trade_tick_size
                                risk_points = sl_dist
                                
                                lot_volume = risk_usd / (risk_points * point_value + 1e-9)
                                # Controlli minimi e massimi di lotto broker
                                lot_volume = max(sym_info.volume_min, min(sym_info.volume_max, lot_volume))
                                
                                sl = tick.ask - sl_dist
                                tp = tick.ask + (4.0 * atr) # TP a 4.0x ATR per asimmetria favorevole
                                
                                ticket = execute_order(symbol, mt5.ORDER_TYPE_BUY, lot_volume, tick.ask, sl, tp, f"v4 BUY {regime}")
                                if ticket:
                                    state["daily_trades_count"] += 1
                                    state["active_tickets"].append(ticket)
                                    # Salva le feature correnti per usarle come label nel training futuro
                                    state["ticket_features"][str(ticket)] = features
                                    save_bot_state(state)
                                    
                                    # Notifica Telegram
                                    msg = (
                                        f"🟢 <b>AMSR v4 BUY Eseguito!</b>\n"
                                        f"• Asset: <code>{symbol}</code>\n"
                                        f"• Lotti: <code>{lot_volume:.2f}</code>\n"
                                        f"• Prezzo: <code>${tick.ask:.2f}</code>\n"
                                        f"• SL / TP: <code>${sl:.2f} / ${tp:.2f}</code>\n"
                                        f"• Regime Rilevato: <code>{regime}</code>\n"
                                        f"• Confluence Score: <code>{buy_score:.1f}/100</code>\n"
                                        f"• ML Pred/Prob BUY: <code>{ml_pred} / {ml_probs[2]*100:.1f}%</code>"
                                    )
                                    send_telegram_message(msg)
                                    n_active += 1
                                    
                        # ──────────────────────────────────────────────────────
                        # SEGNALE SELL
                        # ──────────────────────────────────────────────────────
                        elif sell_score >= current_confluence_threshold:
                            # ML Alignment Check: l'ML non deve predire +1
                            if ml_pred <= 0:
                                weight = weights[idx]
                                risk_usd = current_portfolio_risk_limit * weight
                                
                                sl_dist = atr * 2.5
                                point_value = sym_info.trade_tick_value / sym_info.trade_tick_size
                                risk_points = sl_dist
                                
                                lot_volume = risk_usd / (risk_points * point_value + 1e-9)
                                lot_volume = max(sym_info.volume_min, min(sym_info.volume_max, lot_volume))
                                
                                sl = tick.bid + sl_dist
                                tp = tick.bid - (4.0 * atr)
                                
                                ticket = execute_order(symbol, mt5.ORDER_TYPE_SELL, lot_volume, tick.bid, sl, tp, f"v4 SELL {regime}")
                                if ticket:
                                    state["daily_trades_count"] += 1
                                    state["active_tickets"].append(ticket)
                                    state["ticket_features"][str(ticket)] = features
                                    save_bot_state(state)
                                    
                                    msg = (
                                        f"🔴 <b>AMSR v4 SELL Eseguito!</b>\n"
                                        f"• Asset: <code>{symbol}</code>\n"
                                        f"• Lotti: <code>{lot_volume:.2f}</code>\n"
                                        f"• Prezzo: <code>${tick.bid:.2f}</code>\n"
                                        f"• SL / TP: <code>${sl:.2f} / ${tp:.2f}</code>\n"
                                        f"• Regime Rilevato: <code>{regime}</code>\n"
                                        f"• Confluence Score: <code>{sell_score:.1f}/100</code>\n"
                                        f"• ML Pred/Prob SELL: <code>{ml_pred} / {ml_probs[0]*100:.1f}%</code>"
                                    )
                                    send_telegram_message(msg)
                                    n_active += 1
                                    
            # Chiudi le azioni americane prima del close intraday
            if now_local.hour == 21 and now_local.minute >= 50:
                stock_symbols = ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]
                open_positions = mt5.positions_get(magic=MAGIC_NUMBER)
                if open_positions:
                    for pos in open_positions:
                        if pos.symbol in stock_symbols:
                            print(f"\n[INFO] Chiusura automatica intraday per azione: {pos.symbol}")
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
                                "comment": "STOCK INTRADAY CLOSE",
                                "type_time": mt5.ORDER_TIME_GTC,
                                "type_filling": mt5.ORDER_FILLING_IOC
                            }
                            mt5.order_send(req)
                            
            # Sincronizzazione PnL e tracciamento trade per ML
            active_positions = mt5.positions_get(magic=MAGIC_NUMBER)
            current_active_tickets = [p.ticket for p in active_positions] if active_positions else []
            
            # Aggiungi posizioni rilevate esternamente
            state_updated = False
            for pos in (active_positions or []):
                if pos.ticket not in state["active_tickets"]:
                    state["active_tickets"].append(pos.ticket)
                    if features:
                        state["ticket_features"][str(pos.ticket)] = features
                    state_updated = True
            if state_updated:
                save_bot_state(state)
                
            # Controlla ticket chiusi
            for t in list(state["active_tickets"]):
                if t not in current_active_tickets:
                    # Il trade è chiuso! Ottieni il deal per calcolare il profitto reale
                    time.sleep(1.0)
                    history = mt5.history_deals_get(position=t)
                    trade_pnl = 0.0
                    symbol_closed = ""
                    if history:
                        for deal in history:
                            if deal.entry in [mt5.DEAL_ENTRY_OUT, mt5.DEAL_ENTRY_OUT_BY]:
                                trade_pnl += deal.profit + deal.commission + deal.swap
                                symbol_closed = deal.symbol
                                
                    # Genera la label per il Triple-Barrier Method
                    label = 0
                    if trade_pnl > 5.0:
                        label = 1
                    elif trade_pnl < -5.0:
                        label = -1
                        
                    # Estrae le feature salvate all'apertura del trade
                    saved_features = state["ticket_features"].get(str(t))
                    if saved_features:
                        ml_model.add_to_history(symbol_closed if symbol_closed else "UNKNOWN", saved_features, label)
                        del state["ticket_features"][str(t)]
                        
                    # Aggiorna lo stato
                    state["daily_pnl"] += trade_pnl
                    state["active_tickets"].remove(t)
                    save_bot_state(state)
                    
                    msg = (
                        f"📊 <b>Trade Chiuso (AMSR v4)</b>\n"
                        f"• Ticket: <code>{t}</code>\n"
                        f"• PnL: <code>${trade_pnl:+.2f}</code>\n"
                        f"• Label ML registrata: <code>{label}</code>\n"
                        f"• PnL Giornaliero Accumulato: <code>${state['daily_pnl']:+.2f}</code>"
                    )
                    send_telegram_message(msg)
            
            # Salva i dati per la Dashboard
            active_list = []
            for p in (active_positions or []):
                active_list.append({
                    "ticket": int(p.ticket),
                    "symbol": p.symbol,
                    "type": "BUY" if p.type == mt5.ORDER_TYPE_BUY else "SELL",
                    "volume": float(p.volume),
                    "open_price": float(p.price_open),
                    "current_price": float(p.price_current),
                    "pnl": float(p.profit + p.swap),
                    "sl": float(p.sl),
                    "tp": float(p.tp)
                })
                
            dashboard_data = {
                "balance": float(acct.balance) if acct else INITIAL_BALANCE,
                "equity": float(acct.equity) if acct else INITIAL_BALANCE,
                "daily_pnl": float(state["daily_pnl"]),
                "daily_trades_count": int(state["daily_trades_count"]),
                "active_positions": active_list,
                "watchlist": symbol_watchlist_stats,
                "trading_enabled": trading_enabled,
                "confluence_threshold": current_confluence_threshold,
                "portfolio_risk_limit_usd": current_portfolio_risk_limit,
                "last_updated": datetime.now().isoformat()
            }
            try:
                with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
                    json.dump(dashboard_data, f, indent=4)
            except Exception as e:
                print(f"\n[ERROR] Scrittura dashboard fallita: {e}")
            
            # Console log
            print(f"\r[AMSR AI v4] Attivi: {len(active_positions) if active_positions else 0} | PnL Oggi: ${state['daily_pnl']:+.2f} | ML: {'Trained' if ml_model.is_trained else 'Awaiting'}", end="", flush=True)
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n[INFO] Arresto del Bot richiesto dall'utente.")
    finally:
        mt5.shutdown()

if __name__ == "__main__":
    run_quantum_bot_v4()
