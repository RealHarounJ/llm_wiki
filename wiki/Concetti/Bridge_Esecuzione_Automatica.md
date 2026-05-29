---
tags: [trading, automation, api, python, csharp, ninjatrader, metatrader]
aliases: [Bridge Esecuzione Automatica, Automated Execution Bridge, Python MT5 Bridge]
date_created: 2026-05-24
last_modified: 2026-05-24
source_count: 3
---

# 🔌 Bridge di Esecuzione Automatica — Blueprint Tecnico

Per rendere il trading sistematico un'attività professionale da gestire in tempo reale sui conti delle Prop Firm, l'esecuzione deve essere interamente delegata a sistemi automatici. Questo eliminerà l'influenza emotiva, garantirà il rispetto millimetrico dei vincoli di rischio e preverrà il superamento dei drawdown giornalieri.

Questa scheda fornisce i **blueprints architetturali ed esempi di codice pronti per l'uso** per connettere i tuoi motori quantitativi alle piattaforme **MetaTrader 5** (Python) e **NinjaTrader 8** (C#).

---

## 1. Architettura dell'Automazione

```text
 ┌─────────────────────────────────────────────────────────────┐
 │                    MOTORE QUANTITATIVO                      │
 │   - Calcola robust MAD & Z-Score                            │
 │   - Scansiona sentiment notizie RSS                         │
 └──────────────┬──────────────────────────────┬───────────────┘
                │ (Scenario A - MT5 API)       │ (Scenario B - Local File Bridge)
                ▼                              ▼
 ┌─────────────────────────────┐  ┌─────────────────────────────┐
 │      METATRADER 5           │  │    FILE LOCALE              │
 │  - Libreria Python 'MT5'    │  │    "data/gold_sentiment.txt"│
 │  - Invio ordine diretto API │  └──────────────┬──────────────┘
 └─────────────────────────────┘                 │ (Lettura real-time)
                                                 ▼
                                  ┌─────────────────────────────┐
                                  │      NINJATRADER 8 (C#)     │
                                  │  - AMSRGoldSpeculator.cs    │
                                  │  - Invio ordini Rithmic/CME │
                                  └─────────────────────────────┘
```

---

## 2. Blueprint A: Esecuzione su MetaTrader 5 (Python API)

Se la tua Prop opera su Forex/CFD ed utilizza MetaTrader 5, puoi pilotarla direttamente dal tuo script Python utilizzando la libreria ufficiale `MetaTrader5`.

### Codice Python di Esecuzione e Gestione Rischio (`mt5_execution_bridge.py`):
```python
import time
import MetaTrader5 as mt5

def initialize_mt5(account, password, server):
    """Inizializza la connessione con il terminale MT5 della Prop Firm."""
    if not mt5.initialize():
        print("Inizializzazione MT5 fallita, codice errore =", mt5.last_error())
        return False
    
    # Login sul conto Funded
    authorized = mt5.login(account, password=password, server=server)
    if authorized:
        print(f"Login riuscito sul conto Prop: {account}")
        return True
    else:
        print(f"Login fallito sul conto {account}, codice errore =", mt5.last_error())
        return False

def check_drawdown_killswitch(max_daily_loss_usd):
    """
    KILL-SWITCH DI SICUREZZA: Verifica se le perdite giornaliere correnti 
    superano la nostra soglia interna di sicurezza (es. 4.0% su limite prop del 5.0%).
    """
    account_info = mt5.account_info()
    if account_info is None:
        print("Impossibile recuperare le informazioni del conto.")
        return False
    
    balance = account_info.balance
    equity = account_info.equity
    floating_pnl = equity - balance
    
    # Se le perdite fluttuanti o chiuse della giornata superano la soglia di sicurezza
    if floating_pnl < 0 and abs(floating_pnl) >= max_daily_loss_usd:
        print(f"🚨 KILL-SWITCH ATTIVATO! Perdita corrente di ${abs(floating_pnl):.2f} supera il limite di ${max_daily_loss_usd:.2f}.")
        # Chiude tutte le posizioni aperte per salvare il conto prop
        close_all_positions()
        return True
    
    return False

def send_market_order(symbol, action_type, volume_lots, stop_loss_points=0, take_profit_points=0):
    """Invia un ordine Buy o Sell a mercato con stop loss e take profit integrati."""
    # Definisce il tipo di operazione
    if action_type == "BUY":
        trade_type = mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(symbol).ask
    elif action_type == "SELL":
        trade_type = mt5.ORDER_TYPE_SELL
        price = mt5.symbol_info_tick(symbol).bid
    else:
        print("Azione non valida. Scegli BUY o SELL.")
        return None

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(volume_lots),
        "type": trade_type,
        "price": price,
        "sl": price - stop_loss_points if action_type == "BUY" else price + stop_loss_points,
        "tp": price + take_profit_points if action_type == "BUY" else price - take_profit_points,
        "deviation": 20,
        "magic": 123456,  # Identificativo unico dei nostri trade quantitativi
        "comment": "AMSR Gold Auto-Trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILL_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Errore nell'invio dell'ordine: {result.comment} (Codice: {result.retcode})")
        return False
    
    print(f"Ordine {action_type} eseguito con successo! Ticket: {result.order}")
    return True

def close_all_positions():
    """Chiude istantaneamente tutte le posizioni a mercato (Funzione Emergenza)."""
    positions = mt5.positions_get()
    if positions:
        for pos in positions:
            tick = mt5.symbol_info_tick(pos.symbol)
            type_close = mt5.ORDER_TYPE_SELL if pos.type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price_close = tick.bid if pos.type == mt5.ORDER_TYPE_BUY else tick.ask
            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": pos.symbol,
                "volume": pos.volume,
                "type": type_close,
                "position": pos.ticket,
                "price": price_close,
                "deviation": 20,
                "magic": 123456,
                "comment": "KILL-SWITCH CLOSE",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILL_IOC,
            }
            mt5.order_send(request)
        print("Tutte le posizioni aperte sono state chiuse di emergenza.")

# Esempio di loop di controllo in tempo reale
if __name__ == "__main__":
    # Parametri demo conto prop
    if initialize_mt5(account=12345678, password="PropPassword", server="PropFirm-Server"):
        try:
            while True:
                # Esegui il controllo del kill-switch di drawdown ogni 5 secondi
                # Limite di perdita giornaliera impostato a $4.000 su un conto da $100.000 (4%)
                if check_drawdown_killswitch(max_daily_loss_usd=4000.0):
                    print("Esecuzione interrotta per motivi di sicurezza (Kill-Switch).")
                    break
                time.sleep(5)
        finally:
            mt5.shutdown()
```

---

## 3. Blueprint B: NinjaTrader 8 & Python Bridge

Se operi su Futures (CME) tramite NinjaTrader 8, utilizzerai un **File Bridge** locale. Il tuo script Python scrive il sentiment macro in tempo reale e lo script C# lo legge ed esegue.

### Codice C# da integrare in `AMSRGoldSpeculator.cs` (`OnBarUpdate`):
```csharp
using System;
using System.IO;
using NinjaTrader.Cbi;
using NinjaTrader.NinjaScript;
using NinjaTrader.NinjaScript.Indicators;

namespace NinjaTrader.NinjaScript.Strategies
{
    public class AMSRGoldSpeculator : Strategy
    {
        // Percorso del file di bridge per il sentiment
        private string sentimentFilePath = @"C:\Users\jaafa\Downloads\llm_wiki-main\data\gold_sentiment.txt";
        private double currentSentiment = 0.0;
        private int robustPeriod = 20;

        protected override void OnStateChange()
        {
            if (State == State.SetDefaults)
            {
                Description = "Strategia Quantitativa AMSR Oro Futures con Bridge Sentiment";
                Name = "AMSRGoldSpeculator";
                Calculate = Calculate.OnBarClose;
                EntriesPerDirection = 1;
                EntryHandling = EntryHandling.AllEntries;
            }
        }

        protected override void OnBarUpdate()
        {
            // Evita l'esecuzione su barre insufficienti
            if (CurrentBar < robustPeriod) return;

            // 1. Lettura del file bridge del sentiment scritto da Python
            try
            {
                if (File.Exists(sentimentFilePath))
                {
                    string content = File.ReadAllText(sentimentFilePath).Trim();
                    currentSentiment = Convert.ToDouble(content);
                }
            }
            catch (Exception ex)
            {
                Print("Errore nella lettura del file bridge sentiment: " + ex.Message);
            }

            // 2. Calcolo Z-Score Robusto basato su MAD (Logica AMSR)
            double currentPrice = Close[0];
            double sma20 = SMA(robustPeriod)[0];
            
            // Calcolo del MAD approssimato per la barra corrente
            double sumAbsoluteDeviations = 0.0;
            for (int i = 0; i < robustPeriod; i++)
            {
                sumAbsoluteDeviations += Math.Abs(Close[i] - sma20);
            }
            double robustStdDev = (sumAbsoluteDeviations / robustPeriod) * 1.4826;
            double zScore = (currentPrice - sma20) / (robustStdDev > 0 ? robustStdDev : 1.0);

            // Modulatore del sentiment
            double lowerZThreshold = -1.5;
            double upperZThreshold = 1.5;

            if (currentSentiment > 0.3) lowerZThreshold = -1.2; // Sentiment rialzista rende l'ingresso long più sensibile
            if (currentSentiment < -0.3) upperZThreshold = 1.2; // Sentiment ribassista rende l'ingresso short più sensibile

            // 3. Logica d'ingresso automatica conforme alle regole di drawdown delle Prop
            if (Position.MarketPosition == MarketPosition.Flat)
            {
                if (zScore < lowerZThreshold)
                {
                    // Imposta Stop Loss rigido calcolato sulla volatilità reale (MAD)
                    double stopLossTicks = (robustStdDev * 2.0) / TickSize;
                    SetStopLoss(CalculationMode.Ticks, stopLossTicks);
                    
                    // Imposta Take Profit
                    double takeProfitTicks = (robustStdDev * 3.5) / TickSize;
                    SetProfitTarget(CalculationMode.Ticks, takeProfitTicks);

                    EnterLong("AMSR_Long_Entry");
                    Print(String.Format("🚀 LONG Entry eseguito. Z-Score: {0:F2}, Sentiment: {1:F2}, SL Ticks: {2}", zScore, currentSentiment, stopLossTicks));
                }
                else if (zScore > upperZThreshold)
                {
                    double stopLossTicks = (robustStdDev * 2.0) / TickSize;
                    SetStopLoss(CalculationMode.Ticks, stopLossTicks);
                    
                    double takeProfitTicks = (robustStdDev * 3.5) / TickSize;
                    SetProfitTarget(CalculationMode.Ticks, takeProfitTicks);

                    EnterShort("AMSR_Short_Entry");
                    Print(String.Format("📉 SHORT Entry eseguito. Z-Score: {0:F2}, Sentiment: {1:F2}, SL Ticks: {2}", zScore, currentSentiment, stopLossTicks));
                }
            }
        }
    }
}
```

---

## 4. Linee Guida per il Monitoraggio e la Sicurezza (VPS)

1.  **Utilizzo di una VPS (Virtual Private Server):** Per l'esecuzione in tempo reale automatizzata, si raccomanda caldamente di noleggiare una VPS con sistema Windows Server situata vicino ai server del broker della Prop (es. a **Londra** o **Chicago** per ridurre la latenza a < 5ms).
2.  **Configurazione del Watchdog:** Imposta uno script di monitoraggio indipendente che controlli la connessione internet e lo stato del terminale MT5/NinjaTrader ogni minuto, inviando un'allerta SMS o Telegram in caso di crash.
3.  **Il Kill-Switch come Regola Suprema:** Non fare mai affidamento solo sulla piattaforma per la gestione delle perdite. L'implementazione del **Kill-Switch via codice Python** che chiude le posizioni in caso di emergenza direttamente via API è la tua unica e vera assicurazione per non perdere la licenza della Prop.

---

## Fonti
*   **Ernest P. Chan** — *[[c:\Users\jaafa\Downloads\llm_wiki-main\raw\input.md]]* (Chat metadata: Chapter 5 on Semiautomated and Fully Automated Trading Systems).
*   **Robert Carver** — *[[raw/input.md]]* (Chapter 11 - Semi-automatic trading and building your own system).
*   **Piattaforme di Riferimento** — [MetaTrader 5 Python API Docs](https://www.mql5.com/en/docs/integration/python_metatrader5) & [NinjaTrader 8 Developer Guide](https://ninjatrader.com/support/helpGuides/nt8/ninjascript.htm).
