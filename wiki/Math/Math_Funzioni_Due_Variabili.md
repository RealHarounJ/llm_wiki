---
tags: [math, multivariable, partial-derivatives, hessian, lagrange, exam-prep, gradient, domain-2d]
aliases: [Funzioni di Due Variabili, Multivariable Functions]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 🗺️ Functions of Two Variables (Module 9 + Ex10)
> [!NOTE]
> Back to [[Math_Home]] | Prof. Riccardo De Blasis — Marche Polytechnic University

---

## 1. Domain in ℝ²

Same rules as 1-variable, applied to both x and y **simultaneously**.

| Condition | Restriction |
|:---|:---|
| Under square root | expression ≥ 0 (or > 0 if also under log) |
| Log / ln | argument > 0 |
| Denominator | ≠ 0 |

**Example (May 27, 2026 Q3):**
```
f(x,y) = 1/√(x−1) + log(y)

Conditions:
1. x − 1 > 0  →  x > 1
2. y > 0

Dom(f) = {(x,y) ∈ ℝ² : x > 1 AND y > 0}
= (1,+∞) × (0,+∞)  [open first quadrant, shifted]
```

**Example (Ex10 + Jan 9, 2025 Q3):**
```
f(x,y) = ln(1−x²−y²)

Conditions:
1 − x² − y² > 0  →  x² + y² < 1

Dom(f) = {(x,y) : x² + y² < 1}  = open unit disk
```

**Example (Feb 4, 2026 Q3):**
```
f(x,y) = √(x² − 2y)

Conditions: x² − 2y ≥ 0  →  y ≤ x²/2

Dom(f) = {(x,y) : y ≤ x²/2}  [at or below parabola y = x²/2]
```

**Example (Ex10):**
```
f(x,y) = ln(x−3y)
Dom(f) = {(x,y) : x − 3y > 0}  = half-plane above line x = 3y
```

> [!TIP]
> **Drawing the domain:** Sketch the boundary curve (equality), then shade the feasible region. Solid line = boundary included (≥), dashed line = excluded (>).

### Level Curves
Level curves of f(x,y) = c: set f(x,y) = c and sketch the resulting curve.
- f(x,y) = x² + y² → level curves are **circles** centered at origin
- f(x,y) = x + y → level curves are **lines**

---

## 2. Partial Derivatives (Ex10)

### Definition
- **∂f/∂x** = fₓ: differentiate w.r.t. x, treating **y as a constant**
- **∂f/∂y** = fᵧ: differentiate w.r.t. y, treating **x as a constant**

### Examples (Ex10)
```
f(x,y) = x² + y²
  fₓ = 2x,  fᵧ = 2y

f(x,y) = x²y² + 9
  fₓ = 2xy², fᵧ = 2x²y

f(x,y) = x − log(10 + 4y²)
  fₓ = 1,    fᵧ = −8y/(10+4y²)

f(x,y) = y² − x·e^(10+2y)
  fₓ = −e^(10+2y),   fᵧ = 2y − 2x·e^(10+2y)

f(x,y) = x²y + x² − 2y      [May 27, 2026 Q4]
  fₓ = 2xy + 2x = 2x(y+1)
  fᵧ = x² − 2
```

---

## 3. Gradient

The **gradient** of f at point (x,y):
> ∇f(x,y) = (∂f/∂x , ∂f/∂y) = (fₓ, fᵧ)

- Points in the direction of **steepest ascent**
- ∇f = **0** at critical points

**Example (QuizA, all exams):**
```
f(x,y) = αx² + βy²
∇f(u,v) = (2αu, 2βv)

f(x,y) = x² + 2y²
∇f(0,0) = (0, 0)
∇f(2,2) = (4, 8)
```

---

## 4. Second-Order Partial Derivatives & Hessian Matrix (Ex10)

### Second Partial Derivatives
```
fₓₓ = ∂²f/∂x²      (diff fₓ w.r.t. x)
fᵧᵧ = ∂²f/∂y²      (diff fᵧ w.r.t. y)
fₓᵧ = ∂²f/∂x∂y     (diff fₓ w.r.t. y)
fᵧₓ = ∂²f/∂y∂x     (diff fᵧ w.r.t. x)
```

> [!TIP]
> **Schwarz's theorem:** If f is twice continuously differentiable, then **fₓᵧ = fᵧₓ**

### The Hessian Matrix
```
H(x,y) = |fₓₓ  fₓᵧ|
          |fᵧₓ  fᵧᵧ|

det(H) = fₓₓ · fᵧᵧ − (fₓᵧ)²
```

**Worked Examples (Ex10):**
```
f(x,y) = x²y² + 9
  fₓₓ = 2y², fᵧᵧ = 2x², fₓᵧ = 4xy
  H = |2y²  4xy|
      |4xy  2x²|
  det(H) = 4x²y² − 16x²y²= −12x²y²

f(x,y) = y² − x·e^(10+2y)
  fₓₓ = 0, fᵧᵧ = 2 − 4x·e^(10+2y), fₓᵧ = −2e^(10+2y)
  H = |0          −2e^(10+2y)    |
      |−2e^(10+2y) 2−4xe^(10+2y) |
```

---

## 5. Critical Points & Classification (Ex10)

### Step 1: Find Critical Points
Solve the **system**:
> ∂f/∂x = 0
> ∂f/∂y = 0

Simultaneously → gives candidate points (x₀, y₀)

### Step 2: Classify with Hessian

Compute **det(H)** at each critical point:

| Condition | Classification |
|:---|:---|
| det(H) > 0 AND fₓₓ > 0 | **Local MINIMUM** |
| det(H) > 0 AND fₓₓ < 0 | **Local MAXIMUM** |
| det(H) < 0 | **Saddle point** |
| det(H) = 0 | **Inconclusive** |

### Worked Examples (Ex10)

**Standard examples:**
```
f(x,y) = x² − y²
  fₓ = 2x = 0 → x=0; fᵧ = −2y = 0 → y=0
  Critical: (0,0). fₓₓ=2, fᵧᵧ=−2, fₓᵧ=0
  det(H) = 2·(−2) − 0 = −4 < 0 → SADDLE POINT

f(x,y) = −(x−4)² − y²
  fₓ = −2(x−4) = 0 → x=4; fᵧ = −2y = 0 → y=0
  Critical: (4,0). fₓₓ=−2, fᵧᵧ=−2, fₓᵧ=0
  det(H) = 4 > 0, fₓₓ < 0 → LOCAL MAXIMUM

f(x,y) = x³ + y³ + xy
  fₓ = 3x² + y = 0 → y = −3x²
  fᵧ = 3y² + x = 0 → x = −3y²
  Substituting: x = −3(−3x²)² = −27x⁴ → x=0 or x=−1/3
  Critical points: (0,0) and (−1/3, −1/3)
  (0,0): det(H) = 0·0 − 1 = −1 < 0 → SADDLE
  (−1/3,−1/3): det(H) = 9·(1/9)·9·(1/9) − 1 = 1−1=0... check carefully

f(x,y) = x·y·e^(−(x²+y²)/2)
  Critical points: (0,0) saddle; (1,1) and (−1,−1) local max; (1,−1) and (−1,1) local min
```

**May 27, 2026 Exam (Q4):**
```
f(x,y) = x²y + x² − 2y

fₓ = 2xy + 2x = 2x(y+1) = 0  →  x=0 or y=−1
fᵧ = x² − 2 = 0              →  x=±√2

Case 1: x=0 → from fᵧ: 0−2=−2≠0 → no critical point with x=0
Case 2: y=−1 → from fᵧ: x²=2 → x=±√2
Critical points: (√2, −1) and (−√2, −1)

fₓₓ = 2(y+1) = 2(−1+1) = 0
fᵧᵧ = 0
fₓᵧ = 2x

At (√2, −1): det(H) = 0·0 − (2√2)² = −8 < 0 → SADDLE POINT
At (−√2, −1): det(H) = 0·0 − (−2√2)² = −8 < 0 → SADDLE POINT
→ No local maxima or minima! All critical points are saddle points.
```

**Feb 4, 2026 Exam (Q4):**
```
f(x,y) = 2(y²+x²−2xy) − x⁴ − y⁴ + 15
       = 2y²+2x²−4xy − x⁴ − y⁴ + 15

fₓ = 4x − 4y − 4x³ = 4(x − y − x³) = 0
fᵧ = 4y − 4x − 4y³ = 4(y − x − y³) = 0
Adding: −4x³ − 4y³ = 0 → y = −x
Subst: x−(−x)−x³=0 → 2x−x³=0 → x(2−x²)=0 → x=0,±√2

Critical points: (0,0), (√2,−√2), (−√2,√2)
```

---

## 6. Constrained Optimization — Lagrange Multipliers (Ex10)

### Problem
Maximize/minimize f(x,y) subject to constraint g(x,y) = 0

### Method
Solve the system:
```
∇f = λ · ∇g

i.e.:
∂f/∂x = λ · ∂g/∂x
∂f/∂y = λ · ∂g/∂y
g(x,y) = 0          ← constraint equation
```
3 equations, 3 unknowns (x, y, λ).

Then evaluate f at all solutions and compare values.

### Worked Examples (Ex10)

```
f(x,y) = xy  subject to  x + y = 1  → g = x+y−1 = 0
fₓ = y = λ·1, fᵧ = x = λ·1 → x = y
Constraint: 2x=1 → x=y=1/2
Solution: (1/2, 1/2), f(1/2,1/2) = 1/4

f(x,y) = e^(−(x²+y²))  subject to  3x+4y = 25
fₓ = −2xe^(−(x²+y²)) = 3λ
fᵧ = −2ye^(−(x²+y²)) = 4λ
Dividing: y/x = 4/3 → y = 4x/3
3x + 4·(4x/3) = 25 → x=3, y=4
Solution: (3,4)

f(x,y) = x  subject to  x²+y² = 10   [Extreme Value Theorem]
fₓ = 1 = 2λx → λ = 1/(2x)
fᵧ = 0 = 2λy → y=0 (since λ≠0)
x² = 10 → x = ±√10
Max: (√10, 0) with f=√10; Min: (−√10, 0) with f=−√10

f(x,y) = x−y  subject to  x²+y² = 2
Solution: (1,−1) absolute max f=2; (−1,1) absolute min f=−2
```

### Constrained Optimization by Substitution
If g(x,y) = 0 can be solved for y = h(x), substitute and treat as 1-variable problem.

**Example (Ex10):**
```
Minimize f(x,y) = 3x²+y²−3x+4  subject to  2x+y−1=0
  y = 1−2x → substitute:
  F(x) = 3x²+(1−2x)²−3x+4 = 3x²+1−4x+4x²−3x+4 = 7x²−7x+5
  F'(x) = 14x−7 = 0 → x=1/2, y=0
  → Absolute minimum at (1/2, 0)
```

---

## 7. Extreme Value Theorem (Ex10)

If f is continuous on a **closed and bounded** region, then f attains its **absolute maximum and minimum**.

Strategy:
1. Find all critical points inside the region
2. Check boundary (use Lagrange or parametrize the boundary)
3. Compare all values

---

## 🏆 Exam Strategy for 2-Variable Functions

```
UNCONSTRAINED:
1. Find domain in ℝ² and sketch it
2. Compute fₓ, fᵧ
3. Solve {fₓ=0, fᵧ=0} → critical points
4. Compute fₓₓ, fᵧᵧ, fₓᵧ at each critical point
5. Compute det(H) = fₓₓ·fᵧᵧ − (fₓᵧ)²
6. Classify: min (det>0, fₓₓ>0) / max (det>0, fₓₓ<0) / saddle (det<0)

CONSTRAINED (Lagrange):
1. Set up ∇f = λ∇g and g=0
2. Solve the 3-equation system
3. Evaluate f at all solutions
4. State absolute max/min

DOMAIN DRAWING:
1. Identify boundary curves (equality)
2. Shade feasible region (use test point)
3. Draw with solid (≥,≤) or dashed (>,<) boundary
```

---

## 📝 Typical Exam Exercises

| Type | Example |
|:---|:---|
| Domain | f(x,y) = ln(x−3y): half-plane {x−3y>0} |
| Domain | f(x,y) = √(x²+y²−4): exterior of disk of radius 2 |
| Domain | f(x,y) = 1/√(x−1) + log y: {x>1, y>0} |
| Hessian | f(x,y) = x²+y²−2x−4y+1 → min at (1,2) |
| Saddle | f(x,y) = x²−y², f(x,y) = xy → (0,0) saddle |
| Lagrange | Maximize xy on x+y=4 → max at x=y=2 |
| Lagrange | Min distance from origin to line ax+by=c |

### Real Exam Questions:
- **Jan 9, 2025:** f(x,y) = ln(1−x²−y²) → domain = open unit disk, min/max/saddle, level curves are circles
- **Jan 22, 2026:** f(x,y) = e^(x−y)·(x²−2y²) → find and classify critical points
- **Feb 4, 2026:** f(x,y) = 2(y²+x²−2xy) − x⁴ − y⁴ + 15 → critical points at origin and (±√2, ∓√2)
- **May 27, 2026:** f(x,y) = x²y + x² − 2y → all critical points are saddle points

---

*Fonti: → [[Math_Home]] | [[Math_Formulario]] | Module9, Ex10, All past exams*
