#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------------
🔮 Academic Alpha Vantage Market Prediction Tool
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Utilizza le API di Alpha Vantage per scaricare dati storici giornalieri.
             Implementa un modello di previsione quantitativa basato sullo Z-Score Robusto
             e calcola l'Information Coefficient (IC) empirico in accordo con la
             "Legge Fondamentale dell'Active Management" (Grinold & Kahn).
Requisiti: Python 3.x (Nessuna dipendenza esterna, usa librerie standard)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError

# 1. Caricamento della chiave API dal file .env
def load_api_key():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        env_path = ".env"
        if not os.path.exists(env_path):
            print("❌ Errore: File .env non trovato.")
            sys.exit(1)
            
    api_key = None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("ALPHAVANTAGE_API_KEY="):
                api_key = line.strip().split("=", 1)[1].strip()
                break
                
    if not api_key:
        print("❌ Errore: Chiave ALPHAVANTAGE_API_KEY non configurata in .env")
        sys.exit(1)
    return api_key

# 2. Strumenti Matematici Quantitativi (Pure Python)
def calculate_median(data_list):
    sorted_data = sorted(data_list)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2.0

def calculate_robust_z_score(current_val, window_vals):
    median_val = calculate_median(window_vals)
    deviations = [abs(x - median_val) for x in window_vals]
    mad = calculate_median(deviations) * 1.4826
    mad = mad if mad > 1e-6 else 1e-6
    return (current_val - median_val) / mad

def mean(x):
    return sum(x) / len(x)

def pearson_correlation(x, y):
    n = len(x)
    if n == 0:
        return 0
    x_mean = mean(x)
    y_mean = mean(y)
    
    num = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    den_x = sum((x[i] - x_mean) ** 2 for i in range(n))
    den_y = sum((y[i] - y_mean) ** 2 for i in range(n))
    
    if den_x == 0 or den_y == 0:
        return 0
    return num / math.sqrt(den_x * den_y)

# 3. Download dati da Alpha Vantage
def fetch_alpha_vantage_data(ticker, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=compact&apikey={api_key}"
    print(f"📥 Richiesta dati in corso da Alpha Vantage per {ticker}...")
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
    except URLError as e:
        print(f"❌ Errore di rete: {e}")
        return None
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        return None
        
    if "Error Message" in data:
        print(f"❌ Errore Alpha Vantage: Ticker '{ticker}' non trovato o non supportato.")
        return None
    elif "Note" in data:
        print("⚠️ Nota API (Frequenza Limiti superata):")
        print(data["Note"])
        return None
    elif "Time Series (Daily)" not in data:
        print("❌ Errore: Risposta API non valida o vuota.")
        print(data)
        return None
        
    return data["Time Series (Daily)"]

# 4. Modello di Previsione e Calcolo dell'IC
def run_predictive_model(ticker, raw_data):
    # Ordinamento cronologico
    sorted_dates = sorted(raw_data.keys())
    prices = [float(raw_data[date]["4. close"]) for date in sorted_dates]
    
    n_days = len(prices)
    if n_days < 30:
        print("❌ Errore: Dati storici insufficienti per l'analisi quantitativa (minimo 30 record).")
        return
        
    # Calcolo dei rendimenti giornalieri effettivi
    returns = []
    for i in range(1, n_days):
        returns.append(math.log(prices[i] / prices[i-1]))
        
    # Finestra di lookback per Z-Score Robusto
    lookback = 20
    signals = []
    subsequent_returns = []
    
    # Costruzione storica dei segnali predittivi (Z-Score inverso di Mean Reversion)
    # Se il prezzo è molto ipervenduto (Z-Score negativo), il segnale predice un rialzo (segnale positivo)
    for t in range(lookback, n_days - 1):
        window = prices[t - lookback:t]
        z_score = calculate_robust_z_score(prices[t], window)
        
        # Segnale di Mean-Reversion: inverso dello Z-score
        signal = -z_score
        signals.append(signal)
        
        # Rendimento del giorno successivo (t + 1)
        sub_ret = returns[t] # returns[t] corrisponde a ln(prices[t+1]/prices[t])
        subsequent_returns.append(sub_ret)
        
    # Calcolo dell'Information Coefficient (IC) empirico del modello
    ic = pearson_correlation(signals, subsequent_returns)
    
    # Calcolo della volatilità storica dei rendimenti (standard deviation)
    ret_mean = mean(returns)
    volatility = math.sqrt(sum((r - ret_mean)**2 for r in returns) / (len(returns) - 1))
    
    # Calcolo dell'ultimo segnale corrente (per prevedere domani!)
    current_window = prices[-lookback:]
    latest_z = calculate_robust_z_score(prices[-1], current_window)
    latest_signal = -latest_z
    
    # Formula di Grinold & Chincarini per il rendimento attivo atteso
    # E[R_active] = Signal * Volatilità * IC
    # Assumiamo un coefficiente di trasferimento TC di 1.0 per semplicità
    expected_active_return = latest_signal * volatility * ic
    
    # Stampa del Report Accademico
    print("\n" + "="*70)
    print(f"🔮 REPORT PREVISIONALE ACCADEMICO (ALPHA VANTAGE): {ticker.upper()}")
    print("="*70)
    print(f"• Prezzo Ultimo Registrato:     {prices[-1]:.2f}")
    print(f"• Finestra Storica Analizzata:  {n_days} giorni di borsa aperta")
    print(f"• Volatilità Giornaliera (σ):    {volatility*100:.3f}%")
    print("-"*70)
    print(f"📊 LEGGE FONDAMENTALE DI GRINOLD & KAHN:")
    print(f"• Information Coefficient (IC): {ic:.4f}")
    
    if ic > 0.05:
        print("  🟢 STRUTTURA PREDITTIVA SOLIDA (IC > 0.05):")
        print("     Il modello mostra un edge predittivo statisticamente significativo.")
    elif ic > 0.0:
        print("  ⚖️ SEGNALE DEBOLE MA POSITIVO (0.0 < IC <= 0.05):")
        print("     Il modello ha una correlazione positiva ma debole con i rendimenti futuri.")
    else:
        print("  🔴 NESSUN EDGE / CORRELAZIONE INVERSA (IC <= 0.0):")
        print("     Il modello è in controtendenza o non presenta alcun potere predittivo.")
        
    print("-"*70)
    print(f"🔮 PREVISIONE PER LA PROSSIMA SESSIONE DI BORSA:")
    print(f"• Z-Score Robusto Corrente:     {latest_z:.2f}")
    print(f"• Segnale Predittivo Generato:  {latest_signal:.2f}")
    
    direzione = "RIALZISTA (Mean Reversion)" if latest_signal > 0 else "RIBASSISTA (Mean Reversion)"
    color = "🟢" if latest_signal > 0 else "🔴"
    
    print(f"• Direzione Forecast:          {color} {direzione}")
    print(f"• Rendimento Attivo Atteso E[R]: {expected_active_return*100:.4f}%")
    
    print("\n💡 Nota Accademica (Grinold):")
    print(f"  La stima E[R] = {expected_active_return*100:.4f}% si basa sulla legge: E[R] = Signal * σ * IC.")
    print("  Con un Information Ratio teorico annualizzato stimato.")
    print("="*70 + "\n")

def main():
    # Forza codifica UTF-8 per console Windows
    if sys.platform.startswith('win'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("🚀 Inizializzazione pipeline predittiva Alpha Vantage...")
    api_key = load_api_key()
    
    ticker = "SPY"
    if len(sys.argv) > 1:
        ticker = sys.argv[1]
        
    raw_data = fetch_alpha_vantage_data(ticker, api_key)
    if raw_data:
        run_predictive_model(ticker, raw_data)

if __name__ == "__main__":
    main()
