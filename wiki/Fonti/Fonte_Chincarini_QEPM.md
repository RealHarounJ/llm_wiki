---
tags: [fonte, finanza, quantitativa, portfolio-management, qepm, chincarini]
aliases: [Chincarini_QEPM]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# 📖 Fonte: Quantitative Equity Portfolio Management — Chincarini

**File Raw:** `raw/Quantitative_Equity_Portfolio_Management_Chincarini.txt`
**Autore:** Ludwig B. Chincarini
**Tipo:** Libro accademico completo (2nd Edition, 2023, McGraw Hill, 800 Pagine, 1.69 MB)

> Testo accademico avanzato per la gestione quantitativa di portafogli azionari. Fornisce un framework matematico rigoroso che unisce la teoria finanziaria classica (CAPM, APT) a tecniche econometriche avanzate, modelli multi-fattore, ottimizzazione quadratica di pesi con costi di transazione e attribuzione delle performance.

---

## Capitoli Fondamentali e Mapping Wiki

| Capitolo | Contenuto Principale | Note di Concetto |
|---|---|---|
| **Chapter 2** | *Fundamentals of QEPM*: ex-ante/ex-post $\alpha$, Information Ratio, i 7 principi della finanza quantitativa, la legge fondamentale dell'active management ed information criterion. | [[Information_Ratio_IR]], [[Fundamental_Law_of_Active_Management]] |
| **Chapter 3** | *Basic QEPM Models*: scelta dei fattori, z-score screening, modelli ibridi di ranking ed expected returns. | [[Z_Score_Stock_Screening]] |
| **Chapter 4** | *Factors and Factor Choice*: fattori fondamentali (Valuation, Size, Efficiency, Solvency) e tecnici (Liquidity, Momentum), regressioni univariate/multiple per la selezione. | [[Fundamental_Factor_Models_Advanced]] |
| **Chapter 5** | *Stock Screening and Ranking*: screening simultaneo vs sequenziale, Z-score aggregato ed equivalenza con modelli fattoriali. Gestione degli outlier (MAD, Winsorization). | [[Z_Score_Stock_Screening]] |
| **Chapter 6** | *Fundamental Factor Models*: stime OLS e MAD (robust) dei premi dei fattori, errori HAC standard, decomposizione del rischio attivo. | [[Fundamental_Factor_Models_Advanced]] |
| **Chapter 9** | *Portfolio Weights*: programmazione quadratica Mean-Variance con vincoli di short-sale, settore, volume e tracking error. Ghost benchmark tracking. | [[Portfolio_Weights_Optimization]] |
| **Chapter 10** | *Rebalancing & Transactions Costs*: modellizzazione lineare e non-lineare dei costi di impatto sul mercato, ottimizzazione dei pesi netta. | [[Portfolio_Weights_Optimization]] |
| **Chapter 13** | *Market Neutral*: costruzione di portafogli dollar-neutral e beta-neutral, leva finanziaria e Portable Alpha. | [[Market_Neutral_Portfolios]] |
| **Chapter 15** | *Performance Measurement*: Sharpe Ratio, Information Ratio (ex-post) ed attribuzione delle performance (Fama-French ed attribuzione a fattori). | [[Information_Ratio_IR]] |

---

## Formule Chiave Trattate nel Libro

- **Benchmark $\alpha$ (Active Return)**:
  $$R_p - R_b = \alpha + \beta_p(R_m - R_b) + \epsilon_p$$
- **Ex-Ante ed Ex-Post Information Ratio (IR)**:
  $$IR = \frac{\alpha}{\omega}$$
  dove $\omega$ è l'Active Risk o Tracking Error.
- **Z-Score Individuale**:
  $$Z_{i,f} = \frac{X_{i,f} - \mu_f}{\sigma_f}$$
- **Z-Score Aggregato**:
  $$AZ_i = \sum_{f=1}^F w_f Z_{i,f}$$

---

## Note Metodologiche
Il testo rappresenta lo stato dell'arte dell'equity portfolio management quantitativo. Viene utilizzato come testo di riferimento accademico avanzato e per lo sviluppo di modelli di trading quantitativi buy-side in fondi azionari sistematici.

## Fonti
* [[wiki/Fonti/Fonte_Grinold_Kahn_APM.md]]
* [[wiki/Fonti/Fonte_Corporate_Finance_Libro_Professore.md]]
