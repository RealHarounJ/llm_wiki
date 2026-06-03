---
tags: [math, integrals, integration, exam-prep, analysis, definite, improper, area]
aliases: [Integrali, Integration]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# ∫ Integrals (Module 8 + Ex9)
> [!NOTE]
> Back to [[Math_Home]] | Prof. Riccardo De Blasis — Marche Polytechnic University

---

## 1. Indefinite Integrals — Basic Formulas

| Function | Integral |
|:---|:---|
| xⁿ (n ≠ −1) | xⁿ⁺¹/(n+1) + C |
| x⁻¹ = 1/x | ln\|x\| + C |
| eˣ | eˣ + C |
| eᵏˣ | eᵏˣ/k + C |
| aˣ | aˣ/ln(a) + C |
| sin x | −cos x + C |
| cos x | sin x + C |
| 1/cos²x | tan x + C |
| 1/sin²x | −cot x + C |
| 1/√(1−x²) | arcsin x + C |
| 1/(1+x²) | arctan x + C |
| ln x | x·ln(x) − x + C |

> [!TIP]
> **QuizA (all exams, Q8 and Q19):** ∫ 1/x dx = ln\|x\| + C and ∫ 1/x² dx = −x⁻¹ + C = −1/x + C

---

## 2. Integration Techniques (Ex9)

### A) Substitution (Change of Variable)
Use when you see f(g(x))·g'(x).

**Method:**
1. Set u = g(x)
2. Then du = g'(x) dx
3. Rewrite integral in terms of u
4. Integrate in u
5. Substitute back x

**Examples (Ex9):**
```
∫ 2x·e^(x²) dx
  u = x², du = 2x dx
  → ∫ eᵘ du = eᵘ + C = e^(x²) + C

∫ 3x²/(−2x³+1) dx
  u = −2x³+1, du = −6x²dx
  → −(1/2) ∫ du/u = −(1/2)ln|u| + C = −(1/2)ln|−2x³+1| + C

∫ x/(x²−5) dx
  u = x²−5, du = 2x dx
  → (1/2)∫ du/u = (1/2)ln|x²−5| + C

∫ (30x−12)/(5x²−4x+9) dx
  Numerator = 3·(10x−4) = 3·d/dx(5x²−4x+9)
  → 3·ln|5x²−4x+9| + C
```

**General pattern for ∫ g'(x)/g(x) dx:**
> = ln|g(x)| + C

**Pattern for ∫ (numerator is derivative of denominator) dx:**
> If numerator = k·d/dx(denominator), then result = k·ln|denominator| + C

### B) Inverse Substitution
From ∫ f(x)dx → ∫ f(g(t))·g'(t)dt with x = g(t)

**Examples (Ex9):**
```
∫ e^√x / √x dx
  x = t², dx = 2t dt, √x = t
  → ∫ eᵗ/t · 2t dt = 2∫ eᵗ dt = 2eᵗ + C = 2e^√x + C

∫ x√(1+x) dx
  t = 1+x, x = t−1, dx = dt
  → ∫ (t−1)√t dt = ∫(t^(3/2) − t^(1/2)) dt
  = (2/5)t^(5/2) − (2/3)t^(3/2) + C
  = (2/5)(1+x)^(5/2) − (2/3)(1+x)^(3/2) + C
```

---

### C) Integration by Parts
Use when you see a **product** of two functions.

**Formula:** ∫ f(x)·g'(x) dx = f(x)·g(x) − ∫ f'(x)·g(x) dx

**LIATE rule** — choose f (u) in this priority order:
1. **L**ogarithms
2. **I**nverse trig (arctan, arcsin...)
3. **A**lgebraic (polynomials xⁿ)
4. **T**rigonometric (sin, cos)
5. **E**xponential (eˣ)

**Immediate formulas (Ex9):**
```
∫ p(x)·eˣ dx = p(x)eˣ − ∫ p'(x)eˣ dx       [f=p(x), g'=eˣ]
∫ p(x)·ln x dx = P(x)ln x − ∫ P(x)/x dx     [f=lnx, g'=p(x)]
∫ φ(x) dx = x·φ(x) − ∫ x·φ'(x) dx
```

**Examples (Ex9):**
```
∫ x·eˣ dx
  f=x, g'=eˣ → f'=1, g=eˣ
  = x·eˣ − ∫ eˣ dx = x·eˣ − eˣ + C = eˣ(x−1) + C

∫ x·e^(3x) dx
  = (1/9)e^(3x)(3x−1) + C

∫ x·ln x dx
  f=lnx, g'=x → f'=1/x, g=x²/2
  = (x²/2)ln x − ∫ (x²/2)·(1/x) dx = (x²/2)ln x − x²/4 + C

∫ ln x dx
  f=lnx, g'=1 → f'=1/x, g=x
  = x·ln x − x + C

∫ x²·eˣ dx
  = eˣ(x²−2x+2) + C   [apply by parts twice]

∫ √x·ln x dx
  = (2/9)x^(3/2)(3ln x − 2) + C
```

**May 27, 2026 Exam (Q2):**
```
∫ log₂(x) dx = ∫ ln(x)/ln(2) dx = (1/ln 2)·∫ ln x dx
= (1/ln 2)·[x·ln x − x] + C = x·log₂(x) − x/ln(2) + C
```

---

### D) Partial Fractions
Use for rational functions P(x)/Q(x) where deg(P) < deg(Q).

**Step 1:** Factor the denominator Q(x)

**Step 2:** Decompose:
```
1/(x−a)(x−b) = A/(x−a) + B/(x−b)       [distinct real roots]
1/(x−a)²     = A/(x−a) + B/(x−a)²      [repeated root]
1/((x−a)(x²+bx+c)) = A/(x−a) + (Bx+C)/(x²+bx+c)  [irreducible quadratic]
```

**Step 3:** Multiply both sides by denominator and solve for A, B, C.

**Example:**
```
∫ 1/((x+1)(x−2)) dx

1 = A(x−2) + B(x+1)
x=2:  1 = 3B → B = 1/3
x=−1: 1 = −3A → A = −1/3

= (−1/3)ln|x+1| + (1/3)ln|x−2| + C = (1/3)ln|(x−2)/(x+1)| + C
```

---

## 3. Definite Integrals

### Fundamental Theorem of Calculus
If F'(x) = f(x), then:
> ∫ₐᵇ f(x) dx = F(b) − F(a) = F(x)|ₐᵇ

### Key Properties
```
∫ₐᵇ f(x) dx = −∫ᵦₐ f(x) dx
∫ₐᵃ f(x) dx = 0
∫ₐᵇ [f(x) + g(x)] dx = ∫ₐᵇ f + ∫ₐᵇ g
∫ₐᵇ c·f(x) dx = c·∫ₐᵇ f(x) dx
∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f  (additivity)
```

> [!IMPORTANT]
> **ODD FUNCTION TRICK (all QuizAs):** If f is odd (f(−x) = −f(x)), then ∫₋ₐᵃ f(x) dx = 0
> **Example:** ∫₋ₐᵃ x³ dx = 0 for any a. This appears in EVERY QuizA (Q14/Q6)!

### Worked Examples (Ex9)
```
∫₀² (x²−3x+1) dx = [x³/3 − 3x²/2 + x]₀² = (8/3 − 6 + 2) − 0 = −4/3

∫₀¹ (eˣ+e⁻ˣ) dx = [eˣ−e⁻ˣ]₀¹ = (e−1/e) − 0 = (e²−1)/e

∫₁⁴ (√x+1) dx = [2x^(3/2)/3 + x]₁⁴ = (16/3+4)−(2/3+1) = 23/3

∫₁² (x−1)³ dx = [(x−1)⁴/4]₁² = 1/4

∫₀^(1/2) e^(4x) dx = [e^(4x)/4]₀^(1/2) = (e²−1)/4
```

### Area Between Two Curves (Jan 22, 2026 — Q2)
Area between f(x) and g(x) from a to b:
> A = ∫ₐᵇ |f(x) − g(x)| dx

**Jan 22, 2026 Exam (Q2):**
```
Area between y² = 9x and x² = 9y
• From y² = 9x: y = 3√x (parabola opening right)
• From x² = 9y: y = x²/9 (parabola opening up)
• Intersection: 3√x = x²/9 → x=0, x=9
• A = ∫₀⁹ (3√x − x²/9) dx = [2x^(3/2) − x³/27]₀⁹ = 18 − 27 = ... 
  = 2·27 − 9³/27 = 54 − 27 = 27
```

---

## 4. Improper Integrals

### Type 1: Infinite Bounds
> ∫₁^∞ f(x) dx = lim(t→∞) ∫₁ᵗ f(x) dx

**Convergence test:** ∫₁^∞ 1/xᵖ dx
- Converges if **p > 1**
- Diverges if **p ≤ 1**

### Type 2: Discontinuity at Endpoint
> ∫ₐᵇ f(x) dx where f(a) = ∞ → lim(ε→0⁺) ∫ₐ₊ₑᵇ f(x) dx

---

## 🏆 Exam Strategy for Integrals

```
Given ∫ f(x) dx:

Step 1: Is it a basic form? → Direct formula
Step 2: Does denominator = derivative of numerator (or proportional)? → ln rule
Step 3: Is there a composite f(g(x))·g'(x)? → Substitution
Step 4: Is it a product of functions? → Integration by parts (LIATE)
Step 5: Is it rational P(x)/Q(x)? → Partial fractions
Step 6: Trigonometric? → Trig identities first
```

> [!TIP]
> Always check your answer by **differentiating** the result — it should give back the integrand!

---

## 📝 Typical Exam Exercises

| Exercise | Technique | Result |
|:---|:---|:---|
| ∫ x·eˣ dx | By parts (f=x, g'=eˣ) | eˣ(x−1) + C |
| ∫ ln x dx | By parts (f=lnx, g'=1) | x·ln(x) − x + C |
| ∫ x²·ln x dx | By parts (f=lnx, g'=x²) | (x³/3)·ln x − x³/9 + C |
| ∫ 1/(x²−1) dx | Partial fractions | (1/2)ln\|(x−1)/(x+1)\| + C |
| ∫₀¹ x·eˣ dx | By parts + evaluate | eˣ(x−1)\|₀¹ = 0−(−1) = 1 |
| ∫₋ₐᵃ x³ dx | Odd function | 0 |
| ∫ x/(x²−5) dx | Substitution | (1/2)ln\|x²−5\| + C |
| ∫ log₂(x) dx | By parts | x·log₂(x) − x/ln2 + C |

---

*Fonti: → [[Math_Home]] | [[Math_Formulario]] | Module8, Ex9, Exam Jan22/Feb4/May27*
