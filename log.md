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

