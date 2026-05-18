---
tags: [corporate-finance, capital-budgeting, NPV, OCF, excel, esercitazione]
aliases: [Valutazione Progetti, Free Cash Flow Calculation]
---

# Esercitazione Pratica: Capital Budgeting & NPV

Il **Capital Budgeting** è il cuore delle decisioni di investimento. All'esame pratico, non ti daranno i flussi di cassa già pronti, ma ti daranno vendite, costi e ammortamenti e ti chiederanno di costruirti i **Free Cash Flows (FCF)** da zero per poi calcolare l'NPV.

Ecco la struttura standard (simile a Excel) che devi usare per risolvere qualsiasi problema di Capital Budgeting.

### Dati del Progetto (Assumptions):
*   **Initial Investment (CAPEX):** 30.000 € (Acquisto macchinario oggi, Year 0).
*   **Project Life:** 3 anni.
*   **Depreciation (Ammortamento):** Straight-line (a quote costanti) fino a zero = 10.000 € all'anno.
*   **Net Working Capital (NWC):** Richiesto un investimento iniziale in scorte di 2.000 € all'Anno 0, che verrà interamente recuperato alla fine del progetto (Anno 3).
*   **Sales:** 25.000 € all'anno.
*   **Operating Costs:** 10.000 € all'anno.
*   **Tax Rate:** 20%.
*   **Cost of Capital (Discount Rate):** 10%.

---

### Step 1: Calcolo dell'Operating Cash Flow (OCF) per gli anni 1, 2 e 3

La formula standard dell'OCF (approccio "Bottom-Up") è: **Net Income + Depreciation**.

| Item (Income Statement approach) | Anno 1-3 | Spiegazione |
| :--- | :--- | :--- |
| **Sales** | 25.000 | |
| - Operating Costs | (10.000) | |
| - Depreciation | (10.000) | *Ammortamento non è un'uscita di cassa, ma abbassa le tasse!* |
| **= EBIT (Operating Income)** | **5.000** | |
| - Taxes (20%) | (1.000) | |
| **= Net Income** | **4.000** | |
| + Depreciation | + 10.000 | *Aggiungiamo indietro l'ammortamento perché non è una spesa "cash".* |
| **= OPERATING CASH FLOW (OCF)**| **14.000** | *Questo è il flusso di cassa puro generato dalle operazioni ogni anno.* |

---

### Step 2: La Tabella dei Free Cash Flows e calcolo NPV

Ora uniamo l'OCF con gli investimenti iniziali e le variazioni di Working Capital per trovare il flusso totale da scontare.

| Item | Year 0 | Year 1 | Year 2 | Year 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Operating Cash Flow (OCF)** | 0 | 14.000 | 14.000 | 14.000 |
| **CAPEX (Macchinario)** | (30.000) | 0 | 0 | 0 |
| **Net Working Capital (NWC)** | (2.000) | 0 | 0 | + 2.000 |
| **TOTAL FREE CASH FLOWS** | **(32.000)** | **14.000** | **14.000** | **16.000** |
| | | | | |
| *Discount Factor a 10%* | *1.000* | *0.909* | *0.826* | *0.751* |
| **Present Value (PV) dei Flussi** | **(32.000)** | **12.726** | **11.564** | **12.016** |

### Step 3: Conclusione
Il **Net Present Value (NPV)** è la somma algebrica di tutti i Present Value (Anno 0 + Anno 1 + Anno 2 + Anno 3).

*   NPV = -32.000 + 12.726 + 11.564 + 12.016 = **+ 4.306 €**

Poiché l'**NPV > 0**, la decisione del manager è: **ACCEPT THE PROJECT**. Il valore dell'azienda per gli azionisti è aumentato di 4.306 €.
