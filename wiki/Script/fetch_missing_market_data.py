#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch only the missing assets (IPRV, BLK, SMSN) to complete the dataset.
"""

import os
import sys
import json
import math
import base64
import time
import datetime
from urllib.request import Request, urlopen

TICKER_MAPPING = {
    "IPRV": "PSP",
    "BLK": "BLK",
    "SMSN": "SSNLF"
}

def load_credentials():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    polygon_key = None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("POLYGON_API_KEY="):
                polygon_key = line.strip().split("=", 1)[1].strip()
                break
    return polygon_key

def fetch_polygon_history(ticker, polygon_key, days=60):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days)
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
                return data["results"]
    except Exception as e:
        print(f"⚠️ Errore per {ticker}: {e}")
    return None

def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    polygon_key = load_credentials()
    missing = ["IPRV", "BLK", "SMSN"]
    output_dir = "data"
    
    print("⏳ Recupero dei 3 asset mancanti (IPRV, BLK, SMSN)...")
    
    for idx, ticker in enumerate(missing):
        if idx > 0:
            time.sleep(13) # Attesa per rate limit
            
        print(f"📥 Download di {ticker}...")
        results = fetch_polygon_history(ticker, polygon_key)
        if not results:
            print(f"❌ Impossibile recuperare {ticker}")
            continue
            
        prices = [bar["c"] for bar in results]
        dates = []
        for bar in results:
            timestamp = bar["t"] / 1000.0
            dates.append(datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d'))
            
        returns = []
        for i in range(1, len(prices)):
            returns.append(math.log(prices[i] / prices[i-1]))
            
        csv_file = os.path.join(output_dir, f"{ticker.lower()}_market_data.csv")
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write("Data,Prezzo_Chiusura,Rendimento_Logaritmico\n")
            f.write(f"{dates[0]},{prices[0]:.6f},0.000000\n")
            for i in range(1, len(prices)):
                f.write(f"{dates[i]},{prices[i]:.6f},{returns[i-1]:.6f}\n")
        print(f"💾 Salvato {csv_file} con {len(prices)} giorni di dati!")

if __name__ == "__main__":
    main()
