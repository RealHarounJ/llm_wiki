---
tags: [database, data-warehouse, exam-prep, OLAP, ETL, MDM]
aliases: [DW, Data Warehousing]
date_created: 2026-05-18
last_modified: 2026-05-18
source_count: 1
---

# Data Warehouse (DW) — Super Technical Theory

Un Data Warehouse è un sistema progettato per supportare le decisioni aziendali strategiche attraverso l'analisi di dati storici.

## 1. OLTP vs OLAP — La Distinzione Fondamentale

| Proprietà | [[OLTP]] (Operational DB) | [[OLAP]] (Data Warehouse) |
| :--- | :--- | :--- |
| **Scopo** | Registrare transazioni (INSERT/UPDATE/DELETE) | Analisi storica (Solo SELECT) |
| **Dati** | Attuali, volatili, dettagliati | Storici, **non volatili**, aggregati |
| **Schema** | Normalizzato (3NF) per evitare ridondanze | Denormalizzato (Star/Snowflake) per velocità |
| **Query** | Brevi, veloci, prevedibili | Complesse, ad-hoc, su moli di dati enormi |

---

## 2. Definizione di Inmon (Le 4 Proprietà)
Secondo William Inmon, un DW è:
1. **Subject-Oriented:** Organizzato intorno a temi aziendali (Vendite, Finanza), NON per singole applicazioni.
2. **Integrated:** I dati da fonti eterogenee (es. CRM, ERP) sono unificati in un formato coerente.
3. **Time-Variant:** Ogni record ha una chiave temporale. La storia viene preservata.
4. **Non-Volatile:** I dati vengono caricati e poi sono in sola lettura. Non ci sono UPDATE o DELETE.

---

## 3. L'Architettura ETL e MDM

### [[ETL]] (Extract, Transform, Load)
È la "pipeline" che sposta fisicamente i dati dai sistemi sorgente al DW.
1. **Extract:** Estrazione dei dati grezzi da fonti eterogenee verso una *Staging Area* temporanea.
2. **Transform:** La fase più complessa (standardizzazione, conversione, calcoli).
3. **Load:** Caricamento nel DW (solitamente incrementale). L'ordine è vitale: *Master Data* prima delle *Transazioni* per non violare l'integrità referenziale.

### [[Master Data Management]] (MDM) — "The Truth Machine"
È l'insieme di regole e algoritmi eseguiti durante la fase **Transform** (nella Staging Area) per creare un'unica versione della verità.
- **Problema:** John Smith nel CRM e J. Smith nell'ERP sono la stessa persona?
- **Le 3 Fasi MDM:**
  1. **Cleansing:** Correzione errori tipografici e standardizzazione formati.
  2. **Matching:** Uso di algoritmi per capire se i record rappresentano la stessa entità.
  3. **Merging:** Fusione delle informazioni migliori.
- **Risultato:** Il **Golden Record**, il profilo perfetto e inconfutabile che verrà caricato nel DW.

> **Backflushing:** Pratica in cui il Golden Record pulito viene rimandato ai sistemi sorgente per "aggiustare" i loro dati sporchi.

---

## 4. I Tre Motori OLAP

Come interroghiamo i dati nel DW? Tramite tre architetture principali che bilanciano velocità di query e scalabilità.

| Motore | Funzionamento | Pro & Contro |
| :--- | :--- | :--- |
| **[[MOLAP]] (Multidimensional)** | I dati sono pre-calcolati e salvati in array multidimensionali (Cubi fisici). | ⚡ **Pro:** Velocità estrema.<br>❌ **Contro:** "Data Explosion" (non scala per Petabytes di dati). |
| **[[ROLAP]] (Relational)** | I dati restano in tabelle relazionali. Il motore traduce le query in complessi JOIN SQL on-the-fly. | ✅ **Pro:** Altamente scalabile (es. Amazon).<br>🐢 **Contro:** Più lento per query complesse. |
| **[[HOLAP]] (Hybrid)** | Dati di dettaglio in ROLAP, dati aggregati in MOLAP. | ⚖️ **Pro/Contro:** Bilanciato, ma architettura molto complessa da mantenere. |

---

## 5. Data Modeling: Star vs Snowflake Schema

Nei sistemi ROLAP, i dati sono organizzati tramite il Modello Multidimensionale, basato su:
- **Fact Table:** Contiene le variabili quantitative misurabili (es. Revenue, Quantity).
- **Dimension Tables:** Contengono gli attributi descrittivi (es. Regione, Prodotto, Data).

Come strutturiamo queste tabelle per massimizzare le performance o lo spazio?

### [[Star Schema]]
La Fact Table centrale è circondata da Dimension Tables piatte.
- **Vantaggio:** ⚡ Velocità di query massima (pochissimi JOIN richiesti).
- **Svantaggio:** 💾 Altissima **ridondanza** di dati (spreco di spazio).

### [[Snowflake Schema]]
Le Dimension Tables dello Star Schema vengono **normalizzate** (spezzate in sotto-tabelle, es. Store → City → State).
- **Vantaggio:** 💾 Elimina completamente la ridondanza (risparmia tantissimo spazio).
- **Svantaggio:** 🐢 Query lentissime a causa dei continui `JOIN` tra le sotto-tabelle.

### [[Fact Constellation]] (Galaxy Schema)
Due o più Fact Tables (es. Vendite e Spedizioni) che condividono le stesse Dimension Tables in mezzo.

---

## Fonti
- [[Fonte_Data_Warehouse_Mining_Notes]] -> Note estratte dal file raw "DATA Warehouse.md"
- Discussioni pratiche su casi aziendali (es. Amazon ROLAP scalability, University MDM matching).
