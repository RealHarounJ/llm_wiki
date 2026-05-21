---
tags: [finanza, tvm, present-values, topic-4]
date_created: 2026-05-07
source: "raw/Teaching materials of Corporate Finance-20260505/Topic 4"
---

# ⏳ Topic 4 — Present Values & Time Value of Money

## 🎯 Il Principio Fondamentale
> **Un euro oggi vale più di un euro domani** perché può essere investito e produrre rendimento.

## 📐 Formule Essenziali

### Valore Attuale / Futuro (base)
$$PV = \frac{FV}{(1+r)^t} \qquad FV = PV \cdot (1+r)^t$$

### Rendita (Annuity) — flussi costanti per n periodi
$$PV_{annuity} = C \cdot \frac{1 - \frac{1}{(1+r)^n}}{r}$$

### Perpetuità — flussi costanti per sempre
$$PV_{perpetuity} = \frac{C}{r}$$

### Perpetuità Crescente — flussi che crescono al tasso g
$$PV_{growing\ perp.} = \frac{C_1}{r - g} \qquad \text{(con } r > g\text{)}$$

### Rendita Crescente (Growing Annuity)
$$PV_{growing\ ann.} = \frac{C_1}{r-g} \left[1 - \left(\frac{1+g}{1+r}\right)^n\right]$$

## 🔑 Regola d'Oro
Solo flussi allo **stesso momento temporale** possono essere sommati. Bisogna sempre attualizzare (portare al tempo 0) prima di sommare.

## 💡 Tasso Effettivo vs Nominale
$$r_{eff} = \left(1 + \frac{r_{nom}}{m}\right)^m - 1$$
dove m = numero di capitalizzazioni annue.

## 🔗 Collegato a
- [[Topic_5_NPV_Investment_Criteria]]
- [[Topic_7_8_CAPM_Cost_of_Capital]]
- [[Corporate_Finance_Hub]]

## Fonti
* [[wiki/Fonti/Fonte_Corporate_Finance_Book.md]]
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
