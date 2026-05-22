---
tags: [fonte, finanza, quantitativa, portfolio-management, apm, grinold, kahn]
aliases: [Grinold_Kahn_APM]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# 📖 Fonte: Active Portfolio Management — Grinold & Kahn

**File Raw:** `raw/Active_Portfolio_Management_Grinold_Kahn.txt`
**Autori:** Richard C. Grinold, Ronald N. Kahn
**Tipo:** Libro accademico completo (2nd Edition, 2014, Meccanica di Trading, Traduzione Cinese, 922 KB, ~500 pagine equivalenti)

> Il testo sacro ("Quant Bible") della gestione attiva del portafoglio. Introduce formalmente i concetti di rischio residuale, Information Ratio ed elabora la celeberrima **Legge Fondamentale dell'Active Management** ($IR = IC \cdot \sqrt{BR}$), definendo un approccio strutturato e rigoroso per quantificare le abilità predittive dell'analista e l'efficienza nell'esecuzione del portafoglio.

---

## 🌐 Dizionario Termini Quantitativi (Cinese ➔ Inglese Accademico)
Poiché il file sorgente è la traduzione ufficiale cinese, di seguito viene definita la mappatura formale per allineare lo studio agli standard accademici in inglese presenti nelle note di concetto:

| Termine in Cinese | Traduzione Inglese Standard | Simbolo/Definizione |
|---|---|---|
| **一致预期收益率** | Consensus Expected Return | CAPM $E[R]$ |
| **残差风险** | Residual Risk (Tracking Error) | $\omega$ |
| **残差收益率** | Residual Return (Active Alpha) | $\alpha$ |
| **信息率** | Information Ratio | $IR = \alpha / \omega$ |
| **信息系数** | Information Coefficient | $IC = \text{Corr}(\alpha_{\text{forecast}}, \alpha_{\text{realized}})$ |
| **策略宽度 / 预测频数** | Breadth (Numero di scommesse indipendenti) | $BR$ |
| **主动管理基本定律** | Fundamental Law of Active Management | $IR = IC \cdot \sqrt{BR}$ |
| **传输系数** | Transfer Coefficient | $TC = \text{Corr}(w_{\text{active}}, \alpha_{\text{forecast}})$ |
| **主动附加值** | Active Value Added | $V_A = \alpha_p - \lambda_A \omega_p^2$ |
| **多空投资** | Long-Short Investing | Strategie Market Neutral |

---

## Capitoli Chiave e Mapping Wiki

| Capitolo | Contenuto Principale | Note di Concetto |
|---|---|---|
| **Chapter 3** | *Risk*: definizione assiomatica di rischio attivo e residuale, importanza della matrice di covarianza. | [[Information_Ratio_IR]] |
| **Chapter 4** | *Active Returns*: eccesso di rendimento rispetto al benchmark, residual returns ed il concetto di *Value Added*. | [[Information_Ratio_IR]] |
| **Chapter 5** | *Information Ratio*: residual risk e residual return, l'Information Ratio come metrica suprema dell'attivo. | [[Information_Ratio_IR]] |
| **Chapter 6** | *Fundamental Law*: la legge fondamentale dell'active management, breadth e coefficiente di informazione. | [[Fundamental_Law_of_Active_Management]] |
| **Chapter 10** | *Forecasting*: basi econometriche per la previsione dei rendimenti attivi e normalizzazione delle informazioni. | [[Z_Score_Stock_Screening]] |
| **Chapter 14** | *Portfolio Construction*: ottimizzazione dei pesi e rimozione di vincoli per massimizzare il Transfer Coefficient. | [[Portfolio_Weights_Optimization]] |
| **Chapter 15** | *Long-Short*: rimozione del vincolo long-only per liberare tutta la potenza del Breadth. | [[Market_Neutral_Portfolios]] |

---

## Formule Chiave Estratte
- **The Fundamental Law of Active Management (Basic)**:
  $$IR = IC \cdot \sqrt{BR}$$
- **The Fundamental Law of Active Management (Extended with Constraints)**:
  $$IR = TC \cdot IC \cdot \sqrt{BR}$$
- **Active Value Added (Valore Aggiunto Attivo)**:
  $$V_A = \alpha_p - \lambda_A \cdot \omega_p^2$$
  dove $\lambda_A$ rappresenta l'avversione al rischio residuale del gestore.

---

## Note Metodologiche
La forza del framework di Grinold & Kahn risiede nella scomposizione dell'abilità predittiva pura ($IC$) dall'efficienza costruttiva del portafoglio ($TC$), consentendo ai gestori istituzionali di capire se i sotto-rendimenti sono dovuti a cattive previsioni o a vincoli eccessivi (es. vincolo Long-Only).

## Fonti
* [[wiki/Fonti/Fonte_Chincarini_QEPM.md]]
* [[wiki/Fonti/Fonte_Corporate_Finance_Libro_Professore.md]]
