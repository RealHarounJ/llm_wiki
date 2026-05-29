---
tags: [esercitazione, corporate-finance, study-guide, exam-prep, grafici, formule]
aliases: [Exam Graphs and Formulas Guide, Guida Grafici e Formule]
date_created: 2026-05-23
last_modified: 2026-05-23
---

# 📊 Blackboard Masterclass — Exam Graphs and Formulas

In the oral exam, the professor will frequently ask you to **"go to the blackboard, write down the formula, and plot the graph."** 

This guide provides the **Top 4 Blackboard Drawings** you must master, complete with exactly what to label on the axes, the key points to mark, the math to write next to the drawing, and the verbal explanation to deliver while drawing.

---

## 📈 Graph 1: The NPV Profile (NPV Curve)

This graph shows the relationship between a project's Net Present Value (NPV) and the discount rate ($r$).

### ✏️ How to Draw it on the Blackboard:
1. Draw the **Y-axis** and label it **NPV (€)**.
2. Draw the **X-axis** and label it **Discount Rate r (%)**.
3. Plot a **downward-sloping, convex curve** (curving slightly upward like a slide).
4. Label the **Y-intercept** where the curve touches the Y-axis.
5. Label the **X-intercept** where the curve crosses the X-axis.

```text
       NPV (€)
         ▲
  CF_0 + │* (Y-intercept: NPV at r = 0% = Simple sum of all Cash Flows)
  Sum(CF)│ *
         │   *
         │     *
         │       *
        0┼─────────*───────────────► Discount Rate r (%)
         │          \
         │           * IRR (X-intercept: NPV = 0)
         │            *
         ▼             *
```

### 🧮 The Formulas to Write:
* **The General NPV Formula:**
  $$NPV = CF_0 + \sum_{t=1}^{T} \frac{CF_t}{(1+r)^t}$$
* **The IRR Definition (where $NPV = 0$):**
  $$NPV = CF_0 + \sum_{t=1}^{T} \frac{CF_t}{(1+IRR)^t} = 0$$

### 🗣️ What to Say to the Professor:
> "Professor, this is the **NPV Profile**. The Y-axis represents the project's NPV, and the X-axis represents the discount rate $r$. 
> 
> * **The Y-intercept** represents the NPV when the discount rate is exactly $0\%$. At this point, there is no discounting, so the NPV is simply the algebraic sum of all cash flows ($CF_0 + \sum CF_t$).
> * **The slope is negative** because as the discount rate increases, the present value of future cash inflows shrinks, reducing the overall NPV.
> * **The X-intercept** is the most critical point: it is the **Internal Rate of Return (IRR)**, which is the unique discount rate that brings the project's NPV exactly to zero.
> * If our cost of capital $r$ is to the left of the IRR ($r < IRR$), the project has a positive NPV and we accept it. If it is to the right ($r > IRR$), NPV is negative and we reject it."

---

## 🛡️ Graph 2: Portfolio Diversification (Total Risk vs. Number of Stocks)

This graph demonstrates how total portfolio risk decreases as you add more non-perfectly correlated assets to a portfolio.

### ✏️ How to Draw it on the Blackboard:
1. Draw the **Y-axis** and label it **Portfolio Volatility $\sigma_p$ (%)** (or Portfolio Standard Deviation).
2. Draw the **X-axis** and label it **Number of Stocks in Portfolio (N)**.
3. Draw a **horizontal dotted line** representing the market's systematic risk.
4. Draw a curve starting high on the Y-axis (for $N=1$) that **slopes downwards and flattens out**, asymptotically approaching the horizontal dotted line.
5. Shade and label the two distinct risk areas.

```text
Portfolio Volatility
      σ_p (%)
         ▲
         │ *
  Risk of│   *
  Single │     *   ◄─── Unsystematic Risk (Diversifiable / Idiosyncratic Risk)
  Stock  │       *      (Can be eliminated by holding ~30 stocks)
         │─────────*──-----------------------------
         │            * * * * * * * * * * * * * *  ◄─── Dotted Line
         │                                         
         │         Systematic Risk (Market / Non-Diversifiable Risk)
         │         (Triggered by macro factors; cannot be diversified away)
        0┼─────────────────────────────────────────► Number of Stocks (N)
```

### 🧮 The Formulas to Write:
* **The 2-Asset Portfolio Variance (to show the math behind correlation):**
  $$\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_A w_B \rho_{AB} \sigma_A \sigma_B$$
* Explain that if correlation $\rho_{AB} < 1$, the portfolio standard deviation $\sigma_p$ is strictly less than the weighted average of the individual standard deviations ($\sigma_p < w_A\sigma_A + w_B\sigma_B$).

### 🗣️ What to Say to the Professor:
> "Professor, this graph illustrates the **Modern Portfolio Theory of Diversification**. The Y-axis represents total portfolio risk ($\sigma_p$), and the X-axis is the number of stocks in the portfolio ($N$).
> 
> * Total risk is composed of two parts: **Unsystematic Risk** and **Systematic Risk**.
> * **Unsystematic risk** (the top area) is stock-specific. Because different stocks have independent micro-events, these events cancel each other out as we add more assets. By the time we hold roughly 25 to 30 stocks, unsystematic risk is practically **zero**.
> * **Systematic risk** (the bottom area below the dotted line) is market-wide and driven by macro factors like interest rates or recessions. It cannot be diversified away. 
> * Because investors can eliminate unsystematic risk for free, the market only compensates them for bearing **systematic risk**, which is why our CAPM formula only rewards the stock's Beta ($\beta$) and ignores its total volatility ($\sigma$)."

---

## 📈 Graph 3: The Security Market Line (SML)

The SML is the graphical representation of the Capital Asset Pricing Model (CAPM). It shows the expected return of an asset as a function of its systematic risk (Beta).

### ✏️ How to Draw it on the Blackboard:
1. Draw the **Y-axis** and label it **Expected Return E[R] (%)**.
2. Draw the **X-axis** and label it **Systematic Risk (Beta β)**.
3. Mark $1.0$ on the X-axis and label it **$\beta_M$** (Market Beta).
4. Mark the **y-intercept** and label it **$R_f$** (Risk-Free Rate).
5. Draw a **straight line** starting from $R_f$ that goes up and to the right.
6. Find the point on the line where $\beta = 1.0$ and map it to the Y-axis as **$E[R_m]$** (Expected Market Return).
7. Draw a point **above the line** (Undervalued) and a point **below the line** (Overvalued).

```text
Expected Return
     E[R] (%)
         ▲
         │                       / (SML)
   E[R_m]┼ - - - - - - - - - - -*  (Market Portfolio: Beta = 1.0)
         │                     /│  
         │      ▲             / │  
         │    Alpha > 0      /  │  
         │  (Undervalued)   /   │  
     R_f ┼─────────────────*    │  
         │                /     │  
         │               /      │  
         │              /       │  
        0┼─────────────*────────┴─────────► Systematic Risk (Beta β)
                      0        1.0
```

### 🧮 The Formulas to Write:
* **The CAPM Equation (The Equation of the SML):**
  $$E[R_i] = R_f + \beta_i \cdot (E[R_m] - R_f)$$
* **The Slope of the SML (Market Risk Premium):**
  $$\text{Slope} = E[R_m] - R_f$$
* **Jensen's Alpha ($\alpha$):**
  $$\alpha_i = E[R_{i, \text{actual}}] - E[R_{i, \text{CAPM}}]$$

### 🗣️ What to Say to the Professor:
> "Professor, this is the **Security Market Line (SML)**, which graphically represents the **CAPM**. The Y-axis is the Expected Return, and the X-axis is the systematic risk measured by Beta.
> 
> * **The Y-intercept** is the **Risk-Free Rate ($R_f$)**, where an asset has zero systematic risk ($\beta = 0$).
> * **The slope of the line** represents the **Market Risk Premium ($E[R_m] - R_f$)**, which is the reward investors demand for taking on an average unit of market risk.
> * Any asset that is in equilibrium must lie **exactly on the SML**.
> * If a stock lies **above the SML**, it has a positive **Jensen's Alpha ($\alpha > 0$)**. This means it offers a higher return than required for its level of risk. It is **undervalued** (a 'buy') because its price is too low, forcing the expected return up.
> * If it lies **below the SML**, it has a negative Alpha. It is **overvalued** (a 'sell') because it underperforms relative to its risk level."

---

## ⚖️ Graph 4: WACC, Cost of Capital, and Leverage (Trade-off Theory)

This graph shows how a firm's cost of capital changes as it takes on debt ($D/E$ or $D/V$), illustrating the optimal capital structure under the **Trade-off Theory**.

### ✏️ How to Draw it on the Blackboard:
1. Draw the **Y-axis** and label it **Cost of Capital (%)**.
2. Draw the X-axis and label it **Debt-to-Value Ratio (D/V)** or **Debt-to-Equity (D/E)**.
3. Draw a flat or slightly upward-sloping curve at the bottom for the **after-tax Cost of Debt: $R_d \cdot (1-\tau_c)$**.
4. Draw an upward-sloping curve at the top for the **Cost of Equity: $R_e$** (it rises because financial leverage increases risk).
5. Draw a **U-shaped curve** in the middle for the **WACC**.
6. Mark the **minimum point** of the WACC curve, draw a vertical dotted line to the X-axis, and label it **$D/V^*$ (Optimal Capital Structure)**.

```text
Cost of Capital (%)
         ▲
         │                                *  Cost of Equity R_e
         │                            *      (Rises due to financial leverage)
         │                        *
     R_u ┼                     * 
         │                   * * * * * * *
         │               *                 * WACC (U-shaped)
         │             *
         │            *  <-- Min WACC
         │───────────*─────────────────────────────
     R_d ┼          / * * * * * * * * * * * * * * Cost of Debt R_d
         │         /                             (after-tax: R_d * (1-t))
        0┼────────*────────────────────────────────► Leverage Ratio (D/V)
                  0          D/V* 
                       (Optimal Debt Level)
```

### 🧮 The Formulas to Write:
* **The WACC Formula:**
  $$WACC = \left(\frac{E}{V} \cdot R_e\right) + \left(\frac{D}{V} \cdot R_d \cdot (1 - \tau_c)\right)$$
* **Modigliani-Miller II (with taxes) to explain why $R_e$ rises:**
  $$R_e = R_u + (R_u - R_d) \cdot \frac{D}{E} \cdot (1 - \tau_c)$$

### 🗣️ What to Say to the Professor:
> "Professor, this graph represents the **Trade-off Theory of Capital Structure**. 
> 
> * As we increase debt ($D/V$), we initially **lower our WACC** because debt is cheaper than equity and its cost is further reduced by the interest tax shield, $R_d(1-\tau_c)$.
> * However, as leverage increases, **the cost of equity ($R_e$) rises** because of financial leverage (as shown by Modigliani-Miller Proposition II). 
> * Eventually, at high levels of debt, the probability of bankruptcy rises, and **financial distress costs** kick in, dragging down the firm's value and forcing both $R_e$ and WACC to rise.
> * The **Optimal Capital Structure ($D/V^*$)** is the exact point where the WACC is **minimized**. Minimizing the WACC is mathematically equivalent to **maximizing the total value of the firm ($V$)**."

---

## 🎯 Quick Cheat-Sheet for Blackboard Success:
1. **Always label your axes immediately.** The professor will dock points if you draw a line without defining $X$ and $Y$.
2. **Write the governing formula next to the graph.** It shows that your drawing is mathematically backed.
3. **Talk while you draw.** Don't draw in silence. Explain what every line means *as* your hand is moving. It projects immense confidence.
