---
tags: [finanza, capital-budgeting, risk-analysis, sensitivity]
date_created: 2026-05-11
source: "raw/extracted/Chapter_10.md"
---

# 🔍 Analisi di Sensitività, Scenari e Break-Even

L'analisi del rischio nel capital budgeting è un processo "bottom-up" che cerca di quantificare l'incertezza legata alle previsioni dei flussi di cassa.

## 1. Analisi di Sensitività (Sensitivity Analysis)
Analizza come varia l'NPV al variare di **una sola variabile** alla volta (es. vendite, costi, prezzo), mantenendo le altre costanti (*ceteris paribus*).

*   **Pessimistic vs Optimistic:** Si definiscono scenari "worst-case" e "best-case" per ogni variabile chiave.
*   **Limiti:** 
    1. **Soggettività:** La definizione di "ottimistico" o "pessimistico" dipende dal manager.
    2. **Mancanza di Correlazione:** Non considera che le variabili sono spesso correlate (es. se aumentano i volumi, probabilmente aumentano anche i costi variabili).

## 2. Analisi di Scenario (Scenario Analysis)
Analizza l'impatto sull'NPV di cambiamenti **simultanei e coerenti** in più variabili.
*   **Vantaggio:** Più realistica della sensitività perché cattura le interdipendenze (es. uno shock petrolifero che aumenta i costi e deprime la domanda).
*   **Limite:** Estremamente dispendiosa in termini di tempo; spesso limitata a 2-3 scenari complessi.

## 3. Break-Even Analysis (Analisi del Punto di Pareggio)
Individua il livello critico (solitamente vendite) in cui il progetto smette di perdere e inizia a guadagnare.

| Tipo di Break-Even | Obiettivo | Definizione |
|---|---|---|
| **Accounting Break-Even** | Profitto Contabile = 0 | Vendite che coprono tutti i costi (incluso ammortamento). |
| **Financial/NPV Break-Even** | **NPV = 0** | Vendite che rendono l'investimento conveniente dal punto di vista finanziario. |

> [!IMPORTANT]
> Il **Financial Break-Even** è sempre più alto dell'Accounting Break-Even perché deve coprire anche il costo opportunità del capitale.

## 4. Operating Leverage (Leva Operativa)
Misura la sensibilità del profitto alle variazioni delle vendite. Dipende dalla proporzione di **costi fissi**.

*   **Formula DOL (Degree of Operating Leverage):**
    $$DOL = \frac{\% \text{ variazione Profitti}}{\% \text{ variazione Vendite}}$$
*   **Significato:** Un'azienda con alti costi fissi ha un DOL elevato: un piccolo calo di vendite causa un crollo dei profitti, ma un piccolo aumento causa un "killing" (guadagni massicci).
