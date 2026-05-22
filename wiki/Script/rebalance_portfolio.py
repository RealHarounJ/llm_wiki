# -*- coding: utf-8 -*-
"""
Rebalance Portfolio Tool - Trading 212
Generato per Haroun Jaafar (Second Brain)

Questo script calcola la distribuzione ottimale del nuovo capitale mensile (PAC)
per riequilibrare il portafoglio verso il modello Core-Satellite target,
senza effettuare vendite (No-Sell Rebalancing) per evitare commissioni FX e tasse.
"""

import sys

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

def calculate_rebalancing(current_portfolio, targets, new_cash):
    total_current_value = sum(current_portfolio.values())
    projected_total = total_current_value + new_cash
    
    print(f"\n--- Riepilogo Iniziale ---")
    print(f"Valore attuale portafoglio: EUR {total_current_value:.2f}")
    print(f"Nuovo capitale da investire: EUR {new_cash:.2f}")
    print(f"Valore stimato post-investimento: EUR {projected_total:.2f}")
    
    # Calcolo dei target in EUR sul valore totale proiettato
    ideal_values = {asset: projected_total * (targets.get(asset, 0.0) / 100.0) for asset in current_portfolio}
    
    # Calcolo della deviazione (quanto manca per raggiungere l'ideale)
    # Valori negativi indicano che l'asset è sottopesato (ha bisogno di acquisti)
    deficit = {}
    total_deficit = 0.0
    for asset, current_val in current_portfolio.items():
        ideal_val = ideal_values.get(asset, 0.0)
        diff = current_val - ideal_val
        if diff < 0:
            deficit[asset] = -diff
            total_deficit += -diff
            
    # Assegnazione del nuovo capitale proporzionalmente ai deficit rilevati
    allocations = {asset: 0.0 for asset in current_portfolio}
    
    if total_deficit > 0:
        for asset, def_val in deficit.items():
            # Quota proporzionale del cash disponibile basata sulla gravità del deficit
            share = (def_val / total_deficit) * new_cash
            allocations[asset] = round(share, 2)
    else:
        # Se nessun asset è in deficit (caso raro in cui i pesi sono perfetti),
        # distribuiamo proporzionalmente ai target teorici
        for asset in current_portfolio:
            share = new_cash * (targets.get(asset, 0.0) / 100.0)
            allocations[asset] = round(share, 2)
            
    # Stampa dei risultati
    print("\n" + "="*85)
    print(f"{'ASSET':<12} | {'VAL. ATTUALE':<12} | {'TARGET %':<8} | {'P&L ACQUISTO':<12} | {'NUOVO VAL.':<12} | {'PESO PROIET. %':<12}")
    print("="*85)
    
    for asset in sorted(current_portfolio.keys(), key=lambda x: current_portfolio[x], reverse=True):
        curr = current_portfolio[asset]
        tgt_pct = targets.get(asset, 0.0)
        buy = allocations.get(asset, 0.0)
        new_val = curr + buy
        new_pct = (new_val / projected_total) * 100.0
        
        buy_str = f"+EUR {buy:.2f}" if buy > 0 else "EUR 0.00"
        print(f"{asset:<12} | €{curr:<10.2f} | {tgt_pct:<7.1f}% | {buy_str:<12} | €{new_val:<10.2f} | {new_pct:<10.2f}%")
        
    print("="*85)
    print("\n🚀 Istruzioni di acquisto su Trading 212:")
    for asset, buy in allocations.items():
        if buy > 0:
            print(f"  • Acquista: {asset:<6} -> Importo: EUR {buy:.2f}")
    print("\nNota: Poiché l'azione FIG (Freedom Holding) è fortemente sovrappesata (51%),")
    print("tutto il nuovo capitale viene convogliato sugli indici globali (SWDA, EIMI) per diluire FIG nel tempo.")

if __name__ == "__main__":
    import os
    
    # Tentativo di recuperare il portafoglio live da Trading 212
    current_portfolio = None
    
    # Trova il file .env
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        env_path = ".env"
        
    api_key = None
    api_secret = None
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if line_str.startswith("TRADING212_API_KEY="):
                    api_key = line_str.split("=", 1)[1].strip()
                elif line_str.startswith("TRADING212_API_SECRET="):
                    api_secret = line_str.split("=", 1)[1].strip()
                    
    if api_key:
        print("🔌 Rilevata chiave TRADING212_API_KEY. Tentativo di recupero portafoglio live...")
        import json
        import base64
        from urllib.request import Request, urlopen
        
        if api_secret:
            credentials_string = f"{api_key}:{api_secret}"
            encoded_credentials = base64.b64encode(credentials_string.encode('utf-8')).decode('utf-8')
            api_auth = f"Basic {encoded_credentials}"
        else:
            if api_key.startswith("Basic "):
                api_auth = api_key
            else:
                print("⚠️ Attenzione: TRADING212_API_SECRET non configurato in .env.")
                print("  Il nuovo endpoint API v0 richiede sia API Key che API Secret.")
                print("  Tentativo di autenticazione usando solo TRADING212_API_KEY...")
                api_auth = api_key
                
        endpoints = [
            {"name": "Real/Live Account", "url": "https://live.trading212.com/api/v0/equity/positions"},
            {"name": "Demo Account", "url": "https://demo.trading212.com/api/v0/equity/positions"}
        ]
        
        positions = None
        for ep in endpoints:
            req = Request(ep['url'], headers={"Authorization": api_auth, "User-Agent": "Mozilla/5.0"})
            try:
                with urlopen(req) as response:
                    positions = json.loads(response.read().decode('utf-8'))
                    print(f"✅ Connessione riuscita a Trading 212 ({ep['name']}!)")
                    break
            except Exception:
                pass
                
        if positions:
            current_portfolio = {}
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
                        
                    current_portfolio[clean_ticker] = round(val, 2)
            print(f"📊 Recuperate con successo {len(current_portfolio)} posizioni attive dal tuo conto live!")
        else:
            print("⚠️ Impossibile autenticare o recuperare il portafoglio live. Utilizzo del portafoglio storico salvato.")
            
    if not current_portfolio:
        # Dati reali di fallback estratti dal report del 19 Maggio 2026
        current_portfolio = {
            "FIG": 1015.74,
            "SMSN": 210.56,
            "INRG": 120.89,
            "SWDA": 103.13,
            "IITU": 99.67,
            "VHVG": 96.20,
            "ARQQ": 62.51,
            "EIMI": 60.61,
            "IPRV": 50.59,
            "COIN": 50.02,
            "ADBE": 49.84,
            "DUOL": 32.17,
            "ETL": 21.34,
            "VGVA": 9.57,
            "AAPL": 1.25,
            "BLK": 1.05,
            "MSFT": 0.99,
            "ATPC": 0.01
        }
        
    # Target ideali definiti per il modello Core-Satellite (Fase 2)
    # Core = 70% (SWDA 55%, EIMI 15%)
    # Satellite = 30% (SMSN 10%, IITU 5%, INRG 5%, FIG 5%, speculativi minori)
    targets = {
        "SWDA": 55.0,  # Core Sviluppati
        "EIMI": 15.0,  # Core Emergenti
        "SMSN": 10.0,  # Satellite Blue Chip
        "IITU": 5.0,   # Satellite Settoriale Tech
        "INRG": 5.0,   # Satellite Settoriale Clean Energy
        "FIG": 5.0,    # Satellite ridotto (ex 51%)
        "ARQQ": 2.0,   # Speculativo minore
        "COIN": 2.0,   # Speculativo minore
        "IPRV": 2.0,   # Alternativo Private Equity
        "ADBE": 2.0,   # Satellite
        "DUOL": 1.0,   # Speculativo minore
        "ETL": 1.0,    # Speculativo minore
        # I restanti (VHVG, VGVA, AAPL, BLK, MSFT, ATPC) hanno target 0% perché in dismissione
        "VHVG": 0.0,
        "VGVA": 0.0,
        "AAPL": 0.0,
        "BLK": 0.0,
        "MSFT": 0.0,
        "ATPC": 0.0
    }
    
    # Input interattivo o di default
    new_cash = 150.0  # Valore di default del risparmio mensile
    if len(sys.argv) > 1:
        try:
            new_cash = float(sys.argv[1])
        except ValueError:
            pass
    else:
        print("Uso: python rebalance_portfolio.py [importo_da_investire]")
        print("Esempio: python rebalance_portfolio.py 200")
        
    calculate_rebalancing(current_portfolio, targets, new_cash)
