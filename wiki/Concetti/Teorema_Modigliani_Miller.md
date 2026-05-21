---
tags: [concept, finance, theory]
source_count: 1
last_modified: 2026-05-05
---

# 📐 Modigliani-Miller Theorem

The **Modigliani-Miller Theorem** (1958) is one of the pillars of modern finance. It establishes the conditions under which [[Struttura_del_Capitale]] is irrelevant to firm value.

## Proposition I — Capital Structure Irrelevance

> *In a perfect market (no taxes, no bankruptcy costs, no information asymmetry), firm value is independent of its capital structure.*

```
V(levered) = V(unlevered)
```

The total value of the "pie" (firm) doesn't change by redistributing the slices between debt and equity.

## Proposition II — Cost of Equity and Leverage

> *The cost of equity increases linearly with the D/E ratio.*

```
Re = R₀ + (R₀ - Rd) × (D/E)
```

- **R₀** = cost of capital of the unlevered firm
- More debt → more risk for shareholders → equity becomes more expensive
- WACC remains constant (more expensive equity offsets cheaper debt)

## With Taxes (Corrected M&M)

Introducing corporate taxes:
```
V(levered) = V(unlevered) + Tc × D
```

- **Tc × D** = present value of the **tax shield**
- Implication: debt **creates value** → 100% debt structure would be optimal
- In reality, **distress costs** limit leverage

## Assumptions (Perfect Market)
1. No taxes
2. No transaction costs
3. No bankruptcy costs
4. Symmetric information
5. Individuals and firms can borrow at the same rate

## Practical Implications

Violations of these assumptions make capital structure relevant:
- **Taxes** → tax shield favors debt
- **Bankruptcy costs** → limit on leverage
- **Information asymmetry** → pecking order theory
- **Agency costs** → conflicts among shareholders, creditors, and managers ([[Corporate_Governance]])

## Connections
- Theoretical foundation of [[Struttura_del_Capitale]]
- Linked to [[Costo_del_Capitale]] (WACC)
- Its limitations explain optimal [[Leva_Finanziaria]]
- Authors: [[Franco_Modigliani]] and [[Merton_Miller]]

---
*Sources: [[Corporate_Finance]]*

## Fonti
* [[wiki/Fonti/Fonte_Corporate_Finance_Book.md]]
* [[wiki/Fonti/Fonte_Slides_Corporate_Finance.md]]
