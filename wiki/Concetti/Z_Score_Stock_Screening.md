---
tags: [concetto, finanza, quantitativa, stock-screening, z-score, ranking, multi-factor]
aliases: [Z_Score_Screening, Stock_Ranking, Winsorization]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 2
---

# 📊 Stock Screening and Ranking using Z-Scores

Nello sviluppo di modelli quantitativi sistematici, lo **Stock Screening and Ranking** è la procedura utilizzata per scansionare un ampio universo di titoli (es. S&P 500, Russell 3000) e ordinarli dal più attraente al meno attraente sulla base di molteplici fattori fondamentali o tecnici. Il metodo standard per rendere confrontabili metriche di natura diversa (es. P/E ratio, Market Cap, EBITDA Margin) è la standardizzazione tramite **Z-Score**.

---

## 1. Il Calcolo dello Z-Score Individuale

Per un dato titolo $i$ e un singolo fattore $f$ (es. Book-to-Market), lo Z-score individuale misura quante deviazioni standard il valore di quel titolo si discosta dalla media dell'universo analizzato:

$$Z_{i,f} = \frac{X_{i,f} - \mu_f}{\sigma_f}$$

Dove:
- $X_{i,f}$ è il valore grezzo del fattore $f$ per il titolo $i$.
- $\mu_f$ è la media aritmetica del fattore $f$ sull'intero universo di stock:
  $$\mu_f = \frac{1}{N}\sum_{i=1}^N X_{i,f}$$
- $\sigma_f$ è la deviazione standard del fattore $f$ sull'intero universo:
  $$\sigma_f = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (X_{i,f} - \mu_f)^2}$$

---

## 2. Trattamento degli Outlier: Tecniche Robuste

I dati finanziari reali contengono forti distorsioni e valori estremi (outlier) che possono falsare completamente il calcolo di media ($\mu$) e deviazione standard ($\sigma$). Esistono tre metodi fondamentali per gestire queste anomalie:

### A. Winsorization (Winsorizzazione)
Invece di rimuovere gli outlier, i valori estremi oltre una certa soglia percentile (tipicamente l'1% e il 99%) vengono impostati al valore di quella stessa soglia:

$$\text{Se } X_{i,f} > P_{99} \implies X_{i,f} = P_{99}$$
$$\text{Se } X_{i,f} < P_{1} \implies X_{i,f} = P_{1}$$

### B. Trimming (Rifilatura)
Gli outlier vengono completamente eliminati dal dataset. Sebbene mantenga i dati rimanenti puliti, riduce l'ampiezza campionaria dell'universo investibile.

### C. Standardizzazione Robusta tramite MAD (Median Absolute Deviation)
Un approccio matematicamente superiore e robusto che sostituisce la media con la mediana e la deviazione standard con la **MAD**:

$$\text{MAD}_f = \text{Median}\left( \left| X_{i,f} - \text{Median}(X_{j,f}) \right| \right)$$

Lo Z-score robusto viene calcolato dividendo lo scostamento dalla mediana per la MAD, riscalata per un fattore di consistenza ($1.4826$) che la rende equivalente alla deviazione standard sotto distribuzione normale:

$$Z_{i,f}^{\text{robust}} = \frac{X_{i,f} - \text{Median}(X_{j,f})}{1.4826 \cdot \text{MAD}_f}$$

---

## 3. L'Aggregate Z-Score (Z-Score Aggregato)

Per combinare molteplici fattori (es. segnali Value, Momentum e Quality) in un unico punteggio decisionale per ciascuna azione, si calcola l'**Aggregate Z-Score**:

$$AZ_i = \sum_{f=1}^F w_f \cdot Z_{i,f}$$

Dove:
- $w_f$ è il peso assegnato al fattore $f$ (tale che $\sum_{f=1}^F w_f = 1$).
- $Z_{i,f}$ è lo z-score normalizzato del titolo $i$ sul fattore $f$.

> [!TIP]
> **Segnali Inversi**: Per fattori in cui un valore più basso è preferibile (es. P/E Ratio o Debt-to-Equity), lo Z-score deve essere invertito moltiplicandolo per $-1$ prima dell'aggregazione:
> $$Z_{i,\text{P/E}} = -1 \cdot \left( \frac{X_{i,\text{P/E}} - \mu_{\text{P/E}}}{\sigma_{\text{P/E}}} \right)$$

---

## 4. Conversione dello Z-Score in Rendimenti Attesi ($E[R]$)

Per poter implementare un algoritmo di Mean-Variance Optimization, è necessario convertire il punteggio adimensionale dell'Aggregate Z-score ($AZ_i$) in una stima esplicita del rendimento attivo atteso ($E[R_{\text{active}, i}]$). 

La regola empirica standard formulata da Chincarini ed allineata con la teoria di Grinold è:

$$E[R_{\text{active}, i}] = AZ_i \cdot \sigma_{\text{active}} \cdot IC$$

Dove:
- $\sigma_{\text{active}}$ è la deviazione standard attesa dei rendimenti attivi storici dell'universo.
- $IC$ è l'[[Fundamental_Law_of_Active_Management#3. Analisi dei Componenti Chiave|Information Coefficient]] (l'abilità stimata del modello quantitativo).

### Esempio Numerico:
Supponiamo che per il titolo Apple (AAPL) si calcoli un $AZ_{\text{AAPL}} = 1.5$. Se la deviazione standard dei rendimenti attivi annui è $\sigma_{\text{active}} = 12\%$ ed il nostro modello ha un'abilità conservativa $IC = 0.08$:
$$E[R_{\text{active}, \text{AAPL}}] = 1.5 \cdot 0.12 \cdot 0.08 = 0.0144 \text{ o } 1.44\% \text{ annuo}$$

---

## Fonti
* [[wiki/Fonti/Fonte_Chincarini_QEPM.md]]
* [[wiki/Fonti/Fonte_Grinold_Kahn_APM.md]]
* [[wiki/Concetti/Fundamental_Law_of_Active_Management.md]]
* [[wiki/Concetti/Information_Ratio_IR.md]]
