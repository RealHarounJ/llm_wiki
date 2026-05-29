---
tags: [python, data-science, numpy, vectorization, memory-contiguity, quantitative-finance]
aliases: [Lesson 1: NumPy and Vectorization, Lezione 1: NumPy e Vettorializzazione]
date_created: 2026-05-29
last_modified: 2026-05-29
source_count: 1
---

# 🚀 Lesson 1: NumPy and Vectorization

Welcome to your first quantitative lesson! To build high-performance trading systems, financial modeling tools, or data science pipelines, you must understand **how** data is represented in memory and **why** pure Python is too slow for large-scale quantitative computations. 

This lesson explores **NumPy (Numerical Python)**, the bedrock of the Python scientific computing stack, and explains the principles of **Vectorization**, **Memory Contiguity**, and **SIMD CPU acceleration**.

---

## 🔍 1. The Core Problem: Why Pure Python Lists are Too Slow

A standard Python `list` is extremely flexible. It can hold integers, strings, floats, and objects all in the same container:
```python
my_list = [42, "Gold Price", 2030.4, {"asset": "XAUUSD"}]
```
To achieve this dynamic flexibility, Python represents every single item in the list as a complete **PyObject** in heap memory.
*   **Dynamic Type Boxing/Unboxing:** Each number is "boxed" with metadata (reference counts, object type info, size). Every time you perform an addition, Python must look up the type, unbox the value, perform the addition, and box the result into a new PyObject.
*   **Memory Fragmentation:** A Python list doesn't store the actual data contiguously. Instead, it stores **pointers** to these scattered PyObjects in memory. When you iterate through a list, your CPU has to jump around different locations in RAM. This causes frequent **cache misses** (the CPU cache cannot pre-fetch the data because it doesn't know where the next pointer points).

### 🚀 Comparison in CPU Cycles
| Operation | Pure Python List | NumPy `ndarray` |
| :--- | :--- | :--- |
| **Storage** | Array of pointers to boxed objects | Contiguous, flat block of raw bytes |
| **Type Check** | Done at runtime for *every* element (slow) | Done once for the entire array (dtype) |
| **Cache Locality** | Extremely poor (random heap jumps) | Perfect (data fits L1/L2 CPU caches) |
| **Execution** | Interpreted bytecode loop (slow) | Vectorized compiled C-level loops (native speed) |

---

## 📦 2. The Solution: NumPy's `ndarray`

NumPy introduces the **`ndarray`** (N-dimensional array), which is a multidimensional container of **homogeneous** items (all elements share the same type, like `float64` or `int32`).

```python
import numpy as np
# Creating a homogeneous 1D array of 64-bit floats
prices = np.array([2005.1, 2010.5, 1998.2, 2020.4], dtype=np.float64)
```

### Key Architectural Concepts:
1.  **Memory Contiguity:** The values are stored as a continuous block of bytes in RAM. For instance, four `float64` numbers occupy exactly $4 \times 8 = 32$ bytes of adjacent space.
2.  **Strides:** An array keeps track of its "shape" and "strides". Strides are the number of bytes the CPU must step through in memory to move to the next element along an axis.
    *   *C-Contiguous (Row-Major):* Moving along a row steps through adjacent memory addresses. This is the default in NumPy.
    *   *Fortran-Contiguous (Column-Major):* Moving along a column steps through adjacent memory addresses.
3.  **No Explicit Loops (Vectorization):** When you multiply a NumPy array by a scalar, the loop is executed entirely in compiled C code at the hardware level.

```python
# Scaling prices by a volatility factor - Vectorized (No loops!)
scaled_prices = prices * 1.05
```

---

## ⚡ 3. Hardware Acceleration: SIMD

At the processor level, vectorized operations leverage **SIMD (Single Instruction, Multiple Data)** instructions. 

```
Standard CPU Loop (Scalar):
[ Fetch Price 1 ] ──> [ Multiply by 1.05 ] ──> [ Store Result 1 ]
[ Fetch Price 2 ] ──> [ Multiply by 1.05 ] ──> [ Store Result 2 ]

SIMD CPU Operation (Vectorized):
[ Price 1, Price 2, Price 3, Price 4 ] ──> [ Multiply All by 1.05 in 1 Cycle ] ──> [ Store All Results ]
```

Modern CPUs have wide registers (AVX-2, AVX-512, or ARM Neon) that can process 256 or 512 bits of data simultaneously. In a single clock cycle, a modern CPU can multiply four or eight 64-bit floats at once. NumPy leverages these hardware extensions natively!

---

## 📐 4. Broadcasting Rules

One of NumPy's most powerful features is **Broadcasting**. It allows arithmetic operations on arrays of different shapes, as long as they meet specific compatibility rules.

### The Broadcasting Rule:
To broadcast, start matching dimensions from the **rightmost (trailing)** dimension and work your way left. Two dimensions are compatible if:
1.  They are **equal**, OR
2.  One of them is **1**.

If a dimension is `1`, NumPy virtually duplicates the data along that axis to match the larger array, without physically copying memory.

```python
# Example 1: Matrix (3, 4) and Row Vector (1, 4)
matrix = np.ones((3, 4))
row_vector = np.array([10, 20, 30, 40]) # Shape (4,), treated as (1, 4)

# Broadcasting works! The row_vector is stretched to 3 rows
result = matrix + row_vector
# Result Shape: (3, 4)
```

---

## 📈 5. Quantitative Financial Application: Vectorized Maximum Drawdown

Let's look at a concrete financial quantitative problem: calculating the **Maximum Drawdown (MDD)** of a price series. 
*   **Maximum Drawdown** is the maximum peak-to-trough decline in a portfolio value before a new peak is attained.
*   In pure Python, you would write a slow nested `for` loop tracking the running maximum.
*   In NumPy, we vectorize it completely using `np.maximum.accumulate`.

```python
import numpy as np

# 1. Generate hypothetical stock prices
prices = np.array([100.0, 105.0, 102.0, 98.0, 104.0, 95.0, 107.0, 101.0])

# 2. Compute the running peak (vectorized cumulative maximum)
peaks = np.maximum.accumulate(prices)
# Result: [100.0, 105.0, 105.0, 105.0, 105.0, 105.0, 107.0, 107.0]

# 3. Compute vectorized drawdowns for each point
drawdowns = (prices - peaks) / peaks
# Result: [0.0, 0.0, -0.028, -0.066, -0.0095, -0.095, 0.0, -0.056]

# 4. Find the Maximum Drawdown
max_drawdown = drawdowns.min()
print(f"Maximum Drawdown: {max_drawdown * 100:.2f}%")
# Result: -9.52% (Peak of 105.0 dropping to trough of 95.0)
```

---

## 🛠️ 6. Exercise 1: Volatility & Sharpe Ratio calculation
Now it's your turn to practice. Let's write a small script to compute the **Annualized Volatility** and **Sharpe Ratio** of a daily price stream using NumPy operations.

### 📝 Problem Description:
Given a 1D NumPy array of daily stock prices:
1.  Compute the daily log returns: 
    $$R_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$
    *Hint:* Use `np.log()` and slicing `prices[1:]` / `prices[:-1]`.
2.  Calculate the daily standard deviation of returns using `np.std(returns)`.
3.  Annualize the volatility by multiplying the daily standard deviation by the square root of $252$ (trading days in a year):
    $$\sigma_{annual} = \sigma_{daily} \times \sqrt{252}$$
    *Hint:* Use `np.sqrt()`.
4.  Calculate the Sharpe Ratio, assuming a risk-free rate of $0\%$ ($R_f = 0$):
    $$\text{Sharpe Ratio} = \frac{\text{Mean Annualized Return}}{\text{Annualized Volatility}} = \frac{\text{Mean Daily Return} \times 252}{\sigma_{annual}}$$

---

## Fonti
* `[[Fonte_McKinney_Python_Data_Analysis]]` — Chapter 2: NumPy Basics.
* `[[Python_Data_Analysis]]` — Section 1: NumPy and Vectorization.
