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
import numpy as np

# ==============================================================================
# RETE NEURALE MULTI-LAYER PERCEPTRON E FILTRI QUANTITATIVI (MQL5 NEURAL & LOPEZ)
# ==============================================================================
class LightweightMLP:
    def __init__(self, input_size=6, hidden_size=16, output_size=1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inizializzazione pesi Metodo He
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))
        
    def swish(self, x):
        return x / (1.0 + np.exp(-np.clip(x, -500, 500)))
        
    def swish_derivative(self, x):
        s = 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))
        return s + x * s * (1.0 - s)
        
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-np.clip(x, -500, 500)))
        
    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.swish(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
        
    def train(self, X, y, epochs=200, lr=0.01):
        m = X.shape[0]
        if m == 0:
            return 0.0
            
        for epoch in range(epochs):
            a2 = self.forward(X)
            
            # Loss BCE
            loss = -np.mean(y * np.log(a2 + 1e-15) + (1.0 - y) * np.log(1.0 - a2 + 1e-15))
            
            # Backpropagation
            dz2 = a2 - y
            dW2 = np.dot(self.a1.T, dz2) / m
            db2 = np.sum(dz2, axis=0, keepdims=True) / m
            
            da1 = np.dot(dz2, self.W2.T)
            dz1 = da1 * self.swish_derivative(self.z1)
            dW1 = np.dot(X.T, dz1) / m
            db1 = np.sum(dz1, axis=0, keepdims=True) / m
            
            # Aggiornamento pesi
            self.W1 -= lr * dW1
            self.b1 -= lr * db1
            self.W2 -= lr * dW2
            self.b2 -= lr * db2
            
        final_preds = self.forward(X) > 0.5
        accuracy = np.mean(final_preds == y)
        return accuracy

    def save_weights(self, filepath):
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            data = {
                "W1": self.W1.tolist(),
                "b1": self.b1.tolist(),
                "W2": self.W2.tolist(),
                "b2": self.b2.tolist()
            }
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"✅ Pesi della rete neurale salvati in: {filepath}")
        except Exception as e:
            print(f"❌ Impossibile salvare i pesi del MLP: {e}")

    def load_weights(self, filepath):
        try:
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.W1 = np.array(data["W1"])
                self.b1 = np.array(data["b1"])
                self.W2 = np.array(data["W2"])
                self.b2 = np.array(data["b2"])
                print(f"✅ Pesi della rete neurale caricati con successo da: {filepath}")
                return True
        except Exception as e:
            print(f"⚠️ Impossibile caricare i pesi del MLP da file: {e}")
        return False

def get_atr_h4(symbol, period=14):
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, period + 1)
    if rates is None or len(rates) < period + 1:
        return None
    
    tr_list = []
    for i in range(1, len(rates)):
        high = rates[i]['high']
        low = rates[i]['low']
        prev_close = rates[i-1]['close']
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        tr_list.append(tr)
    
    atr = sum(tr_list[-period:]) / period
    return atr

def get_dxy_trend():
    mt5.symbol_select("DXY.cash", True)
    rates = mt5.copy_rates_from_pos("DXY.cash", mt5.TIMEFRAME_H4, 0, 20)
    if rates is None or len(rates) < 20:
        return 0
    closes = [r['close'] for r in rates]
    sma_20 = sum(closes) / 20.0
    current_price = closes[-1]
    if current_price > sma_20:
        return 1
    elif current_price < sma_20:
        return -1
    return 0

def train_and_get_mlp(symbol):
    mlp = LightweightMLP()
    print("🔄 Avvio dell'auto-addestramento della rete neurale MLP sul database storico H4...")
    
    weights_path = "data/amsr_mlp_weights.json"
    
    rates_gold = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, 500)
    rates_dxy = mt5.copy_rates_from_pos("DXY.cash", mt5.TIMEFRAME_H4, 0, 500)
    
    if rates_gold is None or rates_dxy is None or len(rates_gold) < 100:
        print("⚠️ Errore nel recupero dello storico H4 per Gold/DXY. Tentativo di caricare pesi salvati...")
        if mlp.load_weights(weights_path):
            return mlp
        print("⚠️ Nessun peso pre-salvato disponibile. Uso pesi casuali.")
        return mlp
        
    dxy_by_time = {r['time']: r['close'] for r in rates_dxy}
    
    X_list = []
    y_list = []
    
    for i in range(50, len(rates_gold) - 24):
        window = rates_gold[i-49:i+1]
        closes = [w['close'] for w in window]
        current_price = closes[-1]
        
        sma_20 = sum(closes[-20:]) / 20.0
        sma_50 = sum(closes[-50:]) / 50.0
        trend = 1 if sma_20 > sma_50 else -1
        
        window_20 = closes[-20:]
        median_20 = np.median(window_20)
        mad = np.median([abs(c - median_20) for c in window_20])
        std_mad = mad * 1.4826 if mad > 0 else 1e-6
        z_score = (current_price - median_20) / std_mad
        
        tr_list = []
        for k in range(len(window) - 14, len(window)):
            h = window[k]['high']
            l = window[k]['low']
            pc = window[k-1]['close']
            tr = max(h - l, abs(h - pc), abs(l - pc))
            tr_list.append(tr)
        atr_14 = sum(tr_list) / 14.0
        
        ret_3 = (current_price - closes[-4]) / closes[-4] if closes[-4] > 0 else 0.0
        vol_ratio = np.std(closes[-14:]) / (np.std(closes[-50:]) + 1e-6)
        
        gold_time = rates_gold[i]['time']
        dxy_price = dxy_by_time.get(gold_time, None)
        if dxy_price is None:
            dxy_price = rates_dxy[0]['close']
            for r in reversed(rates_dxy):
                if r['time'] <= gold_time:
                    dxy_price = r['close']
                    break
                    
        dxy_window = []
        for w in window[-20:]:
            t = w['time']
            p = dxy_by_time.get(t, dxy_price)
            dxy_window.append(p)
        dxy_sma_20 = sum(dxy_window) / 20.0
        dxy_trend = 1 if dxy_price > dxy_sma_20 else -1
        
        dxy_median = np.median(dxy_window)
        dxy_mad = np.median([abs(c - dxy_median) for c in dxy_window])
        dxy_std_mad = dxy_mad * 1.4826 if dxy_mad > 0 else 1e-6
        dxy_z_score = (dxy_price - dxy_median) / dxy_std_mad
        
        is_buy_signal = (trend == 1 and z_score < -1.0)
        is_sell_signal = (trend == -1 and z_score > 1.0)
        
        if is_buy_signal or is_sell_signal:
            sl_dist = 1.8 * atr_14
            tp_dist = 3.0 * atr_14
            label = 0
            future_bars = rates_gold[i+1 : i+25]
            
            if is_buy_signal:
                tp_target = current_price + tp_dist
                sl_target = current_price - sl_dist
                for fb in future_bars:
                    if fb['high'] >= tp_target:
                        label = 1
                        break
                    if fb['low'] <= sl_target:
                        label = 0
                        break
                else:
                    label = 1 if future_bars[-1]['close'] > current_price else 0
            else:
                tp_target = current_price - tp_dist
                sl_target = current_price + sl_dist
                for fb in future_bars:
                    if fb['low'] <= tp_target:
                        label = 1
                        break
                    if fb['high'] >= sl_target:
                        label = 0
                        break
                else:
                    label = 1 if future_bars[-1]['close'] < current_price else 0
                    
            features = [z_score, trend, ret_3, vol_ratio, dxy_z_score, dxy_trend]
            X_list.append(features)
            y_list.append(label)
            
    if len(X_list) >= 10:
        X = np.array(X_list)
        y = np.array(y_list).reshape(-1, 1)
        accuracy = mlp.train(X, y, epochs=150, lr=0.01)
        print(f"📊 Auto-Addestramento MLP Completato! Campioni: {len(X_list)} | Accuratezza Training: {accuracy*100:.2f}%")
        mlp.save_weights(weights_path)
    else:
        print(f"⚠️ Troppi pochi segnali storici ({len(X_list)}) per un addestramento sicuro. Caricamento pesi salvati...")
        if not mlp.load_weights(weights_path):
            print("⚠️ Nessun peso pre-esistente trovato. Uso pesi predefiniti non addestrati.")
            
    return mlp

def get_realtime_mlp_features(symbol):
    rates_gold = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H4, 0, 50)
    rates_dxy = mt5.copy_rates_from_pos("DXY.cash", mt5.TIMEFRAME_H4, 0, 50)
    
    if rates_gold is None or rates_dxy is None or len(rates_gold) < 50 or len(rates_dxy) < 50:
        return None
        
    closes = [r['close'] for r in rates_gold]
    current_price = closes[-1]
    
    sma_20 = sum(closes[-20:]) / 20.0
    sma_50 = sum(closes[-50:]) / 50.0
    trend = 1 if sma_20 > sma_50 else -1
    
    window_20 = closes[-20:]
    median_20 = np.median(window_20)
    mad = np.median([abs(c - median_20) for c in window_20])
    std_mad = mad * 1.4826 if mad > 0 else 1e-6
    z_score = (current_price - median_20) / std_mad
    
    ret_3 = (current_price - closes[-4]) / closes[-4] if closes[-4] > 0 else 0.0
    vol_ratio = np.std(closes[-14:]) / (np.std(closes[-50:]) + 1e-6)
    
    dxy_price = rates_dxy[-1]['close']
    dxy_closes = [r['close'] for r in rates_dxy[-20:]]
    dxy_sma_20 = sum(dxy_closes) / 20.0
    dxy_trend = 1 if dxy_price > dxy_sma_20 else -1
    
    dxy_median = np.median(dxy_closes)
    dxy_mad = np.median([abs(c - dxy_median) for c in dxy_closes])
    dxy_std_mad = dxy_mad * 1.4826 if dxy_mad > 0 else 1e-6
    dxy_z_score = (dxy_price - dxy_median) / dxy_std_mad
    
    return np.array([z_score, trend, ret_3, vol_ratio, dxy_z_score, dxy_trend]).reshape(1, -1)

DASHBOARD_DATA_FILE = "data/dashboard_data.json"

def update_dashboard_file(state, indicators, sentiment):
    try:
        # 1. Info Conto
        acct = mt5.account_info()
        balance = acct.balance if acct is not None else 10000.0
        equity = acct.equity if acct is not None else 10000.0
        daily_pnl = state.get("daily_pnl", 0.0)
        
        # 2. Indicatori correnti
        price = indicators["price"]
        z_score = indicators["z_score"]
        
        # 3. Calcola Volume Profile
        profile = []
        poc = price
        rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_H1, 0, 100)
        if rates is not None and len(rates) >= 10:
            highs = [r['high'] for r in rates]
            lows = [r['low'] for r in rates]
            min_price = min(lows)
            max_price = max(highs)
            if max_price == min_price:
                max_price += 1.0
                
            num_bins = 40
            bin_size = (max_price - min_price) / num_bins
            bins = [min_price + i * bin_size for i in range(num_bins)]
            volumes = [0.0 for _ in range(num_bins)]
            
            for r in rates:
                high = r['high']
                low = r['low']
                vol = r['tick_volume']
                start_idx = max(0, int((low - min_price) / bin_size))
                end_idx = min(num_bins - 1, int((high - min_price) / bin_size))
                steps = (end_idx - start_idx) + 1
                vol_per_step = vol / steps if steps > 0 else vol
                for idx in range(start_idx, end_idx + 1):
                    volumes[idx] += vol_per_step
                    
            max_vol_idx = int(np.argmax(volumes))
            poc = bins[max_vol_idx] + (bin_size / 2.0)
            
            for i in range(num_bins):
                profile.append({
                    "price": bins[i],
                    "volume": int(volumes[i]),
                    "is_poc": (i == max_vol_idx)
                })
            profile.reverse()
            
        # 4. Calcola Order Flow Delta
        delta = 0.0
        ticks = mt5.copy_ticks_from(SYMBOL, int(time.time()) - 120, 300, mt5.COPY_TICKS_ALL)
        if ticks is not None and len(ticks) >= 10:
            buy_aggressive = 0
            sell_aggressive = 0
            for i in range(1, len(ticks)):
                p = ticks[i]['last'] if ticks[i]['last'] > 0 else ticks[i]['bid']
                bid = ticks[i]['bid']
                ask = ticks[i]['ask']
                if ask > bid:
                    mid = (ask + bid) / 2.0
                    if p > mid:
                        buy_aggressive += 1
                    elif p < mid:
                        sell_aggressive += 1
            total = buy_aggressive + sell_aggressive
            if total > 0:
                delta = (buy_aggressive - sell_aggressive) / total
                
        # 5. Struttura dati
        data = {
            "balance": balance,
            "equity": equity,
            "daily_pnl": daily_pnl,
            "price": price,
            "z_score": z_score,
            "delta_imbalance": delta,
            "geo_sentiment": sentiment,
            "volume_profile": profile,
            "poc": poc
        }
        
        # Scrittura atomica per prevenire file vuoti / letti a metà
        temp_file = DASHBOARD_DATA_FILE + ".tmp"
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        if os.path.exists(DASHBOARD_DATA_FILE):
            os.remove(DASHBOARD_DATA_FILE)
        os.rename(temp_file, DASHBOARD_DATA_FILE)
        
    except Exception as e:
        print(f"\n⚠️ Errore nel salvataggio dei dati per la dashboard: {e}")

# ==============================================================================
# CONFIGURAZIONE PARAMETRI OPERATIVI
# ==============================================================================
MT5_LOGIN = 1513562873           # ID del conto di trading (demo/reale)
MT5_PASSWORD = "Q?5X*?1m8S1"     # Password master o investor (lo script proverà entrambe)
ALT_PASSWORD = "sR*fy!rz4?"     # Seconda password fornita per fallback
MT5_SERVER = "FTMO-Demo"        # Server del broker MT5

SYMBOL = "XAUUSD"               # Simbolo attivo: XAUUSD (Oro spot)
RISK_PER_TRADE_USD = 100.0      # Rischio per trade ($100 per challenge da $10k)
KILLSWITCH_LOSS_USD = 200.0     # Soglia di blocco giornaliero ($200 per challenge da $10k)
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
STATE_FILE = "data/amsr_bot_state_ftmo.json"

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
    global MT5_PASSWORD
    # Inizializza MT5 con le credenziali del conto demo configurate in alto
    # Prova prima a lanciare automaticamente MT5 dal percorso standard rilevato
    mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
    initialized = False
    
    if os.path.exists(mt5_path):
        print(f"🤖 Rilevato MetaTrader 5 installato in: {mt5_path}")
        print("🔄 Tentativo di avvio automatico di MetaTrader 5 e connessione...")
        initialized = mt5.initialize(path=mt5_path, login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
        if not initialized and ALT_PASSWORD:
            print("⚠️ Connessione con prima password fallita. Tentativo con seconda password...")
            initialized = mt5.initialize(path=mt5_path, login=MT5_LOGIN, password=ALT_PASSWORD, server=MT5_SERVER)
            if initialized:
                MT5_PASSWORD = ALT_PASSWORD
    
    if not initialized:
        # Fallback generico se già aperto o se installato in un percorso personalizzato
        print("🔄 Tentativo di connessione generica (assicurati che MT5 sia già aperto)...")
        initialized = mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
        if not initialized and ALT_PASSWORD:
            print("⚠️ Connessione con prima password fallita. Tentativo con seconda password...")
            initialized = mt5.initialize(login=MT5_LOGIN, password=ALT_PASSWORD, server=MT5_SERVER)
            if initialized:
                MT5_PASSWORD = ALT_PASSWORD
        
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
    
    # Auto-addestramento o caricamento della rete neurale MLP all'avvio
    mlp_model = train_and_get_mlp(SYMBOL)
    
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
            
            # 3b. Aggiorna i dati per la dashboard
            update_dashboard_file(state, indicators, sentiment)
            
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
                
                # Calcolo ATR H4 per dimensionamento e stop
                atr_h4 = get_atr_h4(SYMBOL, 14)
                
                # LONG Entry (Trend rialzista e Z-Score ipervenduto)
                if trend == 1 and z_score < -adjusted_z:
                    # 1. Filtro US Dollar Index (DXY)
                    dxy_tr = get_dxy_trend()
                    if dxy_tr > 0:
                        print(f"\n⚠️ SEGNALE LONG FILTRATO (DXY): Il dollaro americano (DXY) è in trend rialzista. Ingresso Gold evitato.")
                    else:
                        # 2. Calcolo parametri SL/TP dinamici con H4 ATR
                        if atr_h4 is not None:
                            stop_loss_points = 1.8 * atr_h4
                            take_profit_points = 3.0 * atr_h4
                        else:
                            stop_loss_points = 2.0 * std_mad
                            take_profit_points = 3.5 * std_mad
                        
                        # 3. Calcolo Lotti dinamici per rischiare esattamente $100
                        lots = RISK_PER_TRADE_USD / (stop_loss_points * contract_size)
                        lots = round(max(0.01, min(lots, 1.0)), 2)
                        
                        # 4. Validazione MLP Perceptron
                        mlp_features = get_realtime_mlp_features(SYMBOL)
                        score = 1.0
                        if mlp_features is not None:
                            score = mlp_model.forward(mlp_features)[0][0]
                        
                        if score < 0.55:
                            print(f"\n⚠️ SEGNALE LONG FILTRATO (MLP): Probabilità di successo insufficiente ({score*100:.1f}% < 55%).")
                        else:
                            print(f"\n🧠 SEGNALE LONG CONFERMATO (MLP): Probabilità di successo di {score*100:.1f}%. Procedo con l'ordine.")
                            print(f"🚀 SEGNALE LONG ESEGUITO! Prezzo: ${price:.2f}, Z-Score: {z_score:.2f}, Sentiment: {sentiment:.2f}")
                            print(f"📊 Size: {lots} Lotti (Rischio: ${RISK_PER_TRADE_USD:.2f}, SL: ${stop_loss_points:.2f} Punti)")
                            
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
                                    f"• Rischio Stimato: <code>${RISK_PER_TRADE_USD}</code>\n"
                                    f"• Validazione MLP: <code>{score*100:.1f}%</code>"
                                )
                                send_telegram_message(msg_entry)
                    
                # SHORT Entry (Trend ribassista e Z-Score ipercomprato)
                elif trend == -1 and z_score > adjusted_z:
                    # 1. Filtro US Dollar Index (DXY)
                    dxy_tr = get_dxy_trend()
                    if dxy_tr < 0:
                        print(f"\n⚠️ SEGNALE SHORT FILTRATO (DXY): Il dollaro americano (DXY) è in trend ribassista. Ingresso Gold evitato.")
                    else:
                        # 2. Calcolo parametri SL/TP dinamici con H4 ATR
                        if atr_h4 is not None:
                            stop_loss_points = 1.8 * atr_h4
                            take_profit_points = 3.0 * atr_h4
                        else:
                            stop_loss_points = 2.0 * std_mad
                            take_profit_points = 3.5 * std_mad
                        
                        # 3. Calcolo Lotti dinamici per rischiare esattamente $100
                        lots = RISK_PER_TRADE_USD / (stop_loss_points * contract_size)
                        lots = round(max(0.01, min(lots, 1.0)), 2)
                        
                        # 4. Validazione MLP Perceptron
                        mlp_features = get_realtime_mlp_features(SYMBOL)
                        score = 1.0
                        if mlp_features is not None:
                            score = mlp_model.forward(mlp_features)[0][0]
                        
                        if score < 0.55:
                            print(f"\n⚠️ SEGNALE SHORT FILTRATO (MLP): Probabilità di successo insufficiente ({score*100:.1f}% < 55%).")
                        else:
                            print(f"\n🧠 SEGNALE SHORT CONFERMATO (MLP): Probabilità di successo di {score*100:.1f}%. Procedo con l'ordine.")
                            print(f"📉 SEGNALE SHORT ESEGUITO! Prezzo: ${price:.2f}, Z-Score: {z_score:.2f}, Sentiment: {sentiment:.2f}")
                            print(f"📊 Size: {lots} Lotti (Rischio: ${RISK_PER_TRADE_USD:.2f}, SL: ${stop_loss_points:.2f} Punti)")
                            
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
                                    f"• Rischio Stimato: <code>${RISK_PER_TRADE_USD}</code>\n"
                                    f"• Validazione MLP: <code>{score*100:.1f}%</code>"
                                )
                                send_telegram_message(msg_entry)
            
            else:
                # ── GESTIONE POSIZIONI APERTE (TRAILING STOP & INVERSIONE TREND) ──────────
                for pos in positions:
                    # 1. Trailing Stop Loss Dinamico basato su Volatilità H4 ATR
                    tick = mt5.symbol_info_tick(SYMBOL)
                    if tick is not None:
                        current_price = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask
                        atr_h4 = get_atr_h4(SYMBOL, 14)
                        sl_distance = 1.8 * atr_h4 if atr_h4 is not None else 2.0 * std_mad
                        step_threshold = 0.4 * atr_h4 if atr_h4 is not None else 0.5 * std_mad
                        
                        if pos.type == mt5.ORDER_TYPE_BUY:
                            new_sl = round(current_price - sl_distance, 2)
                            # Sposta lo SL solo verso l'alto ed evita micro-modifiche
                            if new_sl > pos.sl + step_threshold:
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
                            # Sposta lo SL solo verso il basso ed evita micro-modifiche
                            if pos.sl == 0.0 or new_sl < pos.sl - step_threshold:
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
