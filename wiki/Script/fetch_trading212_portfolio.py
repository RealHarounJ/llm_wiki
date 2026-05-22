#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
💼 Live Trading 212 Portfolio Fetcher
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Si connette alle API ufficiali di Trading 212 (Demo o Live) utilizzando
             la chiave API definita nel file .env per estrarre le posizioni correnti.
Requisiti: Python 3.x (Librerie standard)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import base64
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# 1. Caricamento e configurazione delle credenziali di Trading 212
def load_trading212_credentials():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        env_path = ".env"
        if not os.path.exists(env_path):
            print("❌ Errore: File .env non trovato.")
            sys.exit(1)
            
    api_key = None
    api_secret = None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line_str = line.strip()
            if line_str.startswith("TRADING212_API_KEY="):
                api_key = line_str.split("=", 1)[1].strip()
            elif line_str.startswith("TRADING212_API_SECRET="):
                api_secret = line_str.split("=", 1)[1].strip()
                
    if not api_key:
        print("❌ Errore: Chiave TRADING212_API_KEY non configurata in .env")
        sys.exit(1)
        
    if api_secret:
        # Genera l'header di Basic Authentication richiesto da API v0
        credentials_string = f"{api_key}:{api_secret}"
        encoded_credentials = base64.b64encode(credentials_string.encode('utf-8')).decode('utf-8')
        auth_header = f"Basic {encoded_credentials}"
    else:
        # Fallback se non è configurato il secret
        if api_key.startswith("Basic "):
            auth_header = api_key
        else:
            print("⚠️ Attenzione: TRADING212_API_SECRET non configurato in .env.")
            print("  Il nuovo endpoint API v0 richiede sia API Key che API Secret.")
            print("  Tentativo di autenticazione usando solo TRADING212_API_KEY...")
            auth_header = api_key
            
    return auth_header

# 2. Interrogazione dell'API di Trading 212 (Supporta sia Live che Demo)
def fetch_positions(api_auth):
    endpoints = [
        {"name": "Real/Live Account", "url": "https://live.trading212.com/api/v0/equity/positions"},
        {"name": "Demo Account", "url": "https://demo.trading212.com/api/v0/equity/positions"}
    ]
    
    positions = None
    successful_endpoint = None
    
    for ep in endpoints:
        print(f"📥 Tentativo di connessione a Trading 212 ({ep['name']})...")
        req = Request(ep['url'], headers={
            "Authorization": api_auth,
            "User-Agent": "Mozilla/5.0"
        })
        
        try:
            with urlopen(req) as response:
                positions = json.loads(response.read().decode('utf-8'))
                successful_endpoint = ep['name']
                break
        except HTTPError as e:
            # 401 o 403 indicano che la chiave non è autorizzata su questo specifico endpoint
            if e.code in [401, 403]:
                print(f"  ⚠️ Non autorizzato su {ep['name']} (Codice {e.code}). Provo l'endpoint alternativo...")
            else:
                print(f"  ❌ Errore HTTP su {ep['name']}: {e.code} - {e.reason}")
        except URLError as e:
            print(f"  ❌ Errore di rete su {ep['name']}: {e.reason}")
        except Exception as e:
            print(f"  ❌ Errore imprevisto su {ep['name']}: {e}")
            
    if not positions:
        print("\n❌ Impossibile connettersi a Trading 212. Verifica che la chiave sia corretta e attiva.")
        return None, None
        
    return positions, successful_endpoint

def clean_ticker_name(ticker):
    if not ticker:
        return ""
    base = ticker.split("_")[0]
    # Se il ticker base ha un suffisso minuscolo (es. l per Londra, p per Parigi) e il resto è maiuscolo, lo rimuove
    if len(base) > 1 and base[-1].islower() and base[:-1].isupper():
        base = base[:-1]
    # Gestione cambio ticker Arqit Quantum (CENH -> ARQQ)
    if base == "CENH":
        base = "ARQQ"
    return base

def display_portfolio(positions, endpoint_name):
    print("\n" + "="*80)
    print(f"💼 PORTAFOGLIO LIVE TRADING 212 ({endpoint_name.upper()})")
    print("="*80)
    print(f"{'TICKER':<10} | {'QUANTITÀ':<12} | {'PREZZO MEDIO':<15} | {'PREZZO CORR.':<15} | {'VALORE CORR.':<15}")
    print("-"*80)
    
    total_val = 0.0
    for pos in positions:
        instrument = pos.get("instrument", {})
        ticker = instrument.get("ticker") or pos.get("ticker", "N/A")
        quantity = float(pos.get("quantity", 0.0))
        avg_price = float(pos.get("averagePricePaid") or pos.get("averagePrice", 0.0))
        curr_price = float(pos.get("currentPrice", 0.0))
        
        # Estrazione del valore in EUR tramite walletImpact
        value = pos.get("walletImpact", {}).get("currentValue")
        if value is None:
            value = pos.get("value")
            if value is None:
                value = quantity * curr_price
            else:
                value = float(value)
        else:
            value = float(value)
        
        total_val += value
        
        # Stampa dei prezzi originali
        currency = instrument.get("currency", "EUR")
        curr_symbol = "€" if currency == "EUR" else ("$" if currency == "USD" else ("p" if currency == "GBX" else currency))
        print(f"{ticker:<10} | {quantity:<12.5f} | {curr_symbol}{avg_price:<12.4f} | {curr_symbol}{curr_price:<12.4f} | €{value:<13.2f}")
        
    print("-"*80)
    print(f"{'VALORE TOTALE DEL PORTAFOGLIO:':<58} €{total_val:.2f}")
    print("="*80 + "\n")
    
    # Esporta in formato dizionario con ticker ripulito (es. AAPL_US_EQ -> AAPL)
    portfolio_dict = {}
    for pos in positions:
        ticker = pos.get("instrument", {}).get("ticker") or pos.get("ticker")
        if ticker:
            clean_ticker = clean_ticker_name(ticker)
            quantity = float(pos.get("quantity", 0.0))
            curr_price = float(pos.get("currentPrice", 0.0))
            
            val = pos.get("walletImpact", {}).get("currentValue")
            if val is None:
                val = pos.get("value")
                if val is None:
                    val = quantity * curr_price
                else:
                    val = float(val)
            else:
                val = float(val)
                
            portfolio_dict[clean_ticker] = round(val, 2)
            
    return portfolio_dict

def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    api_auth = load_trading212_credentials()
    positions, ep_name = fetch_positions(api_auth)
    if positions is not None:
        display_portfolio(positions, ep_name)

if __name__ == "__main__":
    main()
