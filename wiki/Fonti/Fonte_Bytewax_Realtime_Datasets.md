---
tags: [fonte, dataset, real-time, finanza, criptovalute, market-data]
aliases: [Bytewax_Realtime_Datasets]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# 📖 Fonte: Bytewax Awesome Public Real-Time Datasets

**File Raw:** `raw/bytewaxawesome-public-real-time-datasets A list of publicly available datasets with real-time data maintained by the team at bytewax.io.md`
**Editore:** Bytewax.io GitHub Community (2026)
**Tipo:** Repository di dataset pubblici ad accesso real-time tramite HTTP REST, RSS, WebSocket e protocolli di streaming (Kafka, STOMP, MQTT).

> Raccolta curata di sorgenti dati in tempo reale, suddivise tra gratuite (Free) e a pagamento (Paid), essenziali per lo sviluppo di pipeline di ingestione dati per il trading algoritmico, l'analisi macroeconomica ed il monitoraggio di sentiment in tempo reale.

---

## 📊 Mapping Sorgenti Finanziarie e Cripto

Di seguito viene sintetizzata la catalogazione delle principali fonti estratte utili alla finanza quantitativa ed alla speculazione:

### 1. Risorse Gratuite (Free Financial Data)
*   **Azionario USA & Criptovalute (Real-time & Storico)**:
    *   **[Polygon.io](https://polygon.io/docs/stocks/getting-started)**: Fornisce ticker, trades e dati book da tutti gli exchange US. Fondamentale per i modelli fattoriali ed il calcolo di premi a frequenza intraday.
    *   **[Alpaca Markets](https://alpaca.markets/docs/market-data/)**: Dati storici e real-time gratuiti tramite WebSocket. Utilizzato per l'esecuzione algoritmica e il backtesting di strategie ad active risk controllato.
    *   **[FinancialData.Net](https://financialdata.net/documentation)**: Bilanci societari storici, insider trading, e flussi istituzionali. Fondamentale per [[Z_Score_Stock_Screening]] su dati fondamentali.
*   **Forex (Cambi Valutari)**:
    *   **[OANDA API Stream](https://github.com/oanda/py-api-streaming)**: Stream gratuito di tassi FX tramite endpoint HTTP. Permette l'implementazione di modelli di arbitraggio statistico ed hedging internazionale.
*   **Macroeconomia e Sentiment**:
    *   **[SEC EDGAR API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)**: Accesso in tempo reale ai filing regolamentari (10-K, 10-Q, 8-K) e dati finanziari strutturati in XBRL. Ideale per la modellizzazione di prior qualitativi e sentiment tramite [[Bayesian_Portfolio_Mojo]].
    *   **[GDELT 2.0 Event Database](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/)**: Monitoraggio globale degli eventi geopolitici in tempo reale con calcolo di valenza emotiva e sentiment per l'analisi macroeconomica sistematica.
*   **Criptovalute & Decentralized Finance**:
    *   **[Pyth Network](https://docs.pyth.network/)**: Oracoli decentralizzati cross-asset operanti a bassa latenza su varie blockchain, eccellente per strategie DeFi cross-chain.
    *   **[Coinbase WebSocket](https://docs.cloud.coinbase.com/exchange/docs/websocket-overview)** & **[Binance Stream](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams)**: Flusso continuo L1 e L2 del limit order book (LOB) per lo studio della microstruttura dei mercati.

### 2. Risorse Professionali (Paid Financial Data)
*   **[Data Bento](https://databento.com/live)**: Soluzione d'élite per la finanza quantitativa a bassa latenza. Offre dati normalizzati da multipli mercati e borse mondiali con API binarie proprietarie (TCP) e client nativi in Python e Rust. Fondamentale per ridurre i costi di latenza ed ottimizzare il coefficiente di trasferimento ($TC$).
*   **[Bloomberg B-PIPE](https://developer.bloomberg.com/)**: Feed consolidato in tempo reale istituzionale a bassissima latenza per la gestione del rischio attivo ed esecuzione di portafogli multi-asset complessi.
*   **[NYSE Cloud Streaming](https://www.nyse.com/data-products)**: Accesso diretto in tempo reale in formato Kafka ai flussi dati nativi del New York Stock Exchange.

---

## 📈 Connessione con il Second Brain

Le sorgenti presenti in questo dataset costituiscono l'infrastruttura di input ("data pipeline") indispensabile per implementare i concetti teorici discussi nel Second Brain:
1.  **Stima dei Fattori Intraday**: I dati real-time di *Polygon.io* consentono di calcolare la covarianza e i fattori sistematici illustrati in [[Fundamental_Factor_Models_Advanced]].
2.  **Calcolo dello Spread in Tempo Reale**: I feed di *OANDA* e *Coinbase* consentono di implementare strategie di pair trading a media-reversione regolate sui costi di transazione in [[Portfolio_Weights_Optimization]].
3.  **Generazione di Bayesian Alpha**: Le news e i sentiment estratti da *GDELT 2.0* o *SEC EDGAR* possono essere modellati tramite funzioni di densità cumulata per generare il vettore delle visioni dell'analista ($\mathbf{Q}$ e $\mathbf{P}$) richiesto in [[Bayesian_Portfolio_Mojo]].

---

## Fonti
*   `raw/bytewaxawesome-public-real-time-datasets A list of publicly available datasets with real-time data maintained by the team at bytewax.io.md`
*   [[wiki/Concetti/Portfolio_Weights_Optimization.md]]
*   [[wiki/Concetti/Fundamental_Factor_Models_Advanced.md]]
