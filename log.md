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

## [2026-05-18] INGEST | Data Warehouse � Teoria Tecnica e Modelli

**Operazione:** Creazione e sintesi degli appunti di Data Warehouse a seguito della simulazione d'esame.
**Fonte:** Sessione di studio interattiva + Appunti raw in DATA Warehouse.md

**File creati � wiki/Concetti/:**
- `Data_Warehouse.md` � Super Technical Theory (OLTP vs OLAP, Inmon, ETL, MDM, MOLAP/ROLAP/HOLAP, Star vs Snowflake Schema)

**Wikilinks creati:** [[OLTP]], [[OLAP]], [[ETL]], [[Master Data Management]], [[MOLAP]], [[ROLAP]], [[HOLAP]], [[Star Schema]], [[Snowflake Schema]], [[Fact Constellation]]
