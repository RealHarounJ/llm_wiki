---
tags: [python, data-science, data-analysis, pandas, numpy, programming]
aliases: [Python per Analisi Dati, Data Wrangling con Pandas]
date_created: 2026-05-29
last_modified: 2026-05-29
source_count: 1
---

# Analisi dei Dati in Python: Guida Concettuale e Pratica

L'ecosistema Python per l'analisi dei dati rappresenta uno standard per lo sviluppo quantitativo, l'apprendimento automatico e la manipolazione di dataset complessi. A differenza dello sviluppo software generico, l'analisi dei dati richiede prestazioni computazionali di livello scientifico unite a una flessibilità espressiva che consenta cicli rapidi di prototipazione interattiva.

Questa guida concettuale, basata sulle metodologie formalizzate da Wes McKinney in [[Fonte_McKinney_Python_Data_Analysis]], illustra i principi matematici, le strutture dati e le operazioni essenziali dello stack scientifico di Python: **NumPy**, **Pandas** e **IPython/Jupyter**.

---

## 🚀 1. L'Infrastruttura di Calcolo: NumPy e la Vettorizzazione

Alla base del calcolo scientifico in Python vi è **NumPy** (Numerical Python). Python nativo è un linguaggio interpretato e dinamicamente tipizzato; questo introduce un overhead significativo quando si manipolano grandi sequenze di dati (ogni elemento in una lista Python standard è un oggetto completo con metadati, allocato in posizioni sparse di memoria).

NumPy risolve questo problema strutturale introducendo l'oggetto **[[ndarray]]** (N-dimensional array).

### ndarray vs Liste Python
1.  **Omogeneità dei dati:** Tutti gli elementi dell'array devono condividere lo stesso tipo di dato primitivo (`dtype`), consentendo un'allocazione di memoria fissa e prevedibile per elemento.
2.  **Contiguità fisica in memoria:** Gli elementi sono memorizzati in un blocco contiguo di byte in memoria RAM. Questo permette di sfruttare la cache della CPU e di implementare algoritmi scritti in C/Fortran a bassissimo livello.
3.  **Vectorization (Vettorizzazione):** L'esecuzione di operazioni matematiche avviene su interi blocchi di dati simultaneamente senza ricorrere a cicli `for` espliciti, sfruttando le istruzioni hardware SIMD (Single Instruction, Multiple Data) della CPU.

```python
import numpy as np

# Creazione di un array NumPy bidimensionale (3 righe, 4 colonne)
data = np.array([[1.5, 2.3, 0.9, 4.2],
                 [3.0, 1.2, 5.5, 2.1],
                 [0.8, 4.4, 1.7, 3.3]])

# Calcolo vettorializzato: moltiplicazione di ogni elemento per 10 (senza loop)
data_scaled = data * 10
# Risultato: tutti gli elementi sono moltiplicati all'istante a basso livello C

# Slicing multidimensionale (selezioniamo le prime due righe e le colonne centrali)
subset = data[:2, 1:3]
```

---

## 📊 2. Strutture Dati ad Alto Livello: Pandas

Sebbene NumPy offra prestazioni numeriche impareggiabili, manca di funzionalità necessarie per la manipolazione quotidiana dei dati del mondo reale, come la gestione delle etichette (metadata) e il trattamento dei dati mancanti. **Pandas** colma questo divario fornendo due strutture dati fondamentali: la **Series** e il **DataFrame**.

### 1. La Series
Una Series è un array monodimensionale etichettato in grado di contenere qualsiasi tipo di dato. Condivide la velocità di calcolo di NumPy, ma associa a ogni valore un'etichetta denominata **Index** (Indice).

```python
import pandas as pd

# Creazione di una Series con indice personalizzato
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])

# Accesso immediato tramite etichetta
val = obj['b'] # Restituisce 7.2
```

### 2. Il DataFrame
Il DataFrame è la struttura dati regina di Pandas. Rappresenta una tabella bidimensionale, analoga a una tabella di un database relazionale o a un foglio di calcolo. Può essere pensato come un dizionario di Series che condividono lo stesso indice di riga.

```python
# Creazione di un DataFrame da un dizionario
data_dict = {
    'Stato': ['Corea', 'Arabia', 'Corea', 'Arabia'],
    'Anno': [2026, 2026, 2027, 2027],
    'Valore': [100.5, 85.2, 110.1, 90.4]
}
df = pd.DataFrame(data_dict)

# Selezione di una colonna (restituisce una Series)
stato_col = df['Stato']

# Selezione basata su etichetta (.loc) o posizione (.iloc)
row_2026 = df.loc[1]     # Riga in indice 1 (Arabia, 2026, 85.2)
cell_val = df.iloc[2, 2] # Valore in riga 2, colonna 2 (110.1)
```

---

## 🧹 3. Data Cleaning e Preparation (Pulizia dei Dati)

I dati del mondo reale sono intrinsecamente "sporchi" o incompleti. Pandas fornisce un arsenale di strumenti ottimizzati per ripulire i dataset prima dell'analisi o dell'elaborazione algoritmica.

### Gestione dei Valori Mancanti (Missing Data)
In Pandas, i dati mancanti vengono rappresentati dal valore a virgola mobile `NaN` (Not a Number) o dall'oggetto `None`.

*   **Rilevamento:** `.isna()` restituisce una maschera booleana che identifica i valori nulli.
*   **Filtro:** `.dropna()` elimina le righe o le colonne che contengono valori nulli.
*   **Imputazione:** `.fillna()` sostituisce i valori nulli con un valore specifico o calcolato (es. la media o la mediana).

```python
# Creazione di una serie con dati mancanti
dirty_data = pd.Series([1.0, np.nan, 3.5, np.nan, 7.0])

# Imputazione robusta tramite interpolazione o valore statico (es. mediana della serie)
clean_data = dirty_data.fillna(dirty_data.median())
```

### Rimozione Duplicati e Trasformazioni
*   `drop_duplicates()`: Identifica ed elimina le righe duplicate lungo il DataFrame.
*   `map()` / `replace()`: Sostituisce valori basandosi su dizionari di corrispondenza predefiniti.

---

## 🔗 4. Data Wrangling: Join, Combine e Reshape

Spesso l'analisi richiede la combinazione di più dataset eterogenei o la riorganizzazione della forma fisica del DataFrame per facilitare le aggregazioni o i grafici.

### Fusione Relazionale (pd.merge)
Simile alle operazioni di `JOIN` in ambiente SQL, `pd.merge()` unisce le righe di due DataFrame basandosi su una o più chiavi comuni.

```python
df1 = pd.DataFrame({'Key': ['b', 'b', 'a', 'c'], 'Data1': range(4)})
df2 = pd.DataFrame({'Key': ['a', 'b', 'd'], 'Data2': range(3)})

# Esegue un Inner Join basandosi sulla colonna 'Key'
merged_df = pd.merge(df1, df2, on='Key')
```

### Concatenazione Fisica (pd.concat)
Allinea e unisce fisicamente DataFrame diversi lungo l'asse delle righe (asse 0) o delle colonne (asse 1), riempiendo con `NaN` le etichette non corrispondenti.

```python
# Unione verticale di due DataFrame con colonne identiche
combined_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)
```

---

## 🔄 5. Il Paradigma Split-Apply-Combine (GroupBy)

Una delle operazioni analitiche più importanti è il raggruppamento e l'aggregazione sistematica dei dati. Pandas implementa formalmente il paradigma **Split-Apply-Combine** teorizzato da Hadley Wickham e reso celebre da Wes McKinney.

```
       [DATI ORIGINALI]
              |
      ┌───────┼───────┐
   [Split] [Split] [Split]     <-- Suddivisione per chiavi (es. Stato)
      │       │       │
   [Apply] [Apply] [Apply]     <-- Calcolo aggregazioni (es. Media o Somma)
      │       │       │
      └───────┼───────┘
              |
      [RISULTATO UNITO]
```

### Esempio Pratico di Aggregazione
```python
# Esempio di raggruppamento per calcolare statistiche di gruppo
grouped = df.groupby('Stato')

# Applica la funzione media a ciascun gruppo per la sola colonna 'Valore'
mean_by_state = grouped['Valore'].mean()
```

---

## 📈 6. Analisi delle Serie Storiche (Time Series)

Pandas è nato nel settore finanziario (sviluppato da Wes McKinney presso AQR Capital Management). Per questo motivo, possiede un supporto nativo di livello assoluto per la manipolazione di serie storiche temporali, fondamentale per l'analisi tecnica, gli indicatori finanziari e il trading sistematico.

### Strumenti Temporali Essenziali
1.  **DCA (Dollar Cost Averaging) e Shifting:** Spostare i dati nel tempo (`.shift()`) per calcolare variazioni percentuali storiche o rendimenti.
2.  **Resampling (Ricampionamento):** Modificare la frequenza temporale dei dati.
    *   *Downsampling:* Ridurre la frequenza (es. da candele orarie a giornaliere aggregando con la funzione `ohlc` o `mean`).
    *   *Upsampling:* Aumentare la frequenza temporale (es. da mensile a giornaliero tramite interpolazione lineare).
3.  **Rolling Windows (Finestre Mobili):** Calcolo di statistiche scorrevoli lungo l'asse del tempo (`.rolling()`).

### Esempio Finanziario Quantitativo (Calcolo Z-Score robusto basato su MAD)
Ecco l'implementazione in Pandas dell'esatta logica utilizzata dai bot di trading sistematico finanziario per identificare anomalie statistiche di prezzo (Z-Score robusto basato su [[Vectorization]]):

```python
# Assumiamo di avere una Series storica di prezzi giornalieri indicizzati per data
prezzi = pd.Series([2000.5, 2010.2, 1995.8, 2025.1, 2030.4, 1985.0, 2005.2], 
                   index=pd.date_range('2026-05-20', periods=7))

# 1. Calcolo della Media Mobile a 3 periodi (SMA 3)
sma_3 = prezzi.rolling(window=3).mean()

# 2. Calcolo della Volatilità Robusta MAD (Median Absolute Deviation)
def calcola_mad(window):
    mediana = window.median()
    return (window - mediana).abs().median()

# Applica MAD scorrevole su una finestra di 3 periodi
mad_3 = prezzi.rolling(window=3).apply(calcola_mad, raw=False)
std_mad_3 = mad_3 * 1.4826 # Costante di scala per allineare alla deviazione standard

# 3. Calcolo dello Z-Score robusto vettorializzato
z_score = (prezzi - sma_3) / std_mad_3
```

---

## 💡 Best Practices per l'Efficienza Computazionale

Quando si lavora su dataset di grandi dimensioni (milioni di righe), le prestazioni di Pandas dipendono fortemente dall'approccio di programmazione utilizzato.

*   **Evita i cicli `for` espliciti:** Non scorrere mai le righe di un DataFrame con un ciclo Python standard (`for i in range(len(df))`). È incredibilmente lento perché distrugge i vantaggi in memoria contigua.
*   **Prediligi la Vettorizzazione:** Sfrutta sempre le funzioni native di Pandas o NumPy che operano sull'intera colonna simultaneamente.
*   **Utilizza il tipo `Categorical`:** Per le colonne di testo con un numero limitato di valori univoci ripetuti (es. stati, generi, categorie), converti il tipo in `category` per ridurre il consumo di memoria RAM fino al 90%.

```python
# Ottimizzazione memoria per colonne a bassa cardinalità
df['Stato'] = df['Stato'].astype('category')
```

---

## Fonti
* `[[Fonte_McKinney_Python_Data_Analysis]]` — Teoria strutturale di NumPy, Pandas e IPython.
* `[[wiki/Script/ST_1_IO_Dataframe.py]]` — Script integrati nel Second Brain per l'I/O ed operazioni su DataFrame.
