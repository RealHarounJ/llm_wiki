#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
📈 Complete Multi-Asset Portfolio Market Data Ingestor
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Si connette alle API di Trading 212 per estrarre le posizioni reali del 
             portafoglio di Haroun Jaafar. Mappa ciascun ticker (inclusi gli ETF LSE/europei) 
             sul corrispondente ticker compatibile con Polygon.io. Scarica 60 giorni di 
             dati storici, calcola metriche quantitative avanzate e salva ciascun dataset 
             in formato CSV nella cartella 'data/'.
             Implementa un ritardo di 12.5 secondi tra le chiamate per rispettare il limite
             di 5 richieste al minuto di Polygon.io.
Requisiti: Python 3.x (Librerie standard)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import base64
import time
import datetime
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# 1. Mappatura Ticker Trading 212 -> Polygon US equivalents (ETF LSE e ADR/OTC)
TICKER_MAPPING = {
    "SWDA": "URTH",   # iShares MSCI World ETF (Proxy per MSCI World)
    "VHVG": "VEA",    # Vanguard FTSE Developed Markets ETF (Proxy per Developed World)
    "EIMI": "IEMG",   # iShares Core MSCI Emerging Markets ETF (Proxy per Emerging Markets)
    "VGVA": "VFVA",   # Vanguard U.S. Value Factor ETF (Proxy per Global Value)
    "IITU": "XLK",    # Technology Select Sector SPDR (Proxy per S&P 500 Tech)
    "INRG": "ICLN",   # iShares Global Clean Energy ETF (Proxy per Clean Energy)
    "IPRV": "PSP",    # Invesco Global Listed Private Equity ETF (Proxy per Private Equity)
    "SMSN": "SSNLF",  # Samsung Electronics GDR (LSE -> US OTC GDR)
    "FIG":  "FRHC",   # Freedom Holding Corp (Trading 212 FIG -> Nasdaq FRHC)
    "CENH": "ARQQ",   # Constellation Acquisition -> Arqit Quantum (Nasdaq ARQQ)
    "ARQQ": "ARQQ",   # Arqit Quantum
    "ETL":  "EUTLF",  # Eutelsat Communications (Euronext -> US OTC EUTLF)
    # Ticker standard USA non necessitano di mappatura ma vengono inclusi per completezza
    "COIN": "COIN",
    "ADBE": "ADBE",
    "DUOL": "DUOL",
    "AAPL": "AAPL",
    "BLK":  "BLK",
    "MSFT": "MSFT",
    "ATPC": "ATPC",
}

# 2. Caricamento credenziali da .env
def load_credentials():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        env_path = ".env"
        if not os.path.exists(env_path):
            print("❌ Errore: File .env non trovato.")
            sys.exit(1)
            
    trading212_key = None
    trading212_secret = None
    polygon_key = None
    
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith("TRADING212_API_KEY="):
                trading212_key = line_str.split("=", 1)[1].strip()
            elif line_str.startswith("TRADING212_API_SECRET="):
                trading212_secret = line_str.split("=", 1)[1].strip()
            elif line_str.startswith("POLYGON_API_KEY="):
                polygon_key = line_str.split("=", 1)[1].strip()
                
    if not trading212_key or not polygon_key:
        print("❌ Errore: Credenziali incomplete in .env. Assicurati che siano presenti:")
        print("   - TRADING212_API_KEY")
        print("   - POLYGON_API_KEY")
        sys.exit(1)
        
    # Creazione Auth Header per Trading 212
    if trading212_secret:
        credentials_string = f"{trading212_key}:{trading212_secret}"
        encoded_credentials = base64.b64encode(credentials_string.encode('utf-8')).decode('utf-8')
        t212_auth = f"Basic {encoded_credentials}"
    else:
        t212_auth = trading212_key if trading212_key.startswith("Basic ") else f"Basic {trading212_key}"
        
    return t212_auth, polygon_key

# 3. Recupero posizioni reali da Trading 212
def fetch_trading212_portfolio(t212_auth):
    endpoints = [
        {"name": "Real/Live Account", "url": "https://live.trading212.com/api/v0/equity/positions"},
        {"name": "Demo Account", "url": "https://demo.trading212.com/api/v0/equity/positions"}
    ]
    
    positions = None
    for ep in endpoints:
        req = Request(ep['url'], headers={"Authorization": t212_auth, "User-Agent": "Mozilla/5.0"})
        try:
            with urlopen(req) as response:
                positions = json.loads(response.read().decode('utf-8'))
                print(f"✅ Connesso con successo al conto Trading 212 ({ep['name']})!")
                break
        except Exception:
            continue
            
    if not positions:
        print("⚠️ Impossibile connettersi alle API di Trading 212. Utilizzo del portafoglio di fallback standard.")
        # Fallback se le API falliscono o non hanno fondi
        return [
            {"ticker": "IPRVl_EQ", "quantity": 1.86350, "currentPrice": 23.03},
            {"ticker": "BLK_US_EQ", "quantity": 0.00112, "currentPrice": 1063.72},
            {"ticker": "ATPC_US_EQ", "quantity": 0.00286, "currentPrice": 3.70},
            {"ticker": "MSFT_US_EQ", "quantity": 0.00273, "currentPrice": 420.69},
            {"ticker": "INRGl_EQ", "quantity": 11.46801, "currentPrice": 9.38},
            {"ticker": "AAPL_US_EQ", "quantity": 0.00489, "currentPrice": 305.77},
            {"ticker": "ADBE_US_EQ", "quantity": 0.22725, "currentPrice": 245.80},
            {"ticker": "COIN_US_EQ", "quantity": 0.30858, "currentPrice": 194.22},
            {"ticker": "SMSNl_EQ", "quantity": 0.05370, "currentPrice": 4832.00},
            {"ticker": "IITU_EQ", "quantity": 2.39987, "currentPrice": 36.42},
            {"ticker": "DUOL_US_EQ", "quantity": 0.33110, "currentPrice": 105.79},
            {"ticker": "CENH_US_EQ", "quantity": 5.66278, "currentPrice": 16.74},
            {"ticker": "VGVAl_EQ", "quantity": 0.41444, "currentPrice": 20.29},
            {"ticker": "ETLp_EQ", "quantity": 7.50194, "currentPrice": 3.83},
            {"ticker": "EIMIl_EQ", "quantity": 1.33260, "currentPrice": 53.22},
            {"ticker": "VHVGl_EQ", "quantity": 0.76569, "currentPrice": 109.64},
            {"ticker": "FIG_US_EQ", "quantity": 48.45866, "currentPrice": 21.69},
            {"ticker": "SWDAl_EQ", "quantity": 0.85562, "currentPrice": 105.08}
        ]
        
    return positions

def clean_ticker_name(ticker):
    if not ticker:
        return ""
    base = ticker.split("_")[0]
    if len(base) > 1 and base[-1].islower() and base[:-1].isupper():
        base = base[:-1]
    if base == "CENH":
        base = "ARQQ"
    return base

# 4. Ingestione dati da Polygon.io
def fetch_polygon_history(ticker, polygon_key, days=60):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days)
    
    # Formattazione ticker standard per Polygon
    formatted_ticker = TICKER_MAPPING.get(ticker, ticker).upper()
    
    url = (
        f"https://api.polygon.io/v2/aggs/ticker/{formatted_ticker}/range/1/day/"
        f"{start_date}/{end_date}?adjusted=true&sort=asc&limit=120&apiKey={polygon_key}"
    )
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("status") in ["OK", "DELAYED"] and data.get("results"):
                return data["results"], formatted_ticker
    except Exception as e:
        if hasattr(e, 'code') and e.code == 429:
            print(f"⚠️ Rate limit raggiunto per {formatted_ticker} (429).")
        else:
            print(f"⚠️ Errore per {formatted_ticker}: {e}")
    return None, formatted_ticker

# 5. Calcolo statistiche per il dashboard
def calculate_metrics(results):
    prices = [bar["c"] for bar in results]
    dates = []
    for bar in results:
        timestamp = bar["t"] / 1000.0
        dates.append(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
        
    returns = []
    for i in range(1, len(prices)):
        returns.append(math.log(prices[i] / prices[i-1]))
        
    if not returns:
        return None
        
    # Calcolo della deviazione standard (volatilità giornaliera)
    mean_ret = sum(returns) / len(returns)
    variance = sum((r - mean_ret) ** 2 for r in returns) / len(returns)
    daily_vol = math.sqrt(variance)
    annual_vol = daily_vol * math.sqrt(252)
    
    # Rendimento cumulato nel periodo
    cum_return = (prices[-1] / prices[0] - 1.0) * 100
    
    return {
        "prices": prices,
        "dates": dates,
        "returns": returns,
        "last_price": prices[-1],
        "daily_vol": daily_vol,
        "annual_vol": annual_vol,
        "cum_return": cum_return
    }

def main():
    print("🚀 Avvio Pipeline di Ingestione Dati di Mercato per tutti gli Asset...")
    t212_auth, polygon_key = load_credentials()
    
    positions = fetch_trading212_portfolio(t212_auth)
    
    # Cartella di output 'data'
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    dashboard_data = []
    
    print(f"\n📥 Download dati storici da Polygon.io per {len(positions)} asset in corso...")
    print("💡 Nota: Per rispettare il limite gratuito di Polygon (5 richieste/minuto), applicheremo un ritardo di 12.5 secondi tra ogni richiesta.")
    
    for idx, pos in enumerate(positions):
        raw_ticker = pos.get("instrument", {}).get("ticker") or pos.get("ticker")
        clean_ticker = clean_ticker_name(raw_ticker)
        
        if not clean_ticker:
            continue
            
        if idx > 0:
            # Sleep di 12.5 secondi per non superare il limite di 5 rich/min
            print(f"⏳ Attesa regolamentare per rate-limiting (12.5s) prima di scaricare {clean_ticker}...")
            time.sleep(12.5)
            
        results, polygon_ticker = fetch_polygon_history(clean_ticker, polygon_key)
        
        if not results:
            print(f"❌ Impossibile scaricare i dati per {clean_ticker} (Polygon: {polygon_ticker})")
            continue
            
        metrics = calculate_metrics(results)
        if not metrics:
            print(f"⚠️ Dati insufficienti per calcolare metriche su {clean_ticker}")
            continue
            
        # Salva in formato CSV
        csv_file = os.path.join(output_dir, f"{clean_ticker.lower()}_market_data.csv")
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write("Data,Prezzo_Chiusura,Rendimento_Logaritmico\n")
            f.write(f"{metrics['dates'][0]},{metrics['prices'][0]:.6f},0.000000\n")
            for i in range(1, len(metrics['prices'])):
                f.write(f"{metrics['dates'][i]},{metrics['prices'][i]:.6f},{metrics['returns'][i-1]:.6f}\n")
                
        print(f"💾 {clean_ticker:<6} -> {csv_file} (Salvati {len(metrics['prices'])} giorni, mappato su {polygon_ticker})")
        
        dashboard_data.append({
            "ticker": clean_ticker,
            "poly_ticker": polygon_ticker,
            "last_price": metrics["last_price"],
            "daily_vol": metrics["daily_vol"] * 100,
            "annual_vol": metrics["annual_vol"] * 100,
            "cum_return": metrics["cum_return"]
        })
        
    # Visualizzazione Dashboard Finale
    print("\n" + "="*95)
    print(f"📊 DASHBOARD DEI DATI DI MERCATO ATTUALIZZATI ({datetime.date.today().strftime('%d/%m/%Y')})")
    print("="*95)
    print(f"{'TICKER':<8} | {'PROXY US':<10} | {'PREZZO CHIUSURA':<16} | {'VOLATILITÀ GG (%)':<18} | {'VOLATILITÀ ANN (%)':<18} | {'RET. 60g (%)':<12}")
    print("-"*95)
    
    for row in dashboard_data:
        print(f"{row['ticker']:<8} | {row['poly_ticker']:<10} | ${row['last_price']:<15.2f} | {row['daily_vol']:<17.3f}% | {row['annual_vol']:<17.2f}% | {row['cum_return']:>+10.2f}%")
        
    print("-"*95)
    print(f"✅ Pipeline completata! Tutti i file .csv sono pronti nella cartella 'data/'.")
    print("="*95 + "\n")

if __name__ == "__main__":
    main()
