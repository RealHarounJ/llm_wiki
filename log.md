# 📓 Log — Registro Cronologico del Vault

Registro **append-only** di tutte le operazioni sul Second Brain. Ogni entry segue il formato:
`## [YYYY-MM-DD] Tipo | Descrizione`

---

## [2026-05-07] REBUILD | Ricostruzione completa Second Brain da zero

**Operazione:** Reset totale e ricostruzione struttura wiki
**Motivo:** L'utente aveva eliminato le wiki e richiesto un ingest pulito

**File creati — wiki/Concetti/:**
- `Corporate_Finance_Hub.md` — Hub CF con mappa completa
- `Topic_1_Intro_Corporate_Finance.md`
- `Topic_2_Financial_Analysis.md`
- `Topic_3_Statement_of_Cash_Flows.md`
- `Topic_3c_Financial_Planning.md` — EFN formula
- `Topic_3d_Cash_Budgeting.md` — Budget di cassa trimestrale
- `Topic_4_Present_Values.md` — TVM completo
- `Topic_5_NPV_Investment_Criteria.md` — NPV, IRR, PI
- `Topic_6_Risk_and_Return.md` — Varianza, diversificazione
- `Topic_7_8_CAPM_Cost_of_Capital.md` — CAPM, WACC, Beta
- `Data_Mining_Hub.md` — Hub DM con mappa completa
- `Classificazione_Decision_Tree.md` — Decision Tree, Entropia (cap.28 Elmasri)
- `Clustering_KMeans.md` — K-Means base
- `KMeans_Guida_Completa.md` — K-Means avanzato con Python (Towards Data Science)
- `Regole_di_Associazione.md` — Apriori, Support, Confidence, Lift
- `LLM_Hub.md` — Hub AI/LLM
- `GPT_Models.md` — Storia GPT, scaling laws, emergent abilities (Wikipedia)
- `LLM_Changing_Search.md` — LLM e ricerca web, SEO (Analytics Insight)
- `RAG.md` — Retrieval-Augmented Generation architettura completa
- `Semantic_Search.md` — Embedding, cosine similarity
- `AI_in_Education.md` — UNESCO framework (raw/Artificial intelligence in education.md)
- `SQL_Basics.md` — SQL commands, JOIN, aggregazioni

**File creati — wiki/Fonti/:**
- `Fonte_Corporate_Finance_Book.md`
- `Fonte_Slides_Corporate_Finance.md`
- `Fonte_Database_Systems_Elmasri.md`

**File creati — wiki/Progetti/:**
- `Master_Page_Corporate_Finance.md`
- `Master_Page_Data_Mining.md`
- `Master_Page_AI_LLM.md`

**File creati — root:**
- `wiki/Home.md` — Pagina di accesso principale

**Fonti raw processate:**
- `raw/Teaching materials of Corporate Finance-20260505/` (25 file PDF/XLS)
- `raw/Generative pre-trained transformer.md` (Wikipedia GPT)
- `raw/How is LLM Changing Search on the Web.md` (Analytics Insight)
- `raw/7 Most Asked Questions on K-Means Clustering.md` (Towards Data Science)
- `raw/Artificial intelligence in education.md` (UNESCO)
- `raw/SQL_Overview.md`
- `wiki/Fonti/‎Google Gemini.md` (sessione Gemini cap.28 Elmasri)

---

## [2026-05-07] INIT | Creazione index.md e log.md

**Operazione:** Creazione file obbligatori mancanti come da CLAUDE.md
- Creato `index.md` — catalogo centrale di tutte le pagine
- Creato `log.md` — questo file, registro append-only

---

## [2026-05-07] INGEST | Corporate finance.md � Libro Completo Professore

**Fonte raw:** `raw/Corporate finance.md` (326 KB)

**File aggiornati:**
- `wiki/Concetti/Topic_2_Financial_Analysis.md` - RISCRITTA con formule esatte del prof (MVA, EVA, ROC, ROA, ROE, DuPont, Efficiency, Leverage, Liquidity)
- `wiki/Fonti/Fonte_Corporate_Finance_Libro_Professore.md` - Scheda fonte nuova

**Capitoli coperti:** Ch.1, Ch.29 (Financial Analysis), Ch.30 (Planning), Ch.2 (PV/NPV), Ch.5 (IRR), Ch.6 (Capital Budgeting)

---

## [2026-05-12] INGEST | Debt Financing & Real Options

**Fonti raw:** 
- 
aw/Note Taking & Research Assistant Powered by AI 2.md (Debt Financing)
- 
aw/Note Taking & Research Assistant Powered by AI 1.md (Real Options)

**File aggiornati:**
- wiki/Concetti/Debt_Financing.md [NEW]
- wiki/Concetti/Real_Options.md [NEW]
- index.md (Aggiornato catalogo)

**Argomenti coperti:**
- Classificazione debito per scadenza (Maturity), seniority e security.
- Tipologie di obbligazioni (Convertibili, Callable, Exotic).
- Debito bancario e Commercial Paper.
- Opzioni reali: espansione, abbandono, timing, produzione.
- Alberi decisionali per flessibilit� NPV.

---

## [2026-05-12] INGEST | NoSQL & Business Information Systems

**Fonte raw:** 
aw/Fundamentals of Database Systems (Elmasri) Cap. 24

**File aggiornati:**
- wiki/Concetti/NoSQL_Databases.md [NEW]
- index.md (Aggiornato catalogo)

**Argomenti coperti:**
- NoSQL vs SQL: 3V of Big Data.
- 4 NoSQL Models: Key-Value, Document, Column-Family, Graph.
- CAP Theorem (Consistency, Availability, Partition Tolerance).
- BASE properties vs ACID.

---

## [2026-05-14] Ingest | haroun_academy.sql e healthcare_db.sql

## [2026-05-16] INGEST | Sociologia � Digitalizzazione e Welfare State (8 Capitoli)

**Fonte:** Libro "Digitalization and the Future of the Democratic Welfare State"
**Capitoli ingested:** Cap. 2, 3, 13, 15, 18 + Introduzione

**File creati � wiki/Fonti/:**
- `Fonte_Sociologia_Digitalizzazione.md` � Scheda fonte completa con tutti i capitoli

**File creati � wiki/Sociologia/:**
- `Q1_Digitalization_and_Labour_Market.md` � RBTC, SBTC, Labour Market Polarization, Platform Work (Picot)
- `Q2_Digitalization_and_Welfare_State.md` � Pension systems, ADM/SyRI, UBI, Social Investment
- `Q3_Health_Care_and_Digitalization.md` � Crowding Out Effect, Cultural Health Capital, Jensen & Kersbergen

**Wikilinks creati:** [[RBTC]], [[SBTC]], [[Labour Market Polarization]], [[Platform Work]], [[Universal Basic Income]], [[Crowding Out Effect]], [[Cultural Health Capital]], [[ADM Automated Decision-Making]], [[Pension Systems Three Pillars]], [[Social Investment State]]

**Domande esame coperte:** Q1 Labour Market, Q2 Welfare State, Q3 Healthcare (Esame 12 Giugno 2024)

## [2026-05-18] INGEST | Data Warehouse  Teoria Tecnica e Modelli

**Operazione:** Creazione e sintesi degli appunti di Data Warehouse a seguito della simulazione d'esame.
**Fonte:** Sessione di studio interattiva + Appunti raw in DATA Warehouse.md

**File creati  wiki/Concetti/:**
- `Data_Warehouse.md`  Super Technical Theory (OLTP vs OLAP, Inmon, ETL, MDM, MOLAP/ROLAP/HOLAP, Star vs Snowflake Schema)

**Wikilinks creati:** [[OLTP]], [[OLAP]], [[ETL]], [[Master Data Management]], [[MOLAP]], [[ROLAP]], [[HOLAP]], [[Star Schema]], [[Snowflake Schema]], [[Fact Constellation]]

---

## [2026-05-19] INGEST | Industrial Organization & Data Mining Chapter 28

**Operazione:** Creazione delle schede di concetto per Industrial Organization (Lezioni 1-16) e della sessione di studio per Data Mining.
**Fonti:** Slide corso IO, libro Richards et al. (2014) + Capitolo 28 Elmasri & Navathe (Data Mining).

**File creati/modificati:**
- `wiki/Progetti/Master_Page_Industrial_Organization.md` — Cruscotto dello studio di IO
- `wiki/Concetti/IO_01_Microeconomics.md` ... `IO_08_Econometrics.md` — Concetti chiave delle lezioni
- `wiki/Esercitazioni/Data_Mining_Full_Session.md` — Cheat sheet e sintesi teorica KDD, Apriori, Decision Trees, K-Means, BIRCH, Genetic Algorithms.
- `index.md` — Aggiornato catalogo

---

## [2026-05-20] STUDY | Esercizio 1 — Conference Review Database (ER Schema)

**Operazione:** Analisi dei requisiti e stesura del diagramma ER concettuale e logico per la gestione delle sottomissioni e revisioni articoli.
**Fonte:** Esercizio 1 da traccia d'esame.

**File creati/modificati:**
- `wiki/Esercitazioni/Esercizio_Conference_Review.md` — Analisi dettagliata, diagramma ER Crow's Foot e Chen (Mermaid), schema logico e gestione vincoli.
- `index.md` — Indicizzazione della sezione Esercitazioni.

---

## [2026-05-20] STUDY | Car Dealer Mapping, Netflix ER & NoSQL Advanced Masterclass

**Operazione:** Risoluzione esercizio di mappatura avanzata (Car Dealer), modellazione ER streaming (Netflix), chiarimenti sui vincoli relazionali di integrità (PK/FK) e stesura della Masterclass sui database NoSQL avanzati.
**Fonte:** Esercizio 2 da traccia d'esame, traccia Netflix ed Elmasri & Navathe Cap. 24.

**File creati/modificati:**
- `wiki/Esercitazioni/Esercizio_Car_Dealer_Mapping.md` — Mappatura EER a Relazionale passo-passo, opzione 8A per superclasse/sottoclassi, risoluzione della chiave primaria su relazione ternaria con partecipazione (1,1).
- `wiki/Esercitazioni/Esercizio_Netflix_ER.md` — Requisiti, modello ER e schema relazionale per una piattaforma di streaming.
- `wiki/Concetti/NoSQL_Databases.md` — Riscritto da zero in italiano per fungere da Masterclass NoSQL (Consistent Hashing, Ring Topology, Virtual Nodes, Quorum N-R-W e Orologi Vettoriali).
- `index.md` — Aggiornati riferimenti e descrizioni catalogo.

---

## [2026-05-20] STUDY | SQL DML Operations and Data Warehouse Theory Quiz

**Operazione:** Risoluzione interattiva di query DML (INSERT, UPDATE, DELETE) e ripasso dei concetti teorici fondamentali sul Data Warehouse.
**Fonte:** Esercitazioni di SQL e quiz di teoria DWH (OLAP vs OLTP, ETL loading precedence, MDM Backflushing, Star vs Snowflake ROLAP, ed OLAP Operations).

**File modificati:**
- `log.md` — Aggiornato il registro delle sessioni di studio.

---

## [2026-05-20] INGEST | Hedge Funds & Group 11 Comparative Digitalization Case Study

- **Fonti raw:** `raw/How can I start hedgefund.md`, `raw/Step-by-Step Guide to Starting a Hedge Fund.md`, `raw/I have worked on trading floor in investment banks for over a decade, ask me anything.md`, `raw/group_11_extracted.txt`.
- **File creati:**
  - `wiki/Fonti/Fonte_Reddit_Hedge_Fund_Start.md`
  - `wiki/Fonti/Fonte_Investopedia_Hedge_Fund_Guide.md`
  - `wiki/Fonti/Fonte_Reddit_Trading_Floor_AMA.md`
  - `wiki/Concetti/Hedge_Funds_and_Trading_Desks.md`
  - `wiki/Fonti/Fonte_Presentazione_Gruppo_11.md`
  - `wiki/Sociologia/Caso_Studio_Digitalizzazione_Comparata.md`
- **File modificati:**
  - `wiki/Sociologia/Q1_Digitalization_and_Labour_Market.md` (integrato impatto RBTC coreano: -73k impieghi manifatturieri vs +492k servizi)
  - `wiki/Sociologia/Q2_Digitalization_and_Welfare_State.md` (integrato AI Basic Act e "My Data" Welfare Portal coreani)
  - `wiki/Sociologia/Q3_Health_Care_and_Digitalization.md` (integrato calo spesa istruzione -4.4% in Arabia Saudita come validazione di Crowding Out)
  - `index.md` (indicizzato tutti i 6 nuovi file)
  - `log.md` (questo file)

---

## [2026-05-20] STUDY | Analisi Quantitativa del Portafoglio di Haroun (Trading 212)

- **Operazione:** Analisi e strutturazione del portafoglio personale di Trading 212, evidenziando i rischi di concentrazione e proponendo una strategia Core-Satellite basata sulla finanza classica.
- **File creati:** `wiki/Progetti/Analisi_Portafoglio_Haroun.md` [NEW]
- **File modificati:**
  - `index.md` (registrato il nuovo progetto di analisi finanziaria)
  - `log.md` (questo file)

---

## [2026-05-20] DEV | Creazione Script di Rebalancing Portafoglio Haroun

- **Operazione:** Sviluppo di uno script Python locale per il calcolo del "No-Sell Rebalancing" per gli investimenti mensili ricorrenti del PAC, pre-popolato con le posizioni e i pesi reali e allineato ai target del modello Core-Satellite.
- **File creati:** `wiki/Script/rebalance_portfolio.py` [NEW]
- **File modificati:**
  - `index.md` (indicizzato il nuovo script in libreria)
  - `log.md` (questo file)

---

## [2026-05-21] STUDY | Interactive Sociology & C1 English Tutoring: Welfare State Dilemmas & Essays

- **Operazione:** Sessione di studio interattiva e stesura di risposte d'esame complete in inglese accademico C1. Redatti i tre saggi d'esame completi ("Full Exam-Ready Essay Answers") per la Domanda 1 (Mercato del Lavoro: SBTC vs RBTC, polarizzazione, gig economy), la Domanda 2 (Welfare State: Veil of Ignorance, ADM, pensioni e sindacati, Social Investment vs UBI) e il Caso Studio Comparato del Gruppo 11 (Corea del Sud vs Arabia Saudita: Vision 2030, Baumol's Cost Disease, Crowding Out e AI Basic Act).
- **File modificati:**
  - `wiki/Sociologia/Q1_Digitalization_and_Labour_Market.md` (aggiunta la sezione di saggio d'esame completo ottimizzato in inglese C1)
  - `wiki/Sociologia/Q2_Digitalization_and_Welfare_State.md` (aggiunto il saggio d'esame completo in inglese C1, più l'integrazione di tutte le risposte ottimizzate)
  - `wiki/Sociologia/Caso_Studio_Digitalizzazione_Comparata.md` (aggiunto il saggio d'esame completo in inglese C1 con l'analisi empirica dettagliata della presentazione)
  - `log.md` (questo file)

---

## [2026-05-21] DEV | Vault Linting & Structural Cleanup

- **Operazione:** Bonifica strutturale completa (linting) del vault Obsidian per eliminare ridondanze, allineare la struttura a quanto sancito da `CLAUDE.md`, rimuovere file vuoti o non tracciati e garantire la perfetta consistenza delle relazioni.
- **Cartelle ed Elementi Eliminati:**
  - Eliminata la cartella cache duplicata `_fit/` (2.117 file obsoleti generati da plugin esterni).
  - Rimossa la cartella vuota `Notion/`.
  - Eliminato il file corrotto duplicato `wiki/Fonti/‎Google Gemini.md` (ritagli di sessioni non strutturati).
- **Riorganizzazione Fonti Notion (Database e Data Mining):**
  - Rinominati e formattati 10 file grezzi in `wiki/Fonti/` (da `Where teams and agents work together*.md` e `data mining 1.md` a `Fonte_Elmasri_Cap*.md`), inserendo H1 significativi, correggendo l'HTML Notion, aggiungendo YAML frontmatter valido e agganciando la sezione `## Fonti` alla risorsa originaria `Fundamentals of Database Systems`.
- **Creazione Nuove Pagine Concettuali:**
  - `wiki/Concetti/ETL_Process.md` (Pipeline ETL, MDM, Golden Record, Backflushing).
  - `wiki/Concetti/Transformer_Architecture.md` (Self-attention, Positional Encoding, Multi-head, Encoder-Decoder).
  - `wiki/Concetti/Architettura_DBMS.md` (Architettura a tre schemi, indipendenza fisica/logica dei dati, ruoli DBA/designer).
- **Automazione & Metadati:**
  - Esecuzione di script custom PowerShell per normalizzare i frontmatter YAML (`tags`, `aliases`, `date_created`, `last_modified`, `source_count`) ed eliminare intestazioni orfane o malformate (es. raddoppio intestazioni `## ## Fonti`).
- **Sincronizzazione Indici:**
  - Aggiornato e allineato integralmente `index.md` con l'inclusione di tutti i 10 file Elmasri rinominati, 13 concetti di Corporate Finance prima non indicizzati, guide linguistiche (`wiki/Lingua/`), ristoranti (`wiki/Kiro_Kiro/`), schede esercitazione ed `ETL_Process`, `Transformer_Architecture`, `Architettura_DBMS`.
- **Verifica Finale:**
  - Eseguito `lint_check.ps1` ottenendo il **100% di conformità**: 0 file vuoti, 0 file orfani/non collegati, 0 dead link, 0 violazioni strutturali su 144 file markdown totali in `wiki/`.

---

## [2026-05-21] INGEST | Quantitative Portfolio Management — Ingestione Completa (Fasi 1, 2, 3, 4)

- **Fonti raw:** `raw/Quantitative_Equity_Portfolio_Management_Chincarini.md`, `raw/Active_Portfolio_Management_Grinold_Kahn.md`
- **File creati — wiki/Fonti/:**
  - `Fonte_Chincarini_QEPM.md` — Scheda fonte completa per Ludwig Chincarini's QEPM (2023)
  - `Fonte_Grinold_Kahn_APM.md` — Scheda fonte per Grinold & Kahn's Active Portfolio Management con dizionario bilingue di finanza quantitativa (Cinese ➔ Inglese)
- **File creati — wiki/Concetti/:**
  - **Fase 1 (Fundamentals & IR)**: 
    - `Information_Ratio_IR.md` — Rigorosa trattazione teorica e matematica di ex-ante ed ex-post Information Ratio, confronto con Sharpe Ratio e standard empirici.
    - `Fundamental_Law_of_Active_Management.md` — La legge fondamentale di Grinold nelle versioni base ed estesa con Transfer Coefficient ($TC$), Information Coefficient ($IC$) e Breadth ($BR$).
  - **Fase 2 (Factor Modeling & Screening)**:
    - `Z_Score_Stock_Screening.md` — Punteggi Z-score singoli ed aggregati, Winsorization, standardizzazione robusta MAD e conversione in rendimenti attesi.
    - `Fundamental_Factor_Models_Advanced.md` — Regressione a fattori cross-sectional via OLS e MAD pesato, errori standard HAC (Newey-West), decomposizione del rischio attivo.
  - **Fase 3 (Portfolio Optimization & Market Neutral)**:
    - `Portfolio_Weights_Optimization.md` — Formulazione QP di media-varianza ed active risk (tracking error), vincoli reali, costi di transazione lineari e non lineari (market impact).
    - `Market_Neutral_Portfolios.md` — Dollar neutrality vs Beta neutrality, 2-Alpha mojo, analisi della varianza e dell'IR in leva, Prime Brokerage, prestito titoli e Portable Alpha.
  - **Fase 4 (Performance Attribution & Bayesian Alpha)**:
    - `Bayesian_Portfolio_Mojo.md` — priorità bayesiana, quantificazione di prior qualitativi da stock screens/rankings/raccomandazioni (prior Chincarini), e il Modello di Black-Litterman matriciale.
    - `Performance_Attribution_Active.md` — Decomposizione classica di Brinson-Hood-Beebower (BHB) e Brinson-Fachler (BF), e attribuzione quantitativa multi-fattoriale del rendimento attivo ex-post.
- **File modificati:**
  - `index.md` (registrate e indicizzate tutte le nuove fonti e note concettuali)
  - `log.md` (questo file)

---

## [2026-05-21] INGEST | Bytewax Real-Time Datasets List

- **Fonte raw:** `raw/bytewaxawesome-public-real-time-datasets A list of publicly available datasets with real-time data maintained by the team at bytewax.io.md`
- **File creati — wiki/Fonti/:**
  - `Fonte_Bytewax_Realtime_Datasets.md` — Scheda fonte con mappatura di feed per finanza quantitativa e sentiment
- **File modificati:**
  - `index.md` (registrata e indicizzata la nuova fonte nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-21] DEV | Integrazione Polygon API Key e Script Market Data

- **Operazione:** Configurazione delle credenziali API dell'utente e sviluppo dello script per l'ingestione e l'analisi quantitativa.
- **File creati:**
  - `.env` [NEW] — Contiene in modo sicuro la chiave API di Polygon.io.
  - `wiki/Script/fetch_market_data.py` [NEW] — Script Python autoinstallante (standard library) per l'estrazione di dati storici e real-time e calcolo delle metriche statistiche MAD e Z-Score robusti.
- **File modificati:**
  - `index.md` (registrato il nuovo script nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-22] DEV | Integrazione Strategia Speculativa Oro (AMSR)

- **Operazione:** Progettazione, sviluppo e validazione della strategia quantitativa multi-day swing trading sull'oro spot (modello AMSR). Integrazione di feed storici (AurumRates) e macro-news sentiment (Google News RSS via NLP lessicale).
- **File creati/modificati:**
  - `wiki/Script/gold_swing_trader.py` [NEW] — Motore quantitativo con download prezzi, sentiment analysis lessicale, robust MAD-based Z-score, crossover trend, backtest storico completo e dashboard UTF-8.
  - `wiki/Concetti/Gold_Speculation_Strategy.md` [NEW] — Nota metodologica Obsidian su crossover trend, gestione del rischio con stop loss dinamici e trailing stop MAD-based.
  - `index.md` (indicizzati i nuovi file nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-22] DEV | Collegamento Strategia AMSR a NinjaTrader 8 (Bridge Demo)

- **Operazione:** Sviluppo del bridge di sentiment ed esportazione in tempo reale della strategia quantitativa sull'oro su NinjaTrader 8 (Demo). Scrittura di uno script C# NinjaScript nativo per i grafici e la gestione ordini.
- **File creati/modificati:**
  - `wiki/Script/AMSRGoldSpeculator.cs` [NEW] — Strategia NinjaScript C# per NinjaTrader 8. Calcola SMA crossover, robust MAD, Z-score ed integra il file bridge di sentiment.
  - `wiki/Script/gold_swing_trader.py` (modificato per scrivere automaticamente `data/gold_sentiment.txt` ad ogni esecuzione).
  - `index.md` (registrato il nuovo script C# nel catalogo centrale).
  - `log.md` (questo file).

---
**File creati  wiki/Concetti/:**
- `Data_Warehouse.md`  Super Technical Theory (OLTP vs OLAP, Inmon, ETL, MDM, MOLAP/ROLAP/HOLAP, Star vs Snowflake Schema)

**Wikilinks creati:** [[OLTP]], [[OLAP]], [[ETL]], [[Master Data Management]], [[MOLAP]], [[ROLAP]], [[HOLAP]], [[Star Schema]], [[Snowflake Schema]], [[Fact Constellation]]

---

## [2026-05-19] INGEST | Industrial Organization & Data Mining Chapter 28

**Operazione:** Creazione delle schede di concetto per Industrial Organization (Lezioni 1-16) e della sessione di studio per Data Mining.
**Fonti:** Slide corso IO, libro Richards et al. (2014) + Capitolo 28 Elmasri & Navathe (Data Mining).

**File creati/modificati:**
- `wiki/Progetti/Master_Page_Industrial_Organization.md` — Cruscotto dello studio di IO
- `wiki/Concetti/IO_01_Microeconomics.md` ... `IO_08_Econometrics.md` — Concetti chiave delle lezioni
- `wiki/Esercitazioni/Data_Mining_Full_Session.md` — Cheat sheet e sintesi teorica KDD, Apriori, Decision Trees, K-Means, BIRCH, Genetic Algorithms.
- `index.md` — Aggiornato catalogo

---

## [2026-05-20] STUDY | Esercizio 1 — Conference Review Database (ER Schema)

**Operazione:** Analisi dei requisiti e stesura del diagramma ER concettuale e logico per la gestione delle sottomissioni e revisioni articoli.
**Fonte:** Esercizio 1 da traccia d'esame.

**File creati/modificati:**
- `wiki/Esercitazioni/Esercizio_Conference_Review.md` — Analisi dettagliata, diagramma ER Crow's Foot e Chen (Mermaid), schema logico e gestione vincoli.
- `index.md` — Indicizzazione della sezione Esercitazioni.

---

## [2026-05-20] STUDY | Car Dealer Mapping, Netflix ER & NoSQL Advanced Masterclass

**Operazione:** Risoluzione esercizio di mappatura avanzata (Car Dealer), modellazione ER streaming (Netflix), chiarimenti sui vincoli relazionali di integrità (PK/FK) e stesura della Masterclass sui database NoSQL avanzati.
**Fonte:** Esercizio 2 da traccia d'esame, traccia Netflix ed Elmasri & Navathe Cap. 24.

**File creati/modificati:**
- `wiki/Esercitazioni/Esercizio_Car_Dealer_Mapping.md` — Mappatura EER a Relazionale passo-passo, opzione 8A per superclasse/sottoclassi, risoluzione della chiave primaria su relazione ternaria con partecipazione (1,1).
- `wiki/Esercitazioni/Esercizio_Netflix_ER.md` — Requisiti, modello ER e schema relazionale per una piattaforma di streaming.
- `wiki/Concetti/NoSQL_Databases.md` — Riscritto da zero in italiano per fungere da Masterclass NoSQL (Consistent Hashing, Ring Topology, Virtual Nodes, Quorum N-R-W e Orologi Vettoriali).
- `index.md` — Aggiornati riferimenti e descrizioni catalogo.

---

## [2026-05-20] STUDY | SQL DML Operations and Data Warehouse Theory Quiz

**Operazione:** Risoluzione interattiva di query DML (INSERT, UPDATE, DELETE) e ripasso dei concetti teorici fondamentali sul Data Warehouse.
**Fonte:** Esercitazioni di SQL e quiz di teoria DWH (OLAP vs OLTP, ETL loading precedence, MDM Backflushing, Star vs Snowflake ROLAP, ed OLAP Operations).

**File modificati:**
- `log.md` — Aggiornato il registro delle sessioni di studio.

---

## [2026-05-20] INGEST | Hedge Funds & Group 11 Comparative Digitalization Case Study

- **Fonti raw:** `raw/How can I start hedgefund.md`, `raw/Step-by-Step Guide to Starting a Hedge Fund.md`, `raw/I have worked on trading floor in investment banks for over a decade, ask me anything.md`, `raw/group_11_extracted.txt`.
- **File creati:**
  - `wiki/Fonti/Fonte_Reddit_Hedge_Fund_Start.md`
  - `wiki/Fonti/Fonte_Investopedia_Hedge_Fund_Guide.md`
  - `wiki/Fonti/Fonte_Reddit_Trading_Floor_AMA.md`
  - `wiki/Concetti/Hedge_Funds_and_Trading_Desks.md`
  - `wiki/Fonti/Fonte_Presentazione_Gruppo_11.md`
  - `wiki/Sociologia/Caso_Studio_Digitalizzazione_Comparata.md`
- **File modificati:**
  - `wiki/Sociologia/Q1_Digitalization_and_Labour_Market.md` (integrato impatto RBTC coreano: -73k impieghi manifatturieri vs +492k servizi)
  - `wiki/Sociologia/Q2_Digitalization_and_Welfare_State.md` (integrato AI Basic Act e "My Data" Welfare Portal coreani)
  - `wiki/Sociologia/Q3_Health_Care_and_Digitalization.md` (integrato calo spesa istruzione -4.4% in Arabia Saudita come validazione di Crowding Out)
  - `index.md` (indicizzato tutti i 6 nuovi file)
  - `log.md` (questo file)

---

## [2026-05-20] STUDY | Analisi Quantitativa del Portafoglio di Haroun (Trading 212)

- **Operazione:** Analisi e strutturazione del portafoglio personale di Trading 212, evidenziando i rischi di concentrazione e proponendo una strategia Core-Satellite basata sulla finanza classica.
- **File creati:** `wiki/Progetti/Analisi_Portafoglio_Haroun.md` [NEW]
- **File modificati:**
  - `index.md` (registrato il nuovo progetto di analisi finanziaria)
  - `log.md` (questo file)

---

## [2026-05-20] DEV | Creazione Script di Rebalancing Portafoglio Haroun

- **Operazione:** Sviluppo di uno script Python locale per il calcolo del "No-Sell Rebalancing" per gli investimenti mensili ricorrenti del PAC, pre-popolato con le posizioni e i pesi reali e allineato ai target del modello Core-Satellite.
- **File creati:** `wiki/Script/rebalance_portfolio.py` [NEW]
- **File modificati:**
  - `index.md` (indicizzato il nuovo script in libreria)
  - `log.md` (questo file)

---

## [2026-05-21] STUDY | Interactive Sociology & C1 English Tutoring: Welfare State Dilemmas & Essays

- **Operazione:** Sessione di studio interattiva e stesura di risposte d'esame complete in inglese accademico C1. Redatti i tre saggi d'esame completi ("Full Exam-Ready Essay Answers") per la Domanda 1 (Mercato del Lavoro: SBTC vs RBTC, polarizzazione, gig economy), la Domanda 2 (Welfare State: Veil of Ignorance, ADM, pensioni e sindacati, Social Investment vs UBI) e il Caso Studio Comparato del Gruppo 11 (Corea del Sud vs Arabia Saudita: Vision 2030, Baumol's Cost Disease, Crowding Out e AI Basic Act).
- **File modificati:**
  - `wiki/Sociologia/Q1_Digitalization_and_Labour_Market.md` (aggiunta la sezione di saggio d'esame completo ottimizzato in inglese C1)
  - `wiki/Sociologia/Q2_Digitalization_and_Welfare_State.md` (aggiunto il saggio d'esame completo in inglese C1, più l'integrazione di tutte le risposte ottimizzate)
  - `wiki/Sociologia/Caso_Studio_Digitalizzazione_Comparata.md` (aggiunto il saggio d'esame completo in inglese C1 con l'analisi empirica dettagliata della presentazione)
  - `log.md` (questo file)

---

## [2026-05-21] DEV | Vault Linting & Structural Cleanup

- **Operazione:** Bonifica strutturale completa (linting) del vault Obsidian per eliminare ridondanze, allineare la struttura a quanto sancito da `CLAUDE.md`, rimuovere file vuoti o non tracciati e garantire la perfetta consistenza delle relazioni.
- **Cartelle ed Elementi Eliminati:**
  - Eliminata la cartella cache duplicata `_fit/` (2.117 file obsoleti generati da plugin esterni).
  - Rimossa la cartella vuota `Notion/`.
  - Eliminato il file corrotto duplicato `wiki/Fonti/‎Google Gemini.md` (ritagli di sessioni non strutturati).
- **Riorganizzazione Fonti Notion (Database e Data Mining):**
  - Rinominati e formattati 10 file grezzi in `wiki/Fonti/` (da `Where teams and agents work together*.md` e `data mining 1.md` a `Fonte_Elmasri_Cap*.md`), inserendo H1 significativi, correggendo l'HTML Notion, aggiungendo YAML frontmatter valido e agganciando la sezione `## Fonti` alla risorsa originaria `Fundamentals of Database Systems`.
- **Creazione Nuove Pagine Concettuali:**
  - `wiki/Concetti/ETL_Process.md` (Pipeline ETL, MDM, Golden Record, Backflushing).
  - `wiki/Concetti/Transformer_Architecture.md` (Self-attention, Positional Encoding, Multi-head, Encoder-Decoder).
  - `wiki/Concetti/Architettura_DBMS.md` (Architettura a tre schemi, indipendenza fisica/logica dei dati, ruoli DBA/designer).
- **Automazione & Metadati:**
  - Esecuzione di script custom PowerShell per normalizzare i frontmatter YAML (`tags`, `aliases`, `date_created`, `last_modified`, `source_count`) ed eliminare intestazioni orfane o malformate (es. raddoppio intestazioni `## ## Fonti`).
- **Sincronizzazione Indici:**
  - Aggiornato e allineato integralmente `index.md` con l'inclusione di tutti i 10 file Elmasri rinominati, 13 concetti di Corporate Finance prima non indicizzati, guide linguistiche (`wiki/Lingua/`), ristoranti (`wiki/Kiro_Kiro/`), schede esercitazione ed `ETL_Process`, `Transformer_Architecture`, `Architettura_DBMS`.
- **Verifica Finale:**
  - Eseguito `lint_check.ps1` ottenendo il **100% di conformità**: 0 file vuoti, 0 file orfani/non collegati, 0 dead link, 0 violazioni strutturali su 144 file markdown totali in `wiki/`.

---

## [2026-05-21] INGEST | Quantitative Portfolio Management — Ingestione Completa (Fasi 1, 2, 3, 4)

- **Fonti raw:** `raw/Quantitative_Equity_Portfolio_Management_Chincarini.md`, `raw/Active_Portfolio_Management_Grinold_Kahn.md`
- **File creati — wiki/Fonti/:**
  - `Fonte_Chincarini_QEPM.md` — Scheda fonte completa per Ludwig Chincarini's QEPM (2023)
  - `Fonte_Grinold_Kahn_APM.md` — Scheda fonte per Grinold & Kahn's Active Portfolio Management con dizionario bilingue di finanza quantitativa (Cinese ➔ Inglese)
- **File creati — wiki/Concetti/:**
  - **Fase 1 (Fundamentals & IR)**: 
    - `Information_Ratio_IR.md` — Rigorosa trattazione teorica e matematica di ex-ante ed ex-post Information Ratio, confronto con Sharpe Ratio e standard empirici.
    - `Fundamental_Law_of_Active_Management.md` — La legge fondamentale di Grinold nelle versioni base ed estesa con Transfer Coefficient ($TC$), Information Coefficient ($IC$) e Breadth ($BR$).
  - **Fase 2 (Factor Modeling & Screening)**:
    - `Z_Score_Stock_Screening.md` — Punteggi Z-score singoli ed aggregati, Winsorization, standardizzazione robusta MAD e conversione in rendimenti attesi.
    - `Fundamental_Factor_Models_Advanced.md` — Regressione a fattori cross-sectional via OLS e MAD pesato, errori standard HAC (Newey-West), decomposizione del rischio attivo.
  - **Fase 3 (Portfolio Optimization & Market Neutral)**:
    - `Portfolio_Weights_Optimization.md` — Formulazione QP di media-varianza ed active risk (tracking error), vincoli reali, costi di transazione lineari e non lineari (market impact).
    - `Market_Neutral_Portfolios.md` — Dollar neutrality vs Beta neutrality, 2-Alpha mojo, analisi della varianza e dell'IR in leva, Prime Brokerage, prestito titoli e Portable Alpha.
  - **Fase 4 (Performance Attribution & Bayesian Alpha)**:
    - `Bayesian_Portfolio_Mojo.md` — priorità bayesiana, quantificazione di prior qualitativi da stock screens/rankings/raccomandazioni (prior Chincarini), e il Modello di Black-Litterman matriciale.
    - `Performance_Attribution_Active.md` — Decomposizione classica di Brinson-Hood-Beebower (BHB) e Brinson-Fachler (BF), e attribuzione quantitativa multi-fattoriale del rendimento attivo ex-post.
- **File modificati:**
  - `index.md` (registrate e indicizzate tutte le nuove fonti e note concettuali)
  - `log.md` (questo file)

---

## [2026-05-21] INGEST | Bytewax Real-Time Datasets List

- **Fonte raw:** `raw/bytewaxawesome-public-real-time-datasets A list of publicly available datasets with real-time data maintained by the team at bytewax.io.md`
- **File creati — wiki/Fonti/:**
  - `Fonte_Bytewax_Realtime_Datasets.md` — Scheda fonte con mappatura di feed per finanza quantitativa e sentiment
- **File modificati:**
  - `index.md` (registrata e indicizzata la nuova fonte nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-21] DEV | Integrazione Polygon API Key e Script Market Data

- **Operazione:** Configurazione delle credenziali API dell'utente e sviluppo dello script per l'ingestione e l'analisi quantitativa.
- **File creati:**
  - `.env` [NEW] — Contiene in modo sicuro la chiave API di Polygon.io.
  - `wiki/Script/fetch_market_data.py` [NEW] — Script Python autoinstallante (standard library) per l'estrazione di dati storici e real-time e calcolo delle metriche statistiche MAD e Z-Score robusti.
- **File modificati:**
  - `index.md` (registrato il nuovo script nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-22] DEV | Integrazione Strategia Speculativa Oro (AMSR)

- **Operazione:** Progettazione, sviluppo e validazione della strategia quantitativa multi-day swing trading sull'oro spot (modello AMSR). Integrazione di feed storici (AurumRates) e macro-news sentiment (Google News RSS via NLP lessicale).
- **File creati/modificati:**
  - `wiki/Script/gold_swing_trader.py` [NEW] — Motore quantitativo con download prezzi, sentiment analysis lessicale, robust MAD-based Z-score, crossover trend, backtest storico completo e dashboard UTF-8.
  - `wiki/Concetti/Gold_Speculation_Strategy.md` [NEW] — Nota metodologica Obsidian su crossover trend, gestione del rischio con stop loss dinamici e trailing stop MAD-based.
  - `index.md` (indicizzati i nuovi file nel catalogo centrale)
  - `log.md` (questo file)

---

## [2026-05-22] DEV | Collegamento Strategia AMSR a NinjaTrader 8 (Bridge Demo)

- **Operazione:** Sviluppo del bridge di sentiment ed esportazione in tempo reale della strategia quantitativa sull'oro su NinjaTrader 8 (Demo). Scrittura di uno script C# NinjaScript nativo per i grafici e la gestione ordini.
- **File creati/modificati:**
  - `wiki/Script/AMSRGoldSpeculator.cs` [NEW] — Strategia NinjaScript C# per NinjaTrader 8. Calcola SMA crossover, robust MAD, Z-score ed integra il file bridge di sentiment.
  - `wiki/Script/gold_swing_trader.py` (modificato per scrivere automaticamente `data/gold_sentiment.txt` ad ogni esecuzione).
  - `index.md` (registrato il nuovo script C# nel catalogo centrale).
  - `log.md` (questo file).

---

## [2026-05-22] EXERCISE | Esercitazione Corporate Finance - Soluzioni Complete

- **Operazione:** Risoluzione rigorosa, accademica e definitiva di tutte le domande del file grezzo `questions corporate finance.md`. Scrittura del modulo del caso pratico "Vega Corporation" (Blocco 6) con attualizzazioni a leva (WACC 8.6%) e unlevered (Equity 13%), calcolo dell'Operating Cash Flow, variazione del capitale circolante e dimostrazione della conservazione dell'IRR al variare della struttura finanziaria.
- **File creati/modificati:**
  - `wiki/Esercitazioni/Soluzioni_Domande_Corporate_Finance.md` (Completato con l'inserimento dell'intero Blocco 6, tabelle di sconto LaTeX ed analisi di sensitività/struttura finanziaria).
  - `index.md` (Aggiornato il catalogo per indicizzare la nuova risorsa sotto la sezione wiki/Esercitazioni/).
  - `log.md` (Questo file).

---

## [2026-05-24] INGEST & STUDY | Systematic Trading & Prop Firm Automation Skill

- **Operazione:** Ingestione del manuale "Leveraged Trading" di Robert Carver (`raw/input.md`) e sintesi delle sezioni chiave di "Quantitative Trading" di Ernest Chan. Creazione della Skill completa per Obsidian per guidare la selezione di Prop Firm vantaggiose, l'impostazione di strategie sistematiche di lungo termine (Starter System, Volatility Target, drawdown management) e la stesura dell'architettura per l'esecuzione automatizzata (MT5 Python API e NinjaTrader 8 C# file bridge). Sviluppo del simulatore prop firm e del bot reale per MT5 in demo.
- **File creati/modificati:**
  - `wiki/Concetti/Guida_Selezione_Prop_Firm.md` [NEW] — Checklist quantitativa e formule per drawdown e coerenza nelle Prop Firm.
  - `wiki/Concetti/Strategia_Lungo_Termine_Systematic.md` [NEW] — Blueprint strategico basato su Carver (Starter System, risk target) e Chan (look-ahead bias, data-snooping, survivorship bias).
  - `wiki/Concetti/Bridge_Esecuzione_Automatica.md` [NEW] — Blueprint di esecuzione con codici pronti per MT5 (Python) e NinjaTrader 8 (C#) con kill-switch di emergenza.
  - `wiki/Script/run_gold_paper_trading.py` [NEW] — Bot autonomo in tempo reale per conti demo MetaTrader 5 (MT5) con calcolo Z-score robusto, sentiment e drawdown kill-switch. Modificato successivamente per forzare la codifica UTF-8 su Windows ed implementare l'Auto-Avvio automatico del terminale da percorso standard.
  - `scratch/simulate_prop_challenge.py` [NEW] — Simulatore storico ed in tempo reale per challenge prop da $50k su oro futures.
  - `index.md` (aggiornato l'indice centrale includendo le nuove risorse quantitative e script).
  - `log.md` (questo file).
- **Risoluzione Problemi ed Ottimizzazioni (Bug Fix & Auto-Launch):**
  - Risolto errore di codifica `UnicodeEncodeError` in Windows console forzando la codifica `utf-8` all'avvio dello script `run_gold_paper_trading.py` per garantire stabilità su caratteri speciali ed emoji.
  - Integrata funzionalità di Auto-Avvio automatica in `run_gold_paper_trading.py` per scansionare il sistema del cliente, localizzare `terminal64.exe` in `C:\Program Files\MetaTrader 5\terminal64.exe` e lanciarlo automaticamente all'occorrenza.
  - Riavviato con successo il bot in background con l'ambiente Anaconda Python corretto, ora stabile e operativo.
  - Aggiornate le credenziali del conto demo MT5 su richiesta dell'utente (nuovo Login: `10011042813`, Password: `_6XmOxUc`), strutturando lo script in modo pulito con costanti globali all'inizio per facilitare future modifiche.
  - Esteso lo script `run_gold_paper_trading.py` per renderlo **completamente multi-asset ed agnostico**: ora rileva dinamicamente le specifiche di contratto MT5 (tramite `trade_contract_size` per ricalcolare i lotti al volo su BTCUSD, XAUUSD o indici), rileva automaticamente la keyword corretta per raschiare il sentiment delle news (es. "bitcoin" o "gold") e adatta tutte le stringhe di log. Impostato l'asset attivo su `BTCUSD` su richiesta dell'utente per testare il bot nel weekend.
  - Risolto errore `❌ Errore nel recupero delle candele storiche da MT5` implementando l'auto-selezione ed attivazione automatica del simbolo attivo (es. `BTCUSD`) in Market Watch all'avvio dello script, affiancata da un loop di riprova (retry loop) con delay per tollerare la latenza di sincronizzazione dei dati storici del terminale MT5.
  - Ripristinato il simbolo attivo su `XAUUSD` (Oro) mantenendo l'infrastruttura dinamica pronta per la riapertura dei mercati di domani mattina.
- **Sviluppo Moduli Quant Analyst (Fase 1: Stato Persistente):**
  - Progettato ed implementato il sistema di **Stato Persistente di Produzione (`state.json`)** in `run_gold_paper_trading.py` per garantire la massima resilienza contro crash e riavvii improvvisi del PC.
  - Sviluppata logica di auto-sincronizzazione all'avvio che rileva automaticamente eventuali trade aperti su MT5 riconciliandoli con lo stato locale.
  - Integrato modulo di riconciliazione automatica delle posizioni chiuse (SL/TP) tramite interrogazione dello storico dei deal di MT5 (`history_deals_get`), con calcolo automatico in tempo reale del PnL giornaliero e del conteggio trade per rispettare le regole di coerenza.
- **Sviluppo Moduli Quant Analyst (Fase 2: Notifiche Telegram):**
  - Progettato e implementato il modulo nativo di **Notifiche Telegram** in `run_gold_paper_trading.py` utilizzando esclusivamente le librerie standard di Python (`urllib.request` e `json`) per evitare dipendenze esterne.
  - Creati template di messaggi in formato HTML premium per notificare in tempo reale sul cellulare: Avvio del Bot (Heartbeat), Segnali d'ingresso LONG (BUY) con prezzi precisi di SL/TP e rischio, Segnali d'ingresso SHORT (SELL), Chiusura posizioni con PnL del trade e profitto giornaliero accumulato, e l'attivazione del Kill-Switch di emergenza per drawdown.
  - Aggiunti parametri di configurazione facoltativi `TELEGRAM_TOKEN` e `TELEGRAM_CHAT_ID` all'inizio del file per una configurazione immediata da parte dell'utente.
  - Inserito con successo il **Token Bot Telegram** fornito dall'utente (`8215784991:AAE-780dQk3pZZVSY22Cfq_nXBlyZjT-q1dA`), correggendo automaticamente lo spazio di copia-incolla con un trattino basso (`_`) conforme agli standard API di Telegram.
- **Sviluppo Moduli Quant Analyst (Fase 3: Trailing Stop Volatilità):**
  - Progettato e implementato il modulo di **Trailing Stop Loss Dinamico basato su Volatilità (MAD)** in `run_gold_paper_trading.py`.
  - Configurato l'aggiornamento automatico dello SL a una distanza di sicurezza rigida di `2.0 * std_mad` dal prezzo corrente, muovendo il livello solo a favore del trade (in alto per BUY, in basso per SELL) per bloccare i profitti.
  - Implementata una soglia minima di scostamento pari a `0.5 * std_mad` per evitare micro-modifiche eccessive ed evitare il rate-limiting del broker.
  - Collegato l'aggiornamento dello SL alle notifiche Telegram per ricevere messaggi istantanei sul cellulare ad ogni modifica significativa.

---

## [2026-05-29] INGEST | Python for Data Analysis (Wes McKinney)

- **Operazione:** Ingestione ed elaborazione del libro "Python for Data Analysis" di Wes McKinney per la creazione della sezione dedicata all'analisi dei dati in Python nel Second Brain.
- **File creati:**
  - `wiki/Fonti/Fonte_McKinney_Python_Data_Analysis.md` [NEW] — Scheda fonte completa con capitoli, temi e strutture dati trattate.
  - `wiki/Concetti/Python_Data_Analysis.md` [NEW] — Guida di riferimento concettuale e tecnica a NumPy (vettorizzazione, ndarray), Pandas (Series, DataFrame, data cleaning, wrangling, GroupBy) e calcoli temporali quantitativi (rolling MAD, Z-score).
- **File modificati:**
  - `index.md` (registrate e indicizzate le nuove risorse scientifiche nell'indice centrale).
  - `log.md` (questo file).

---

## [2026-05-29] DEV | Creazione Telegram Remote Bridge per Studio e Controllo Remoto

- **Operazione:** Sviluppo del modulo bridge di controllo bidirezionale Telegram per permettere all'utente di studiare, lanciare ed esplorare script sul PC fisso direttamente dal proprio smartphone.
- **File creati:**
  - `wiki/Script/telegram_bridge.py` [NEW] — Script per l'ingestione ed elaborazione dei messaggi inviati dall'utente al Bot Telegram.
  - `wiki/Script/send_telegram.py` [NEW] — Utility per inviare messaggi di risposta formattati in HTML al canale dell'utente.
  - `wiki/Script/telegram_listener.py` [NEW] — Listener real-time ad alta reattività (5s) basato su loop e terminazione per scatenare il Reactive Wakeup.
- **File modificati:**
  - `index.md` (registrati i nuovi script nella sezione wiki/Script/).
  - `log.md` (questo file).

---

## [2026-05-29] STUDY | Lezione 1 — NumPy e Vettorializzazione

- **Operazione:** Avviata la prima lezione dell'insegnamento di Analisi Dati Quantitativi.
- **File creati:**
  - `wiki/Concetti/Lezione_1_NumPy_Vettorializzazione.md` [NEW] — Lezione teorica e pratica approfondita su dynamic boxing, arrays contigui in memoria, ottimizzazione cache L1/L2, SIMD, regole di Broadcasting ed un'applicazione finanziaria vettorializzata per il calcolo del Max Drawdown.
- **File modificati:**
  - `index.md` (registrato il nuovo concetto nel catalogo sotto la sezione Python & Data Analysis)
  - `log.md` (questo file)

---

## [2026-05-29] STUDY | Strategie Oro r/algotrading

- **Operazione:** Scansione e sintesi delle migliori strategie quantitative per il trading dell'Oro (XAUUSD / GC) discusse sulla community r/algotrading.
- **File creati:**
  - `wiki/Concetti/Strategie_Reddit_Algotrading_Oro.md` [NEW] — Studio approfondito su Intraday Mean Reversion (Robust Z-Score e MAD), lead-lag macro-correlato (TIPS real yields e DXY Index), e stop-hunting tramite l'automazione di Liquidity Sweeps / Smart Money Concepts (SMC) con relativi requisiti di latenza (LD4/NY4 VPS) e slippage.
- **File modificati:**
  - `index.md` (registrato il concetto nel catalogo)
  - `log.md` (questo file)



---

## [2026-06-03] INGEST | Slide Corso Sales Competences (Thomas Berger)

- **Operazione:** Ingestione ed elaborazione dei materiali del corso "Sales Competences" inviati dall'utente tramite Telegram.
- **File creati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` [NEW] — Scheda fonte completa con contenuti estratti dalle slide 12, 13, 15 e 16.
  - `wiki/Concetti/Technical_Sales_vs_Traditional_Sales.md` [NEW] — Scheda di confronto concettuale tra vendita tecnica complessa e vendita tradizionale B2C/B2B.
  - `wiki/Concetti/Technical_Expert_Sales_Process.md` [NEW] — Scheda sul processo di vendita tecnica e le sue 8 fasi secondo Holopainen et al. (2020), con diagramma Mermaid.
  - `wiki/Concetti/Current_Challenges_in_Sales.md` [NEW] — Scheda sulle sfide contemporanee nelle vendite basata sullo studio multinazionale di Berger et al., con mappa concettuale Mermaid.
  - `wiki/Concetti/Gartner_Hype_Cycle_Sales_2024.md` [NEW] — Scheda sul ciclo di maturità delle tecnologie di vendita con focus su AR/VR, Generative AI per le vendite, Sales AI Assistants e Revenue Intelligence.
  - `wiki/Progetti/Master_Page_Sales_Competences.md` [NEW] — Master Page e cruscotto di studio per la materia Sales Competences.
- **File modificati:**
  - `wiki/Home.md` (collegata la nuova Master Page nella tabella delle materie universitarie).
  - `index.md` (registrate e indicizzate tutte le nuove risorse e concetti nel catalogo generale).
  - `log.md` (questo file).

---

## [2026-06-03] INGEST | Slide 23 Sales Competences (Different Kinds of Utility)

- **Operazione:** Ingestione ed elaborazione della Slide 23 inviata dall'utente tramite Telegram, raffigurante il modello delle utilità e del valore del cliente (Vogel, 2006).
- **File creati:**
  - `wiki/Concetti/Different_Kinds_of_Utility.md` [NEW] — Scheda concettuale sul modello delle utilità basato sui benefici totali (prodotto, servizio, brand, relazione) e costi totali (monetari e non-monetari) con diagramma Mermaid.
- **File modificati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` (aggiunto il riassunto della Slide 23 e linkata la nuova scheda).
  - `wiki/Progetti/Master_Page_Sales_Competences.md` (aggiunta la risorsa all'indice delle lezioni e inseriti i punti di controllo nel cruscotto di studio).
  - `index.md` (indicizzato il nuovo concetto nella sezione Sales Competences).
  - `log.md` (questo file).

---

## [2026-06-03] INGEST | Slide 24-25 Sales Competences (Value Conversion & Financial Benefits)

- **Operazione:** Ingestione ed elaborazione delle Slide 24 e 25 inviate dall'utente tramite Telegram, riguardanti la quantificazione e conversione del valore nei processi di vendita complessi (Jensen, 2013).
- **File creati:**
  - `wiki/Concetti/Classification_of_Financial_Benefits.md` [NEW] — Scheda concettuale sulla categorizzazione dei benefici finanziari in 7 classi di risparmio ed incremento fatturato secondo Jensen (2013).
  - `wiki/Concetti/Technical_to_Financial_Value_Conversion.md` [NEW] — Scheda sul framework a tre stadi (Caratteristica Tecnica $\rightarrow$ Beneficio Operativo $\rightarrow$ Argomento Finanziario) con matrice di esempi industriali.
- **File modificati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` (aggiunti i riassunti delle Slide 24 e 25 e linkate le nuove schede).
  - `wiki/Progetti/Master_Page_Sales_Competences.md` (aggiunte le risorse all'indice delle lezioni e inseriti gli obiettivi nel cruscotto di studio dell'esame).
  - `index.md` (indicizzati i nuovi concetti nella sezione Sales Competences del catalogo).
  - `log.md` (questo file).

---

## [2026-06-03] INGEST | Slide 30 Sales Competences (Total Cost of Ownership)

- **Operazione:** Ingestione ed elaborazione della Slide 30 inviata dall'utente tramite Telegram, riguardante il calcolo del costo totale sul ciclo di vita dell'asset (TCO).
- **File creati:**
  - `wiki/Concetti/Total_Cost_of_Ownership.md` [NEW] — Scheda concettuale sulla formula e l'applicazione pratica del TCO (confronto Competitore vs CLX 350 su orizzonte di 3 anni).
- **File modificati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` (aggiunto il riassunto della Slide 30 e linkata la nuova scheda).
  - `wiki/Progetti/Master_Page_Sales_Competences.md` (aggiunta la risorsa all'indice delle lezioni e inserito il relativo obiettivo di studio nel cruscotto).
  - `index.md` (indicizzato il nuovo concetto nella sezione Sales Competences del catalogo).
  - `log.md` (questo file).

---

## [2026-06-03] INGEST | Slide 32 Sales Competences (Seven Sales Virtues)

- **Operazione:** Ingestione ed elaborazione della Slide 32 inviata dall'utente tramite Telegram, riguardante il framework delle sette virtù delle vendite (Diephuis & Skiver / FOSTER).
- **File creati:**
  - `wiki/Concetti/Seven_Sales_Virtues.md` [NEW] — Scheda concettuale sulle 7 virtù commerciali e i corrispondenti costrutti organizzativi (market orientation, cross-functional integration, ecc.), corredata da mappa concettuale Mermaid.
- **File modificati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` (aggiunto il riassunto della Slide 32 e linkata la nuova scheda).
  - `wiki/Progetti/Master_Page_Sales_Competences.md` (aggiunta la risorsa all'indice delle lezioni e inserito il relativo obiettivo di studio nel cruscotto).
  - `index.md` (indicizzato il nuovo concetto nella sezione Sales Competences del catalogo).
  - `log.md` (questo file).

---

## [2026-06-03] INGEST | Slide 40 Sales Competences (Ambivert Advantage)

- **Operazione:** Ingestione ed elaborazione della Slide 40 inviata dall'utente tramite Telegram, riguardante lo studio empirico sulla personalità del venditore (Adam Grant, 2013).
- **File creati:**
  - `wiki/Concetti/Ambivert_Advantage_in_Sales.md` [NEW] — Scheda concettuale sull'effetto curvilineo (forma a U rovesciata) dell'estroversione sulle performance di vendita, con i risultati statistici della regressione gerarchica.
- **File modificati:**
  - `wiki/Fonti/Slide_Sales_Competences_Thomas_Berger.md` (aggiunto il riassunto della Slide 40 e linkata la nuova scheda).
  - `wiki/Progetti/Master_Page_Sales_Competences.md` (aggiunta la risorsa all'indice delle lezioni e inserito il relativo obiettivo di studio nel cruscotto).
  - `index.md` (indicizzato il nuovo concetto nella sezione Sales Competences del catalogo).
  - `log.md` (questo file).

## [2026-06-04] UPDATE | Upgrade Bot di Trading (Forex Scalping)

- **Operazione:** Transizione del bot quantistico `amsr_quantum_portfolio_bot.py` a una configurazione di scalping a breve termine (timeframe H1 / M15 / M5) ed espansione da 5 a 12 asset totali (aggiunta di GBPUSD, USDJPY, AUDUSD, USDCAD, USDCHF, GBPJPY, EURJPY).
- **File modificati:**
  - `wiki/Script/amsr_quantum_portfolio_bot.py` (modificati parametri timeframe, pesi dinamici e risk target a $40).
  - `log.md` (questo file).





