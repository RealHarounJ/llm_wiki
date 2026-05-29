---
tags: [python, data-science, data-analysis, pandas, numpy, IPython]
aliases: [Fonte McKinney, Python for Data Analysis]
date_created: 2026-05-29
last_modified: 2026-05-29
source_count: 1
---

# Fonte | Python for Data Analysis (Wes McKinney)

*   **Titolo Completo:** *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*
*   **Autore:** Wes McKinney (Creatore originario della libreria [[Pandas]])
*   **Editore:** O'Reilly Media
*   **File di Riferimento:** [Python for Data Analysis (Wes McKinney).pdf](file:///c:/Users/jaafa/Downloads/llm_wiki-main/raw/Python%20for%20Data%20Analysis%20Data%20Wrangling%20with%20Pandas,%20NumPy,%20and%20IPython%20(Wes%20McKinney)%20(z-library.sk,%201lib.sk,%20z-lib.sk).pdf)

---

## 📖 Panoramica dell'Opera

Questo testo rappresenta il pilastro fondamentale e lo standard industriale indiscusso per la manipolazione, la pulizia, l'elaborazione e la modellizzazione dei dati in Python. Wes McKinney guida il lettore attraverso l'ecosistema scientifico di Python, focalizzandosi sugli strumenti per effettuare operazioni di **Data Wrangling** (il processo di trasformazione dei dati "grezzi" in un formato adatto all'analisi).

Il libro si concentra su tre librerie cardine:
1.  **IPython e Jupyter:** Ambienti interattivi ad alte prestazioni per lo sviluppo rapido ed esplorativo di codice.
2.  **NumPy (Numerical Python):** L'infrastruttura sottostante basata su array multidimensionali ad alte prestazioni ([[ndarray]]) per il calcolo scientifico e vettorizzato.
3.  **Pandas:** Strutture dati di alto livello (Series e DataFrame) progettate per manipolare dati tabulari e serie storiche in modo intuitivo e veloce.

---

## 🛠️ Capitoli e Contenuti Chiave

### 1. IPython e Jupyter Notebooks
*   **L'approccio interattivo:** Utilizzo della shell interattiva per l'esplorazione rapida del codice, introspezione dei dati, e cronologia dei comandi.
*   **Comandi Magici (%):** Scorciatoie integrate (es. `%timeit` per profilare i tempi, `%run` per eseguire script esterni, `%matplotlib inline` per l'embedding dei grafici).

### 2. NumPy Basics: Vettorizzazione ed Array Multidimensionali
*   **L'oggetto [[ndarray]]:** Struttura dati omogenea in memoria contigua per ottimizzare i calcoli numerici ad alte prestazioni, superando le lentezze dei cicli `for` in Python standard.
*   **Vectorization (Vettorizzazione):** Esecuzione di operazioni matematiche in blocco su interi array senza loop, sfruttando l'architettura SIMD e implementazioni ottimizzate in C.
*   **Broadcasting:** Meccanismo matematico che permette di applicare operazioni tra array di forme differenti ma compatibili (es. aggiungere uno scalare a una matrice).

### 3. Introduzione a Pandas: Series e DataFrame
*   **Series:** Array monodimensionale etichettato dotato di un indice associato che ne mappa i dati.
*   **DataFrame:** Struttura tabulare bidimensionale, simile a un foglio di calcolo o a una tabella SQL, in cui ogni colonna rappresenta una Series etichettata e le righe condividono lo stesso indice.
*   **Indicizzazione e Selezione:** Utilizzo di `.loc` (selezione basata su etichette) e `.iloc` (selezione basata su posizioni intere).

### 4. Data Loading, Storage e Formati File
*   **Parsing dei File di Testo:** Lettura di file CSV, TSV e fixed-width tramite `pd.read_csv()` e `pd.read_table()`, con gestione di delimitatori, intestazioni mancanti e commenti.
*   **Integrazione ed Export:** Interazione con formati efficienti come JSON, database SQL, file Excel ed HDF5.

### 5. Data Cleaning e Preparation (Pulizia dei Dati)
*   **Missing Data (Dati Mancanti):** Trattamento dei valori `NaN` (Not a Number) tramite funzioni dedicate come `.dropna()` per filtrare, `.fillna()` per imputare valori sostitutivi o `.isna()` per il rilevamento.
*   **Rimozione Duplicati e Trasformazioni:** Utilizzo di `.drop_duplicates()` e del metodo `.map()` per trasformare o mappare etichette basandosi su dizionari di corrispondenza.
*   **String Manipulation:** Manipolazione efficiente di testo vettorizzato tramite l'attributo `.str`.

### 6. Data Wrangling: Join, Combine e Reshape
*   **Merging & Joining (Fusing):** Fusione di DataFrame tramite logica relazionale SQL-like (Inner, Left, Right, Outer Join) utilizzando `pd.merge()`.
*   **Concatenazione:** Allineamento e unione fisica di oggetti lungo un asse verticale o orizzontale mediante `pd.concat()`.
*   **Reshaping (Rimodellamento):** Trasformazione dei dati da formato largo a lungo (e viceversa) usando `.stack()`, `.unstack()`, `.pivot()` e `pd.melt()`.

### 7. Data Aggregation e GroupBy (Split-Apply-Combine)
*   **Il paradigma Split-Apply-Combine:**
    1.  **Split:** Suddivisione dei dati in gruppi basandosi su una o più chiavi.
    2.  **Apply:** Applicazione di funzioni di aggregazione (es. media, somma, funzioni custom) a ciascun gruppo in modo indipendente.
    3.  **Combine:** Unione dei risultati intermedi in una nuova struttura dati consolidata.
*   **Pivot Table e Cross-Tabulation:** Generazione di tabelle pivot dinamiche tramite `.pivot_table()`.

### 8. Time Series Analysis (Serie Storiche)
*   **Elementi Temporali:** Gestione di date, periodi e timestamp utilizzando tipi nativi Pandas (`Timestamp`, `DatetimeIndex`).
*   **Resampling (Ricampionamento):** Conversione di frequenza temporale da alta a bassa (Downsampling, es. da giornaliero a mensile aggregando con la media) o da bassa ad alta (Upsampling, inserendo interpolazioni) tramite `.resample()`.
*   **Shifting (Spostamento):** Spostamento dei dati in avanti o all'indietro lungo l'asse temporale (`.shift()`) per calcolare variazioni percentuali o rendimenti storici.
*   **Finestre Mobili (Rolling Windows):** Calcolo di statistiche cumulate su intervalli temporali scorrevoli tramite `.rolling()` (es. medie mobili a 20 o 50 giorni per l'analisi tecnica finanziaria).

---

## 🧠 Concetti Chiave Estratti ed Interconnessi

*   [[ndarray]] — L'array multidimensionale alla base di NumPy.
*   [[Vectorization]] — Elaborazione massiva ed efficiente senza cicli Python espliciti.
*   [[Pandas_DataFrame]] — La struttura dati centrale a tabelle etichettate.
*   [[Split_Apply_Combine]] — La metodologia computazionale per raggruppare ed aggregare.
*   [[Time_Series_Analysis]] — Modelli di indicizzazione e calcolo temporale.

---

## Fonti
* [Python for Data Analysis (Wes McKinney).pdf](file:///c:/Users/jaafa/Downloads/llm_wiki-main/raw/Python%20for%20Data%20Analysis%20Data%20Wrangling%20with%20Pandas,%20NumPy,%20and%20IPython%20(Wes%20McKinney)%20(z-library.sk,%201lib.sk,%20z-lib.sk).pdf)
