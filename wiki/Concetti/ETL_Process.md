---
tags: [database, data-warehouse, ETL, data-integration]
aliases: [Extract Transform Load, Processo ETL]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 2
---

# ⚙️ Processo ETL (Extract, Transform, Load)

Il processo **ETL (Extract, Transform, Load)** è una pipeline fondamentale per l'integrazione dei dati in sistemi di business intelligence e, in particolare, per il popolamento di un **[[Data_Warehouse]]**. Essa sposta fisicamente i dati dai sistemi operazionali (sorgenti) verso il sistema analitico finale.

---

## 1. Le Tre Fasi del Processo

### 📥 1. Extraction (Estrazione)
I dati grezzi vengono estratti da fonti eterogenee (es. database relazionali OLTP, file JSON/XML, log di server, API esterne). 
*   **Staging Area:** I dati estratti non vengono caricati direttamente nel Data Warehouse, ma vengono copiati in un'area di transito temporanea chiamata *Staging Area*. Questo evita di sovraccaricare i sistemi di produzione con calcoli complessi.

### 🔄 2. Transformation (Trasformazione)
Questa è la fase più critica e complessa. I dati grezzi vengono ripuliti, standardizzati e convertiti in un formato coerente. Le attività includono:
*   **Filtering & Cleansing:** Rimozione di record duplicati, gestione dei valori nulli o mancanti e correzione di errori di battitura.
*   **Standardizzazione:** Conversione delle date in un unico formato (es. YYYY-MM-DD), allineamento delle valute e standardizzazione dei codici (es. formati telefonici o indirizzi).
*   **Deduplica e Consolidamento:** Identificazione di entità identiche provenienti da sistemi diversi.

### 📤 3. Loading (Caricamento)
I dati trasformati e puliti vengono importati nel Data Warehouse.
*   **Ordine di Caricamento:** Per non violare i vincoli di integrità referenziale, è essenziale caricare prima le tabelle dei dati anagrafici (Master Data) e successivamente le tabelle dei fatti (Transazioni).
*   **Caricamento Incrementale:** Tipicamente, dopo il primo caricamento massivo (Initial Load), si effettuano caricamenti periodici (es. notturni) dei soli record modificati o aggiunti (Delta Load).

---

## 2. ETL e Master Data Management (MDM)

Durante la fase di **Transform**, viene spesso applicato il **Master Data Management (MDM)**, definito come "The Truth Machine" (la macchina della verità). Il suo scopo è risolvere le incongruenze tra fonti diverse per lo stesso soggetto (es. un cliente registrato in due modi diversi nel CRM e nell'ERP).

### Le Tre Fasi dell'MDM:
1.  **Cleansing:** Standardizzazione dei formati di input.
2.  **Matching:** Uso di algoritmi deterministici o probabilistici per capire se due record rappresentano la stessa entità fisica.
3.  **Merging:** Fusione delle informazioni per creare il profilo perfetto, chiamato **Golden Record**.

> [!TIP]
> **Backflushing:** È la pratica di rimandare il *Golden Record* pulito direttamente ai sistemi sorgente operazionali per "curare" i dati originari sporchi alla fonte.

---

## Fonti
* [[wiki/Fonti/Fonte_Elmasri_Cap25_Data_Warehouse.md]]
* [[wiki/Concetti/Data_Warehouse.md]]
