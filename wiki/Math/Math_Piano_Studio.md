---
tags: [math, study-plan, exam-prep, schedule]
aliases: [Piano di Studio, Study Plan]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 🗓️ Study Plan — From Zero to 30/30

> [!IMPORTANT]
> **Starting point:** Long time without math — need full refresh from basics.
> **Target:** 30/30 on written exam (5 exercises in 60 min) + pass multiple choice.
> **Strategy:** Learn each topic → practice exercises → drill past exam questions.

Back to [[Math_Home]] | 🗺️ Vai alla mappa stile Duolingo: **[[Percorso_Studio_Matematica]]**

---

## 🧭 Learning Path (in order)

```
PHASE 0: Foundations (non-negotiable base)
  └── Algebra, fractions, inequalities, exponentials, logarithms

PHASE 1: Linear Algebra
  └── Vectors → Matrices → Determinants → Linear Systems → Eigenvalues

PHASE 2: Functions & Limits
  └── Domain → Graph types → Limits → Continuity

PHASE 3: Derivatives
  └── Rules → Monotonicity → Extrema → Convexity → Full function study

PHASE 4: Integrals
  └── Antiderivatives → Substitution → By Parts → Partial Fractions → Definite

PHASE 5: Two-Variable Functions
  └── Domain in ℝ² → Partial derivatives → Hessian → Lagrange

PHASE 6: Exam Drilling
  └── Solve all 4 past exams under timed conditions
```

---

## 📘 PHASE 0 — Foundations (Start HERE)

> If these aren't solid, everything else breaks.

### What you need to remember cold:

**Fractions & Algebra**
- a/b + c/d = (ad + bc)/bd
- (a+b)² = a² + 2ab + b²
- (a−b)² = a² − 2ab + b²
- (a+b)(a−b) = a² − b²
- a³ − b³ = (a−b)(a² + ab + b²)

**Solving equations:**
- Linear: ax + b = 0 → x = −b/a
- Quadratic: ax² + bx + c = 0 → x = (−b ± √(b²−4ac)) / 2a
- Discriminant Δ = b²−4ac: Δ>0 two roots, Δ=0 one root, Δ<0 no real roots

**Inequalities — Sign Rules:**
- ab > 0 ↔ same sign (both + or both −)
- ab < 0 ↔ opposite signs
- Always: flip inequality when multiplying by NEGATIVE number

**Powers & Roots:**
- aᵐ · aⁿ = aᵐ⁺ⁿ
- aᵐ / aⁿ = aᵐ⁻ⁿ
- (aᵐ)ⁿ = aᵐⁿ
- a⁰ = 1 (for a ≠ 0)
- a⁻ⁿ = 1/aⁿ
- √a · √b = √(ab)
- ⁿ√(aᵐ) = aᵐ/ⁿ

**Logarithms (CRITICAL — appears in almost every exam):**
- log(ab) = log(a) + log(b)
- log(a/b) = log(a) − log(b)
- log(aⁿ) = n·log(a)
- logₐ(a) = 1
- logₐ(1) = 0
- ln(eˣ) = x
- e^(ln x) = x
- log → defined only for POSITIVE argument

**Exponentials:**
- eˣ > 0 always
- eˣ is always increasing
- e⁰ = 1, e¹ = e ≈ 2.718

**Trigonometry (basic):**
- sin²x + cos²x = 1
- sin(0)=0, cos(0)=1, sin(π/2)=1, cos(π/2)=0
- tan(x) = sin(x)/cos(x)

---

## 📗 PHASE 1 — Linear Algebra
→ [[Math_Algebra_Lineare]]

**Learn in this order:**
1. **Vectors:** operations, dot product, norm, linear independence
2. **Matrices:** types, operations (sum, product, transpose)
3. **Determinants:** 2×2 formula, 3×3 Sarrus, cofactor expansion, properties
4. **Inverse matrix:** condition (det ≠ 0), formula for 2×2
5. **Linear systems:** Gaussian elimination, Rouché-Capelli theorem
6. **Parametric systems:** discuss cases by parameter → EXAM STAPLE (Q5)
7. **Eigenvalues:** characteristic equation, eigenvectors

**Practice:** Ex1, Ex2, Ex3

**Exam connection:** Q5 is ALWAYS a parametric linear system

---

## 📙 PHASE 2 — Functions & Limits
→ [[Math_Studio_Funzioni]]

**Learn in this order:**
1. **Functions:** domain, range, injective/surjective
2. **Standard functions:** polynomial, rational, √, exp, log, trig, absolute value
3. **Domain:** how to compute for each function type
4. **Limits:** informal concept → formal definition → computation
5. **Standard limits** to memorize (sin x/x=1, etc.)
6. **L'Hôpital's rule:** for 0/0 or ∞/∞ forms
7. **Asymptotes:** vertical, horizontal, oblique

**Practice:** Ex4, Ex5

---

## 📒 PHASE 3 — Derivatives
→ [[Math_Studio_Funzioni]] (sections 3–5)

**Learn in this order:**
1. **Derivative definition:** tangent line, rate of change
2. **Derivative rules:** power, product, quotient, chain rule
3. **Standard derivatives:** memorize the table
4. **Monotonicity:** f' > 0 increasing, f' < 0 decreasing
5. **Critical points:** f'(x) = 0 → classify as max/min/neither
6. **Second derivative:** convex/concave, inflection points
7. **Full function study:** domain → limits → f' → f'' → graph

**Practice:** Ex6, Ex7, Ex8

**Exam connection:** Q1 is ALWAYS a full function study

---

## 📕 PHASE 4 — Integrals
→ [[Math_Integrali]]

**Learn in this order:**
1. **Antiderivative concept:** reverse of derivative
2. **Basic integral table:** memorize
3. **Substitution method:** u-substitution
4. **Integration by parts:** LIATE rule
5. **Partial fractions:** rational functions
6. **Definite integrals:** Fundamental Theorem of Calculus
7. **Area between curves:** |f − g| integrated
8. **Improper integrals:** infinite bounds

**Practice:** Ex9

**Exam connection:** Q2 is ALWAYS an integral (often by parts or substitution)

---

## 📔 PHASE 5 — Two-Variable Functions
→ [[Math_Funzioni_Due_Variabili]]

**Learn in this order:**
1. **Domain in ℝ²:** combine conditions in 2D
2. **Partial derivatives:** ∂f/∂x and ∂f/∂y
3. **Gradient:** ∇f = (fₓ, fᵧ)
4. **Critical points:** solve fₓ = 0, fᵧ = 0 simultaneously
5. **Hessian matrix:** compute det(H), classify min/max/saddle
6. **Level curves:** f(x,y) = c → draw curves in xy-plane
7. **Lagrange multipliers:** constrained optimization

**Practice:** Ex10

**Exam connection:** Q3/Q4 are ALWAYS 2-variable functions

---

## 🎯 PHASE 6 — Exam Drilling
→ [[Math_Esami_Passati]]

**Solve these in order, timed:**
1. Exam 9 Jan 2025 (oldest — warmup)
2. Exam 22 Jan 2026
3. Exam 4 Feb 2026
4. Exam 27 May 2026 ← **most recent, most representative**

**Rule:** Solve under real exam conditions (no notes, 60 min timer).
Then review mistakes → go back to relevant phase.

---

## ⚡ Priority Matrix — What Gives Most Points

| Topic | Exam Weight | Difficulty | Priority |
|:------|:-----------|:-----------|:---------|
| Study of function (Q1) | ~25% | Medium-High | ⭐⭐⭐⭐⭐ |
| Linear system with param (Q5) | ~20% | Medium | ⭐⭐⭐⭐⭐ |
| 2-var critical points (Q4) | ~20% | Medium | ⭐⭐⭐⭐ |
| Integrals (Q2) | ~20% | Medium-High | ⭐⭐⭐⭐ |
| 2-var domain (Q3) | ~15% | Low-Medium | ⭐⭐⭐ |

---

## 📌 Daily Session Structure (recommended)

```
Session (2-3 hours):
  [20 min] Review theory from wiki
  [60 min] Solve exercises from Ex PDF
  [30 min] Solve one question from a past exam
  [10 min] Write down what was hard → review tomorrow
```
