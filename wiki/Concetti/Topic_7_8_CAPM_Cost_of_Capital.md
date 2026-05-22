---
tags: [finanza, capm, wacc, costo-capitale, topic-7, topic-8]
date_created: 2026-05-07
source: "raw/Teaching materials of Corporate Finance-20260505/Topics 7 and 8"
---

# 📡 Topic 7 & 8 — CAPM, WACC e Costo del Capitale

## 🎯 Il CAPM (Capital Asset Pricing Model)
Il CAPM descrive la relazione tra rischio sistematico e rendimento atteso:

$$E[R_i] = r_f + \beta_i \cdot (E[R_m] - r_f)$$

| Simbolo | Significato |
|---|---|
| $r_f$ | Tasso risk-free (es. BTP 10 anni) |
| $\beta_i$ | Sensibilità del titolo al mercato |
| $E[R_m] - r_f$ | Market Risk Premium (ERP) |

### Il Beta (β)
$$\beta_i = \frac{Cov(R_i, R_m)}{\sigma^2_m}$$

- **β = 1:** Il titolo si muove come il mercato
- **β > 1:** Più volatile del mercato (es. tech)
- **β < 1:** Meno volatile (es. utilities)
- **β = 0:** Nessuna correlazione con il mercato (risk-free)

## 📐 La Security Market Line (SML)
La SML è la rappresentazione grafica del CAPM:
- Asse X: **Beta**
- Asse Y: **Rendimento atteso**
- Titoli **sopra la SML** → sottovalutati (α > 0)
- Titoli **sotto la SML** → sopravvalutati (α < 0)

## 📐 WACC — Weighted Average Cost of Capital
$$WACC = \frac{E}{D+E} \cdot r_E + \frac{D}{D+E} \cdot r_D \cdot (1-t)$$

| Componente | Formula |
|---|---|
| Costo dell'Equity $r_E$ | Via CAPM: $r_f + \beta_E \cdot ERP$ |
| Costo del Debito $r_D$ | Tasso del debito al netto delle tasse |
| Scudo Fiscale | Il debito riduce le tasse: $(1-t)$ |

## 🔑 Regola: Il WACC come tasso di sconto
Il WACC è il tasso da usare per attualizzare i flussi di cassa di un progetto con lo stesso rischio dell'azienda. Se il progetto ha rischio diverso, bisogna stimare un beta specifico.

## 🔗 Collegato a
- [[Topic_6_Risk_and_Return]]
- [[Topic_5_NPV_Investment_Criteria]]
- [[Struttura_del_Capitale]]

## Fonti
* [[wiki/Fonti/Fonte_Corporate_Finance_Book.md]]
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
