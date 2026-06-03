---
tags: [math, exercises, exam-prep, worked-solutions]
aliases: [Esercizi Tipo, Typical Exercises]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 📝 Typical Exam Exercises — Worked Solutions

> [!IMPORTANT]
> These are extracted directly from the official exercise sheets (Ex1–Ex10) and past exams.
> Master these → you will recognize every question on the real exam.

Back to [[Math_Home]] | [[Math_Esami_Passati]]

---

## 🔢 TOPIC 1 — Linear Systems with Parameters (Q5 in every exam)

### Pattern: Discuss and solve as parameter varies

**Exercise (from Ex3):**
Solve the system as k ∈ ℝ varies:
```
kx + y       = 1
x  + y + (1−k)z = k
     y + z   = 1
```
**Method:**
1. Write augmented matrix [A|b]
2. Compute det(A) = k³ − 3k + 2 = (k−1)²(k+2)
3. Cases:
   - k ≠ 1, −2 → rank = 3 → **unique solution**
   - k = 1 → rank < 3 → **infinite solutions** (find them)
   - k = −2 → rank(A) < rank(A|b) → **no solution**

> [!TIP]
> Always factorize det(A) completely. The roots give the critical values of k.

---

**Exercise (from Exam 27 May 2026):**
```
−x + ky + kz = 1
−kx + y + z = 2+k
```
**Approach:** 2 equations, 3 unknowns → always ∞ solutions unless inconsistent. Compute rank of [A|b] for each k.

---

### Practice Problems (from Ex3):
1. Solve: `kx + y = 1; 4x + ky = 2k` → Solution: k=2: ∞¹; k=−2: impossible; else unique
2. Solve: `x − x₂ = 3; 2x₁ − 2x₂ = k` → k≠6: no solution; k=6: ∞¹ solutions
3. Solve: `x₁ − 3x₂ = 1; 2x₁ − hx₂ = k` → h=6,k≠2: no sol; h≠6: unique; h=6,k=2: ∞¹

---

## 📈 TOPIC 2 — Study of Function (Q1 in every exam)

### Pattern: Always `eˣ × something` or `ln × something`

**Exercise (from Exam 4 Feb 2026):** Study `f(x) = x·e^(−x/2)`

```
Step 1 — Domain: D = ℝ (no restrictions)

Step 2 — Sign: x·e^(−x/2) > 0 ↔ x > 0

Step 3 — Intercepts: f(0) = 0; f(x)=0 → x = 0

Step 4 — Limits:
  lim(x→+∞) x·e^(−x/2) = 0  [exp beats polynomial]
  lim(x→−∞) x·e^(−x/2) = −∞
  → Horizontal asymptote: y = 0 as x→+∞

Step 5 — First derivative:
  f'(x) = e^(−x/2) + x·(−1/2)·e^(−x/2) = e^(−x/2)·(1 − x/2)
  f'(x) = 0 → 1 − x/2 = 0 → x = 2
  f'(x) > 0 for x < 2 (increasing)
  f'(x) < 0 for x > 2 (decreasing)
  → LOCAL MAXIMUM at x=2: f(2) = 2·e^(−1) = 2/e

Step 6 — Second derivative:
  f''(x) = e^(−x/2)·(−1/2)·(1−x/2) + e^(−x/2)·(−1/2)
         = e^(−x/2)·(x/4 − 1)
  f''(x) = 0 → x = 4
  f''(x) < 0 for x < 4 (concave)
  f''(x) > 0 for x > 4 (convex)
  → INFLECTION POINT at x=4: f(4) = 4·e^(−2)

Step 7 — Non-differentiability: none (eˣ and polynomials are C∞)
```

---

**Exercise (from Ex8 — Monotonicity):** Study `f(x) = ln(x−2)/(x−2)`
```
Domain: D = (2, +∞)
f'(x) = [1/(x−2)·(x−2) − ln(x−2)] / (x−2)²
       = [1 − ln(x−2)] / (x−2)²

f'(x) > 0 ↔ 1 > ln(x−2) ↔ x−2 < e ↔ x < e+2
→ Increasing on (2, e+2), Decreasing on (e+2, +∞)
→ Global max at x = e+2: f(e+2) = 1/e
```

---

## ∫ TOPIC 3 — Integrals (Q2 in every exam)

### Integration by Parts Examples

**Exercise:** `∫ log²(x) dx` (from Exam 27 May 2026)
```
u = log²(x)    →  u' = 2·log(x)/x
v' = 1          →  v = x

= x·log²(x) − ∫ x · 2·log(x)/x dx
= x·log²(x) − 2∫ log(x) dx

Now ∫ log(x) dx = x·log(x) − x  [standard result]

= x·log²(x) − 2[x·log(x) − x] + C
= x·log²(x) − 2x·log(x) + 2x + C
```

**Exercise:** `∫₋₁⁰ (2x+1)/(x+2) dx` (from Exam 9 Jan 2025)
```
Polynomial division: (2x+1)/(x+2) = 2 − 3/(x+2)

∫₋₁⁰ [2 − 3/(x+2)] dx = [2x − 3·ln|x+2|]₋₁⁰
= [0 − 3·ln2] − [−2 − 3·ln1]
= −3·ln2 + 2
```

**Exercise (Substitution):** `∫ (x + 4√x)/(3x + √x) dx` (Exam 4 Feb 2026)
```
Let u = √x → x = u², dx = 2u du

= ∫ (u² + 4u)/(3u² + u) · 2u du
= ∫ 2u(u+4) / (u(3u+1)) du
= ∫ 2(u+4)/(3u+1) du

Polynomial division: 2(u+4)/(3u+1) = 2/3 + (22/3)/(3u+1)

= (2/3)u + (22/9)·ln|3u+1| + C
= (2/3)√x + (22/9)·ln|3√x+1| + C
```

---

### Area Between Curves (from Exam 22 Jan 2026)

**Exercise:** Area between `y² = 9x` and `x² = 9y`
```
Intersections: substitute y = x²/9 into y² = 9x
→ x⁴/81 = 9x → x⁴ = 729x → x(x³−729) = 0
→ x = 0 and x = 9

On [0,9]: upper curve = 3√x (from y²=9x), lower = x²/9

Area = ∫₀⁹ (3√x − x²/9) dx
     = [2x^(3/2) − x³/27]₀⁹
     = [2·27 − 729/27] − 0
     = 54 − 27 = 27
```

---

## 🗺️ TOPIC 4 — Two-Variable Functions (Q3/Q4 in every exam)

### Domain in ℝ² Examples

**Exercise (Exam 27 May 2026):** `f(x,y) = 1/√(x−1) + log(y)`
```
Conditions:
1. x − 1 > 0  →  x > 1         [denominator of √ must be > 0]
2. y > 0                         [argument of log must be > 0]

Domain: {(x,y) ∈ ℝ² : x > 1 AND y > 0}
→ Open half-plane x>1 intersected with upper half-plane y>0
→ First quadrant region to the right of x=1
```

**Exercise (Exam 4 Feb 2026):** `f(x,y) = √(x² − 2y)`
```
Condition: x² − 2y ≥ 0 → y ≤ x²/2
Domain: region ON and BELOW the parabola y = x²/2
```

---

### Critical Points + Hessian Examples

**Exercise (Exam 27 May 2026):** Find critical points of `f(x,y) = x²y + x² − 2y`
```
∂f/∂x = 2xy + 2x = 2x(y+1) = 0  →  x=0  OR  y=−1
∂f/∂y = x² − 2 = 0              →  x²=2  →  x=±√2

Critical points from system:
- If x=0: from ∂f/∂y=0 → 0−2=−2≠0 → NO solution with x=0
- If y=−1: from ∂f/∂y=0 → x²=2 → x=±√2

Critical points: (√2, −1) and (−√2, −1)

Hessian:
fₓₓ = 2y+2,  fᵧᵧ = 0,  fₓᵧ = 2x

At (√2, −1): fₓₓ = 0, fᵧᵧ = 0, fₓᵧ = 2√2
  det(H) = 0·0 − (2√2)² = −8 < 0  → SADDLE POINT

At (−√2, −1): fₓₓ = 0, fᵧᵧ = 0, fₓᵧ = −2√2
  det(H) = 0·0 − (−2√2)² = −8 < 0 → SADDLE POINT
```

---

## 🔑 Determinants — Quick Practice

**2×2:**
```
|2  3|  = 2·1 − 3·4 = 2 − 12 = −10
|4  1|
```

**3×3 Sarrus:**
```
|1  2  3|
|4  5  6| = 1·5·9+2·6·7+3·4·8 − 3·5·7−2·4·9−1·6·8
|7  8  9|  = 45+84+96 − 105−72−48 = 225−225 = 0
```
*(This matrix has det=0 → rank < 3)*

---

*Back to [[Math_Home]] | [[Math_Esami_Passati]] | [[Math_Formulario]]*
