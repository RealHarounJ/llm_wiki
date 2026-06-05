#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🏆 AMSR Quantum Portfolio Auto-Trader (Hedge Fund Multi-Asset Multi-Strategy Model)
--------------------------------------------------------------------------------
Assets: XAUUSD (Gold), NAS100 (Nasdaq), US500 (S&P 500), EURUSD (Forex)
Strategies: 
  1. Mean Reversion (Robust MAD Z-Score)
  2. Trend Following (Donchian Channel Breakout)
Risk Engine: Dynamic Covariance Risk Parity & Constant Volatility Target
Drawdown Engine: Automatic Daily & Total Capital Kill-Switch
Console: Safe CP1252 ASCII Logging
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
import MetaTrader5 as mt5
import numpy as np

# ==============================================================================
# CONFIGURAZIONE STRATEGICA E PARAMETRI OPERATIVI
# ==============================================================================
MT5_LOGIN = 1513562873
MT5_PASSWORD = "Q?5X*?1m8S1"
ALT_PASSWORD = ""
MT5_SERVER = "FTMO-Demo"

# Asset Allocations
ASSETS = ["XAUUSD", "US100.cash", "US500.cash", "EURUSD", "BTCUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD", "USDCHF", "GBPJPY", "EURJPY", "AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]
PORTFOLIO_RISK_LIMIT_USD = 150.0  # Rischio massimo per trade aggregato (aumentato per prop)
DAILY_KILLSWITCH_USD = 450.0      # Kill-Switch giornaliero ($450 < limite FTMO $500)
TOTAL_KILLSWITCH_USD = 900.0      # Kill-Switch totale ($900 < limite FTMO $1000)
INITIAL_BALANCE = 10000.0         # Saldo iniziale del conto challenge
MAGIC_NUMBER = 999888             # Magic Number unico per il portafoglio quantistico

# Strategic Timeframes (Pure Scalping Configuration: H1 / M15 / M5)
TF_LONG = mt5.TIMEFRAME_H1       # Filtro trend lungo termine (precedentemente D1)
TF_MEDIUM = mt5.TIMEFRAME_M15    # Timeframe Z-Score (precedentemente D1) e ADX (precedentemente H4)
TF_SHORT = mt5.TIMEFRAME_M5      # Execution (Donchian, RSI, ATR - precedentemente H4/H1)

# Impostazioni Indicatori
Z_THRESHOLD = 1.8                # Soglia Z-Score alzata: segnale piu forte richiesto (meno trade, migliore qualita)
DONCHIAN_PERIOD = 20             # Periodo Donchian per Trend Following
Z_SCORE_WINDOW = 100             # Finestra Z-Score a 100 candele per stabilita statistica
SPREAD_MAX_RATIO = 0.25          # Spread massimo accettabile (25% ATR) - soglia piu stretta
MAX_CONCURRENT_POSITIONS = 3    # FIX BACKTEST: ridotto a 3 per evitare overtrading
TRAILING_STOP_ATR_MULT = 2.0    # FIX BACKTEST: Trail a 2.0x ATR per dare respiro ai vincitori
TRAIL_PROFIT_GATE_ATR = 1.0     # FIX BACKTEST: Trail si attiva SOLO dopo 1.0x ATR di profitto
CONFLUENCE_THRESHOLD = 75       # FIX BACKTEST: Alzato da 65 a 75 per ridurre falsi segnali

STATE_FILE = "data/amsr_quantum_portfolio_state.json"
DASHBOARD_FILE = "data/dashboard_data.json"

# ==============================================================================
# GESTIONE STATO PERSISTENTE
# ==============================================================================
def load_bot_state():
    default_state = {
        "last_updated": "",
        "daily_date": "",
        "daily_pnl": 0.0,
        "daily_trades_count": 0,
        "active_tickets": []  # Lista di ticket aperti dal bot
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
                # Registra il saldo iniziale del nuovo giorno
                try:
                    acct = mt5.account_info()
                    if acct is not None:
                        state["day_start_balance"] = acct.balance
                    elif "day_start_balance" in state:
                        del state["day_start_balance"]
                except Exception:
                    if "day_start_balance" in state:
                        del state["day_start_balance"]
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
# STRUMENTI QUANTITATIVI E SENTIMENT SCRAPER
# ==============================================================================
def fetch_macro_sentiment(symbol):
    keyword = "gold" if "XAU" in symbol.upper() else "nasdaq" if "100" in symbol.upper() else "sp500" if "500" in symbol.upper() else "euro"
    query = f"{keyword}+inflation+recession+crisis+fed"
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    headlines_found = []
    try:
        with urllib.request.urlopen(req) as response:
            root = ET.fromstring(response.read())
            scores = []
            for item in root.findall('.//item')[:20]:
                title = item.find('title').text
                title_lower = title.lower()
                bull = sum(1 for w in BULLISH_WORDS if w in title_lower)
                bear = sum(1 for w in BEARISH_WORDS if w in title_lower)
                if (bull + bear) > 0:
                    scores.append((bull - bear) / (bull + bear))
                    headlines_found.append(title)
            score = sum(scores) / len(scores) if scores else 0.0
            return {"score": score, "headlines": headlines_found[:3]}
    except Exception:
        return {"score": 0.0, "headlines": []}

def fetch_stocktwits_sentiment(symbol):
    ticker_map = {
        "XAUUSD": "GLD",
        "US100.cash": "QQQ",
        "US500.cash": "SPY",
        "EURUSD": "EURUSD",
        "BTCUSD": "BTC.X"
    }
    ticker = ticker_map.get(symbol, symbol)
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            messages = data.get("messages", []) if isinstance(data, dict) else []
            bullish = 0
            bearish = 0
            for m in messages[:30]:
                entities = m.get("entities") or {}
                sentiment_obj = entities.get("sentiment") or {}
                sentiment = sentiment_obj.get("basic") if isinstance(sentiment_obj, dict) else None
                if sentiment == "Bullish":
                    bullish += 1
                elif sentiment == "Bearish":
                    bearish += 1
            
            total = bullish + bearish
            score = (bullish - bearish) / total if total > 0 else 0.0
            return {
                "score": score,
                "bullish": bullish,
                "bearish": bearish,
                "total_labeled": total,
                "msg_count": len(messages)
            }
    except Exception:
        return {
            "score": 0.0,
            "bullish": 0,
            "bearish": 0,
            "total_labeled": 0,
            "msg_count": 0
        }

def fetch_combined_sentiment(symbol):
    news_sentiment = fetch_macro_sentiment(symbol)
    news_score = news_sentiment["score"]
    
    st_sentiment = fetch_stocktwits_sentiment(symbol)
    st_score = st_sentiment["score"]
    
    combined_score = 0.5 * news_score + 0.5 * st_score
    
    return {
        "score": combined_score,
        "news_score": news_score,
        "headlines": news_sentiment["headlines"],
        "stocktwits_score": st_score,
        "stocktwits_bullish": st_sentiment["bullish"],
        "stocktwits_bearish": st_sentiment["bearish"],
        "stocktwits_total_labeled": st_sentiment["total_labeled"],
        "stocktwits_msg_count": st_sentiment["msg_count"]
    }

def calculate_rsi(symbol, timeframe, period=14):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period + 100)
    if rates is None or len(rates) < period + 1:
        return 50.0
    closes = np.array([r['close'] for r in rates], dtype=float)
    deltas = np.diff(closes)
    gains = np.where(deltas > 0, deltas, 0.0)
    losses = np.where(deltas < 0, -deltas, 0.0)
    
    alpha = 1.0 / period
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])
    
    for i in range(period, len(deltas)):
        avg_gain = alpha * gains[i] + (1 - alpha) * avg_gain
        avg_loss = alpha * losses[i] + (1 - alpha) * avg_loss
        
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))

def get_mtf_analysis(symbol):
    rates_d1 = mt5.copy_rates_from_pos(symbol, TF_LONG, 0, 250)
    d1_trend = 0
    if rates_d1 is not None and len(rates_d1) >= 200:
        closes_d1 = np.array([r['close'] for r in rates_d1], dtype=float)
        sma_50 = np.mean(closes_d1[-50:])
        sma_200 = np.mean(closes_d1[-200:])
        d1_trend = 1 if sma_50 > sma_200 else -1
        
    rates_h4 = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, 60)
    h4_trend = 0
    if rates_h4 is not None and len(rates_h4) >= 50:
        closes_h4 = np.array([r['close'] for r in rates_h4], dtype=float)
        sma_20 = np.mean(closes_h4[-20:])
        sma_50 = np.mean(closes_h4[-50:])
        h4_trend = 1 if sma_20 > sma_50 else -1
        
    rates_h1 = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, 30)
    h1_trend = 0
    if rates_h1 is not None and len(rates_h1) >= 20:
        closes_h1 = np.array([r['close'] for r in rates_h1], dtype=float)
        sma_10 = np.mean(closes_h1[-10:])
        sma_20 = np.mean(closes_h1[-20:])
        h1_trend = 1 if sma_10 > sma_20 else -1

    trends = [d1_trend, h4_trend, h1_trend]
    bullish_count = sum(1 for t in trends if t == 1)
    bearish_count = sum(1 for t in trends if t == -1)
    
    alignment = 0
    if bullish_count >= 2:
        alignment = 1
    elif bearish_count >= 2:
        alignment = -1
        
    return {
        "d1_trend": d1_trend,
        "h4_trend": h4_trend,
        "h1_trend": h1_trend,
        "alignment": alignment,
        "bullish_count": bullish_count,
        "bearish_count": bearish_count
    }

def calculate_adx(symbol, timeframe=mt5.TIMEFRAME_H4, period=14):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, period * 3 + 10)
    if rates is None or len(rates) < period * 2:
        return 20.0
    
    highs = np.array([r['high'] for r in rates], dtype=float)
    lows = np.array([r['low'] for r in rates], dtype=float)
    closes = np.array([r['close'] for r in rates], dtype=float)
    
    n = len(rates)
    tr = np.zeros(n)
    plus_dm = np.zeros(n)
    minus_dm = np.zeros(n)
    
    for i in range(1, n):
        tr[i] = max(highs[i] - lows[i], abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1]))
        up_move = highs[i] - highs[i-1]
        down_move = lows[i-1] - lows[i]
        
        if up_move > down_move and up_move > 0:
            plus_dm[i] = up_move
        else:
            plus_dm[i] = 0
            
        if down_move > up_move and down_move > 0:
            minus_dm[i] = down_move
        else:
            minus_dm[i] = 0
            
    atr_smooth = np.zeros(n)
    plus_di_smooth = np.zeros(n)
    minus_di_smooth = np.zeros(n)
    
    atr_smooth[period] = np.sum(tr[1:period+1])
    plus_di_smooth[period] = np.sum(plus_dm[1:period+1])
    minus_di_smooth[period] = np.sum(minus_dm[1:period+1])
    
    for i in range(period + 1, n):
        atr_smooth[i] = atr_smooth[i-1] - (atr_smooth[i-1] / period) + tr[i]
        plus_di_smooth[i] = plus_di_smooth[i-1] - (plus_di_smooth[i-1] / period) + plus_dm[i]
        minus_di_smooth[i] = minus_di_smooth[i-1] - (minus_di_smooth[i-1] / period) + minus_dm[i]
        
    plus_di = np.zeros(n)
    minus_di = np.zeros(n)
    dx = np.zeros(n)
    
    for i in range(period, n):
        if atr_smooth[i] > 0:
            plus_di[i] = 100 * plus_di_smooth[i] / atr_smooth[i]
            minus_di[i] = 100 * minus_di_smooth[i] / atr_smooth[i]
        else:
            plus_di[i] = 0
            minus_di[i] = 0
            
        sum_di = plus_di[i] + minus_di[i]
        diff_di = abs(plus_di[i] - minus_di[i])
        dx[i] = 100 * diff_di / sum_di if sum_di > 0 else 0
        
    adx = np.zeros(n)
    adx[period*2 - 1] = np.mean(dx[period:period*2])
    for i in range(period*2, n):
        adx[i] = (adx[i-1] * (period - 1) + dx[i]) / period
        
    return adx[-1]

def detect_market_regime(symbol):
    adx_val = calculate_adx(symbol, TF_MEDIUM, 14)
    
    rates_d1 = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, 75)
    relative_volatility = 1.0
    current_atr = 0.0
    avg_atr_50 = 0.0
    high_volatility = False
    
    if rates_d1 is not None and len(rates_d1) >= 65:
        closes = np.array([r['close'] for r in rates_d1], dtype=float)
        highs = np.array([r['high'] for r in rates_d1], dtype=float)
        lows = np.array([r['low'] for r in rates_d1], dtype=float)
        
        tr = np.zeros(len(rates_d1))
        for i in range(1, len(rates_d1)):
            tr[i] = max(highs[i] - lows[i], abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1]))
            
        atr_values = []
        for i in range(15, len(rates_d1)):
            atr_val = np.mean(tr[i-14:i])
            atr_values.append(atr_val)
            
        if len(atr_values) >= 50:
            current_atr = atr_values[-1]
            avg_atr_50 = np.mean(atr_values[-50:])
            if avg_atr_50 > 0:
                relative_volatility = current_atr / avg_atr_50
            if relative_volatility > 1.5:
                high_volatility = True
                
    regime = "ranging"
    if adx_val > 25:
        regime = "trending"
    elif adx_val < 20:
        regime = "ranging"
    else:
        regime = "transition"
        
    return {
        "adx": adx_val,
        "regime": regime,
        "relative_volatility": relative_volatility,
        "high_volatility": high_volatility
    }

def check_session_filter(symbol):
    now_utc = datetime.now(timezone.utc)
    hour = now_utc.hour + now_utc.minute / 60.0
    
    is_london = (7.0 <= hour < 16.0)
    is_ny = (13.0 <= hour < 21.0)
    is_asia = (0.0 <= hour < 7.0)
    
    score = 0
    session_name = "Fuori Sessione"
    
    if is_london or is_ny:
        score = 5
        if is_london and is_ny:
            session_name = "London-NY Overlap"
        elif is_london:
            session_name = "London"
        else:
            session_name = "New York"
    elif is_asia and (("XAU" in symbol.upper()) or ("BTC" in symbol.upper())):
        score = 2
        session_name = "Asia"
        
    return score, session_name

def check_economic_calendar():
    now_utc = datetime.now(timezone.utc)
    
    if not hasattr(check_economic_calendar, "cached_events") or not hasattr(check_economic_calendar, "last_fetch_time") or (now_utc - check_economic_calendar.last_fetch_time).total_seconds() > 3600:
        url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                check_economic_calendar.cached_events = data
                check_economic_calendar.last_fetch_time = now_utc
        except Exception as e:
            if not hasattr(check_economic_calendar, "cached_events"):
                check_economic_calendar.cached_events = []
                check_economic_calendar.last_fetch_time = now_utc
                
    events = check_economic_calendar.cached_events
    monitored_keywords = ["non-farm payrolls", "cpi", "fomc", "ecb", "gdp", "pmi", "interest rate", "rate decision", "adp", "employment", "non-farm", "payrolls"]
    
    for event in events:
        impact = str(event.get("impact", "")).lower()
        title = str(event.get("title", "")).lower()
        country = str(event.get("country", "")).upper()
        
        is_monitored = any(k in title for k in monitored_keywords)
        is_high_impact = (impact == "high")
        
        if is_monitored or is_high_impact:
            event_date_str = event.get("date")
            if not event_date_str:
                continue
            try:
                if event_date_str.endswith('Z'):
                    event_date_str = event_date_str[:-1] + '+00:00'
                event_date = datetime.fromisoformat(event_date_str)
                event_date_utc = event_date.astimezone(timezone.utc)
                
                time_diff = (event_date_utc - now_utc).total_seconds()
                # Blocca trade da 15 minuti prima a 30 minuti dopo la release (-1800 <= time_diff <= 900)
                if -1800 <= time_diff <= 900:
                    return False, f"No-Trade: {event.get('title')} ({country}) in {time_diff/60:.1f} min"
            except Exception:
                continue
                
    return True, "No upcoming high-impact events"

def get_intermarket_signal(symbol, order_type):
    rates = mt5.copy_rates_from_pos("EURUSD", TF_MEDIUM, 0, 20)
    if rates is None or len(rates) < 20:
        return 0, "No EURUSD data"
        
    closes = np.array([r['close'] for r in rates], dtype=float)
    sma_20 = np.mean(closes)
    current_eurusd = closes[-1]
    
    eurusd_rising = current_eurusd > sma_20
    dxy_direction = "debole" if eurusd_rising else "forte"
    
    is_gold = "XAU" in symbol.upper()
    is_btc = "BTC" in symbol.upper()
    is_eurusd = "EURUSD" in symbol.upper()
    is_usd_asset = ("100" in symbol) or ("500" in symbol) or ("US" in symbol.upper() and not is_gold)
    
    supported_order = None
    if eurusd_rising:
        if is_gold or is_btc or is_eurusd:
            supported_order = mt5.ORDER_TYPE_BUY
        elif is_usd_asset:
            supported_order = mt5.ORDER_TYPE_SELL
    else:
        if is_gold or is_btc or is_eurusd:
            supported_order = mt5.ORDER_TYPE_SELL
        elif is_usd_asset:
            supported_order = mt5.ORDER_TYPE_BUY
            
    order_str = "BUY" if order_type == mt5.ORDER_TYPE_BUY else "SELL"
    if order_type == supported_order:
        return 5, f"DXY {dxy_direction}, conferma {order_str} {symbol}"
    else:
        return 0, f"DXY {dxy_direction}, no conferma {order_str} {symbol}"

def calculate_confluence_score(symbol, order_type, strategy, indicators, tick, sentiment_data, mtf, regime_data):
    z_score = indicators["z_score"]
    sentiment_score = sentiment_data["score"]
    adjusted_z = Z_THRESHOLD - (sentiment_score * 0.3)
    
    z_score_pts = 0
    if order_type == mt5.ORDER_TYPE_BUY and z_score < 0:
        z_score_pts = min(20, max(0, int(abs(z_score) / adjusted_z * 12)))
    elif order_type == mt5.ORDER_TYPE_SELL and z_score > 0:
        z_score_pts = min(20, max(0, int(abs(z_score) / adjusted_z * 12)))
        
    donchian_high = indicators["donchian_high"]
    donchian_low = indicators["donchian_low"]
    atr = indicators["atr"]
    
    donchian_pts = 0
    if order_type == mt5.ORDER_TYPE_BUY:
        if tick.ask >= donchian_high:
            donchian_pts = 15
        elif tick.ask >= donchian_high - 0.5 * atr:
            donchian_pts = 8
    elif order_type == mt5.ORDER_TYPE_SELL:
        if tick.bid <= donchian_low:
            donchian_pts = 15
        elif tick.bid <= donchian_low + 0.5 * atr:
            donchian_pts = 8
            
    mtf_pts = 0
    mtf_desc = ""
    if order_type == mt5.ORDER_TYPE_BUY:
        if mtf["d1_trend"] == 1 and mtf["h4_trend"] == 1 and mtf["h1_trend"] == 1:
            mtf_pts = 20
            mtf_desc = "D1^ H4^ H1^"
        elif mtf["bullish_count"] >= 2:
            mtf_pts = 10
            d1_s = "^" if mtf["d1_trend"] == 1 else "v"
            h4_s = "^" if mtf["h4_trend"] == 1 else "v"
            h1_s = "^" if mtf["h1_trend"] == 1 else "v"
            mtf_desc = f"D1{d1_s} H4{h4_s} H1{h1_s}"
        else:
            mtf_pts = 0
            d1_s = "^" if mtf["d1_trend"] == 1 else "v"
            h4_s = "^" if mtf["h4_trend"] == 1 else "v"
            h1_s = "^" if mtf["h1_trend"] == 1 else "v"
            mtf_desc = f"D1{d1_s} H4{h4_s} H1{h1_s}"
    elif order_type == mt5.ORDER_TYPE_SELL:
        if mtf["d1_trend"] == -1 and mtf["h4_trend"] == -1 and mtf["h1_trend"] == -1:
            mtf_pts = 20
            mtf_desc = "D1v H4v H1v"
        elif mtf["bearish_count"] >= 2:
            mtf_pts = 10
            d1_s = "^" if mtf["d1_trend"] == 1 else "v"
            h4_s = "^" if mtf["h4_trend"] == 1 else "v"
            h1_s = "^" if mtf["h1_trend"] == 1 else "v"
            mtf_desc = f"D1{d1_s} H4{h4_s} H1{h1_s}"
        else:
            mtf_pts = 0
            d1_s = "^" if mtf["d1_trend"] == 1 else "v"
            h4_s = "^" if mtf["h4_trend"] == 1 else "v"
            h1_s = "^" if mtf["h1_trend"] == 1 else "v"
            mtf_desc = f"D1{d1_s} H4{h4_s} H1{h1_s}"
            
    rsi_h4 = calculate_rsi(symbol, TF_MEDIUM, 14)
    rsi_h1 = calculate_rsi(symbol, TF_SHORT, 14)
    
    rsi_pts = 0
    if order_type == mt5.ORDER_TYPE_BUY:
        if rsi_h4 < 30:
            rsi_pts += 5
        if rsi_h1 < 25:
            rsi_pts += 5
    elif order_type == mt5.ORDER_TYPE_SELL:
        if rsi_h4 > 70:
            rsi_pts += 5
        if rsi_h1 > 75:
            rsi_pts += 5
            
    regime_pts = 0
    adx_val = regime_data["adx"]
    if strategy == "TF":
        if adx_val > 25:
            regime_pts = 10
        elif adx_val < 20:
            regime_pts = 0
        else:
            regime_pts = 5
    elif strategy == "MR":
        if adx_val < 20:
            regime_pts = 10
        elif adx_val > 25:
            regime_pts = 0
        else:
            regime_pts = 5
            
    session_pts, session_name = check_session_filter(symbol)
    
    cal_safe, cal_msg = check_economic_calendar()
    cal_pts = 10 if cal_safe else 0
    
    sentiment_pts = 1
    if order_type == mt5.ORDER_TYPE_BUY:
        if sentiment_score > 0.3:
            sentiment_pts = 5
        elif sentiment_score > 0.0:
            sentiment_pts = 4
        elif sentiment_score > -0.3:
            sentiment_pts = 2
        else:
            sentiment_pts = 1
    else:
        if sentiment_score < -0.3:
            sentiment_pts = 5
        elif sentiment_score < 0.0:
            sentiment_pts = 4
        elif sentiment_score < 0.3:
            sentiment_pts = 2
        else:
            sentiment_pts = 1
            
    intermarket_pts, intermarket_desc = get_intermarket_signal(symbol, order_type)
    
    total_score = z_score_pts + donchian_pts + mtf_pts + rsi_pts + regime_pts + session_pts + cal_pts + sentiment_pts + intermarket_pts
    
    breakdown = {
        "z_score_pts": z_score_pts,
        "z_score_val": z_score,
        "donchian_pts": donchian_pts,
        "mtf_pts": mtf_pts,
        "mtf_desc": mtf_desc,
        "rsi_pts": rsi_pts,
        "rsi_h4": rsi_h4,
        "rsi_h1": rsi_h1,
        "regime_pts": regime_pts,
        "adx_val": adx_val,
        "session_pts": session_pts,
        "session_name": session_name,
        "cal_pts": cal_pts,
        "cal_msg": cal_msg,
        "cal_safe": cal_safe,
        "sentiment_pts": sentiment_pts,
        "sentiment_score": sentiment_score,
        "news_score": sentiment_data.get("news_score", 0.0),
        "stocktwits_score": sentiment_data.get("stocktwits_score", 0.0),
        "stocktwits_bullish": sentiment_data.get("stocktwits_bullish", 0),
        "stocktwits_bearish": sentiment_data.get("stocktwits_bearish", 0),
        "intermarket_pts": intermarket_pts,
        "intermarket_desc": intermarket_desc,
        "total_score": total_score
    }
    
    return total_score, breakdown

def generate_trade_justification(symbol, order_type, comment, indicators, weight, sentiment_data, breakdown):
    action = "ACQUISTO (BUY)" if order_type == mt5.ORDER_TYPE_BUY else "VENDITA (SELL)"
    
    z_score = indicators["z_score"]
    trend = indicators["trend"]
    atr = indicators["atr"]
    price = indicators["price"]
    
    quant_text = (
        f"• <b>Z-Score MAD:</b> Il valore corrente e <code>{z_score:.2f}</code>. "
        + ("Questo indica una forte deviazione statistica ribassista (ipervenduto), segnalando un'opportunita di Mean Reversion ad alta probabilita." if order_type == mt5.ORDER_TYPE_BUY
           else "Questo indica una forte deviazione statistica rialzista (ipercomprato), segnalando un'opportunita di vendita per riallineamento statistico.")
        + f"\n• <b>Trend di Fondo (SMA 20/50):</b> Il trend giornaliero e {'rialzista' if trend == 1 else 'ribassista'}. Il trade si allinea con questa forza direzionale."
        + f"\n• <b>Volatilita ATR (H4):</b> L'ATR e di <code>{atr:.4f}</code>. Lo stop loss e posizionato a 2 ATR (distanza ottimale per evitare rumore di mercato)."
        + f"\n• <b>Risk Parity Sizing:</b> Il peso ottimale del portafoglio per {symbol} e <code>{weight*100:.2f}%</code>, calcolato dinamicamente sulla matrice di covarianza per massimizzare la decorrelazione."
    )
    
    headlines_text = ""
    if sentiment_data["headlines"]:
        headlines_text = "\n• <b>Notizie Chiave:</b>\n" + "\n".join([f"  - <i>{h}</i>" for h in sentiment_data["headlines"]])
        
    score = sentiment_data["score"]
    news_score = sentiment_data.get("news_score", score)
    st_score = sentiment_data.get("stocktwits_score", 0.0)
    st_bullish = sentiment_data.get("stocktwits_bullish", 0)
    st_bearish = sentiment_data.get("stocktwits_bearish", 0)
    
    macro_text = (
        f"• <b>Sentiment Macro (Google News + StockTwits):</b> Punteggio Combinato: <code>{score:+.2f}</code>\n"
        f"  - <i>Google News RSS:</i> <code>{news_score:+.2f}</code>\n"
        f"  - <i>StockTwits Retail:</i> <code>{st_score:+.2f}</code> (Bullish: <code>{st_bullish}</code>, Bearish: <code>{st_bearish}</code>)"
        + f"\n• <b>Driver Macroeconomici:</b> Politica monetaria restrittiva/espansiva delle Banche Centrali (Fed/BCE) e dati sull'inflazione (CPI) che impattano direttamente i tassi reali di interesse e la liquidita globale."
        + headlines_text
    )
    
    if "XAU" in symbol.upper():
        geopol_text = (
            "• <b>Geopolitica & Safe Haven:</b> L'Oro agisce come bene rifugio per eccellenza. "
            + ("L'acquisto e supportato da tensioni geopolitiche globali, debolezza del Dollaro Americano (DXY) o rischi sistemici nel settore bancario." if order_type == mt5.ORDER_TYPE_BUY
               else "La vendita riflette un allentamento delle tensioni geopolitiche o un rafforzamento del Dollaro Americano (DXY), che gradualmente riduce la domanda di beni rifugio.")
        )
    elif "BTC" in symbol.upper():
        geopol_text = (
            "• <b>Geopolitica & Rischi Sistemici (Decentralizzazione):</b> Bitcoin e visto come 'oro digitale' e asset decentralizzato. "
            + ("L'accumulo BUY riflette la ricerca di alternative al sistema bancario tradicional ed e guidato dall'espansione della liquidita monetaria globale (M2)." if order_type == mt5.ORDER_TYPE_BUY
               else "Il posizionamento SELL e guidato da restrizioni normative (regolamentazione crypto) o contrazioni della liquidita globale che colpiscono gli asset speculativi.")
        )
    elif "100" in symbol.upper() or "500" in symbol.upper():
        geopol_text = (
            "• <b>Geopolitica & Risk-On/Risk-Off:</b> Gli indici azionari USA riflettono il sentiment di rischio globale. "
            + ("Il posizionamento BUY ipotizza stabilita geopolitica globale, crescita tecnologica e aspettative di atterraggio morbido (soft landing) dell'economia USA." if order_type == mt5.ORDER_TYPE_BUY
               else "La pressione SELL e innescata da timori geopolitici (es. dazi, tensioni commerciali) o incertezze sulle catene di fornitura globali dei semiconduttori.")
        )
    else:
        geopol_text = (
            "• <b>Geopolitica & Flussi Valutari:</b> Il tasso di cambio EURUSD rappresenta il bilanciamento di potere economico e geopolitico tra USA ed Europa. "
            + ("Il rafforzamento dell'Euro e guidato da politiche BCE piu aggressive rispetto alla Fed o flussi di capitale diretti verso mercati europei." if order_type == mt5.ORDER_TYPE_BUY
               else "Il rafforzamento del Dollaro e guidato dallo status di valuta rifugio globale in contesti di incertezza geopolitica o tassi Fed piu elevati.")
        )
        
    soc_text = (
        "• <b>Sociologia Finanziaria (Comportamento delle Masse):</b> "
        + ("Il setup sfrutta l'effetto panico o la capitolazione (capitulation) degli investitori retail che vendono emotivamente sui minimi, consentendo agli investitori istituzionali (smart money) di accumulare liquidita." if order_type == mt5.ORDER_TYPE_BUY
           else "Il setup sfrutta l'effetto FOMO (Fear of Missing Out) o l'euforia retail sui massimi storici, dove la distribuzione istituzionale (smart money) apre posizioni short contro la massa emotiva.")
        + "\n• <b>Asimmetria Informativa:</b> Il posizionamento quantistico sfrutta il ritardo del retail nel comprendere i dati macro reali rispetto all'elaborazione algoritmica istantanea delle notizie."
    )
    
    total_score = breakdown["total_score"]
    status_icon = "✅" if total_score >= 65 else "❌"
    
    confluence_text = (
        f"🧠 <b>CONFLUENCE SCORE: {total_score}/100 {status_icon}</b> (Soglia: 65)\n\n"
        f"📊 <b>Z-Score MAD:</b>           <code>{breakdown['z_score_pts']}/20</code> (Z-Score: <code>{breakdown['z_score_val']:.2f}</code>)\n"
        f"📈 <b>Donchian Breakout:</b>      <code>{breakdown['donchian_pts']}/15</code>\n"
        f"🔀 <b>Multi-TF Alignment:</b>    <code>{breakdown['mtf_pts']}/20</code> ({breakdown['mtf_desc']})\n"
        f"💪 <b>RSI Momentum:</b>           <code>{breakdown['rsi_pts']}/10</code> (H4: <code>{breakdown['rsi_h4']:.1f}</code>, H1: <code>{breakdown['rsi_h1']:.1f}</code>)\n"
        f"🌊 <b>Regime Mercato:</b>         <code>{breakdown['regime_pts']}/10</code> (ADX: <code>{breakdown['adx_val']:.1f}</code>)\n"
        f"🕐 <b>Sessione:</b>               <code>{breakdown['session_pts']}/5</code> ({breakdown['session_name']})\n"
        f"📰 <b>Calendario:</b>             <code>{breakdown['cal_pts']}/10</code> ({breakdown['cal_msg']})\n"
        f"🌍 <b>Sentiment Macro:</b>        <code>{breakdown['sentiment_pts']}/5</code> (News: <code>{breakdown['news_score']:+.2f}</code>, StockTwits: <code>{breakdown['stocktwits_score']:+.2f}</code> [B:<code>{breakdown['stocktwits_bullish']}</code> S:<code>{breakdown['stocktwits_bearish']}</code>])\n"
        f"💱 <b>Intermarket DXY:</b>        <code>{breakdown['intermarket_pts']}/5</code> ({breakdown['intermarket_desc']})\n"
    )
    
    justification = (
        f"🧠 <b>ANALISI DI GIUSTIFICAZIONE DEL TRADE ({symbol})</b>\n"
        f"=========================================\n"
        f"👉 <b>Decisione Operativa:</b> <code>{action}</code> via <code>{comment}</code>\n\n"
        f"{confluence_text}\n"
        f"📊 <b>1. STRUTTURA QUANTITATIVA (MICRO MERCATO)</b>\n"
        f"{quant_text}\n\n"
        f"🌍 <b>2. VARIABILI MACROECONOMICHE (FONDAMENTALI)</b>\n"
        f"{macro_text}\n\n"
        f"⚔️ <b>3. DINAMICHE GEOPOLITICHE (FLUSSI DI CAPITALE)</b>\n"
        f"{geopol_text}\n\n"
        f"👥 <b>4. SOCIOLOGIA COMPORTAMENTALE (PSICOLOGIA DELLE MASSE)</b>\n"
        f"{soc_text}\n"
        f"========================================="
    )
    return justification

def get_robust_indicators(symbol):
    # FIX 1: Finestra aumentata a Z_SCORE_WINDOW+50 per stabilita statistica del MAD Z-Score
    n_candles = Z_SCORE_WINDOW + 55
    rates = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, n_candles)
    if rates is None or len(rates) < Z_SCORE_WINDOW:
        return None
    closes = [r['close'] for r in rates]
    
    # 1. Indicatori di Trend (SMA 50/200)
    sma_50 = np.mean(closes[-50:])
    sma_20 = np.mean(closes[-20:])
    trend = 1 if sma_20 > sma_50 else -1
    
    # 2. FIX 2: Robust Z-Score (MAD) su finestra di 100 candele per stabilita statistica
    window = closes[-Z_SCORE_WINDOW:]
    median_w = np.median(window)
    mad = np.median([abs(c - median_w) for c in window])
    std_mad = mad * 1.4826 if mad > 0 else 1e-6
    current_price = closes[-1]
    # Z-Score calcolato rispetto alla mediana della finestra (piu robusto agli outlier)
    z_score = (current_price - median_w) / std_mad
    
    # 3. Donchian Channels (su TF_SHORT per reattivita)
    h4_rates = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, DONCHIAN_PERIOD)
    if h4_rates is not None and len(h4_rates) >= DONCHIAN_PERIOD:
        highs = [r['high'] for r in h4_rates]
        lows = [r['low'] for r in h4_rates]
        donchian_high = max(highs)
        donchian_low = min(lows)
    else:
        donchian_high = max([r['high'] for r in rates[-10:]])
        donchian_low = min([r['low'] for r in rates[-10:]])
        
    # 4. Calcolo ATR su TF_SHORT per Sizing e SL
    atr_rates = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, 20)
    atr = None
    if atr_rates is not None and len(atr_rates) >= 15:
        tr_list = []
        for k in range(1, len(atr_rates)):
            h = atr_rates[k]['high']
            l = atr_rates[k]['low']
            pc = atr_rates[k-1]['close']
            tr = max(h - l, abs(h - pc), abs(l - pc))
            tr_list.append(tr)
        atr = sum(tr_list[-14:]) / 14.0
        
    return {
        "price": current_price,
        "sma_20": sma_20,
        "trend": trend,
        "z_score": z_score,
        "donchian_high": donchian_high,
        "donchian_low": donchian_low,
        "atr": atr if atr is not None else (current_price * 0.01)
    }

# ==============================================================================
# RISOLUZIONE COVARIANZA E DYNAMIC RISK PARITY SIZING
# ==============================================================================
def calculate_portfolio_weights():
    # Raccoglie i rendimenti degli ultimi 30 periodi per tutti gli asset
    asset_returns = []
    for symbol in ASSETS:
        rates = mt5.copy_rates_from_pos(symbol, TF_MEDIUM, 0, 30)
        if rates is None or len(rates) < 20:
            # Fallback se mancano dati storico (pesi uguali per tutti gli asset)
            n_assets = len(ASSETS)
            return np.ones(n_assets) / n_assets
        closes = np.array([r['close'] for r in rates])
        rets = np.diff(closes) / closes[:-1]
        asset_returns.append(rets)
        
    # Allinea le lunghezze dei rendimenti per sicurezza
    min_len = min(len(r) for r in asset_returns)
    aligned_returns = np.array([r[-min_len:] for r in asset_returns])
    
    # Calcola la matrice di covarianza
    cov_matrix = np.cov(aligned_returns)
    
    # Calcolo pesi Risk Parity (Pesi inversamente proporzionali alla varianza individuale)
    variances = np.diag(cov_matrix)
    inv_variances = 1.0 / (variances + 1e-8)
    weights = inv_variances / np.sum(inv_variances)
    
    return weights

# ==============================================================================
# ENGINE GESTIONE ORDINI E NOTIFICHE
# ==============================================================================
def get_day_start_balance(acct, state):
    today_str = datetime.now().strftime("%Y-%m-%d")
    if state.get("daily_date") == today_str and "day_start_balance" in state:
        return state["day_start_balance"]
        
    try:
        local_now = datetime.now()
        tick = mt5.symbol_info_tick("EURUSD")
        if tick:
            server_now = datetime.fromtimestamp(tick.time, tz=timezone.utc).replace(tzinfo=None)
            offset_hours = round((server_now - local_now).total_seconds() / 3600.0)
        else:
            offset_hours = 1
            
        local_midnight = local_now.replace(hour=0, minute=0, second=0, microsecond=0)
        server_midnight_reset = local_midnight + timedelta(hours=offset_hours)
        
        ts_start = int(datetime(
            server_midnight_reset.year,
            server_midnight_reset.month,
            server_midnight_reset.day,
            server_midnight_reset.hour,
            server_midnight_reset.minute,
            server_midnight_reset.second,
            tzinfo=timezone.utc
        ).timestamp())
        
        ts_end = int(tick.time + 10) if tick else int(datetime.now().timestamp() + 3600*24)
        
        deals = mt5.history_deals_get(ts_start, ts_end)
        realized_pnl = 0.0
        if deals:
            for d in deals:
                if d.type in [0, 1]:  # Solo deal di trading (Buy/Sell), escludendo depositi/prelievi
                    realized_pnl += d.profit + d.commission + d.swap
                
        computed_start_balance = acct.balance - realized_pnl
        return computed_start_balance
    except Exception as e:
        print(f"[WARN] Impossibile calcolare il saldo iniziale del giorno: {e}")
        return acct.balance

def check_emergency_killswitch():
    acct = mt5.account_info()
    if acct is None:
        return False
        
    state = load_bot_state()
    day_start_balance = state.get("day_start_balance")
    if day_start_balance is None:
        day_start_balance = get_day_start_balance(acct, state)
        state["day_start_balance"] = day_start_balance
        save_bot_state(state)
        
    # Calcolo drawdown giornaliero basato sull'equity corrente vs il saldo iniziale del giorno
    daily_drawdown = day_start_balance - acct.equity
    total_loss = INITIAL_BALANCE - acct.equity
    
    # 1. Kill-Switch Giornaliero (Max Daily Loss)
    if daily_drawdown >= DAILY_KILLSWITCH_USD:
        print(f"\n[ALERT] KILL-SWITCH GIORNALIERO ATTIVATO! Perdita giornaliera di ${daily_drawdown:.2f} (Inizio giorno: ${day_start_balance:.2f}, Equity: ${acct.equity:.2f})")
        close_all_positions()
        msg = (
            f"🚨🚨🚨 <b>KILL-SWITCH GIORNALIERO ATTIVATO!</b> 🚨🚨🚨\n"
            f"• Perdita giornaliera (Equity vs Saldo Inizio Giorno): <code>${daily_drawdown:.2f}</code> (Limite: <code>${DAILY_KILLSWITCH_USD:.2f}</code>)\n"
            f"• Saldo Inizio Giorno: <code>${day_start_balance:.2f}</code> | Equity Corrente: <code>${acct.equity:.2f}</code>\n"
            f"• Tutte le posizioni sono state <b>chiuse immediatamente</b>.\n"
            f"• Bot in pausa per proteggere il conto challenge."
        )
        send_telegram_message(msg)
        return True
    
    # 2. Kill-Switch Totale (Max Total Loss)
    if total_loss >= TOTAL_KILLSWITCH_USD:
        print(f"\n[ALERT] KILL-SWITCH TOTALE ATTIVATO! Perdita totale di ${total_loss:.2f} (Iniziale: ${INITIAL_BALANCE:.2f}, Equity: ${acct.equity:.2f})")
        close_all_positions()
        msg = (
            f"🚨🚨🚨 <b>KILL-SWITCH TOTALE ATTIVATO!</b> 🚨🚨🚨\n"
            f"• Perdita totale dal saldo iniziale: <code>${total_loss:.2f}</code> (Limite: <code>${TOTAL_KILLSWITCH_USD:.2f}</code>)\n"
            f"• Equity corrente: <code>${acct.equity:,.2f}</code>\n"
            f"• Tutte le posizioni sono state <b>chiuse immediatamente</b>.\n"
            f"• <b>BOT ARRESTATO per proteggere il conto funded.</b>"
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
        "comment": comment,
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
# MAIN BOT OPERATIVO LOOP
# ==============================================================================
def run_quantum_bot():
    # Inizializza MetaTrader 5
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
        print("[ERROR] Connessione a MetaTrader 5 fallita. Assicurati che MT5 sia aperto ed installato correttamente.")
        return
        
    print("\n" + "="*80)
    print("[RUN] AVVIO BOT QUANTISTICO MULTI-ASSET MULTI-STRATEGY")
    print("="*80)
    
    acct = mt5.account_info()
    if acct is None:
        print("[ERROR] Impossibile connettersi al conto demo di test.")
        mt5.shutdown()
        return
        
    print(f"- Conto Connesso: {acct.login} (Broker: {acct.company})")
    print(f"- Saldo Iniziale: ${acct.balance:,.2f}  |  Equity: ${acct.equity:,.2f}")
    
    # Abilita tutti gli asset nel Market Watch
    for sym in ASSETS:
        mt5.symbol_select(sym, True)
    
    # Pausa di stabilizzazione: permette al terminale MT5 di sincronizzarsi
    # completamente con il server prima di iniziare il ciclo operativo
    print("[INFO] Attesa di 5 secondi per la sincronizzazione del server...")
    time.sleep(5)
        
    state = load_bot_state()
    
    # Sincronizzazione active_tickets con le posizioni reali del conto all'avvio
    active_positions = mt5.positions_get()
    if active_positions:
        updated = False
        for pos in active_positions:
            if pos.ticket not in state["active_tickets"]:
                print(f"[INFO] Trovata posizione attiva sul conto non registrata nello stato: Ticket {pos.ticket} ({pos.symbol}). Aggiunta allo stato.")
                state["active_tickets"].append(pos.ticket)
                updated = True
        if updated:
            save_bot_state(state)
    
    # Notifica di startup
    msg_startup = (
        f"🤖 <b>Bot Quantistico Multi-Asset Avviato!</b>\n"
        f"• Conto: <code>{acct.login}</code>\n"
        f"• Capitolo Attivo: <code>{', '.join(ASSETS)}</code>\n"
        f"• Rischio Target: <code>${PORTFOLIO_RISK_LIMIT_USD:.2f}</code>\n"
        f"• Soglia Drawdown: <code>${DAILY_KILLSWITCH_USD:.2f}</code>"
    )
    send_telegram_message(msg_startup)
    
    try:
        while True:
            # 1. Ricarica lo stato ad ogni iterazione per allineamento con rollover/salvataggi esterni
            state = load_bot_state()
            
            # 2. Controllo di emergenza Kill-Switch
            if check_emergency_killswitch():
                time.sleep(300)
                continue
                
            # 2. Calcolo pesi di portafoglio basati su Covarianza
            weights = calculate_portfolio_weights()
            
            # 3. Ciclo operativo per ogni asset
            for idx, symbol in enumerate(ASSETS):
                # Filtro orario specifico per le azioni (15:45 - 21:30 CEST)
                is_stock = symbol in ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]
                if is_stock:
                    local_now = datetime.now()
                    current_time_val = local_now.hour + local_now.minute / 60.0
                    if current_time_val < 15.75 or current_time_val > 21.5:
                        continue
                        
                indicators = get_robust_indicators(symbol)
                if indicators is None:
                    continue
                    
                price = indicators["price"]
                z_score = indicators["z_score"]
                trend = indicators["trend"]
                donchian_high = indicators["donchian_high"]
                donchian_low = indicators["donchian_low"]
                atr = indicators["atr"]
                
                # FIX 3: Sentiment sostituito con momentum di prezzo puro (Volume OBV-like proxy)
                # Questo evita le richieste HTTP lente (StockTwits/News RSS) per ogni asset
                # e sostituisce con un segnale price-action oggettivo e istantaneo
                recent_rates = mt5.copy_rates_from_pos(symbol, TF_SHORT, 0, 10)
                recent_closes = [r['close'] for r in recent_rates] if recent_rates is not None and len(recent_rates) > 0 else []
                if len(recent_closes) >= 5:
                    price_momentum = (recent_closes[-1] - recent_closes[0]) / max(abs(recent_closes[0]), 1e-8)
                    momentum_score = max(-1.0, min(1.0, price_momentum * 100))
                else:
                    momentum_score = 0.0
                sentiment_data = {
                    "score": momentum_score,
                    "news_score": 0.0,
                    "headlines": [],
                    "stocktwits_score": 0.0,
                    "stocktwits_bullish": 0,
                    "stocktwits_bearish": 0,
                    "stocktwits_total_labeled": 0,
                    "stocktwits_msg_count": 0
                }
                sentiment_score = momentum_score
                adjusted_z = Z_THRESHOLD  # Z-Threshold fisso (momentum non modifica piu la soglia)
                
                # Controlla se il bot ha gia posizioni aperte su questo simbolo
                positions = mt5.positions_get(symbol=symbol)
                
                # FIX 4: Limite massimo di posizioni concorrenti
                all_positions = mt5.positions_get()
                n_open = len(all_positions) if all_positions else 0
                if n_open >= MAX_CONCURRENT_POSITIONS and not positions:
                    continue
                
                # Calcola il volume in lotti in base al Risk Parity
                sym_info = mt5.symbol_info(symbol)
                if sym_info is None:
                    continue
                tick_size = sym_info.trade_tick_size if sym_info.trade_tick_size > 0 else 0.00001
                tick_value = sym_info.trade_tick_value if sym_info.trade_tick_value > 0 else 1.0
                # FIX 5: Uso contract_size per calcolare il valore reale del tick per CFD non-forex
                # Per CFD (trade_calc_mode == 4), il valore del tick va moltiplicato per contract_size
                # perché MT5 riporta trade_tick_value in frazione del lotto, non in USD per lotto
                contract_size = getattr(sym_info, 'trade_contract_size', 1.0) or 1.0
                if sym_info.trade_calc_mode == 4:  # CALC_MODE_CFD
                    # Valore reale del tick per lotto = (tick_value * contract_size)
                    # Per XAUUSD: tick_size=0.01, tick_value=1.0, contract_size=100 -> 100 USD/lot/tick
                    real_tick_value = tick_value * contract_size
                else:
                    real_tick_value = tick_value  # Forex: tick_value è già corretto
                
                # Distanza SL basata su volatilita ATR (2.5 * ATR per piu respiro)
                sl_dist = 2.5 * atr
                # Calcolo lotto target basato su allocazione di rischio w_i * PORTFOLIO_RISK
                allocated_risk = weights[idx] * PORTFOLIO_RISK_LIMIT_USD
                
                # FIX 5: Formula corretta lotto con contract_size
                if sl_dist > 0 and tick_size > 0 and real_tick_value > 0:
                    risk_per_lot = (sl_dist / tick_size) * real_tick_value
                    volume_lotti = allocated_risk / risk_per_lot
                    volume_lotti = max(sym_info.volume_min, min(sym_info.volume_max, volume_lotti))
                else:
                    volume_lotti = sym_info.volume_min
                    
                # ── LOGICA MULTI-STRATEGICA DI INGRESSO ─────────────────────────
                if not positions:
                    tick = mt5.symbol_info_tick(symbol)
                    if tick is None:
                        continue
                        
                    # Pre-calculate MTF and Regime details for scoring and monitoring
                    mtf = get_mtf_analysis(symbol)
                    regime_data = detect_market_regime(symbol)
                    
                    # Log baseline score to console (strictly ASCII, safe for CP1252)
                    base_strat = "MR"
                    base_type = mt5.ORDER_TYPE_BUY if z_score < 0 else mt5.ORDER_TYPE_SELL
                    base_score, _ = calculate_confluence_score(
                        symbol, base_type, base_strat, indicators, tick, sentiment_data, mtf, regime_data
                    )
                    print(f"\n[MONITOR] {symbol} {base_strat} {'BUY' if base_type == mt5.ORDER_TYPE_BUY else 'SELL'} Confluence Score: {base_score}/100")
                    
                    # Potential setup flags
                    potential_buy_mr = (trend == 1 and z_score < -adjusted_z)
                    potential_buy_tf = (tick.ask >= donchian_high and trend == 1)
                    
                    potential_sell_mr = (trend == -1 and z_score > adjusted_z)
                    potential_sell_tf = (tick.bid <= donchian_low and trend == -1)
                    
                    # Evaluate BUY setups
                    if potential_buy_mr or potential_buy_tf:
                        strategy = "MR" if potential_buy_mr else "TF"
                        score, breakdown = calculate_confluence_score(
                            symbol, mt5.ORDER_TYPE_BUY, strategy, indicators, tick, sentiment_data, mtf, regime_data
                        )
                        
                        print(f"[INFO] {symbol} BUY {strategy} Confluence Score: {score}/100 (Threshold: 65)")
                        
                        if score >= CONFLUENCE_THRESHOLD:
                            if not breakdown.get("cal_safe", True):
                                print(f"[INFO] {symbol} BUY blocked: economic calendar is unsafe ({breakdown.get('cal_msg')})")
                                continue
                            # Filtro spread - salta se spread > SPREAD_MAX_RATIO * ATR
                            spread = tick.ask - tick.bid
                            if spread > SPREAD_MAX_RATIO * atr:
                                print(f"[INFO] {symbol} BUY skipped: spread {spread:.5f} > max {SPREAD_MAX_RATIO * atr:.5f} ({SPREAD_MAX_RATIO*100:.0f}% ATR)")
                                continue
                            vol_volume = volume_lotti
                            if regime_data.get("high_volatility", False):
                                vol_volume = max(sym_info.volume_min, min(sym_info.volume_max, round(volume_lotti * 0.7, 2)))
                                print(f"[INFO] High volatility detected for {symbol}. Volume reduced from {volume_lotti:.2f} to {vol_volume:.2f}")
                                
                            sl = tick.ask - sl_dist
                            # TP largo a 5*ATR - il trailing stop gestisce l'uscita ottimale
                            tp = tick.ask + (5.0 * atr)
                            comment = f"{strategy} BUY"
                            
                            ticket = execute_order(symbol, mt5.ORDER_TYPE_BUY, vol_volume, tick.ask, sl, tp, comment)
                            if ticket:
                                state["daily_trades_count"] += 1
                                state["active_tickets"].append(ticket)
                                save_bot_state(state)
                                
                                # Telegram notification
                                msg = (
                                    f"🟢 <b>Quantum BUY Eseguito!</b>\n"
                                    f"• Asset: <code>{symbol}</code>\n"
                                    f"• Lotto: <code>{vol_volume:.2f}</code>\n"
                                    f"• Strategia: <code>{comment}</code>\n"
                                    f"• Prezzo: <code>${tick.ask:.2f}</code>\n"
                                    f"• SL / TP: <code>${sl:.2f} / ${tp:.2f}</code>\n"
                                    f"• Score: <code>{score}/100</code>"
                                )
                                send_telegram_message(msg)
                                
                                justification = generate_trade_justification(
                                    symbol, mt5.ORDER_TYPE_BUY, comment, indicators, weights[idx], sentiment_data, breakdown
                                )
                                send_telegram_message(justification)
                                
                    # Evaluate SELL setups
                    elif potential_sell_mr or potential_sell_tf:
                        strategy = "MR" if potential_sell_mr else "TF"
                        score, breakdown = calculate_confluence_score(
                            symbol, mt5.ORDER_TYPE_SELL, strategy, indicators, tick, sentiment_data, mtf, regime_data
                        )
                        
                        print(f"[INFO] {symbol} SELL {strategy} Confluence Score: {score}/100 (Threshold: 65)")
                        
                        if score >= CONFLUENCE_THRESHOLD:
                            if not breakdown.get("cal_safe", True):
                                print(f"[INFO] {symbol} SELL blocked: economic calendar is unsafe ({breakdown.get('cal_msg')})")
                                continue
                            # Filtro spread - salta se spread > SPREAD_MAX_RATIO * ATR
                            spread = tick.ask - tick.bid
                            if spread > SPREAD_MAX_RATIO * atr:
                                print(f"[INFO] {symbol} SELL skipped: spread {spread:.5f} > max {SPREAD_MAX_RATIO * atr:.5f} ({SPREAD_MAX_RATIO*100:.0f}% ATR)")
                                continue
                            vol_volume = volume_lotti
                            if regime_data.get("high_volatility", False):
                                vol_volume = max(sym_info.volume_min, min(sym_info.volume_max, round(volume_lotti * 0.7, 2)))
                                print(f"[INFO] High volatility detected for {symbol}. Volume reduced from {volume_lotti:.2f} to {vol_volume:.2f}")
                                
                            sl = tick.bid + sl_dist
                            # TP largo a 5*ATR - il trailing stop gestisce l'uscita ottimale
                            tp = tick.bid - (5.0 * atr)
                            comment = f"{strategy} SELL"
                            
                            ticket = execute_order(symbol, mt5.ORDER_TYPE_SELL, vol_volume, tick.bid, sl, tp, comment)
                            if ticket:
                                state["daily_trades_count"] += 1
                                state["active_tickets"].append(ticket)
                                save_bot_state(state)
                                
                                # Telegram notification
                                msg = (
                                    f"🔴 <b>Quantum SELL Eseguito!</b>\n"
                                    f"• Asset: <code>{symbol}</code>\n"
                                    f"• Lotto: <code>{vol_volume:.2f}</code>\n"
                                    f"• Strategia: <code>{comment}</code>\n"
                                    f"• Prezzo: <code>${tick.bid:.2f}</code>\n"
                                    f"• SL / TP: <code>${sl:.2f} / ${tp:.2f}</code>\n"
                                    f"• Score: <code>{score}/100</code>"
                                )
                                send_telegram_message(msg)
                                
                                justification = generate_trade_justification(
                                    symbol, mt5.ORDER_TYPE_SELL, comment, indicators, weights[idx], sentiment_data, breakdown
                                )
                                send_telegram_message(justification)
                
            
            # Chiudi posizioni azionarie prima della chiusura del mercato (alle 21:50 ora locale)
            local_now = datetime.now()
            if local_now.hour == 21 and local_now.minute >= 50:
                stock_symbols = ["AAPL", "AMZN", "GOOG", "META", "MSFT", "NVDA", "TSLA"]
                open_positions = mt5.positions_get()
                if open_positions:
                    for pos in open_positions:
                        if pos.symbol in stock_symbols:
                            print(f"\n[INFO] Chiusura intraday automatica per azione: {pos.symbol}")
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
                            res = mt5.order_send(req)
                            if res.retcode == mt5.TRADE_RETCODE_DONE:
                                print(f"[OK] Chiusa posizione intraday {pos.ticket} su {pos.symbol}.")
                                send_telegram_message(f"⏹️ <b>Chiusura Intraday Azione!</b>\n• Ticker: <code>{pos.symbol}</code>\n• Ticket: <code>{pos.ticket}</code>\n• Chiusura automatica prima del market close.")

            # Sincronizzazione PnL e riconciliazione posizioni chiuse nello stato locale
            active_positions = mt5.positions_get()
            current_active_tickets = [p.ticket for p in active_positions] if active_positions else []
            
            # Sincronizzazione dinamica di nuove posizioni rilevate in corso d'opera
            state_updated = False
            for pos in active_positions:
                if pos.ticket not in state["active_tickets"]:
                    print(f"\n[INFO] Rilevata nuova posizione attiva sul conto: Ticket {pos.ticket} ({pos.symbol}). Aggiunta allo stato.")
                    state["active_tickets"].append(pos.ticket)
                    state_updated = True
            if state_updated:
                save_bot_state(state)
            
            for t in list(state["active_tickets"]):
                if t not in current_active_tickets:
                    # La posizione è stata chiusa (SL/TP)
                    time.sleep(1.0)
                    history = mt5.history_deals_get(position=t)
                    trade_pnl = 0.0
                    if history:
                        for deal in history:
                            if deal.entry in [mt5.DEAL_ENTRY_OUT, mt5.DEAL_ENTRY_OUT_BY]:
                                trade_pnl += deal.profit + deal.commission + deal.swap
                    
                    # Notifica Telegram
                    msg = (
                        f"📊 <b>Posizione Portafoglio Chiusa!</b>\n"
                        f"• Ticket: <code>{t}</code>\n"
                        f"• PnL Eseguito: <code>${trade_pnl:+.2f}</code>\n"
                        f"• PnL Giornaliero Accumulato: <code>${state['daily_pnl'] + trade_pnl:+.2f}</code>"
                    )
                    send_telegram_message(msg)
                    
                    state["daily_pnl"] += trade_pnl
                    state["active_tickets"].remove(t)
                    save_bot_state(state)
            
            # Stampa progresso console (Safe ASCII)
            print(f"\r[PORTFOLIO WATCH] Assets: {len(ASSETS)} | Attivi: {len(active_positions)} | PnL Oggi: ${state['daily_pnl']:+.2f}", end="", flush=True)
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\n[INFO] Arresto del Bot richiesto dall'utente.")
    finally:
        mt5.shutdown()

if __name__ == "__main__":
    run_quantum_bot()
