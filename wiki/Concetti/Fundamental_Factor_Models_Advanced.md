---
tags: [concetto, finanza, quantitativa, factor-model, OLS, robust-MAD, risk-decomposition, active-risk]
aliases: [Factor_Models, Multi_Factor_Models, Risk_Decomposition]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 2
---

# 🧬 Advanced Fundamental Factor Models

I **Modelli Multi-Fattoriali Fondamentali** (Fundamental Factor Models) sono utilizzati per stimare i rendimenti attesi, analizzare le esposizioni al rischio ed effettuare la decomposizione della varianza attiva del portafoglio. A differenza dei modelli macroeconomici, nei modelli fondamentali le **esposizioni** (i Beta dei fattori) sono variabili osservabili e note (es. i bilanci aziendali standardizzati tramite [[Z_Score_Stock_Screening|Z-Score]]), mentre i **premi dei fattori** (Factor Premiums) devono essere stimati econometricamente.

---

## 1. La Struttura Matematica del Modello

Il rendimento del titolo $i$ al tempo $t$ viene modellato come segue:

$$R_i(t) = a_i(t) + \sum_{f=1}^F \beta_{i,f} \cdot f_t + \epsilon_i(t)$$

Dove:
- $R_i(t)$ è il rendimento totale (o in eccesso al tasso risk-free) del titolo $i$.
- $\beta_{i,f}$ è l'**esposizione** (Exposure o Factor Loading) del titolo $i$ al fattore $f$. In genere si utilizzano gli Z-score normalizzati dei bilanci (es. esposizione al fattore Value tramite Book-to-Price).
- $f_t$ è il **premio del fattore** (Factor Premium) al tempo $t$, ovvero il rendimento generato da un portafoglio con esposizione unitaria al fattore $f$ e zero esposizione a tutti gli altri.
- $\epsilon_i(t)$ è il **rendimento residuale/idiosincratico** (Specific Return), non correlato tra i vari titoli:
  $$\text{Cov}(\epsilon_i, \epsilon_j) = 0 \quad \forall i \neq j$$

---

## 2. Stima Econometrica dei Premi dei Fattori

Per ricavare i premi dei fattori $f_t$ ad ogni istante temporale $t$, si esegue una regressione lineare cross-section (ovvero tra tutti i titoli dell'universo nello stesso istante):

### A. Stimatore OLS (Ordinary Least Squares)
Se definiamo la matrice delle esposizioni come $\mathbf{B}$ (di dimensione $N \times F$) e il vettore dei rendimenti dei titoli come $\mathbf{R}$ (di dimensione $N \times 1$), il vettore dei premi stimati $\mathbf{f}$ è ricavato tramite OLS:

$$\mathbf{f} = (\mathbf{B}^T \mathbf{B})^{-1} \mathbf{B}^T \mathbf{R}$$

### B. Stimatore Robusto MAD (Median Absolute Deviation)
I rendimenti di mercato presentano forti code spesse (*fat tails*) ed eventi estremi. Lo stimatore OLS classico è estremamente sensibile a questi outlier. Per evitare distorsioni, si utilizza una stima robusta (es. **WLS - Weighted Least Squares** o stimatori M basati sulla MAD) che assegna pesi inferiori ai titoli con deviazioni estreme:

$$w_i = \min\left(1, \frac{c \cdot \text{MAD}_{\epsilon}}{|\epsilon_i|}\right)$$

dove $c$ è una costante di tuning e $\text{MAD}_{\epsilon}$ è la deviazione assoluta mediana dei residui della regressione.

---

## 3. Correzioni Econometriche: Errori HAC (Newey-West)

Poiché i rendimenti finanziari cross-section presentano fenomeni di eteroschedasticità (la varianza dei residui varia nel tempo) e autocorrelazione seriale, le stime classiche degli errori standard dei coefficienti $\mathbf{f}$ risultano fortemente sottostimate.

Per evitare falsi positivi econometrici ($t$-statistiche artificialmente gonfiate), si applica la correzione di **Newey-West (HAC - Heteroscedasticity and Autocorrelation Consistent)** per la matrice di varianza-covarianza:

$$\mathbf{\Sigma}_{\text{HAC}} = \mathbf{\Sigma}_0 + \sum_{l=1}^L \left( 1 - \frac{l}{L+1} \right) (\mathbf{\Sigma}_l + \mathbf{\Sigma}_l^T)$$

dove $\mathbf{\Sigma}_l$ è la matrice di covarianza lagga al ritardo $l$ ed $L$ è il numero massimo di lag considerati.

---

## 4. Decomposizione Attiva del Rischio (Tracking Error Variance)

Uno degli utilizzi principali dei modelli multifattoriali è scomporre la varianza attiva del portafoglio rispetto ad un benchmark (il quadrato del Tracking Error) in due componenti distinte: **Rischio Sistematico dei Fattori** e **Rischio Idiosincratico (Specifico)**.

Se definiamo il vettore dei pesi attivi del portafoglio come $\mathbf{w}_a = \mathbf{w}_p - \mathbf{w}_b$ (differenza tra pesi di portafoglio e pesi di benchmark), la varianza attiva è data da:

$$\sigma_{\text{active}}^2 = \mathbf{w}_a^T \mathbf{\Omega} \mathbf{w}_a$$

Sostituendo la covarianza del modello a fattori $\mathbf{\Omega} = \mathbf{B} \mathbf{\Omega}_f \mathbf{B}^T + \mathbf{\Delta}$:

$$\sigma_{\text{active}}^2 = \underbrace{\mathbf{w}_a^T (\mathbf{B} \mathbf{\Omega}_f \mathbf{B}^T) \mathbf{w}_a}_{\text{Rischio Sistematico dei Fattori}} + \underbrace{\mathbf{w}_a^T \mathbf{\Delta} \mathbf{w}_a}_{\text{Rischio Specifico / Idiosincratico}}$$

Dove:
- $\mathbf{\Omega}_f$ è la matrice di covarianza dei premi dei fattori (dimensione $F \times F$).
- $\mathbf{\Delta}$ è la matrice diagonale contenente le varianze residue dei singoli titoli ($\sigma_{\epsilon, i}^2$).

> [!IMPORTANT]
> Un buon gestore quantitativo cerca di limitare il **Rischio Sistematico dei Fattori** (es. mantenendo le esposizioni fattoriali del portafoglio vicine a quelle del benchmark, $\mathbf{B}^T \mathbf{w}_a \approx \mathbf{0}$) per fare in modo che la sua sovraperformance sia guidata esclusivamente dall'abilità di stock selection (espressa dal **Rischio Specifico** del portafoglio).

---

## Fonti
* [[wiki/Fonti/Fonte_Chincarini_QEPM.md]]
* [[wiki/Fonti/Fonte_Grinold_Kahn_APM.md]]
* [[wiki/Concetti/Information_Ratio_IR.md]]
* [[wiki/Concetti/Z_Score_Stock_Screening.md]]
