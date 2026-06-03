---
tags: [math, formulario, cheatsheet, exam-prep]
aliases: [Formulario, Math Cheatsheet]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 📋 Math Formulario — Complete Cheatsheet

> [!IMPORTANT]
> Everything on this page must be **memorized**. No calculator, no notes in the exam.

Back to [[Math_Home]]

---

## 🔢 Linear Algebra

```
det(2×2):  |a b|  = ad − bc
           |c d|

Inverse(2×2): A⁻¹ = (1/det) · |d  −b|
                               |−c   a|

Characteristic eq.: det(A − λI) = 0
Trace = sum of eigenvalues = Σ aᵢᵢ
det(A) = product of eigenvalues

Rouché-Capelli:
  r(A) = r(A|b)          → compatible
  r(A) = r(A|b) = n      → unique solution
  r(A) = r(A|b) < n      → ∞ solutions
  r(A) < r(A|b)          → inconsistent
```

---

## 📐 Derivatives

```
(c)' = 0                    (xⁿ)' = nxⁿ⁻¹
(eˣ)' = eˣ                 (aˣ)' = aˣ ln a
(ln x)' = 1/x              (logₐx)' = 1/(x ln a)
(sin x)' = cos x           (cos x)' = −sin x
(tan x)' = 1/cos²x         (cot x)' = −1/sin²x
(arcsin x)' = 1/√(1−x²)    (arccos x)' = −1/√(1−x²)
(arctan x)' = 1/(1+x²)

Product: (fg)' = f'g + fg'
Quotient: (f/g)' = (f'g − fg') / g²
Chain: (f(g))' = f'(g) · g'
```

---

## ∫ Integrals

```
∫xⁿ dx = xⁿ⁺¹/(n+1) + C       ∫1/x dx = ln|x| + C
∫eˣ dx = eˣ + C               ∫aˣ dx = aˣ/ln a + C
∫sin x dx = −cos x + C        ∫cos x dx = sin x + C
∫1/cos²x dx = tan x + C       ∫1/(1+x²) dx = arctan x + C
∫1/√(1−x²) dx = arcsin x + C  ∫ln x dx = x ln x − x + C

Integration by Parts: ∫u v' = uv − ∫u'v
LIATE: Log > Inv.trig > Algebra > Trig > Exp

Fundamental Theorem: ∫ₐᵇ f(x)dx = F(b) − F(a)

Improper: ∫₁^∞ 1/xᵖ  converges iff p > 1
```

---

## 🗺️ Functions of Two Variables

```
Critical points: fₓ = 0  AND  fᵧ = 0

Hessian:  H = |fₓₓ  fₓᵧ|      det(H) = fₓₓ·fᵧᵧ − fₓᵧ²
              |fᵧₓ  fᵧᵧ|

det(H) > 0, fₓₓ > 0  →  local MINIMUM
det(H) > 0, fₓₓ < 0  →  local MAXIMUM
det(H) < 0            →  SADDLE point
det(H) = 0            →  inconclusive

Lagrange: ∇f = λ∇g  +  g(x,y) = 0
  ∂f/∂x = λ·∂g/∂x
  ∂f/∂y = λ·∂g/∂y
  g(x,y) = 0
```

---

## 📈 Standard Limits

```
lim(x→0) sin(x)/x = 1
lim(x→0) (1 − cos x)/x² = 1/2
lim(x→0) (eˣ − 1)/x = 1
lim(x→0) ln(1+x)/x = 1
lim(x→∞) (1 + 1/x)ˣ = e
lim(x→∞) xⁿ/eˣ = 0    ∀n
lim(x→∞) ln(x)/xⁿ = 0  ∀n > 0
lim(x→0⁺) x·ln(x) = 0
```

---

## 🎯 Asymptotes

```
Vertical (x = a):    lim(x→a±) f(x) = ±∞
Horizontal (y = L):  lim(x→±∞) f(x) = L
Oblique (y = mx+q):  m = lim f(x)/x,   q = lim [f(x) − mx]
```

---

## 🔑 Key Inequalities & Facts

```
|sin x| ≤ 1,  |cos x| ≤ 1
eˣ > 0 for all x
ln x defined only for x > 0
√x defined only for x ≥ 0
x² ≥ 0 for all x  (equality at x = 0)
AM-GM: (a+b)/2 ≥ √(ab) for a,b ≥ 0
```
