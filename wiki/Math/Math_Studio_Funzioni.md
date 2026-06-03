---
tags: [math, functions, derivatives, limits, continuity, exam-prep, analysis, taylor]
aliases: [Studio delle Funzioni, Function Analysis]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 📈 Study of Functions (Single Variable)
> [!NOTE]
> Back to [[Math_Home]] | Prof. Riccardo De Blasis — Marche Polytechnic University

---

## Complete Checklist — Full Function Analysis (Exam Template)

- [ ] 1. **Domain** — find where f(x) is defined
- [ ] 2. **Sign** — where f > 0, f < 0
- [ ] 3. **Symmetry** — even/odd check: f(−x) = f(x) or −f(x)?
- [ ] 4. **Intercepts** — y-intercept f(0), x-intercepts f(x)=0
- [ ] 5. **Limits at boundaries** — asymptotes
- [ ] 6. **First derivative f'(x)** → monotonicity, local extrema
- [ ] 7. **Second derivative f''(x)** → convexity, inflection points
- [ ] 8. **Non-differentiability points** — check |f(x)| type functions ← **exam focus!**
- [ ] 9. **Sketch the graph**

---

## 1. Domain (Module 3)

The set of acceptable values for x where f(x) is defined.

| Condition | Restriction |
|:---|:---|
| Fraction | Denominator ≠ 0 |
| Even root √ | Argument ≥ 0 (strictly > 0 if also under log) |
| Logarithm ln/log | Argument > 0 |
| Arcsin/arccos | Argument ∈ [−1, 1] |

**Example (Module 3):**
```
f(x) = 1/√(3−x)  →  D: 3−x > 0  →  x < 3  →  D = (−∞, 3)
```

**Image/Range:** Im(f) = {y = f(x), ∀x ∈ A} ⊆ B

---

## 2. Limits & Asymptotes (Module 4)

### Standard Limits to Memorize
```
lim (x→0) sin(x)/x = 1               ← FUNDAMENTAL
lim (x→0) (1−cos x)/x² = 1/2
lim (x→0) (eˣ−1)/x = 1               ← FUNDAMENTAL
lim (x→0) ln(1+x)/x = 1              ← FUNDAMENTAL (appears in every QuizA!)
lim (x→∞) (1 + 1/x)ˣ = e
lim (x→∞) xⁿ/eˣ = 0   (exponential beats polynomial)
lim (x→∞) ln(x)/xⁿ = 0 (polynomial beats log)
lim (x→∞) aˣ/xᵏ = +∞  (a,k>1)      ← appears in every QuizA!
lim (x→∞) ln(1+x)/x = 0             ← appears in QuizA!
```

### L'Hôpital's Rule (Ex7)
Use when limit gives 0/0 or ∞/∞:
> lim f(x)/g(x) = lim f'(x)/g'(x)

**Examples (Ex7):**
```
lim(x→3) (3x²−27)/(x−3) = lim 6x/1 = 18
lim(x→4) (x²−16)/(x−4) = lim 2x/1 = 8
lim(x→1) (x−1)/(x²−1) = lim 1/(2x) = 1/2
lim(x→0) x·ln(x) = 0   (standard: 0⁺ × −∞)
lim(x→0+) x^(1/3)−1 → use L'Hôpital
```

### Types of Asymptotes

**Vertical asymptote** at x = a:
> lim(x→a⁺) f(x) = ±∞ or lim(x→a⁻) f(x) = ±∞

**Horizontal asymptote** y = L:
> lim(x→+∞) f(x) = L or lim(x→−∞) f(x) = L

**Oblique asymptote** y = mx + q:
> m = lim(x→∞) f(x)/x
> q = lim(x→∞) [f(x) − mx]
> (exists only if m ≠ 0 and both limits are finite)

---

## 3. Continuity (Module 5)

### Definition
f(x) is **continuous at x₀** if:
> lim(x→x₀) f(x) = f(x₀)

**Three conditions must hold simultaneously:**
1. f(x₀) is defined
2. lim(x→x₀) f(x) exists (left = right limits)
3. The limit equals f(x₀)

### Left/Right Continuity
- **Left continuous at x₀**: lim(x→x₀⁻) f(x) = f(x₀)
- **Right continuous at x₀**: lim(x→x₀⁺) f(x) = f(x₀)
- Continuous at x₀ ⟺ both left AND right continuous

### Types of Discontinuities
| Type | Condition |
|:---|:---|
| **Removable** | lim exists but ≠ f(x₀), or f not defined |
| **Jump** | Left limit ≠ right limit (both finite) |
| **Essential** | At least one side limit is ±∞ |

> [!IMPORTANT]
> **Classic exam question:** f(x) = (x²−1)/(x−1) has a **removable discontinuity** at x=1. Set f(1)=2 to make it continuous.

### Theorems (Module 5)
- **Weierstrass Theorem**: A continuous function on [a,b] attains both its **maximum and minimum** values.
- **Intermediate Value Theorem (Bolzano)**: If f continuous on [a,b] and f(a)·f(b) < 0, then ∃c ∈ (a,b) with f(c) = 0.

---

## 4. Derivatives — Rules (Module 6)

### Definition
The **derivative** of f at point c:
> f'(c) = lim(h→0) [f(c+h) − f(c)] / h

**Average rate of change:** Δf/h = [f(c+h) − f(c)] / h

### Differentiation Rules
| Rule | Formula |
|:---|:---|
| Constant | (c)' = 0 |
| Power | (xⁿ)' = nxⁿ⁻¹ |
| Sum | (f+g)' = f' + g' |
| Product | (fg)' = f'g + fg' |
| Quotient | (f/g)' = (f'g − fg') / g² |
| Chain | (f(g(x)))' = f'(g(x)) · g'(x) |

### Standard Derivatives to Memorize
```
(eˣ)' = eˣ
(aˣ)' = aˣ · ln(a)
(ln x)' = 1/x
(logₐx)' = 1/(x·ln a)
(sin x)' = cos x
(cos x)' = −sin x
(tan x)' = 1/cos²x = sec²x
(arcsin x)' = 1/√(1−x²)
(arccos x)' = −1/√(1−x²)
(arctan x)' = 1/(1+x²)
```

### Worked Derivative Examples (Ex6)
```
y = eˣ/(1+eˣ)     → y' = eˣ/(1+eˣ)²
y = ex(x+1)        → y' = eˣ(x+2)
f(x) = ln(3x²+1)  → f'(x) = 6x/(3x²+1)
f(x) = e^(x²)     → f'(x) = 2x·e^(x²)
f(x) = √(ln x)    → f'(x) = 1/(2x√(ln x))
f(x) = eˣ(3x²−5x+1)·ln(x+1) → use product + chain rule
```

### Non-differentiability Points
At a point x₀ where f is piecewise (like |g(x)|):
1. Check continuity at x₀
2. Compute left and right derivatives:
   - **Right derivative**: lim(h→0⁺) [f(x₀+h)−f(x₀)]/h
   - **Left derivative**: lim(h→0⁻) [f(x₀+h)−f(x₀)]/h
3. If left ≠ right → **non-differentiable (angular point)**

> [!IMPORTANT]
> **Exam focus (Jan 9, 2026; Feb 4, 2026; May 27, 2026):** Every written exam asks to "check for non-differentiability points." This always involves an absolute value or piecewise definition. Always do this!

---

## 5. Monotonicity & Extrema (Module 7)

### Method (Ex8)
1. Compute f'(x)
2. Find critical points: f'(x) = 0 or f'(x) undefined
3. Study the sign of f'(x):
   - f' > 0 → f **increasing** ↗
   - f' < 0 → f **decreasing** ↘
4. At critical point x₀:
   - f' changes + → − : **local maximum**
   - f' changes − → + : **local minimum**
   - f' doesn't change sign: **neither** (possible inflection)

### Second Derivative Test (alternative)
At critical point x₀ where f'(x₀) = 0:
- f''(x₀) > 0 → **local minimum** (∪ shape)
- f''(x₀) < 0 → **local maximum** (∩ shape)
- f''(x₀) = 0 → inconclusive → use first derivative test

### Worked Examples (Ex8)
```
f(x) = ln(x−2)/(x−2)
Domain: D = (2, +∞)
f'(x) = [1 − ln(x−2)] / (x−2)²
f'(x) > 0 ⟺ 1 > ln(x−2) ⟺ x < e+2
→ Increasing on (2, e+2), decreasing on (e+2, +∞)
→ Global maximum at x = e+2: f(e+2) = 1/e

f(x) = (x+1)eˣ
f'(x) = eˣ + eˣ(x+1) = eˣ(x+2)
f'(x) > 0 ⟺ x > −2
→ Increasing on (−2, +∞), decreasing on (−∞, −2)
→ Global minimum at x=−2: f(−2) = −1/e²
```

---

## 6. Convexity & Inflection Points

1. Compute f''(x)
2. Study sign of f''(x):
   - f'' > 0 → **convex** (concave up) ∪
   - f'' < 0 → **concave** (concave down) ∩
3. **Inflection point**: where f'' changes sign
   - Necessary: f''(x₀) = 0 (but NOT sufficient)

---

## 7. Even / Odd Functions

| Type | Condition | Graph Symmetry |
|:---|:---|:---|
| **Even** | f(−x) = f(x) | Symmetric about y-axis |
| **Odd** | f(−x) = −f(x) | Symmetric about origin |

**Examples:**
- f(x) = x² → even (f(−x) = x² = f(x))
- f(x) = x³ → odd (f(−x) = −x³ = −f(x))
- f(x) = x⁴−1 → even
- f(x) = |x| → even (NOT odd!)

---

## 8. Taylor Polynomial (Ex7)

The Taylor polynomial of degree n at x₀:
```
T_n(x) = f(x₀) + f'(x₀)(x−x₀) + f''(x₀)/2!(x−x₀)² + ... + f^(n)(x₀)/n!(x−x₀)ⁿ
```

**Key Taylor expansions at x₀ = 0:**
```
eˣ ≈ 1 + x + x²/2 + x³/6 + ...       ← 2nd order: 1 + x + x²/2
sin x ≈ x − x³/6 + ...
cos x ≈ 1 − x²/2 + x⁴/24 + ...
ln(1+x) ≈ x − x²/2 + x³/3 − ...
(1+x)ᵅ ≈ 1 + αx + α(α−1)/2 · x² + ...
```

> [!TIP]
> **QuizA (Jan 22, 2026, Q7):** "Second-order Taylor polynomial of eˣ at 0" = **1 + x + x²/2** ✓

---

## 🏆 Standard Exam Sequence

Given f(x), perform the full analysis:

```
1. Dom(f) = ...
2. Sign: f(x) > 0 when ..., f(x) = 0 at x = ...
3. Symmetry: f(−x) = ... → even/odd/neither
4. y-intercept: f(0) = ..., x-intercept: f(x) = 0 → x = ...
5. lim(x→∓∞) f(x) = ... → horizontal asymptote y = ...
   lim(x→a±) f(x) = ±∞ → vertical asymptote x = a
   If lim f(x)/x = m ≠ 0 → oblique asymptote y = mx+q
6. f'(x) = ...
   f'(x) = 0 → x = ...
   Sign of f': (+) on (...), (−) on (...)
   Local max at x = ..., f = ...
   Local min at x = ..., f = ...
7. f''(x) = ...
   f''(x) = 0 → x = ...
   Convex on ..., Concave on ...
   Inflection at x = ...
8. Non-differentiability check (for |...| or piecewise)
9. Sketch ✏️
```

---

## 📝 Real Exam Written Questions (Function Study)

### Jan 9, 2025 (Q1):
```
f(x) = eˣ|1−2x|
• Domain: ℝ
• Non-differentiable at x = 1/2 (absolute value corner)
• Left derivative at 1/2 ≠ right derivative at 1/2
```

### Jan 22, 2026 (Q1):
```
f(x) = e^(−x) · √(x−1)
• Domain: x ≥ 1 (i.e., [1, +∞))
• Check non-differentiability at x = 1 (√ has vertical tangent at endpoint)
• f'(x) = −e^(−x)√(x−1) + e^(−x)/(2√(x−1))
```

### Feb 4, 2026 (Q1):
```
f(x) = x·e^(−x/2)
• Domain: ℝ
• f'(x) = e^(−x/2) − (x/2)e^(−x/2) = e^(−x/2)(1 − x/2)
• Critical point: x = 2 → local max f(2) = 2/e
• f''(x) = e^(−x/2)(x/4 − 1)
• Inflection at x = 4
```

### May 27, 2026 (Q1):
```
f(x) = x²·e^(−1/x)    [careful: undefined at x=0]
• Domain: ℝ \ {0}
• Check behavior at x = 0⁺ and x = 0⁻
• Non-differentiability? Check corner/cusp at domain boundary
```

---

*Fonti: → [[Math_Home]] | [[Math_Formulario]] | Module3, Module4, Module5, Module6, Module7, Ex4–Ex8*
