---
tags: [finanza, capital-budgeting, npv, topic-5]
date_created: 2026-05-07
source: "raw/Teaching materials of Corporate Finance-20260505/Topic 5a-5e"
---

# 📈 Topic 5 — NPV & Criteri di Investimento

## 🥇 La Regola d'Oro: NPV
$$NPV = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}$$

**Regola:** Accettare tutti i progetti con **NPV > 0**. Tra due progetti mutualmente esclusivi, scegliere quello con NPV maggiore.

> Il NPV misura la creazione di valore per gli azionisti in termini assoluti e in €.

## 📐 Altri Criteri (con limiti)

### IRR — Internal Rate of Return
L'IRR è il tasso r* che rende NPV = 0.
$$0 = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$
- **Regola:** Accettare se IRR > WACC (costo del capitale)
- **⚠️ Limiti IRR:** Problema di scale, flussi non convenzionali (IRR multipli), non confrontabile tra progetti di diversa durata

### Payback Period
Tempo necessario a recuperare l'investimento iniziale.
- **Limite:** Ignora il TVM e i flussi dopo il payback.

### Profitability Index (PI)
$$PI = \frac{NPV}{I_0} + 1 = \frac{PV_{flussi}}{I_0}$$
- Utile quando il **capitale è razionato** (budget limitato)
- **Regola:** Accettare se PI > 1

## 🔑 NPV vs IRR: Quando Divergono?
| Situazione | Usa |
|---|---|
| Progetti indipendenti | Entrambi (stesso risultato) |
| Progetti mutualmente esclusivi con scala diversa | **NPV** |
| Flussi non convenzionali | **NPV** |
| Budget limitato | **PI** |

## 🔗 Collegato a
- [[Topic_4_Present_Values]]
- [[Topic_6_Risk_and_Return]]
- [[Topic_7_8_CAPM_Cost_of_Capital]]

## Fonti
* [[wiki/Fonti/Fonte_Corporate_Finance_Book.md]]
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
