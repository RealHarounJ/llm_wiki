#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
🏆 Gold Momentum & Sentiment Swing Trader (AMSR Strategy)
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione:
  1. Scarica i dati storici reali del prezzo dell'oro da AurumRates API.
  2. Effettua lo scraping delle ultime notizie sull'oro tramite feed RSS
     di Google News ed esegue un'analisi del sentiment basata su un dizionario
     macroeconomico quantitativo.
  3. Calcola il Trend (SMA 50) e l'ipercomprato/ipervenduto statistico tramite
     lo Z-Score robusto (basato sulla Median Absolute Deviation - MAD a 20 giorni).
  4. Esegue un backtest storico completo simulando la strategia multi-day swing
     (con Stop Loss, Take Profit e Trailing Stop robusti).
  5. Genera una Dashboard quantitativa per il terminale e calcola il segnale
     operativo odierno (COMPRA / VENDI / MANTIENI).
Requisiti: Python 3.x (Libreria standard, senza dipendenze esterne)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# Impostazioni strategiche
SMA_FAST_WINDOW = 20
SMA_SLOW_WINDOW = 50
Z_THRESHOLD = 1.0      # Z-Score per ingressi (ottimizzato per bilanciare selettività e partecipazione)
RISK_FREE_RATE = 0.025 # 2.5% annuo
TRADING_DAYS = 252

# Dizionario del sentiment quantitativo dell'oro (Macro-driven)
BULLISH_WORDS = [
    "inflation", "recession", "crisis", "cut", "cuts", "war", "geopolitical", 
    "uncertainty", "stimulus", "easing", "buy", "buying", "purchases", "demand", 
    "deficit", "debt", "safe-haven", "haven", "risk-off", "tension", "tensions", 
    "escalation", "banks", "biden", "fed", "powell", "gold", "bullion", "metals"
]

BEARISH_WORDS = [
    "recovery", "growth", "hike", "hikes", "hawkish", "tightening", "strong", 
    "sell", "selling", "drop", "fall", "peace", "stability", "yields", "dollar", 
    "usd", "strengthens", "bearish", "crash", "plunge", "declines", "down"
]

# 1. Recupero Dati Storici Oro da AurumRates
def fetch_gold_historical_data():
    url = "https://aurumrates.com/api/chart"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print("📥 Connessione alle API di AurumRates...")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            timestamps = data.get("timestamps", [])
            closes = data.get("closes", [])
            symbol = data.get("symbol", "GC=F")
            
            # Costruzione dei record storici con forward-fill / backward-fill robusto per dati mancanti (None)
            history = []
            last_valid_close = None
            
            # Primo passaggio per trovare il primo valore non nullo per eventuale backward-fill iniziale
            for c in closes:
                if c is not None:
                    last_valid_close = float(c)
                    break
            
            for t, c in zip(timestamps, closes):
                if c is not None:
                    last_valid_close = float(c)
                
                if last_valid_close is not None:
                    date_str = datetime.fromtimestamp(t).strftime('%Y-%m-%d')
                    history.append({
                        "date": date_str,
                        "timestamp": t,
                        "close": last_valid_close
                    })
            
            # Ordina per data crescente
            history.sort(key=lambda x: x["date"])
            print(f"✅ Recuperati {len(history)} record storici per l'Oro ({symbol})!")
            return history
    except Exception as e:
        print(f"❌ Errore nel download dei dati storici: {e}")
        sys.exit(1)

# 2. Scraping Notizie RSS (Google News) ed estrazione del Sentiment
def fetch_gold_news_sentiment():
    # Cerca notizie legate a "gold inflation crisis" in inglese
    query = "gold+inflation+recession+crisis+fed"
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    print("📰 Ingestione delle notizie macroeconomiche sull'Oro in corso...")
    
    try:
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            articles = []
            sentiment_scores = []
            
            # Il feed di Google News memorizza le notizie nei nodi <item>
            for item in root.findall('.//item')[:30]: # Prendi i primi 30 articoli più recenti
                title = item.find('title').text
                pub_date = item.find('pubDate').text
                link = item.find('link').text
                
                # Calcola il sentiment basato sulle parole chiave
                title_lower = title.lower()
                bull_count = sum(1 for w in BULLISH_WORDS if w in title_lower)
                bear_count = sum(1 for w in BEARISH_WORDS if w in title_lower)
                
                # Punteggio semplice tra -1.0 (bearish) e +1.0 (bullish)
                total = bull_count + bear_count
                score = (bull_count - bear_count) / total if total > 0 else 0.0
                
                sentiment_scores.append(score)
                articles.append({
                    "title": title,
                    "score": score,
                    "pub_date": pub_date
                })
                
            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
            print(f"✅ Analizzati {len(articles)} articoli. Sentiment Medio: {avg_sentiment:+.3f}")
            return avg_sentiment, articles
            
    except Exception as e:
        print(f"⚠️ Impossibile recuperare notizie (RSS): {e}. Utilizzo sentiment neutro.")
        return 0.0, []

# 3. Calcolo Statistiche Robuste e Indicatori Quantitativi (Z-Score basato su MAD)
def calculate_indicators(history):
    prices = [h["close"] for h in history]
    n = len(prices)
    
    # Inizializziamo i campi
    for h in history:
        h["sma_50"] = None
        h["sma_20"] = None
        h["mad_20"] = None
        h["z_score"] = None
        h["trend"] = None # 1 = Bullish, -1 = Bearish
        
    for i in range(SMA_FAST_WINDOW, n):
        # 1. SMA 20
        window_20 = prices[i - SMA_FAST_WINDOW + 1: i + 1]
        sma_20 = sum(window_20) / SMA_FAST_WINDOW
        history[i]["sma_20"] = sma_20
        
        # 2. Calcolo della Median Absolute Deviation (MAD) standardizzata a 20 giorni
        median_price = sorted(window_20)[SMA_FAST_WINDOW // 2]
        absolute_deviations = [abs(p - median_price) for p in window_20]
        mad = sorted(absolute_deviations)[SMA_FAST_WINDOW // 2]
        
        # Gaussian consistency factor (1.4826)
        std_mad = mad * 1.4826 if mad > 0 else 1e-6
        history[i]["mad_20"] = std_mad
        
        # 3. Robust Z-Score
        current_price = prices[i]
        z_score = (current_price - sma_20) / std_mad
        history[i]["z_score"] = z_score
        
        # 4. SMA 50 (Trend Filter)
        if i >= SMA_SLOW_WINDOW - 1:
            window_50 = prices[i - SMA_SLOW_WINDOW + 1: i + 1]
            sma_50 = sum(window_50) / SMA_SLOW_WINDOW
            history[i]["sma_50"] = sma_50
            history[i]["trend"] = 1 if sma_20 > sma_50 else -1
            
    return history

# 4. Simulatore di Backtest Storico
def run_backtest(history, sentiment_score):
    """
    Esegue il backtest della strategia AMSR sullo storico dell'oro.
    Restituisce i log delle transazioni e le metriche di performance finali.
    """
    initial_cash = 10000.0
    cash = initial_cash
    cash_before_trade = initial_cash
    position = None  # None, 'LONG', o 'SHORT'
    shares = 0.0
    entry_price = 0.0
    stop_loss = 0.0
    take_profit = 0.0
    highest_price = 0.0 # Per il trailing stop
    lowest_price = 999999.0  # Per il trailing stop
    
    trades = []
    equity_history = []
    
    # Il backtest inizia dal giorno 50 (dove abbiamo SMA_50 e Z-Score pronti)
    for i in range(SMA_SLOW_WINDOW, len(history)):
        day = history[i]
        price = day["close"]
        z = day["z_score"]
        trend = day["trend"]
        date = day["date"]
        
        current_equity = cash + (shares * price if position == 'LONG' else (-shares * price + 2 * shares * entry_price if position == 'SHORT' else 0.0))
        equity_history.append({"date": date, "equity": current_equity})
        
        # Calcolo Stop Loss e Take Profit dinamico basato sulla deviazione standard MAD
        mad_vol = day["mad_20"]
        
        if position is None:
            # ── LOGICA DI INGRESSO (SOGGETTA A SENTIMENT) ──────────────────────
            # Filtro sentiment: Il sentiment positivo aumenta il trigger long, il sentiment negativo il short
            adjusted_z_threshold = Z_THRESHOLD - (sentiment_score * 0.3)
            
            # LONG Entry: Trend rialzista e Z-Score indica ipervenduto (dip)
            if trend == 1 and z < -adjusted_z_threshold:
                position = 'LONG'
                cash_before_trade = cash
                shares = cash / price
                cash = 0.0
                entry_price = price
                stop_loss = price - (2.0 * mad_vol)
                take_profit = price + (3.5 * mad_vol)
                highest_price = price
                trades.append({
                    "type": "BUY_LONG",
                    "entry_date": date,
                    "entry_price": price,
                    "stop_loss": stop_loss,
                    "take_profit": take_profit
                })
                
            # SHORT Entry: Trend ribassista e Z-Score indica ipercomprato (peak)
            elif trend == -1 and z > adjusted_z_threshold:
                position = 'SHORT'
                cash_before_trade = cash
                shares = cash / price
                cash = 0.0
                entry_price = price
                stop_loss = price + (2.0 * mad_vol)
                take_profit = price - (3.5 * mad_vol)
                lowest_price = price
                trades.append({
                    "type": "SELL_SHORT",
                    "entry_date": date,
                    "entry_price": price,
                    "stop_loss": stop_loss,
                    "take_profit": take_profit
                })
                
        elif position == 'LONG':
            # Aggiornamento Trailing Stop
            if price > highest_price:
                highest_price = price
                # Alza lo stop loss per proteggere i profitti
                new_stop = price - (2.0 * mad_vol)
                if new_stop > stop_loss:
                    stop_loss = new_stop
                    trades[-1]["stop_loss"] = stop_loss
            
            # ── LOGICA DI USCITA LONG ──────────────────────────────────────────
            # 1. Stop Loss o Trailing Stop colpito
            if price <= stop_loss:
                cash = shares * price
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "STOP_LOSS",
                    "pnl": cash - (trades[-1]["entry_price"] * (cash / price))
                })
            # 2. Take Profit colpito
            elif price >= take_profit:
                cash = shares * price
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "TAKE_PROFIT",
                    "pnl": cash - (trades[-1]["entry_price"] * (cash / price))
                })
            # 3. Uscita per inversione di trend
            elif trend == -1:
                cash = shares * price
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "TREND_REVERSAL",
                    "pnl": cash - (trades[-1]["entry_price"] * (cash / price))
                })
                
        elif position == 'SHORT':
            # Aggiornamento Trailing Stop
            if price < lowest_price:
                lowest_price = price
                # Abbassa lo stop loss per lo short
                new_stop = price + (2.0 * mad_vol)
                if new_stop < stop_loss:
                    stop_loss = new_stop
                    trades[-1]["stop_loss"] = stop_loss
                    
            # ── LOGICA DI USCITA SHORT ─────────────────────────────────────────
            # 1. Stop Loss o Trailing Stop colpito
            if price >= stop_loss:
                pnl = (entry_price - price) * shares
                cash = cash_before_trade + pnl
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "STOP_LOSS",
                    "pnl": pnl
                })
            # 2. Take Profit colpito
            elif price <= take_profit:
                pnl = (entry_price - price) * shares
                cash = cash_before_trade + pnl
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "TAKE_PROFIT",
                    "pnl": pnl
                })
            # 3. Inversione di trend
            elif trend == 1:
                pnl = (entry_price - price) * shares
                cash = cash_before_trade + pnl
                shares = 0.0
                position = None
                trades[-1].update({
                    "exit_date": date,
                    "exit_price": price,
                    "exit_reason": "TREND_REVERSAL",
                    "pnl": pnl
                })
                
    # Calcolo Metriche Finali
    final_equity = equity_history[-1]["equity"] if equity_history else initial_cash
    total_return = (final_equity / initial_cash - 1.0) * 100.0
    
    # Rendimento Buy & Hold dell'Oro nello stesso periodo
    price_start = history[SMA_SLOW_WINDOW]["close"]
    price_end = history[-1]["close"]
    bh_return = (price_end / price_start - 1.0) * 100.0
    
    # Calcolo Win Rate e Profit Factor
    closed_trades = [t for t in trades if "exit_price" in t]
    wins = [t for t in closed_trades if t["pnl"] > 0]
    losses = [t for t in closed_trades if t["pnl"] <= 0]
    
    win_rate = (len(wins) / len(closed_trades) * 100.0) if closed_trades else 0.0
    
    total_gain = sum(t["pnl"] for t in wins)
    total_loss = abs(sum(t["pnl"] for t in losses))
    profit_factor = (total_gain / total_loss) if total_loss > 0 else (999.0 if total_gain > 0 else 1.0)
    
    # Massimo Drawdown (MDD)
    peak = -999999.0
    max_dd = 0.0
    for eq in equity_history:
        val = eq["equity"]
        if val > peak:
            peak = val
        dd = (peak - val) / peak
        if dd > max_dd:
            max_dd = dd
            
    # Calcolo Sharpe Ratio della Strategia (annualizzato)
    equity_returns = []
    for i in range(1, len(equity_history)):
        r = math.log(equity_history[i]["equity"] / equity_history[i-1]["equity"])
        equity_returns.append(r)
        
    if equity_returns:
        mean_ret = sum(equity_returns) / len(equity_returns)
        var = sum((r - mean_ret) ** 2 for r in equity_returns) / len(equity_returns)
        std_ret = math.sqrt(var) if var > 0 else 1e-9
        
        # Annualizza
        ann_mu = mean_ret * TRADING_DAYS
        ann_sigma = std_ret * math.sqrt(TRADING_DAYS)
        strategy_sharpe = (ann_mu - RISK_FREE_RATE) / ann_sigma if ann_sigma > 0 else 0.0
    else:
        ann_mu, ann_sigma, strategy_sharpe = 0.0, 0.0, 0.0
        
    return {
        "final_equity": final_equity,
        "total_return": total_return,
        "bh_return": bh_return,
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "max_drawdown": max_dd * 100.0,
        "sharpe": strategy_sharpe,
        "trades": closed_trades,
        "equity_history": equity_history
    }

# 5. Generatore del Segnale Odierno
def get_daily_signal(today_data, sentiment_score):
    price = today_data["close"]
    z = today_data["z_score"]
    trend = today_data["trend"]
    
    adjusted_z_threshold = Z_THRESHOLD - (sentiment_score * 0.3)
    
    if trend == 1:
        trend_str = "🟢 RIALZISTA (Bullish)"
        if z < -adjusted_z_threshold:
            signal = "COMPRA (LONG ENTRY)"
            action_desc = "Il prezzo dell'Oro è in un trend rialzista ma è momentaneamente ipervenduto. Ottimo timing d'acquisto (Buy the Dip)."
        else:
            signal = "MANTIENI / ATTENDI"
            action_desc = "Il trend dell'Oro è solido ma non ci sono anomalie statistiche per entrare a mercato in questo momento."
    else:
        trend_str = "🔴 RIBASSISTA (Bearish)"
        if z > adjusted_z_threshold:
            signal = "VENDI ALLO SCOPERTO (SHORT ENTRY)"
            action_desc = "Il prezzo dell'Oro è in un trend ribassista ed è momentaneamente ipercomprato. Ottimo timing speculativo a ribasso."
        else:
            signal = "MANTIENI / ATTENDI"
            action_desc = "Il trend dell'Oro è debole; nessuna anomalia statistica rilevata per ingressi a breve termine."
            
    return {
        "signal": signal,
        "trend_desc": trend_str,
        "action_desc": action_desc,
        "z_score": z,
        "adjusted_threshold": adjusted_z_threshold
    }

def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("="*90)
    print("🏆 AVVIO STRATEGIA QUANTITATIVA ORO: AMSR (Aurum Momentum & Sentiment Reversion)")
    print("="*90)
    
    # 1. Recupero dati e calcolo indicatori
    history = fetch_gold_historical_data()
    history = calculate_indicators(history)
    
    # 2. Scraping sentiment notizie
    sentiment_score, articles = fetch_gold_news_sentiment()
    
    # 3. Esecuzione Backtest
    print("\n⚡ Calcolo del Backtest storico sui 255 giorni reali in corso...")
    stats = run_backtest(history, sentiment_score)
    
    # 4. Report Grafico / Statistico
    print("\n" + "="*85)
    print("📊 RISULTATI DEL BACKTEST STORICO SULL'ORO (AMSR Strategia Multi-Day)")
    print("="*85)
    print(f"💰 Capitale Iniziale:                 € 10.000,00")
    print(f"💵 Capitale Finale Strategia:         € {stats['final_equity']:.2f}")
    print(f"📈 Rendimento Totale Strategia:       {stats['total_return']:>+7.2f}%")
    print(f"⚖️  Rendimento Buy & Hold (Oro Fisico): {stats['bh_return']:>+7.2f}%")
    print(f"📊 Sharpe Ratio Strategia:            {stats['sharpe']:>7.3f}")
    print(f"📉 Massimo Drawdown Strategia:        {stats['max_drawdown']:>7.2f}%")
    print(f"🎯 Win Rate (% Trade Vincenti):       {stats['win_rate']:>7.1f}%  ({len(stats['trades'])} operazioni concluse)")
    print(f"💸 Profit Factor (Utili/Perdite):     {stats['profit_factor']:>7.2f}")
    print("="*85)
    
    # Stampa degli ultimi trade
    if stats["trades"]:
        print("\n📜 ESTRATTO REGISTRO OPERATIVO DEI TRADE:")
        print("-"*85)
        print(f"{'TIPO':<12} | {'INGRESSO':<10} | {'PREZZO IN.':<10} | {'USCITA':<10} | {'PREZZO USC.':<12} | {'PnL':<10}")
        print("-"*85)
        for t in stats["trades"][-8:]: # Mostra gli ultimi 8 trade
            pnl_str = f"€{t['pnl']:>+8.2f}"
            print(f"{t['type']:<12} | {t['entry_date']:<10} | ${t['entry_price']:<10.2f} | {t['exit_date']:<10} | ${t['exit_price']:<12.2f} | {pnl_str:<10}")
        print("-"*85)
        
    # Esporta i risultati in formato CSV nella cartella 'data'
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    csv_file = os.path.join(output_dir, "gold_backtest_results.csv")
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("Data,Equità_Strategia\n")
        for eq in stats["equity_history"]:
            f.write(f"{eq['date']},{eq['equity']:.4f}\n")
    print(f"\n💾 Esportati {len(stats['equity_history'])} record storici di equità in: {csv_file}")
    
    # Esporta il solo sentiment score per NinjaTrader 8 in formato testo piano
    sentiment_file = os.path.join(output_dir, "gold_sentiment.txt")
    with open(sentiment_file, "w", encoding="utf-8") as f:
        f.write(f"{sentiment_score:.4f}")
    print(f"📡 Esportato sentiment score ({sentiment_score:+.3f}) per il bridge NinjaTrader in: {sentiment_file}")
    
    # 5. Generazione Segnale Odierno
    today_data = history[-1]
    sig_info = get_daily_signal(today_data, sentiment_score)
    
    print("\n" + "="*85)
    print(f"🎯 SEGNALE QUANTITATIVO ATTIVO PER L'ORO ({datetime.today().strftime('%d/%m/%Y')})")
    print("="*85)
    print(f"• Prezzo Corrente Spot dell'Oro:   ${today_data['close']:.2f}")
    print(f"• Trend Macroeconomico di Fondo:    {sig_info['trend_desc']}")
    print(f"• Robust Z-Score Odierno:           {sig_info['z_score']:+.3f} (Soglia Sentiment-Adjusted: ±{sig_info['adjusted_threshold']:.2f})")
    print(f"• Sentiment Macro dell'Oro:        {sentiment_score:+.3f}  (da {len(articles)} notizie analizzate)")
    print(f"\n📢 RACCOMANDAZIONE OPERATIVA:       {sig_info['signal'].upper()}")
    print(f"👉 Dettaglio Azione:                {sig_info['action_desc']}")
    print("="*85 + "\n")
    
if __name__ == "__main__":
    main()
