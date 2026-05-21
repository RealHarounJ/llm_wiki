---
tags: [corporate-finance, long-term-planning, pro-forma, EFN, excel]
aliases: [Percentage of Sales Method, External Financing Needed]
---

# Esercitazione Pratica: Long-Term Financial Planning

Il **Long-Term Financial Planning** (Pianificazione Finanziaria a Lungo Termine) serve a capire di quanti soldi extra avrà bisogno l'azienda in futuro per sostenere la sua crescita. 

Il metodo standard usato all'esame è il **Percentage of Sales Approach** (Metodo della percentuale sulle vendite).
La logica è semplice: se le vendite aumentano del 20%, l'azienda dovrà produrre il 20% in più. Quindi avrà bisogno del 20% in più di macchinari, inventario e asset in generale. 
Tuttavia, il debito e il capitale sociale *non* crescono automaticamente del 20%. Questo sbilanciamento crea un "buco" che il manager deve riempire: questo buco si chiama **External Financing Needed (EFN)**.

Ecco una simulazione Excel in inglese.

### Data & Assumptions
*   **Sales Growth:** We project a **20%** increase in sales next year.
*   **Assets:** Grow proportionally with sales.
*   **Profit Margin:** Net Income is 20% of Sales.
*   **Dividend Payout Ratio:** We pay 50% of Net Income as dividends. We keep the other 50% as **Retained Earnings**.
*   **Debt:** Does not change automatically.

---

### Excel Simulation: Pro Forma Financial Statements ($)

**1. INCOME STATEMENT PROJECTION**

| Item | Year 0 (Actual) | Year 1 (Projected at +20%) |
| :--- | :--- | :--- |
| **Sales** | 1,000 | **1,200** *(1,000 * 1.20)* |
| Costs | (800) | (960) |
| **Net Income** | **200** | **240** |
| *Dividends (50%)* | *100* | *120* |
| *Retained Earnings (50%)* | *100* | **120** *(This goes to Equity)* |

<br>

**2. BALANCE SHEET PROJECTION (The EFN Calculation)**

| Item | Year 0 (Actual) | Year 1 (Pro Forma) | Explanation for Year 1 |
| :--- | :--- | :--- | :--- |
| **Total Assets** | **1,000** | **1,200** | *Grows exactly by 20% with sales.* |
| | | | |
| **Debt** | 400 | 400 | *Does not grow automatically.* |
| **Equity** | 600 | 720 | *Old Equity (600) + New Retained Earnings (120).* |
| **Total Liabilities & Equity**| **1,000** | **1,120** | *Sum of Debt and new Equity.* |
| | | | |
| **EXTERNAL FINANCING NEEDED (EFN)** | | **+ 80** | **Assets (1,200) - Total Liab & Equity (1,120)** |

---

### How to explain this to the Professor:
1.  **The Goal:** "We use Long-Term Financial Planning to calculate the EFN (External Financing Needed) to support future sales growth."
2.  **The Problem:** "If sales grow by 20%, our Total Assets must grow to 1,200. However, our internal financing (Retained Earnings) only generated 120 of new Equity. This brings our total Liabilities & Equity to only 1,120."
3.  **The Solution:** "Since the Balance Sheet MUST balance (Assets = Liab + Equity), we have a deficit of 80. The company must raise **80$ of External Financing** (by issuing new long-term bonds or new shares) to buy the assets needed to support the 20% sales growth."

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
