#!/usr/bin/env python3
"""
--------------------------------------------------------------------------------
📈 Multi-Asset Market Data Ingestion Tool (Polygon.io)
--------------------------------------------------------------------------------
Autore: Second Brain Quantitative Assistant
Descrizione: Estrae dati storici e real-time per Stock, ETF, Forex e Gold (GLD)
             utilizzando la chiave API Polygon definita nel file .env.
             Calcola metriche econometriche e statistiche robuste (MAD, Z-Score)
             allineate con i concetti di screening di portafoglio del Second Brain.
Requisiti: Python 3.x (Nessuna dipendenza esterna richiesta, usa urllib standard)
--------------------------------------------------------------------------------
"""

import os
import sys
import json
import math
import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError

# 1. Caricamento sicuro della chiave API dal file .env
def load_api_key():
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
    if not os.path.exists(env_path):
        # Cerca nella cartella corrente se eseguito localmente
        env_path = ".env"
        if not os.path.exists(env_path):
            print("❌ Errore: File .env non trovato. Crea un file .env contenente:")
            print("POLYGON_API_KEY=la_tua_chiave")
            sys.exit(1)
            
    api_key = None
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("POLYGON_API_KEY="):
                api_key = line.strip().split("=", 1)[1].strip()
                break
                
    if not api_key:
        print("❌ Errore: Chiave POLYGON_API_KEY non configurata correttamente in .env")
        sys.exit(1)
    return api_key

# 2. Calcolo di statistiche robuste (MAD e Z-Score) coerenti con [[Z_Score_Stock_Screening]]
def calculate_median(data_list):
    sorted_data = sorted(data_list)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2.0

def calculate_robust_stats(prices, returns):
    """
    Calcola la mediana, la MAD (Median Absolute Deviation) standardizzata e lo Z-Score
    robusto per identificare anomalie statistiche o condizioni di ipercomprato/ipervenduto.
    """
    if not returns:
        return {}
        
    median_return = calculate_median(returns)
    
    # Calcolo della Median Absolute Deviation (MAD)
    absolute_deviations = [abs(r - median_return) for r in returns]
    mad = calculate_median(absolute_deviations)
    
    # Fattore di consistenza gaussiana per rendere la MAD confrontabile con la deviazione standard
    standardized_mad = mad * 1.4826 if mad > 0 else 1e-6
    
    # Ultimo rendimento registrato
    latest_return = returns[-1]
    
    # Z-Score robusto dell'ultimo rendimento
    robust_z_score = (latest_return - median_return) / standardized_mad
    
    # Z-Score del prezzo corrente rispetto alla media mobile semplice (SMA)
    current_price = prices[-1]
    avg_price = sum(prices) / len(prices)
    price_deviations = [abs(p - avg_price) for p in prices]
    price_mad = calculate_median(price_deviations) * 1.4826
    price_mad = price_mad if price_mad > 0 else 1e-6
    robust_price_z_score = (current_price - avg_price) / price_mad
    
    return {
        "median_return": median_return,
        "standardized_mad": standardized_mad,
        "latest_return": latest_return,
        "robust_z_score": robust_z_score,
        "sma_price": avg_price,
        "robust_price_z_score": robust_price_z_score
    }

# 3. Chiamata API standard a Polygon.io
def fetch_polygon_data(ticker, api_key, days=60):
    # Calcolo delle date di inizio e fine
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days)
    
    # Formattazione del ticker per l'API Polygon
    # Per il Forex, il ticker deve avere il prefisso C: (es. C:EURUSD)
    # Per le criptovalute, il prefisso X: (es. X:BTCUSD)
    # Per stocks/ETFs, il ticker semplice (es. SPY, GLD)
    formatted_ticker = ticker.upper()
    if len(ticker) == 6 and not ":" in ticker:
        # Se è una coppia FX a 6 lettere, aggiungiamo il prefisso standard
        formatted_ticker = f"C:{ticker}"
        
    url = (
        f"https://api.polygon.io/v2/aggs/ticker/{formatted_ticker}/range/1/day/"
        f"{start_date}/{end_date}?adjusted=true&sort=asc&limit=120&apiKey={api_key}"
    )
    
    print(f"📥 Richiesta dati in corso per {formatted_ticker} dal {start_date} al {end_date}...")
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
    except URLError as e:
        print(f"❌ Errore di rete nella richiesta: {e}")
        return None
    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")
        return None
        
    if data.get("status") not in ["OK", "DELAYED"] or not data.get("results"):
        print(f"⚠️ Errore o nessun risultato restituito da Polygon.io per {formatted_ticker}.")
        if "message" in data:
            print(f"Messaggio API: {data['message']}")
        return None
        
    return data["results"]

# 4. Formattazione e salvataggio dei risultati
def process_and_save_data(ticker, results):
    if not results:
        return
        
    prices = []
    dates = []
    returns = []
    
    # Estrazione dei prezzi di chiusura e delle date
    for bar in results:
        close_price = bar["c"]
        timestamp = bar["t"] / 1000.0
        date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
        
        prices.append(close_price)
        dates.append(date_str)
        
    # Calcolo dei rendimenti logaritmici: ln(P_t / P_{t-1})
    for i in range(1, len(prices)):
        r_t = math.log(prices[i] / prices[i-1])
        returns.append(r_t)
        
    # Calcolo delle statistiche robuste
    stats = calculate_robust_stats(prices, returns)
    if not stats:
        print("⚠️ Dati insufficienti per elaborare le statistiche.")
        return
        
    print("\n" + "="*50)
    print(f"📊 REPORT STATISTICO QUANTITATIVO: {ticker.upper()}")
    print("="*50)
    print(f"• Prezzo Corrente (Chiusura): {prices[-1]:.4f}")
    print(f"• Media Mobile Semplice (SMA-{len(prices)}d): {stats['sma_price']:.4f}")
    print(f"• Z-Score Robusto del Prezzo:  {stats['robust_price_z_score']:.2f}")
    print(f"• Rendimento Giornaliero:      {stats['latest_return']*100:.3f}%")
    print(f"• Rendimento Mediano Storico:  {stats['median_return']*100:.3f}%")
    print(f"• Standardized MAD Storico:   {stats['standardized_mad']*100:.3f}%")
    print(f"• Z-Score Robusto Rendimento:  {stats['robust_z_score']:.2f}")
    print("-"*50)
    
    # Interpretazione speculativa dell'edge statistico
    z_price = stats['robust_price_z_score']
    print("🔮 INTERPRETAZIONE QUANTITATIVA (EDGE SPECULATIVO):")
    if z_price > 2.0:
        print("⚠️ IPERCOMPRATO STATISTICO (Z-Score > +2): Forte deviazione positiva rispetto alla SMA.\n"
              "   Potenziale inversione a ribasso (Short-Term Mean Reversion Edge).")
    elif z_price < -2.0:
        print("🟢 IPERVENDUTO STATISTICO (Z-Score < -2): Forte deviazione negativa rispetto alla SMA.\n"
              "   Opportunità statistica d'acquisto (Long Entry Speculativa).")
    else:
        print("⚖️ STATISTICAMENTE EQUILIBRATO (Z-Score tra -2 e +2).\n"
              "   Il prezzo oscilla all'interno della fascia di fluttuazione normale basata sulla MAD.")
    print("="*50)
    
    # Creazione della cartella per i dati se non esiste
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    csv_file = os.path.join(output_dir, f"{ticker.lower()}_market_data.csv")
    
    # Scrittura dei dati su file CSV
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("Data,Prezzo_Chiusura,Rendimento_Logaritmico\n")
        f.write(f"{dates[0]},{prices[0]:.6f},0.000000\n")
        for i in range(1, len(prices)):
            f.write(f"{dates[i]},{prices[i]:.6f},{returns[i-1]:.6f}\n")
            
    print(f"💾 Dati storici esportati con successo in: {csv_file}")
    print(f"   (Totale record scritti: {len(prices)})\n")

def main():
    # Imposta encoding UTF-8 per l'output su console Windows
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("🚀 Inizializzazione pipeline dati Polygon.io...")
    api_key = load_api_key()
    
    # Prompt o argomento da riga di comando
    default_tickers = ["SPY", "GLD", "EURUSD", "AAPL"]
    
    if len(sys.argv) > 1:
        selected_ticker = sys.argv[1]
    else:
        print("\nSeleziona un asset da analizzare:")
        for idx, t in enumerate(default_tickers, 1):
            print(f"  {idx}) {t}")
        choice = input("\nInserisci il numero o digita un ticker custom (es. TSLA, QQQ, C:GBPUSD): ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(default_tickers):
            selected_ticker = default_tickers[int(choice) - 1]
        else:
            selected_ticker = choice if choice else "SPY"
            
    results = fetch_polygon_data(selected_ticker, api_key)
    process_and_save_data(selected_ticker, results)

if __name__ == "__main__":
    main()
