---
tags: [math, linear-algebra, exam-prep, matrices, determinants, eigenvalues, rank, systems]
aliases: [Linear Algebra, Algebra Lineare]
date_created: 2026-05-30
last_modified: 2026-05-30
---

# 🔢 Linear Algebra
> [!NOTE]
> Back to [[Math_Home]] | Prof. Riccardo De Blasis — Marche Polytechnic University

---

## 0. Logic & Set Theory (Module 1)

### Logic Symbols
| Symbol | Meaning |
|:---|:---|
| ¬ | NOT (negation) |
| ∨ | OR |
| ∧ | AND |
| ∀ | for all |
| ∃ | there exists |
| ∃! | there exists exactly one |
| ⇒ | implies |
| ⇔ | if and only if (iff) |

### Implication P ⇒ Q
- P is a **sufficient** condition for Q
- Q is a **necessary** condition for P
- Example: x > 2 ⇒ x² > 4; xy = 0 ⟺ x = 0 or y = 0

### Set Theory (Ex0)
- **Union**: A ∪ B, **Intersection**: A ∩ B, **Difference**: A \ B
- **Supremum** (sup): least upper bound (may not be in the set)
- **Infimum** (inf): greatest lower bound (may not be in the set)
- **Maximum**: sup that belongs to the set
- **Minimum**: inf that belongs to the set

> [!TIP]
> For S = {1 − 1/n : n ∈ ℕ}: sup S = 1 but max S does NOT exist (1 is never reached). inf S = min S = 0. **This is a classic exam multiple-choice question!**

### Interior, Boundary, Limit Points
- **Interior point** of A: ∃ open interval I(x) ⊂ A
- **Boundary point**: every neighborhood intersects both A and its complement
- **Limit point**: every neighborhood contains a point of A different from itself

**Key fact:** 0 is a limit point of {1/n : n ∈ ℕ} even though 0 ∉ the set.

---

## 1. Vectors in ℝⁿ (Module 2)

A **vector** v ∈ ℝⁿ is an ordered n-tuple: **a** = (a₁, a₂, ..., aₙ)
- **Null vector**: **0** = (0, 0, ..., 0)
- Equality: **a** = **b** ⟺ aᵢ = bᵢ for all i

### Operations
| Operation | Formula |
|:---|:---|
| Sum / Difference | **a** ± **b** = (a₁±b₁, ..., aₙ±bₙ) |
| Scalar multiplication | λ**a** = (λa₁, ..., λaₙ) |
| Dot product | **x**·**y** = x₁y₁ + ... + xₙyₙ ∈ ℝ |
| Norm | ‖**v**‖ = √(**v**·**v**) |
| Distance | d(**x**,**y**) = ‖**x** − **y**‖ |

> [!WARNING]
> **x**·**y** = 0 does NOT mean one of them is zero! e.g., x=(1,1), y=(1,−1) ⇒ x·y = 0

### Linear Combination
Given p vectors x₁, ..., xₚ ∈ ℝⁿ and scalars k₁, ..., kₚ:
> **b** = k₁**x**₁ + k₂**x**₂ + ... + kₚ**x**ₚ

### Linear Independence
Vectors v₁,...,vₖ are **linearly independent** if:
> λ₁v₁ + λ₂v₂ + ... + λₖvₖ = **0** ⟹ all λᵢ = 0

**Example (Ex1):** e₁ = (1,0,0) and x₂ = (0,2,0) are linearly independent.

### Worked Examples (Ex1)
- x=(2,4), y=(1,−1), z=(0,9): x+y = (3,3), x+z = (2,13), 3z = (0,27)
- Orthogonal vectors (dot product = 0): x=(t,−1,3), y=(t,2t,−5): t=−3 or t=5

---

## 2. Matrices (Module 2)

An **m×n matrix** A has m rows and n columns: (Aᵢⱼ)

### Key Matrix Types
| Name | Definition |
|:---|:---|
| Square | m = n |
| Diagonal | aᵢⱼ = 0 for i ≠ j |
| Identity **I** | Diagonal with all 1s on diagonal |
| Symmetric | A = Aᵀ |
| Transpose Aᵀ | (Aᵀ)ᵢⱼ = Aⱼᵢ |
| Idempotent | A² = A |

### Matrix Multiplication
(AB)ᵢⱼ = Σₖ Aᵢₖ · Bₖⱼ  (requires A is m×p and B is p×n)
> ⚠️ AB ≠ BA in general!

### Invertible Matrix
A square matrix A is **invertible** iff **det(A) ≠ 0**.
Then: A · A⁻¹ = A⁻¹ · A = **I**

**2×2 Inverse formula:**
```
A = |a b|     A⁻¹ = (1/det(A)) · | d  -b|
    |c d|                          |-c   a|
```

---

## 3. Determinant (Module 2 + Ex2)

### 2×2 Matrix
> det(A) = ad − bc

### 3×3 Matrix — Sarrus Rule
```
|a b c|
|d e f| = aei + bfg + cdh − ceg − afh − bdi
|g h i|
```

### 3×3 — Cofactor Expansion (along row 1)
det(A) = a₁₁·C₁₁ + a₁₂·C₁₂ + a₁₃·C₁₃
where Cᵢⱼ = (−1)^(i+j) · Mᵢⱼ (Mᵢⱼ = minor = det of submatrix without row i, col j)

### Key Properties
- det(AB) = det(A)·det(B)
- det(Aᵀ) = det(A)
- det(λA) = λⁿ·det(A) for n×n matrix
- Swapping two rows → sign changes
- A row of zeros → det = 0
- Row of zeros or proportional rows → det = 0

### Rank of a Matrix (Ex2)

The **rank** = order of the largest submatrix with non-zero determinant.

**Method A:** Start from highest order submatrices, check det ≠ 0.
**Method B:** Find a nonzero element, build bordered submatrices of increasing size.

**Classic example (Ex2):**
```
A = |-1  2  0  3|
    | 3 -1  2  4|
    | 4 -3  2  1|

All 3×3 submatrix determinants = 0, but det(|-1 2|) = -5 ≠ 0 → rank(A) = 2
                                              | 3 -1|
```

**Parametric rank example (Ex2):**
```
A = |k  1  1|
    |1  k  1|  → det(A) = k³ − 3k + 2 = (k−1)²(k+2)
    |1  1  k|

→ rank 3 if k ≠ 1, −2
→ rank 2 if k = −2
→ rank 1 if k = 1
```

---

## 4. Systems of Linear Equations — Rouché–Capelli Theorem

A system Ax = b is:
- **Compatible** (has solutions) iff **rank(A) = rank(A|b)**
- If compatible and rank = n (# unknowns) → **unique solution**
- If compatible and rank < n → **∞ solutions** (∞^(n−rank) degrees of freedom)
- **Incompatible** (no solutions) if rank(A) < rank(A|b)

### Solution Method: Gaussian Elimination (Row Reduction)
1. Write augmented matrix [A|b]
2. Apply row operations to reach **row echelon form**
3. Back-substitute to find solutions

### Homogeneous System (b = 0)
Ax = 0 always has the trivial solution x = 0.
Has non-trivial solutions iff **det(A) = 0** (i.e., rank(A) < n).

### Solved Examples (Ex3)

**Without parameters:**
```
System: 2x+3y=1,  3x+y=−2
Solution: x=(−1, 1)
```

```
System (4×3): x+y+2z+t=1, 2x−y+z−2t=0, −4x+5y+z+8t=2
Solution: ∞¹ solutions: (1−3z+t/3, 2−3z−4t/3, z, t)
```

**With parameter k (Ex3 — most common exam type):**
```
|k  1  0| |x|   |1|
|1  1 1-k| |y| = |k|
|0  1  1| |z|   |1|

• k ∉ {−1,1}: unique solution x = (−1/(k+1), (2k+1)/(k+1), −k/(k−1))
• k = 1: ∞¹ solutions x = (t, 1−t, t), t ∈ ℝ
• k = −1: IMPOSSIBLE
```

**Key parametric pattern (Ex3, system 9–19):**
- For most values of k: 1 solution
- For special values: ∞ solutions or impossible
- Always check both with Rouché-Capelli

> [!IMPORTANT]
> **Exam exam exam:** To find for which k the system is impossible: compute det(A) = 0 AND check rank(A|b) > rank(A).
> To find for which k there are infinite solutions: rank(A) = rank(A|b) < n.

---

## 5. Eigenvalues & Eigenvectors

### Definition
**λ** is an eigenvalue of A, **v** is the corresponding eigenvector if:
> **Av = λv**, with **v ≠ 0**

### How to Find Them

**Step 1:** Solve the **characteristic equation**:
> det(A − λI) = 0

This gives eigenvalues λ₁, λ₂, ...

**Step 2:** For each λᵢ, solve:
> (A − λᵢI) **v** = **0**

### Example (2×2)
```
A = |3  1|      A − λI = |3−λ  1  |
    |0  2|               |0    2−λ |

det = (3−λ)(2−λ) = 0  →  λ₁ = 3, λ₂ = 2
```

### Key Facts
- Sum of eigenvalues = trace(A) = Σ aᵢᵢ
- Product of eigenvalues = det(A)
- A symmetric matrix has **real eigenvalues**
- Eigenvectors of distinct eigenvalues are **linearly independent**
- The system (A − kI)x = 0 has non-trivial solutions iff det(A − kI) = 0

**From Ex3 (miscellaneous ex5):**
```
A = |3  0  0|  → eigenvalues: k=3, k=1±√2
    |0  1  1|
    |0  2  1|

For k≠3, k≠1±√2: only zero solution
For k=3: infinite solutions of form (x,0,0)
For k=1−√2: infinite solutions of form (0,y,−√2·y)
For k=1+√2: infinite solutions of form (0,y,√2·y)
```

---

## 🏆 Exam-Ready Formula Sheet

| Concept | Formula |
|:---|:---|
| 2×2 det | ad − bc |
| 3×3 det | Sarrus or cofactor expansion |
| Inverse 2×2 | (1/det) · \|d −b; −c a\| |
| Characteristic eq. | det(A − λI) = 0 |
| Rouché-Capelli | r(A) = r(A\|b) → compatible |
| Rank | Max order of non-zero minor |
| Trace | Sum of diagonal elements |
| S = {1−1/n} | sup=1 (no max), min=inf=0 |

---

## 📝 Typical Exam Exercises

1. **Compute det(A)** for a 3×3 matrix (or parametric matrix, find k where det=0)
2. **Compute rank(A)** with varying parameter k (find critical k values)
3. **Solve a 3×3 linear system** using Gaussian elimination
4. **Parametric system**: study number of solutions as k varies (use Rouché-Capelli)
5. **Find eigenvalues and eigenvectors** of a 2×2 or 3×3 matrix
6. **Set theory**: supremum, infimum, limit points of a set
7. **Matrix computations**: AB, Aᵀ, A², finding k such that rank(AB) = given value

### Real Exam System (Jan 22, 2026 — Q4 & Q5):
```
Q4: A=(1 -1; 1 k) B=(0 1; 1 2) Find k such that rk(AB)=1

Q5: A = 4×4 matrix, compute det(A)
    |2  1  3  0|
    |-1 0  1  2|
    |2  0 -1 -1|
    |-3 1  0  1|
```

---

*Fonti: → [[Math_Home]] | [[Math_Formulario]] | Module1, Module2, Ex0, Ex1, Ex2, Ex3*
