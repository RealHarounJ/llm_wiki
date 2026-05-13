---
tags: [finanza, corporate-finance, financial-analysis, ratios, topic-2]
aliases: [Financial Ratios, Indici di Bilancio, Profitability Ratios]
date_created: 2026-05-07
last_modified: 2026-05-07
source_count: 2
---

# 📊 Topic 2 — Financial Analysis (Chapter 29)

> **Fonte:** Corporate finance.md (libro professore, Chapter 29) + Slides UNIVPM 2025/2026

## 🎯 Obiettivo dell'Analisi Finanziaria

Determinare se l'azienda sta raggiungendo il suo obiettivo fondamentale: **massimizzare il valore per gli azionisti (Shareholders' Value / Equity)**.

L'analisi si articola su 4 aree:
1. **Profitabilità** — L'azienda genera valore e profitti?
2. **Efficienza** — Usa bene i suoi asset?
3. **Leverage** — Quanto debito usa? È sostenibile?
4. **Liquidità** — Può ripagare i debiti correnti?

---

## 📈 AREA 1 — Misure di Valore per gli Azionisti

### MVA — Market Value Added
**MVA = Market Capitalisation − Book Value of Shareholders' Equity**

- MVA > 0 → l'azienda ha creato ricchezza **oltre** il capitale investito
- MVA < 0 → il mercato valuta l'azienda meno di quanto ci hanno messo gli azionisti

**Market-to-Book Ratio = Market Value of Equity / Book Value of Equity**

Stesso concetto dell'MVA in forma di rapporto invece che differenza.

> Limite: funziona solo per aziende **quotate**. Se privata, si usa EVA.

---

### EVA — Economic Value Added
**EVA = (After-tax Interest + Net Income) − (WACC × Total Capital at start of year)**

Dove:
- **After-tax Interest** = Interest Expense × (1 − tax rate)
- **Total Capital** = Long-term Debt + Shareholders' Equity (NON include current liabilities)

EVA > 0 → l'azienda guadagna **più del costo del capitale** → crea valore per tutti i finanziatori

Esempio del professore:
- After-tax interest + Net Income = (1 − 0.21) × 603 + 1,512 = **1,988 M**
- WACC × Total Capital = 0.055 × 19,907 = **1,095 M**
- **EVA = 1,988 − 1,095 = 893 M**

---

## 📉 AREA 2 — Misure di Redditività degli Investimenti

### ROC — Return on Capital
**ROC = (After-tax Interest + Net Income) / Total Capital at start of year**

Confronta sempre con **WACC**:
- ROC > WACC → creazione di valore (4.5% di extra-rendimento nell'esempio)
- ROC < WACC → distruzione di valore

Esempio: ROC = 1,988 / 19,907 = **10%** (con WACC = 5.5% → extra return = 4.5%)

---

### ROA — Return on Assets
**ROA = (After-tax Interest + Net Income) / Total Assets at start of year**

Differenza dal ROC: usa **Total Assets** al denominatore (che è più grande perché include current liabilities).

Esempio: ROA = 1,988 / 38,118 = **5.2%**

> ROA e ROC danno informazioni simili ma con denominatori diversi. Usare ROA permette confronti equi tra aziende con strutture del capitale molto diverse.

---

### ROE — Return on Equity
**ROE = Net Income / Equity at start of year**

Misura il rendimento **solo per gli azionisti** (usa Net Income, NON include after-tax interest).

Esempio: ROE = 1,512 / 7,835 = **19.3%**

**ROE > ROA** → l'azienda usa la **leva finanziaria** per amplificare i rendimenti degli azionisti.

---

## 🔗 AREA 2b — Formula DuPont (scomposizione del ROE)

**ROE = Leverage × Asset Turnover × Operating Profit Margin × Debt Burden**

| Componente                  | Formula                                        | Cosa misura                                       |
| --------------------------- | ---------------------------------------------- | ------------------------------------------------- |
| **Leverage**                | (Equity + Liabilities) / Equity                | Quant'è l'uso del debito                          |
| **Asset Turnover**          | Sales / Assets                                 | Efficienza uso asset                              |
| **Operating Profit Margin** | (After-tax Interest + Net Income) / Sales      | Profitto per € venduto (per tutti i finanziatori) |
| **Debt Burden**             | Net Income / (After-tax Interest + Net Income) | Impatto interessi: quanta parte va agli azionisti |

---

## ⚙️ AREA 3 — Misure di Efficienza

### Asset Turnover Ratio
**Asset Turnover = Sales / Total Assets at start of year**

Esempio: 122,286 / 38,118 = **3.21** → ogni euro di asset genera 3.21€ di vendite.

---

### Inventory Turnover
**Inventory Turnover = Cost of Goods Sold / Inventory at start of year**

Esempio: 95,294 / 6,846 = **13.9**

**Inventory Period = Inventory / (COGS / 365) = 26.2 giorni**

---

### Receivables Turnover
**Receivables Turnover = Sales / Receivables at start of year**

Esempio: 122,286 / 1,589 = **77.0**

**Accounts Receivable Period = Receivables / (Sales / 365) = 4.7 giorni**

(media giorni per incassare dai clienti)

---

### Average Payment Period
**Average Payment Period = Accounts Payable / (COGS / 365)**

> Regola: Average Collection Period < Average Payment Period (incasso prima di pagare)

---

## 📊 AREA 3b — Profitto dalle Vendite

### Profit Margin (solo azionisti)
**Profit Margin = Net Income / Sales**

Esempio: 1,512 / 122,286 = **1.24%**

---

### Operating Profit Margin (azionisti + debt holders)
**Operating Profit Margin = (After-tax Interest + Net Income) / Sales**

Esempio: [(1 − 0.21) × 603 + 1,512] / 122,286 = **1.63%**

> Regola: High Asset Turnover ↔ Low Profit Margin (tradeoff industria)

---

## 🏗️ AREA 4 — Misure di Leverage

### Long-term Debt Ratio
**Long-term Debt Ratio = Long-term Debt / (Long-term Debt + Equity)**

Esempio: 12,111 / (12,111 + 8,573) = **59%**

---

### Long-term Debt-to-Equity Ratio
**Long-term Debt/Equity = Long-term Debt / Equity**

Esempio: 12,111 / 8,573 = **140%**

---

### Total Debt Ratio
**Total Debt Ratio = Total Liabilities / Total Assets**

Esempio: 36,683 / 45,256 = **81%**

---

### Times-Interest-Earned (TIE)
**TIE = EBIT / Interest Payments**

Esempio: 2,584 / 603 = **4.3x**

> Banche accettano TIE >= 2-3x. TIE < 1 = impossibile pagare gli interessi.

Limite: EBIT include ammortamenti (non è cash) → non dice se c'è cassa sufficiente.

---

### Cash Coverage Ratio
**Cash Coverage = (EBIT + Depreciation) / Interest Payments**

Esempio: (2,584 + 2,649) / 603 = **8.7x**

---

## 💧 AREA 5 — Misure di Liquidità

**Liquidity** = Capacità di ripagare i debiti in modo:
1. **Corrente**: Puntualmente alla scadenza.
2. **Economico**: Senza svendere asset (es. scorte) a prezzi di liquidazione (*fire-sale prices*).

**Principio di Maturity Matching:** 
- Asset liquidi (correnti) → per debiti a breve.
- Asset fissi → finanziati con fonti a lungo (debito L/T o equity).
- **Nuance**: Le scorte (inventories) sono la parte più illiquida del circolante; idealmente dovrebbero essere coperte da fonti a lungo termine. Se **NWC > 0**, significa che le scorte sono finanziate da capitale stabile.

---

### Net Working Capital to Total Assets
**NWC = Current Assets − Current Liabilities**

Esempio: 10,890 − 14,243 = −3,353 → NWC negativo = problema liquidità!
**NWC / Total Assets = −7.4%** (negativo = rischio)

---

### Current Ratio
**Current Ratio = Current Assets / Current Liabilities**

Esempio: 10,890 / 14,243 = **0.76** (< 1 → problema!)

> Equilibrio richiede Current Ratio > 1. È la forma "ratio" del NWC.

---

### Quick (Acid-Test) Ratio
**Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities**

Esempio: (1,578 + 1,706) / 14,243 = **0.23**

> Esclude inventari (illiquidi). In equilibrio perfetto dovrebbe tendere a **1**. Se < 1, l'azienda usa asset a lungo termine per pagare debiti a breve (pericoloso).

---

### Cash Ratio
**Cash Ratio = (Cash + Marketable Securities) / Current Liabilities**

Esempio: 1,578 / 14,243 = **0.11**

> Un valore basso non è necessariamente un problema se l'azienda ha linee di credito (credit lines) non utilizzate (non visibili nel ratio).

---

## ⚠️ Limiti e Avvertenze dell'Analisi

### 1. Market Value vs Book Value
- **Vantaggio Prezzi**: Oggettivi e riflettono le aspettative future.
- **Svantaggio Prezzi**: Influenzati dal mercato (*bull/bear market*) indipendentemente dal manager. Non disponibili per aziende private o divisioni.

### 2. Problemi Contabili (Accounting bias)
- **Asset Intangibili**: Brand, reputazione e forza lavoro non appaiono in bilancio.
- **R&D**: Trattata come costo (abbassa ROE/EVA subito) ma economicamente è un investimento (crea valore tra 10 anni).
- **Costo Storico**: Gli asset sono a bilancio al prezzo d'acquisto meno ammortamento. Un terreno comprato nel 2000 a 1M può valerne 10M oggi, ma il ROA sembrerà altissimo solo perché il denominatore è "vecchio".

### 3. Buybacks
I riacquisti di azioni riducono il **Book Equity**, rendendo i ratio come ROE o EVA poco significativi o distorti.

## 🔗 Collegato a
- [[Corporate_Finance_Hub]]
- [[Topic_3_Statement_of_Cash_Flows]]
- [[Topic_7_8_CAPM_Cost_of_Capital]]
- [[Pianificazione_Finanziaria_Lungo_Termine]]
- [[Master_Page_Corporate_Finance]]

## Fonti
- `raw/Corporate finance.md` — Libro del professore, Chapter 29
- `raw/Teaching materials of Corporate Finance-20260505/Topic 2 - financial analysis 2025.2026`
