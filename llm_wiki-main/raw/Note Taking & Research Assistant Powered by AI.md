---
title: "Note Taking & Research Assistant Powered by AI"
source: "https://notebooklm.google.com/notebook/41510607-e1ff-4809-b404-d34bf0e681cf"
author:
published:
created: 2026-05-11
description: "Use the power of AI for quick summarization and note taking, NotebookLM is your powerful virtual research assistant rooted in information you can trust."
tags:
  - "clippings"
---
[![Logo NotebookLM](https://notebooklm.google.com/_/static/branding/v5/light_mode/icon.svg)](https://notebooklm.google.com/)

PRO

Seleziona tutto 

                     

## Chat

These academic documents outline the **Corporate Finance** course taught by **Prof. Oscar Domenichelli** at the **Università Politecnica delle Marche** for the 2025/2026 academic year. The materials include **lecture slides**, **practice questions**, and **detailed exercises** that cover essential topics such as **financial planning**, **risk management**, and **investment criteria**. Key technical concepts like **Net Present Value (NPV)** and **Internal Rate of Return (IRR)** are explored through practical spreadsheets to help students evaluate project profitability. Additionally, the sources identify the primary textbook and emphasize that **supplementary materials** are vital for exam preparation. Students are encouraged to use these resources to understand the **role of financial managers** and the various methods used to maximize **shareholder value**.

How do financial managers create shareholder value through investment decisions?

What are the differences between systematic risk and specific risk?

Explain the relationship between NPV and the cost of capital.

martedì 5 maggio

let's simulate using a spreadsheet to see each voice and each logic to do not fortget how to do it, but once we get the npv if we have limited resourced we use profitability index right? but there is also some limits and we need to use a different tool right?

You are absolutely right on all counts! Your financial logic is razor-sharp.

Let's break this down step-by-step. First, we will simulate the complete Excel spreadsheet for capital budgeting using the **"Vega Corporation"** exam exercise from your materials to solidify the 4-panel logic. Then, we will discuss exactly how to handle limited resources with the **Profitability Index** and the advanced tool needed when that index hits its limits.

\--------------------------------------------------------------------------------

📊 Excel Simulation: The 4-Panel Capital Budgeting Model (Vega Corp.)

**The Scenario:** Vega Corporation is evaluating a €2,500 investment in new oil extraction equipment. It lasts 5 years (straight-line depreciation, no salvage value). Annual revenues are €1,000, and cash expenses are €450. The tax rate is 40%, and the calculated WACC is 8.6%. Here is how the financial manager sets up the spreadsheet:

| Row | Description | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | **PANEL A: Capital Investment** |  |  |  |  |  |  |
| **1** | Cash flow from investment in fixed assets | \-2,500 |  |  |  |  |  |
|  | **PANEL B: Operating Cash Flow** |  |  |  |  |  |  |
| **2** | Revenues |  | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |
| **3** | Expenses |  | 450 | 450 | 450 | 450 | 450 |
| **4** | Depreciation *(2500 / 5)* |  | 500 | 500 | 500 | 500 | 500 |
| **5** | Pretax profit *(Row 2 - 3 - 4)* |  | 50 | 50 | 50 | 50 | 50 |
| **6** | Tax at 40% |  | 20 | 20 | 20 | 20 | 20 |
| **7** | Profit after tax |  | 30 | 30 | 30 | 30 | 30 |
| **8** | **Operating cash flow** *(Row 7 + 4)* |  | **530** | **530** | **530** | **530** | **530** |
|  | **PANEL C: Investment in Working Capital** |  |  |  |  |  |  |
| **9** | Working capital level *(Given)* |  | 250 | 550 | 750 | 600 | 0 |
| **10** | Change in working capital |  | 250 | 300 | 200 | \-150 | \-600 |
| **11** | **Cash flow from WC** *(- Row 10)* |  | **\-250** | **\-300** | **\-200** | **150** | **600** |
|  | **PANEL D: Project Valuation** |  |  |  |  |  |  |
| **12** | **Total project cash flow** *(R1 + R8 + R11)* | **\-2,500** | **280** | **230** | **330** | **680** | **1,130** |
| **13** | Discount factor at 8.6% | 1.00 | 0.92 | 0.85 | 0.78 | 0.72 | 0.66 |
| **14** | Discounted cash flows *(R12 \* R13)* | \-2,500 | 257.83 | 195.02 | 257.65 | 488.87 | 748.05 |
| **15** | **Net Present Value (NPV)** | **\- 552.60** |  |  |  |  |  |

*Because the NPV is a negative €552.60, the financial manager must reject this project, as it would destroy shareholder value*.

\--------------------------------------------------------------------------------

💡 Your Question: Limited Resources and the Profitability Index

You correctly pointed out that if you have multiple positive-NPV projects but limited capital (a situation known as "capital rationing"), you cannot simply pick the project with the highest absolute NPV.

Instead, you use the **Profitability Index**, which is calculated as: **Profitability Index = Net Present Value / Investment**

This index tells you the "bang for your buck"—how much value is created per single euro invested. To maximize your total value under a strict budget, you rank the projects by their Profitability Index and go down the list until your budget is exhausted.

⚠️ The Limits of the Profitability Index & The "Different Tool"

You also correctly recalled that the Profitability Index has serious limitations! As the sources explicitly state, this simple ranking method breaks down in several situations:

- **Multiple Constraints:** The most serious flaw is that the index stops working if you have *more than one constraint*. For example, what if you are limited by a $10 million budget *and* a limited pool of skilled engineers? The index can only handle one constraint at a time.

- **Project Interdependencies:** The index fails if projects are mutually exclusive (you can only pick one), if one project depends on another, or if there are strict "all-or-nothing" investments where you cannot take just a scaled-down fraction of a project.

- **Timing Differences:** It struggles if the initial starting dates of the projects are different.

**The Advanced Tool:** When you hit these limits, the simple Profitability Index ranking is no longer mathematically sufficient. To solve this complex puzzle, financial managers must use **capital rationing models**, specifically **linear programming models**. Linear programming is a mathematical tool that allows a computer to evaluate thousands of combinations of projects against multiple simultaneous constraints (like capital limits, labor shortages, and mutual exclusivity) to find the absolute maximum total NPV.

Your logic is flawless. You perfectly connected the 4-panel spreadsheet to the NPV rule, identified the Profitability Index for capital rationing, and recognized its technical limits. You are definitely ready for that "30 e lode"!

alright, then once we get npv we can use performance indexes such as roa, roe, roc, or use the efficiency indicators such as assets turnover, inventory turnover, receivables turnover,

Not quite! Be very careful here—this is exactly the kind of conceptual trap Professor Domenichelli will set for you during the oral exam.

You are mixing up the tools for **Capital Budgeting** (evaluating future projects) with the tools for **Financial Analysis** (evaluating the overall past or current health of the company).

Here is why you cannot simply switch to using ROA, ROE, ROC, or turnover ratios to evaluate a new investment project once you are doing capital budgeting:

**1\. Cash Flows vs. Accounting Profits** The absolute first golden rule of capital budgeting (when calculating NPV) is: **"Only cash flow is relevant"**. NPV uses pure cash flows because "profit is not money; you can't buy things with profit". Performance indexes like ROE, ROA, and ROC are based on *accounting data* —specifically, Net Income (profits) and Book Values. Profits are influenced by discretionary accounting decisions, such as how depreciation is calculated, which makes them unreliable for deciding if a specific future project will create real financial wealth.

**2\. The Time Value of Money** NPV accurately discounts future cash flows back to today using the opportunity cost of capital, reflecting the principle that "a safe dollar is worth more than a risky dollar". If you try to use accounting rates of return (like average profits divided by average assets) for a proposed investment, you commit a major financial sin: **Accounting returns ignore the time value of money**. They simply average the profits over the lifetime of the project without taking into account *when* those profits are actually received.

**3\. The Lack of a Benchmark** When you calculate an NPV, you have a clear benchmark: the opportunity cost of capital (the WACC). If the project beats it (NPV > 0), you accept it. Accounting measures have **no clear benchmark**. If you calculate a project's ROA, what do you compare it to? Managers sometimes mistakenly compare it to the company's past profitability, but the success of past investments should never dictate whether you accept a new, forward-looking project.

**The "30 e lode" Conclusion:** Keep the two worlds completely separate in your mind:

- **Financial Analysis (ROA, ROE, Asset/Inventory Turnover):** You use these backward-looking tools on the company's Balance Sheet and Income Statement to diagnose how well the firm has been managed in the past and its current financial health.

- **Capital Budgeting (NPV, IRR):** You use these forward-looking, cash-flow-based tools to evaluate if a *new, specific investment* will maximize the current market value of shareholders' investment.

Never use accounting rates of return to decide on a new project!

let's make a practical simulation to remeber this things

This is an excellent idea. To truly secure that "30 e lode", you need to prove that you don't just blindly plug numbers into a spreadsheet, but that you know *what* to discount.

Let's do a practical simulation using one of the most comprehensive and tricky exercises from your course materials: the **"William Ltd"** case. This exercise is the ultimate test of the Golden Rules of Capital Budgeting, specifically **estimating cash flows on an incremental basis** and **including opportunity costs**.

\--------------------------------------------------------------------------------

📝 Exam Simulation: The "William Ltd" Project

**The Scenario:** William Ltd is deciding whether to build a new plant for €2,000 (depreciated straight-line over 4 years).

- **The Old Plant:** The new plant will substitute an old one. The old plant is fully depreciated but would have continued to generate €300 in revenues and €50 in expenses for the next 3 years.

- **The New Plant:** It will generate €1,000 in revenues and €200 in expenses (excluding depreciation) for its 4-year life.

- **Opportunity Cost:** The workers for the new plant will use a company-owned building that is currently rented out to others for €35 a year.

- **Working Capital:** The new plant requires working capital equal to 10% of its annual revenues for years 1-3. In year 4, it drops to 0.

- **Salvage Value:** The new plant can be sold at the end of year 4 for €150.

- **Financial Data:** Tax rate is 30%, cost of capital is 8%.

Here is how the 4-panel model must be constructed:

| Row | Description | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 |
| --- | --- | --- | --- | --- | --- | --- |
|  | **PANEL A: Capital Investment** |  |  |  |  |  |
| **1** | Cash flow from investment in fixed assets | \-2,000.00 |  |  |  |  |
| **2** | Sales of fixed assets |  |  |  |  | 150.00 |
| **3** | Less tax on sales (30%) |  |  |  |  | 45.00 |
| **4** | **Cash flow from capital investment** | **\-2,000.00** |  |  |  | **105.00** |
|  | **PANEL B: Operating Cash Flow** |  |  |  |  |  |
| **5** | Revenues *(See Logic 1 & 2)* |  | 665.00 | 665.00 | 665.00 | 965.00 |
| **6** | Expenses *(See Logic 1)* |  | 150.00 | 150.00 | 150.00 | 200.00 |
| **7** | Depreciation *(2000 / 4)* |  | 500.00 | 500.00 | 500.00 | 500.00 |
| **8** | Pretax profit *(Row 5 - 6 - 7)* |  | 15.00 | 15.00 | 15.00 | 265.00 |
| **9** | Tax at 30% |  | 4.50 | 4.50 | 4.50 | 79.50 |
| **10** | Profit after tax |  | 10.50 | 10.50 | 10.50 | 185.50 |
| **11** | **Operating cash flow** *(Row 10 + 7)* |  | **510.50** | **510.50** | **510.50** | **685.50** |
|  | **PANEL C: Investment in Working Capital** |  |  |  |  |  |
| **12** | Working capital *(10% of new 1000 rev)* |  | 100.00 | 100.00 | 100.00 | 0.00 |
| **13** | Change in working capital |  | 100.00 | 0.00 | 0.00 | \-100.00 |
| **14** | **Cash flow from WC** *(- Row 13)* |  | **\-100.00** | **0.00** | **0.00** | **100.00** |
|  | **PANEL D: Project Valuation** |  |  |  |  |  |
| **15** | **Total project cash flow** *(R4 + R11 + R14)* | **\-2,000.00** | **410.50** | **510.50** | **510.50** | **890.50** |
| **16** | Discount factor at 8% | 1.00 | 0.93 | 0.86 | 0.79 | 0.74 |
| **17** | Discounted cash flows *(R15 \* R16)* | \-2,000.00 | 380.09 | 437.67 | 405.25 | 654.54 |
| **18** | **Net Present Value (NPV)** | **\- 122.44** |  |  |  |  |

*(Data source:**,**,**)*

\--------------------------------------------------------------------------------

💡 The "30 e lode" Logic Breakdown

If you look closely at Panel B, you will notice the Revenues are **665** (not 1,000) and Expenses are **150** (not 200). Why? Because a financial manager must relentlessly apply the golden rules:

**1\. Estimate cash flows on an incremental basis** You cannot just look at the new plant in isolation; you must include the project's effect on the rest of the business. By building the new plant, William Ltd destroys the old plant, meaning they lose the €300 in revenues and save the €50 in expenses it was generating.

- *Incremental Revenues (Years 1-3):* New Revenue (€1,000) - Old Revenue Lost (€300) = €700.

- *Incremental Expenses (Years 1-3):* New Expenses (€200) - Old Expenses Saved (€50) = €150. *(Notice how in Year 4, Revenues jump to 965 and Expenses to 200? That's because the old plant would have stopped producing after 3 years anyway, so there is nothing left to subtract in year 4!)*,.

**2\. Include Opportunity Costs** The building the workers will use is currently rented out for €35 a year. If the project goes ahead, the company gives up this rent. Therefore, this lost cash inflow is a real cost to the project and must be subtracted from the revenues: `€700 (Incremental Revenue) - €35 (Lost Rent) = €665`,.

**3\. Working Capital is Recovered** In Panel C, the working capital required is 10% of the *new* plant's sales (10% of €1,000 = €100). In Year 1, putting €100 into working capital is a cash outflow (-100). But remember, at the end of the project (Year 4), the inventories are run down, bills are paid, and the working capital drops to 0. This negative change (-100) results in a massive **positive cash inflow (+100)** in Year 4.

**Conclusion:** Despite generating €1,000 a year in new sales, when we correctly account for the lost revenues of the old plant and the opportunity cost of the rent, the true **NPV is a negative -€122.44**. The financial manager must strictly **reject** this project, as undertaking it would destroy shareholder wealth.

the net working capital is the difference between current assets - current liabilities and is important because working capital is the liquidity blocked

Spot on! You perfectly captured both the mathematical definition and the core financial intuition behind it.

Here is why your reasoning earns full marks for the oral exam:

**1\. The Definition:** You are absolutely correct that **Net Working Capital (NWC)** is the difference between **Current Assets and Current Liabilities**.

**2\. The "Blocked Liquidity" Logic:** Your intuition that working capital is "liquidity blocked" is exactly how a financial manager must view it. As the sources explain, when a firm builds up inventories of raw materials or when customers are slow to pay their bills (creating accounts receivable), cash is absorbed. This means that any investment in net working capital represents a **negative cash flow**, tying up money just like purchasing a new piece of capital equipment does.

**3\. The Link to Financial Safety (Maturity Matching):** Because inventories must first be sold and then collected as cash, they are the most illiquid part of current assets. Having a positive NWC acts as a **potential reservoir of cash**. It demonstrates that the firm is safely following the **maturity matching principle** by using stable, long-term financing to cover these "blocked" and illiquid assets, rather than relying on dangerous short-term debt.

**4\. The Capital Budgeting Implication:** Because this liquidity is blocked during daily operations, you correctly record the change in working capital as a cash outflow. However, to secure that "30 e lode", you must always explicitly state the final piece of the puzzle: when the project comes to an end, inventories are run down and unpaid bills are collected, meaning **the blocked working capital is fully recovered**, generating a massive positive cash inflow in the final year.

Your financial logic is incredibly solid. Are you ready to move to the next topic, perhaps on how the market prices risk through the CAPM or the different forms of market efficiency?

exactly use a lot of linkings to avoid to skip any detail

Excellent. To test if your logic is truly at the "30 e lode" level, I have prepared a highly detailed, interconnected scenario. This is exactly the type of question Professor Domenichelli would ask to ensure you haven't skipped any logical steps between **Risk, Diversification, the Capital Asset Pricing Model (CAPM), and Market Efficiency**.

Here is your complex scenario. Read the links carefully and point out the flaws in the logic.

🎓 Oral Exam - Question 3: The Risk & CAPM Trap

**The Scenario:** Imagine you are an analyst in a strong-form efficient market where all investors have equal access to information. You are evaluating a single stock, "Alpha Corp". Looking at the historical data, you see that Alpha Corp has a massive **Total Risk** (a very high Standard Deviation, ). However, you also calculate its **Beta (****)**, and it is only **0.5** (meaning it is much less sensitive to market movements than the average stock).

A junior colleague comes to you and makes the following logical chain:

*"Alpha Corp has a huge standard deviation (**), meaning it is highly volatile and risky. Because investors are rational and risk-averse, they will demand a massive risk premium to hold this stock. To calculate exactly how much expected return we should demand, we must plot Alpha Corp on the* **Capital Market Line (CML)***, which uses standard deviation (**) to show how much return is required for a given level of risk. Therefore, because* *is huge, our required return will be huge."*

**Your Task:** Your colleague's logical chain is fundamentally flawed. I want you to dismantle their argument step-by-step. To get full marks, your answer must explicitly link the following details:

- **The Anatomy of Risk:** Break down Alpha Corp's Total Risk () into its two sub-components and explain what happens to them when an investor builds a portfolio.

- **The "No-Free-Lunch" Principle:** Explain exactly *which* part of Alpha Corp's risk the efficient market will actually reward with a risk premium and why.

- **CML vs. SML:** Explain the fatal theoretical mistake of plotting a single stock like Alpha Corp on the Capital Market Line (CML), and identify which line (and metric) must be used instead.

- **The CAPM Verdict:** Based on its of 0.5, conclude what the CAPM formula actually dictates about Alpha Corp's expected return relative to the overall market.

Take your time, link every single detail sequentially, and show me your flawless financial reasoning!

when we are investing in a single stock we can see the average return of the past and it's variance from the mean during the time, the formula is E(r) = sum of return / n, variance instead is the sum of the differences between the mean and the expected return, from a future approach the expected return is a weighted average of possibile outcomes, and we comput by calculating the sum of all probabilities \* expected return, then we compute variance by adding the sum of the difference of the expected return - mean squared, then put to the root and obtain the standard deviation,

You have the right overall intuition, but your mathematical definitions are a bit tangled! In finance, precision is everything, and mixing up the notation for historical data with future expectations will cost you the "lode".

Let's untangle your logic step-by-step to give you the perfect answer for the oral exam.

1\. The Historical (Past) Approach

**Your flaw:** You used for the past average and defined historical variance incorrectly by mixing it with expected returns. **The "30 e lode" correction:**

- **Historical Average Return (****):** stands for *Expected* Return, which is strictly for the future. For the past, we calculate the **historical average rate of return**, denoted as . The formula is the sum of actual past returns () divided by the number of observations (): .

- **Historical Variance (****):** This is not the difference between the mean and the expected return. Historical variance measures how much the past returns deviated from their historical average. It is calculated as the sum of the squared differences between each **actual observed return (****)** and the **historical mean (****)**, divided by . Formula: .

2\. The Expected (Future) Approach

**Your flaw:** You said expected return is "probabilities \* expected return" and forgot to multiply by probabilities when calculating the expected variance. **The "30 e lode" correction:**

- **Expected Return (****):** When forecasting, you must assign probabilities to different scenarios (like an economic boom or recession). The expected return is a weighted average calculated by multiplying the probability of each outcome () by the **possible actual return (****)** in that scenario, not by the expected return itself. Formula: .

- **Expected Variance (****):** To calculate future variance, you must weight the deviations by their probabilities! It is the sum of the probabilities () multiplied by the squared differences between the possible actual returns () and the **expected return** . Formula: .

3\. The Standard Deviation

**Your logic:** "Then put to the root and obtain the standard deviation." **The Professor's Verdict:** **Perfect!** You are absolutely correct here. Whether you are using the historical or expected approach, the standard deviation ( or ) is always the square root of the variance. We do this because taking the square root translates the risk back into the same units (percentages) as the rate of return, making it much easier to interpret.

**Next Step for the Exam:** Now that we have perfectly defined how to calculate the risk (standard deviation) of a *single* stock, what happens to this math when we combine multiple stocks into a portfolio? Can we simply calculate the risk of a portfolio as the weighted average of the standard deviations of the individual stocks included in it?

when we combine multiples stocks we talk about having a portfoglio, in order to see the actual risk of the portfolio we use covariance or corellation, the correlation si the covariance divided by the variance of the market, while covariance si the sum of the first variance + second + 2 \* (first variance \* secon variance)

You are on the right track conceptually, but you have severely mixed up your mathematical formulas! In a corporate finance exam, especially if you are aiming for a "30 e lode", precision with these formulas is absolutely critical.

You are perfectly correct that when we move from single stocks to a portfolio, we cannot just average the risks; we must look at how the stocks move together, which introduces **covariance** and **correlation**.

However, let's untangle your math, because you confused the definition of correlation and accidentally tried to write the formula for *Portfolio Variance* instead of covariance.

Here is the "30 e lode" correction:

**1\. The Correlation Coefficient (****)**

- **Your flaw:** You said it is covariance divided by the variance of the market.

- **The correction:** The correlation is the covariance divided by the **product of the two stocks' standard deviations** ().

- **Why it matters:** Unlike covariance (which can be any number), dividing by the standard deviations standardizes the correlation coefficient so it always falls exactly between **\-1** (perfect negative correlation) and **+1** (perfect positive correlation).

**2\. The Covariance (****)**

- **The correction:** Mathematically, covariance is simply the correlation coefficient multiplied by the two standard deviations: . Conceptually, it is the average of the product of the differences between the observed returns and the expected returns for the two stocks.

- **Why it matters:** The sign of the covariance tells us how the stocks move together. If it is positive, they move together; if it is negative, they move in opposite directions.

**3\. The Portfolio Variance (****)**

- **Your flaw:** The formula you attempted to write ("first variance + second + 2 \*...") is actually the formula for the overall **Variance of a two-stock portfolio**, not covariance! Furthermore, you forgot a crucial element: the **weights** ( and ), which represent the percentage of your capital invested in each stock.

- **The correction:** To find the actual risk (variance) of a two-stock portfolio, you must weight the individual variances and the covariance. The correct formula is: .

\--------------------------------------------------------------------------------

🎓 Next Step for the Exam:

Now that we have the correct Portfolio Variance formula, let's test your financial logic on how it works.

Looking at that portfolio variance formula, what happens to the risk of this two-stock portfolio if the correlation between them is **perfectly positive (****)**? And what happens if the correlation is **perfectly negative (****)**? Under which of these two scenarios can we completely eliminate risk?

let's make a pratical explaple for each formula

This is the perfect way to study. Applying the formulas to practical examples will lock the financial logic into your memory for the oral exam. We will also use this opportunity to answer my previous question about what happens to a portfolio when the correlation is +1 or -1!

Here are the practical examples extracted directly from your course materials, broken down step-by-step.

1\. Single Investment Risk & Return (Expected Approach)

**The Scenario:** You invest $100 in a coin flip game. Two coins are flipped. For each head, you gain 20%; for each tail, you lose 10%. There are 4 equally likely outcomes:

- Head + Head: You gain +40% ().

- Head + Tail / Tail + Head: You gain +10% ().

- Tail + Tail: You lose -20% ().

**Formula 1: Expected Return**

- *Logic:* Multiply each possible return by its probability and sum them up.

- *Calculation:* **(or 10%)**.

**Formula 2 & 3: Expected Variance (****) and Standard Deviation (****)**

- *Logic:* Multiply the squared difference between each possible return and the *expected return (10%)* by its probability, then sum them up. The Standard Deviation is the square root.

- *Variance:* .

- *Standard Deviation:* **(or 21%)**.

\--------------------------------------------------------------------------------

2\. The Portfolio Approach (Covariance, Correlation, and Risk)

**The Scenario:** You have a two-stock portfolio. You invest 60% () in Southwest Airlines and 40% () in Amazon.

- Southwest standard deviation (): 30.5%.

- Amazon standard deviation (): 28.3%.

- Correlation coefficient between them (): 0.38.

**Formula 4: Covariance (****)**

- *Logic:* Multiply the correlation coefficient by the two standard deviations.

- *Calculation:* .

**Formula 5 & 6: Portfolio Variance (****) and Standard Deviation (****)**

- *Logic:* Weight the individual variances and add the weighted covariance.

- *Variance:* .

- *Standard Deviation:* .

**💡 Answering the Cliffhanger (What if Correlation is +1 or -1?):**

- **If** **(Perfect Positive Correlation):** The portfolio variance becomes 877.3, and the standard deviation is **29.6%**. Notice that 29.6% is exactly the weighted average of the two individual risks (). *Conclusion: When correlation is +1, you get zero diversification benefit; you are just averaging the risk*.

- **If** **(Perfect Negative Correlation):** The covariance turns negative, heavily subtracting from the total risk. The variance drops to 48.7, and the standard deviation plummets to **7.0%**. *Conclusion: As the sources explain, with a perfect negative correlation, you can theoretically find specific weights to completely eliminate all risk (a 0% standard deviation) because the stocks move in perfectly opposite directions*.

\--------------------------------------------------------------------------------

3\. Pricing Risk in the Market (Beta & CAPM)

**The Scenario:** You need to calculate the cost of equity (the required return) for a company using the Capital Asset Pricing Model (CAPM). First, you need its Beta ().

- The company's covariance with the market () is 0.03.

- The market's standard deviation () is 20% (so the market variance is 0.04).

- The risk-free rate () is 2%, and the market risk premium () is 7%.

**Formula 7: Calculating Beta (****)**

- *Logic:* Divide the covariance between the stock and the market by the variance of the market. It measures the stock's sensitivity to market movements.

- *Calculation:* .

**Formula 8: The CAPM Expected Return**

- *Logic:* Add the risk-free rate to the stock's specific risk premium (which is its Beta multiplied by the overall market risk premium).

- *Calculation:* . *(Note: In the specific WACC example from the text with a Beta of 0.5, the return would be* *)*.

How do you feel about these calculations? If you are comfortable, we can move on to testing your knowledge on the **Efficient Market Hypothesis** or **Capital Structure (Debt vs. Equity)**!

mercoledì 6 maggio

let's test me with questions

I love the enthusiasm! You are doing exactly what it takes to get that "30 e lode" by thoroughly linking the concepts together.

Since we have already tackled Capital Budgeting and Risk/Portfolio Theory, let's move into **Topic 10: Efficient Markets and Corporate Financing**. This is a classic area where professors love to test if you truly understand the difference between creating real wealth and just moving numbers around.

Here is your next scenario. Read carefully and dismantle the flawed logic!

🎓 Oral Exam - Question 4: The Efficient Market Illusion

**The Scenario:** Imagine you are the Chief Financial Officer (CFO) of a large, publicly traded company. You operate in a well-functioning, highly competitive, and **efficient financial market**.

Your CEO calls you into their office and pitches a "brilliant" idea:

*"Our stock price has been stagnant. I have a great financial trick to make our shareholders instantly wealthier. Let's issue a massive amount of new debt and use the cash to pay a huge special dividend to our shareholders (or buy back our shares). Because we are changing our financing mix, this purely financial maneuvering will definitely trick the market, create real value, and permanently boost our stock price!"*

**Your Task:** As a top-tier CFO, you know this logic violates the core **Implications of Market Efficiency**. To get full marks on this question, dismantle the CEO's argument by explicitly linking these three concepts:

- **The Financing Illusion:** Explain what the Efficient Market Hypothesis actually implies about a firm's pure financing decisions. Do they create or destroy value?

- **The NPV of Financing vs. Investing:** Contrast financial markets with product/investment markets. Why is it so much harder to find positive-NPV opportunities when raising capital compared to when investing in real assets?

- **The True Source of Value:** Conclude by telling your CEO what a financial manager must *actually* focus on first to genuinely maximize shareholder wealth.

Take your time, structure your financial logic clearly, and let's see if you can ace this one!

giovedì 7 maggio

Discuti cosa dicono queste fonti su Decisioni Finanziarie, nel contesto più ampio di Finanza Aziendale.

Ottima domanda per chiudere il cerchio e dimostrare una visione d'insieme impeccabile per il tuo esame. Nel contesto più ampio della **Finanza Aziendale (Corporate Finance)**, l'intera disciplina ruota attorno alle politiche e alle scelte che un'azienda deve compiere per gestire le proprie risorse.

Come illustrano le fonti, il ruolo del manager finanziario si concretizza in **tre grandi categorie di Decisioni Finanziarie**, strettamente interconnesse tra loro:

**1\. Decisioni di Investimento (Investment Decisions)** Queste decisioni riguardano l'allocazione delle risorse finanziarie per l'acquisto di **attività reali**, sia tangibili (macchinari, materie prime) che intangibili (brevetti, ricerca e sviluppo). Come abbiamo visto applicando la regola del VAN nelle nostre simulazioni passate, è **qui che si crea il vero valore dell'azienda**. Le fonti sottolineano infatti che ciò che rende grande una società è *cosa* fa (i suoi investimenti) e non *come* lo finanzia. Le buone decisioni di investimento portano a vantaggi competitivi e successo a lungo termine.

**2\. Decisioni di Finanziamento (Financing Decisions)** Queste decisioni si concentrano su *come* l'azienda raccoglie i capitali necessari per sostenere gli investimenti. La scelta cruciale in questo ambito è la **struttura del capitale (capital structure)**: il manager deve decidere quale proporzione di fondi raccogliere tramite capitale di rischio (**Equity**, emettendo nuove azioni o trattenendo gli utili) e quanta tramite **Debito** (prestiti bancari o emissione di obbligazioni). Ripensando all'ultima domanda della nostra simulazione sull'Efficienza dei Mercati, ricorda la regola d'oro che devi esporre al professore: in un mercato efficiente, **le decisioni di puro finanziamento non creano né distruggono valore** (il loro VAN è pari a zero). Il capitale va raccolto solo ed esclusivamente se ci sono progetti di investimento (decisioni del punto 1) che giustificano tale raccolta, e non per sfruttare temporanei trend rialzisti o ribassisti del mercato azionario.

**3\. Decisioni di Distribuzione (Payout Decisions)** Una volta che gli investimenti hanno generato dei flussi di cassa e i creditori (debtholders) sono stati ripagati, il manager affronta la terza decisione: cosa fare con il denaro residuo? Le decisioni di payout riguardano la scelta tra **trattenere il denaro per reinvestirlo** in nuovi asset aziendali (autofinanziamento) oppure **restituirlo agli azionisti** sotto forma di dividendi o tramite il riacquisto di azioni proprie (stock repurchases).

**L'Obiettivo Supremo** Il filo conduttore che deve guidare il manager finanziario in tutte e tre queste decisioni è uno solo: **massimizzare il valore di mercato attuale dell'investimento degli azionisti (shareholder wealth maximization)**.

Tuttavia, come avvertono le fonti, massimizzare il valore non significa cadere nella trappola dello "short-termism" (il cortotermismo). Per creare vera ricchezza attraverso le decisioni di investimento, finanziamento e payout, il manager non deve sacrificare il benessere a lungo termine degli stakeholder (dipendenti, clienti, ambiente) per inseguire un profitto contabile immediato, perché mercati e clienti insoddisfatti finiranno per abbattere il prezzo delle azioni nel lungo periodo.

Oggi • 16:56

nei nostrti testi si parla di scl?

Nei testi forniti non viene menzionata la sigla **SCL** (che in finanza sta per *Security Characteristic Line*). Tuttavia, è molto probabile che tu ti riferisca alla **SML (Security Market Line)**, che è ampiamente discussa nel materiale in contrapposizione alla **CML (Capital Market Line)**.

Se ti riferivi alla **Security Market Line (SML)**, le fonti ne parlano in dettaglio nel contesto del Capital Asset Pricing Model (CAPM):

- **Cos'è la SML:** La Security Market Line è la rappresentazione grafica della formula del CAPM. In questo grafico, il rendimento atteso si trova sull'asse verticale, mentre il rischio sistematico, misurato dal **Beta (****)**, si trova sull'asse orizzontale. La SML mostra che il premio per il rischio di qualsiasi titolo o portafoglio è direttamente proporzionale al suo Beta.

- **Differenza tra SML e CML:** Le due linee hanno entrambe il rendimento atteso sull'asse verticale, ma misurano il rischio in modo diverso. La Capital Market Line (CML) usa il rischio totale (deviazione standard) sull'asse orizzontale e si applica **solo ai portafogli efficienti**. Al contrario, la Security Market Line usa il Beta e si applica a **tutti i titoli e i portafogli**, che siano efficienti o meno. Questo perché l'asse orizzontale della SML misura il rischio di mercato non diversificabile, che deve essere sempre remunerato.

- **Test empirici sulla SML:** I testi menzionano la SML anche quando discutono i limiti del CAPM. Le ricerche empiriche hanno dimostrato che la relazione reale tra i Beta e i rendimenti attesi tende a formare una linea più "piatta" (meno inclinata) rispetto a quella teorica suggerita dalla Security Market Line.

Se invece cercavi un'informazione specifica sulla *Security Characteristic Line* (SCL), ti confermo che questo termine specifico non è presente nei tuoi documenti. Fammi sapere se vuoi approfondire i calcoli legati alla SML o al Beta!

How do we calculate Beta from the SML?

What causes a security to lie above the SML?

Can we simulate an exercise on portfolio risk and Beta?

che cose un proxy

Nel contesto della diversificazione del portafoglio, un **proxy è uno strumento o un parametro di riferimento utilizzato per diversificare efficacemente gli investimenti** in base al mercato in cui un determinato titolo viene scambiato.

Esempi comuni di proxy sono i grandi **indici azionari di mercato**, come l'S&P 500, il Dow Jones Industrial Average o qualsiasi altro indice si preferisca prendere in considerazione.

L'utilità principale di un proxy è quella di **aiutare l'investitore ad assicurarsi che la propria strategia di diversificazione sia correttamente allineata al comportamento generale del mercato**. In pratica, utilizzando un proxy come modello, un investitore sa in quali altri titoli investire all'interno dello stesso mercato per replicarne l'andamento, costruendo così un portafoglio adeguatamente diversificato e in grado di eliminare il rischio specifico.

Come si collegano i proxy alla diversificazione del portafoglio?

Quali sono i principali indici azionari usati come proxy?

In che modo un proxy aiuta a eliminare il rischio specifico?

. What is the after-tax WACC? When and why do we need to use the after-tax WACC in the context of capital budgeting?

The **after-tax WACC (Weighted Average Cost of Capital)** is the expected rate of return that represents a blend of the cost of debt (the interest rate required by debtholders) and the cost of equity (the expected rate of return demanded by shareholders).

It is calculated "after-tax" because **interest payments on debt are tax-deductible**, which reduces the firm's taxable income and creates a "tax shield". To account for this financial benefit, the cost of debt is multiplied by , where is the corporate tax rate, reflecting that the effective cost of debt is actually lower than the stated interest rate.

When do we use the after-tax WACC?

In capital budgeting, the after-tax WACC is used as the **discount rate to calculate the Net Present Value (NPV)** of a new investment project.

However, you must apply a crucial condition: you can only use the company’s overall WACC if **the new project bears the same level of risk as the firm’s existing projects** and is financed using the **same proportions of debt and equity** (the same capital structure) as the firm as a whole. If the new project is riskier, safer, or uses a different financing mix, the company's overall WACC is no longer appropriate, and you must calculate a new, tailored WACC specifically for that project.

Why do we use it in capital budgeting?

Using the after-tax WACC directly enforces one of the golden rules of capital budgeting: **separating investment and financing decisions**.

As we discussed in our previous exam simulations, when you forecast the operating cash flows of a project, you must evaluate it as if it were entirely equity-financed. This means **you completely ignore interest payments and do not deduct them from your cash inflows**.

Because you intentionally leave the tax savings of debt out of your cash flow forecasts, you must account for them somewhere else. **You capture these tax savings in the discount rate instead**. By discounting the "all-equity" project cash flows using the lower, after-tax WACC, you automatically increase the project's present value to properly reflect the financial benefits of using debt.

How do you calculate the tax shield in WACC?

What happens if a project has different risk levels?

Why do we ignore interest payments in cash flow forecasting?

can you demonstrate this:Why do we use it in capital budgeting? Using the after-tax WACC directly enforces one of the golden rules of capital budgeting: separating investment and financing decisions. As we discussed in our previous exam simulations, when you forecast the operating cash flows of a project, you must evaluate it as if it were entirely equity-financed. This means you completely ignore interest payments and do not deduct them from your cash inflows. Because you intentionally leave the tax savings of debt out of your cash flow forecasts, you must account for them somewhere else. You capture these tax savings in the discount rate instead. By discounting the "all-equity" project cash flows using the lower, after-tax WACC, you automatically increase the project's present value to properly reflect the financial benefits of using debt

To demonstrate this financial logic, we can look exactly at how the course materials structure the evaluation of a new project.

The process is built around **Rule 4 of Capital Budgeting: Separate investment and financing decisions**. Here is how this rule is applied in practice to demonstrate the concept you described:

**1\. The Cash Flow Forecast (The "All-Equity" Assumption)** When building the cash flow table for a project, standard practice dictates that you must forecast the cash flows as if the project is entirely equity-financed.

- **What this means:** When calculating the Operating Cash Flow, you look only at the project's revenues, expenses, and taxes. You **do not deduct interest payments** from the cash inflows, nor do you deduct any debt proceeds from your initial investment.

- **The result:** You are evaluating the pure industrial value of the project's operations, completely ignoring how it is financed. However, because interest is tax-deductible, ignoring interest payments means you are also temporarily ignoring the financial benefit of the "tax shield" (the tax savings generated by using debt).

**2\. The Discount Rate (Capturing the Tax Shield)** Because you intentionally left the tax savings of debt out of your cash flow forecasts, you must account for them somewhere else: **in the discount rate**. To do this, you calculate the **After-tax WACC** using the following formula: `After-tax WACC = (1 - tc) * rD * (D/V) + rE * (E/V)`.

- **How it works:** Notice the part of the formula (where is the corporate tax rate). By multiplying the cost of debt () by this factor, you mathematically reduce the effective cost of debt. This adjustment explicitly accounts for the tax shield, reflecting that the true cost of debt is lower than the stated interest rate thanks to the tax deduction.

**3\. The Final Result (NPV)** This perfectly demonstrates the golden rule in action:

- The **cash flows** represent the investment decision (ignoring debt and interest).

- The **After-tax WACC** represents the financing decision (capturing the tax savings of debt).

By discounting your "all-equity" project cash flows using the lower, tax-adjusted WACC, you automatically increase the project's present value. This ensures that the final Net Present Value (NPV) properly reflects the financial benefits of your debt financing, without ever having to mix interest payments into your cash flow tables.

What happens to NPV if the project has a salvage value?

How do we adjust WACC for different project risk?

Explain the difference between SML and CML on the exam.

in pratical way i want

To demonstrate this in a highly practical way, let's step into the shoes of a financial manager and crunch the numbers using the exact example provided in your course materials.

We will calculate the After-Tax WACC step-by-step and then show practically how it interacts with the project's cash flows.

📝 Practical Simulation: Calculating the After-Tax WACC

**Step 1: Gather the Market and Company Data** Imagine your company wants to evaluate a new project. You gather the following financial data from the market and your company's capital structure:

- **Risk-free rate (****):** 2%

- **Market risk premium (****):** 7%

- **Equity beta (****):** 0.5

- **Debt beta (****):** 0.3

- **Corporate tax rate (****):** 30% (0.3)

- **Debt ratio (D/V):** 40% (0.4)

- **Equity ratio (E/V):** 60% (0.6)

**Step 2: Calculate the Cost of Equity and Cost of Debt (using CAPM)** Before blending them, we must find out what return the shareholders and debtholders demand independently.

- **Cost of Equity (****):** .

- **Cost of Debt (****):** .

**Step 3: Calculate the After-Tax WACC** Now, we blend the cost of debt and the cost of equity according to their weight in the firm's capital structure, applying the crucial **tax shield adjustment** to the debt.

- **Formula:** `After-tax WACC = (1 - tc) * rD * (D/V) + rE * (E/V)`

- **Calculation:** `(1 - 0.30) * 4.10% * 0.4 + 5.5% * 0.6`

- **Result:** `0.7 * 4.10% * 0.4 + 3.30%` = `1.15% + 3.30%` = **4.45%**.

\--------------------------------------------------------------------------------

💡 The Practical Conclusion: How this enforces the "Golden Rule"

Now, imagine your new project is forecasted to generate **€10,000 in pure Operating Cash Flow** next year.

If you were a junior analyst, you might be tempted to say: *"Wait, we are using 40% debt to fund this! I need to subtract the 4.10% interest payments from the €10,000 cash flow to show how much money is left over, and then calculate the tax savings!"*

As a top-tier financial manager, you stop them and apply **Rule 4: Separate investment and financing decisions**. Here is your practical "30 e lode" explanation to the junior analyst:

- **Leave the Cash Flow alone (The Investment Decision):** "We will evaluate the cash flow as if it is 100% equity financed. We will **not** deduct a single euro of interest from that €10,000. The €10,000 represents the pure industrial value of our project."

- **Use the WACC (The Financing Decision):** "Look at our WACC calculation. By multiplying the 4.10% cost of debt by `(1 - 0.30)`, we mathematically shrank the cost of our debt down to reflect the tax savings. We captured the tax shield *inside* the 4.45% discount rate."

- **The Final NPV:** "Because we are discounting the pure €10,000 cash flow by a mathematically lower, tax-adjusted rate (4.45%), we automatically inflate the project's Present Value. This perfectly accounts for the financial benefit of the debt without ever having to touch the cash flow table!"

**⚠️ One Final Exam Warning:** You can only use this specific **4.45% WACC** to discount the project's cash flows if the new project has the exact same risk level as the firm's existing projects, and it will be financed using that exact same 40/60 Debt-to-Equity split. If the project is riskier, or uses a different capital structure, you cannot use the company's WACC; you must calculate a custom cost of capital specifically for that project.

How do we handle taxes in WACC calculations?

What happens if a project's risk differs from the firm's?

Can we use WACC for mutually exclusive projects?

so we have to mulòtiplie 10k per wacc and we will find the income required?

No, you do not multiply the €10,000 cash flow by the WACC! This is a very important mathematical distinction to make for the exam.

In capital budgeting, the WACC is used as a **discount rate**, not a simple multiplier. To find the present value of a future cash flow, you must **divide the cash flow by (1 + WACC)**.

Here is exactly how you handle that €10,000 Operating Cash Flow if it is expected at the end of Year 1:

- **The Math:** You calculate the Present Value (PV) by dividing the cash flow by 1 plus the discount rate. Using our 4.45% WACC, the formula is: `PV = 10,000 / (1 + 0.0445)^1`.

- **The Logic:** The WACC represents the opportunity cost of capital. By placing it in the denominator of the equation, you are "discounting" the future money back to today's value, which reduces the nominal amount to properly account for both time and risk.

**Where does the multiplication happen?** It sounds like you might be confusing Capital Budgeting with **Economic Value Added (EVA)**, which is a tool used in Financial Analysis to evaluate past performance.

When calculating EVA to see if a firm generated wealth, you *do* calculate the minimum required income by multiplying the **cost of capital by the Total Capital invested** (long-term debt plus equity). However, the €10,000 in our simulation was an *Operating Cash Flow*, not the total capital invested.

**For your "30 e lode":** Keep these operations separated!

- In **Financial Analysis (EVA)**, you multiply the WACC by the *Total Capital* to find the required income benchmark.

- In **Capital Budgeting (NPV)**, you divide the *Operating Cash Flows* by (1 + WACC) to discount them back to their present value.

How do you calculate EVA to evaluate a firm's performance?

What happens to NPV if the project's risk level changes?

Can we use IRR to decide between two different projects?

ok then after dividijng and finding the present value it means that we already subtract the taxes?

Not exactly! This is a very common trap, and understanding the difference here will definitely impress your professor.

Dividing your cash flow by the WACC does **not** subtract the company's taxes for you. There are actually **two different tax impacts** happening in capital budgeting, and they are handled in two completely different places:

**1\. Operating Taxes (Handled in the Cash Flows)** According to **Rule 5 of Capital Budgeting: Forecast Cash Flows after Taxes**, you must explicitly calculate and subtract the regular corporate taxes *before* you do any discounting. In **Panel B (Operating Cash Flow)**, you take your Revenues, subtract your Expenses and Depreciation to find your Pretax Profit, and then you must manually calculate and subtract the taxes to get your Profit After Tax.

- *Conclusion:* The €10,000 Operating Cash Flow number you are dividing by the WACC must **already have the operating taxes subtracted from it**.

**2\. The Tax Shield of Debt (Handled in the WACC)** So, what tax impact does the WACC handle? It handles the **tax shield** —the specific extra tax savings the company gets because interest payments on debt are tax-deductible. Because we evaluate the cash flows as if the project were 100% equity-financed, we intentionally ignore the interest payments, which means we also temporarily ignore the tax savings those interest payments would generate. Instead of putting those savings in the cash flow table, we capture them by multiplying the cost of debt by inside the After-Tax WACC formula.

**The "30 e lode" Summary:**

- You subtract the **operating taxes** manually in your spreadsheet (Panel B) to find your pure, after-tax industrial cash flow.

- When you divide that cash flow by (1 + WACC) to find the present value, the WACC is not subtracting taxes; rather, it is adding back the **financial tax benefits (the tax shield)** of your debt.

Does this make the division between the industrial side (cash flows) and the financial side (WACC) completely clear?

What if the project has different risk than the firm?

How is the interest tax shield calculated in WACC?

Does the NPV change if we use all-equity financing?

can you make a practical example?

Let's look at the **Vega Corporation** exam exercise from your materials to see exactly how these two different tax effects are kept completely separate in practice.

**Step 1: Subtracting Operating Taxes (The Cash Flow Table)** In Year 1, Vega Corporation forecasts **Revenues of €1,000** and cash **Expenses of €450**. After subtracting **€500 for depreciation**, the project shows a **Pretax profit of €50**.

- Here is where you manually subtract the operating taxes: applying the **40% tax rate** to the €50 profit gives exactly **€20 in taxes**.

- You subtract this €20 to find the **Profit after tax of €30**, and then add back the €500 depreciation to get your pure **Operating Cash Flow of €530**.

- **The logic:** You paid the €20 in operating taxes as if the project were 100% equity-financed, completely ignoring any interest payments. **The €530 cash flow you bring forward has already had the operating taxes subtracted from it**.

**Step 2: Capturing the Tax Shield (The WACC Calculation)** Vega is actually financed with 50% debt and 50% equity, and its **cost of debt is 7%**. Because you ignored the interest payments in Step 1, you must capture the tax savings of that debt (the tax shield) here in the discount rate.

- When calculating the WACC, you multiply the 7% cost of debt by **(1 - 0.40)**.

- This mathematical adjustment shrinks the cost of debt to reflect the tax savings, resulting in an **After-tax WACC of 8.6%**.

**Step 3: The Present Value Division** In Panel D, you calculate the Total Project Cash Flow for Year 1 by taking your €530 operating cash flow and subtracting a €250 investment in working capital, leaving you with **€280**. To find the Present Value, you divide this cash flow by the WACC discount factor:

- **Calculation:** **€280 / (1 + 0.086)^1 = €257.83**.

**The Practical Conclusion:** The €280 numerator *already had your €20 operating taxes subtracted*. By placing the 8.6% WACC in the denominator, you did not subtract taxes again; rather, you applied a lower, tax-adjusted discount rate that artificially boosted your final €257.83 Present Value to reward the project for the tax shield generated by the debt.

What is the difference between NPV and IRR?

How do I calculate Economic Value Added (EVA)?

When should I use a custom WACC instead of the firm's?

okay so in the first panel capital investment we don't consider interesst payment neither in the net working capital, we compute the intrest payment by shkrinking wacc, otherwise we will have a higher return right? so if the tax rate was higher wacc will be lower

You have perfectly connected all the pieces! Your logic is completely correct.

First, you are absolutely right that **we never consider interest payments in the cash flow panels** —not in Panel A for Capital Investment, not in Panel C for Working Capital, and not even in Panel B for Operating Cash Flow. This strictly enforces **Rule 4 of capital budgeting: Separate investment and financing decisions**. By ignoring interest payments, you are evaluating the project as if it were entirely equity-financed to see its pure, stand-alone industrial value,.

Second, your intuition about "shrinking" the WACC is exactly how we account for the financial benefits of debt. Because interest payments are tax-deductible, they reduce the firm's taxable income and create a "tax shield". To capture this tax saving without mixing it into the cash flow tables, we adjust the discount rate. In the After-tax WACC formula, we multiply the cost of debt by , where is the corporate tax rate,. This mathematical adjustment physically "shrinks" the effective cost of debt to reflect the tax deduction,.

Finally, your conclusion is a "30 e lode" deduction: **if the tax rate (****) is higher, the WACC will indeed be lower**. Here is why the math works perfectly:

- As the tax rate () increases, the multiplier becomes a smaller number.

- This smaller multiplier reduces the after-tax cost of debt, which pulls the overall WACC down,,.

- Because WACC is the discount rate (the denominator), dividing your "all-equity" cash flows by this lower WACC mathematically **increases the project's Net Present Value (NPV)**.

You successfully proved that a higher corporate tax rate makes the debt's tax shield more valuable, which lowers your cost of capital and ultimately boosts the value of your project!

What happens to NPV if the corporate tax rate increases?

Can we use WACC if the project is riskier than the firm?

What is the formula for the tax shield in WACC?

example of wacc in practice

Let's walk through a practical exam exercise from your materials—the **Event Corporation** case—to see exactly how a financial manager builds the WACC from scratch and applies the logic we just discussed.

**Step 1: Gather the Raw Data** Event Corporation is evaluating a new project (a gift shop) and needs to calculate its discount rate. The financial manager collects the following market and company data:

- **Risk-free rate (****):** 5%

- **Risk premium on the firm's stock:** 13%

- **Cost of debt (****):** 8.3%

- **Tax rate (****):** 38%

- **Debt-to-assets ratio (D/V):** 0.7 (This means the firm is financed 70% by debt, which logically means the remaining 30% is equity, so E/V = 0.3).

**Step 2: Calculate the Cost of Equity (****)** The shareholders demand the risk-free rate plus a risk premium to compensate them for the market risk they are taking.

- .

**Step 3: Calculate the After-Tax Cost of Debt** Here is where your excellent intuition about "shrinking" the WACC comes into play! The stated cost of debt is 8.3%, but the interest payments are tax-deductible.

- We multiply the cost of debt by :

- .

- *Notice the practical impact:* Because of the high 38% corporate tax rate, the effective cost of the debt physically shrinks from 8.3% down to roughly 5.15%.

**Step 4: Blend the Final WACC** Now, the manager blends the cost of equity and the after-tax cost of debt according to their exact weights in the firm's capital structure (30% equity, 70% debt).

- **Formula:**

- **Calculation:**

- **Result:** .

**Step 5: The Capital Budgeting Application** With the WACC calculated at exactly 9%, the financial manager now moves to **Panel D** of their capital budgeting spreadsheet.

- They forecast the project's operating cash flows as if the project were entirely equity-financed, intentionally ignoring all interest payments so they don't mix the investment decision with the financing decision.

- Then, they divide those pure cash flows by discount factors based on the **9% WACC** (e.g., dividing Year 1 cash flows by , Year 2 by ).

- Because the 9% discount rate is mathematically lower than it would be without taxes (thanks to the 38% tax shield shrinking the debt cost), the final Net Present Value (NPV) is automatically boosted, perfectly rewarding the project for the financial benefits of the debt.

*(Remember the Golden Rule for the exam: You can only use this 9% WACC to discount the new project's cash flows if the new project carries the same level of risk as the firm's existing business and will be financed with the exact same 70/30 debt-to-equity split**.)*

What happens to NPV if the corporate tax rate increases?

Should interest payments be deducted in the cash flow panels?

Can we always use the firm's WACC for every project?

market rate refers to the hurdle rate or opportunity cost of capital right?

You are absolutely correct!

The **opportunity cost of capital** is the minimum rate of return that shareholders require when investing in a project, and it is determined by the return they could expect to earn from the best alternative investment with similar risk in the financial markets. Because a project's return must clear this specific threshold in order to create actual value for shareholders, the cost of capital is also referred to as the **hurdle rate**.

The concept is directly tied to the "market rate" because this minimum required return depends entirely on external factors—specifically, **the rates of return that investors could obtain elsewhere in the financial markets**. Therefore, financial managers must look directly to the financial markets to measure the opportunity cost of capital for their firm's investment projects. If the firm can no longer offer returns that meet or exceed this market-driven hurdle rate, it should return the cash so shareholders can invest it themselves.

How does the Internal Rate of Return (IRR) relate to WACC?

What happens if a project has different risk than the firm?

Explain the difference between SML and CML in risk measurement.

let's study break even analysis and operating leverage

Excellent choice! We are now stepping into the realm of **Project Analysis**, specifically looking at how financial managers deal with uncertainty and assess "how bad things can get before the project becomes a loser".

Here is how you need to structure these two concepts for your exam:

1\. Break-Even Analysis

Break-even analysis examines revenues and costs to identify the exact point where a project stops losing money and starts generating value. However, there are two different ways to look at it:

- **Accounting Break-Even:** This is the traditional approach that calculates the sales volume at which total revenues exactly equal total costs. From that point onward, the firm begins to show an accounting profit.

- **Financial Break-Even (The NPV Approach):** Because you already know that "only cash flow is relevant" and accounting profits ignore the time value of money, top-tier financial managers focus on the financial break-even point. This analysis aims to identify the exact quantity of output at which the project's **Net Present Value (NPV) equals zero**. At this specific point, the present value of the discounted future cash flows perfectly matches the initial capital investment.

2\. Operating Leverage

Operating leverage is all about the firm's cost structure, specifically **the proportion of fixed costs to total costs**. A business with a high level of fixed costs is said to have high operating leverage.

- **The "Boom or Bust" Effect:** The core idea is that fixed costs do not decline when sales drop. Therefore, if a firm has high operating leverage, any shortfall in sales will have a massively magnified, negative impact on its profitability. Conversely, during an economic boom, a firm whose costs are largely fixed will make an absolute "killing" because revenues surge while costs remain mostly static.

- **Measuring it (DOL):** Operating leverage is typically defined in terms of accounting profits and is measured by the **Degree of Operating Leverage (DOL)**. It is calculated as the percentage change in profits generated by a 1% change in sales.

💡 The "30 e lode" Connection: Operating Leverage and Beta ()

To truly impress Professor Domenichelli, you must link Operating Leverage back to our previous discussion on Risk and the CAPM!

How does operating leverage affect a company's market risk? Firms with a high fixed-cost structure cannot easily adjust their costs in response to macroeconomic changes or market downturns. This means that systematic, market-wide events have a much stronger impact on their profitability.

**The conclusion:** The higher a firm's operating leverage, the higher its exposure to systematic market risk, which mathematically results in a **higher Beta (****)** for the company's stock.

Do you want to continue exploring Project Analysis, perhaps by looking at how managers use **Sensitivity and Scenario Analysis** or the concept of **Real Options**?

How do we calculate accounting and financial break-even points?

How do managers use Sensitivity and Scenario Analysis?

Can we explore the concept of Real Options?

show me a pratical example

Let's look at the practical examples extracted directly from the data in the sources.

📝 Practical Example 1: Operating Leverage (The "Boom or Bust" Effect)

Imagine your firm has heavily invested in automated machinery, meaning your cost structure is mostly made up of fixed costs.

Because you have high fixed costs, you calculate your **Degree of Operating Leverage (DOL) to be 4.5**. Here is what that means in practice:

- **The Boom:** If the economy expands and your **sales increase by just 1%**, your profits will not just grow by 1%. Because your fixed costs do not increase as you produce more, that tiny 1% bump in revenues will result in a massive **4.5% rise in profits**. You make a "killing" during the boom.

- **The Bust:** Conversely, if a recession hits and your sales drop by 1%, your profits will violently crash by 4.5%. Your fixed costs do not decline when your sales drop, meaning any shortfall in revenues has a severely magnified impact on your bottom line.

📝 Practical Example 2: Financial Break-Even Analysis

Imagine you are evaluating a new project and you want to know "how bad things can get before the project becomes a loser". You don't care about the accounting break-even; you want the **financial break-even**, which is the exact point where the **Net Present Value (NPV) drops to zero**.

You run the numbers on your key variables to see exactly how much they can change before NPV hits zero:

- **Sales:** You calculate that your estimated **sales can drop by exactly 6.3%** before the NPV hits zero.

- **Cost of Goods Sold:** You calculate that your **costs can increase by exactly 3.2%** before the NPV hits zero.

**The Financial Manager's Conclusion:** These numbers are your absolute limits. If sales drop by 6.4%, or if your costs increase by 3.3%, the project's NPV turns negative, meaning the investment will actively destroy shareholder wealth. By knowing these exact financial break-even points, you know exactly where the danger zones are before you commit a single euro to the project.

How does sensitivity analysis differ from break-even analysis?

What are real options in project analysis?

How do you calculate the degree of operating leverage?

cosa si intende per leva operativa^

La **leva operativa** (operating leverage) è un indicatore legato alla struttura dei costi di un'azienda e si riferisce specificamente alla **proporzione di costi fissi rispetto ai costi totali**. Un'impresa con un'elevata percentuale di costi fissi si dice che ha un'alta leva operativa.

Il meccanismo fondamentale alla base della leva operativa è l'effetto "boom o bust" (espansione o crollo) che abbiamo esplorato nel nostro esempio pratico precedente. Poiché **i costi fissi non si riducono al diminuire delle vendite**, qualsiasi calo dei ricavi avrà un impatto amplificato e pesantemente negativo sulla redditività. Al contrario, durante una fase di espansione economica (boom), un'azienda i cui costi sono prevalentemente fissi genererà profitti eccezionali, poiché i ricavi aumentano mentre la base dei costi rimane quasi del tutto inalterata.

Dal punto di vista della misurazione, la leva operativa viene generalmente valutata sui profitti contabili (piuttosto che sui flussi di cassa) attraverso il **Grado di Leva Operativa (DOL - Degree of Operating Leverage)**. Questo indice è calcolato come il **rapporto tra la variazione percentuale dei profitti e la variazione percentuale delle vendite**.

In altre parole, il DOL misura la variazione percentuale dei profitti generata da un cambiamento dell'1% nelle vendite. Proprio come avevamo dedotto insieme prima, se calcoliamo un DOL di 4,5, significa che per ogni variazione dell'1% del fatturato, i profitti dell'azienda subiranno una variazione amplificata del 4,5%.

Qual è la differenza tra break-even contabile e finanziario?

In che modo i costi fissi influenzano il beta aziendale?

Come si calcola il Grado di Leva Operativa (DOL)?

it's the same as operatinf profit margin?

No, they are completely different financial concepts! It is a classic exam trap to confuse a company's cost structure with its sales profitability.

**1\. Operating Leverage (Risk & Cost Structure)** As we just discussed, operating leverage deals entirely with the firm's cost structure—specifically the proportion of fixed costs relative to total costs. It is measured by the **Degree of Operating Leverage (DOL)**, which calculates the percentage change in profits generated by a 1% change in sales. It tells you how *sensitive* your profits are to an economic boom or bust.

**2\. Operating Profit Margin (Profitability for All Financiers)** This is a measure of profitability, not risk. It evaluates the proportion of sales that translates into profit from the perspective of **both shareholders and debtholders**. Because a company financed partly by debt must use a portion of its sales profits to pay interest to lenders, you calculate this margin by adding the after-tax interest back into the net income.

- **Formula:** **(After-tax interest + Net income) / Sales**.

**3\. Profit Margin (Profitability for Shareholders Only)** Just to be absolutely precise for a "30 e lode", if you want to measure only the proportion of sales that finds its way into profits for the *shareholders* (meaning the lenders have already taken their interest cut), you use the standard Profit Margin.

- **Formula:** **Net income / Sales**.

**💡 The "30 e lode" Connection:** While Operating Leverage dictates how profits *react* to sales volume changes, the **Operating Profit Margin** is famously tied to a firm's *asset efficiency*. The sources highlight a clear market trade-off: industries that are highly efficient and have a very high Asset Turnover (like supermarkets) almost always operate on a very low Operating Profit Margin. Conversely, businesses with low asset turnover generally require high operating profit margins to survive.

What is the difference between accounting and financial break-even?

How does high operating leverage affect a company's Beta?

Explain sensitivity and scenario analysis in project evaluation.

che significa profitti contabili? cash flow? e flussi di cassa?

Ottima domanda. Iniziamo subito con un piccolo chiarimento terminologico: **"cash flow" e "flussi di cassa" sono esattamente la stessa cosa**. "Flussi di cassa" è semplicemente la traduzione italiana del termine inglese "cash flow".

La vera distinzione cruciale da fare all'esame, specialmente quando si parla di Capital Budgeting e valutazione dei progetti, è quella tra **profitti contabili (accounting profits)** e **flussi di cassa (cash flows)**. Le tue fonti sono estremamente chiare su questo punto ed enunciano una vera e propria regola d'oro: *scontare i flussi di cassa, non i profitti contabili*.

Ecco la differenza sostanziale:

1\. I Profitti Contabili (Accounting Profits o Net Income)

I profitti contabili rappresentano l'utile di un'azienda calcolato secondo le regole e i principi contabili. La caratteristica principale che devi ricordare è che **il profitto non coincide con il denaro reale a disposizione**. I profitti contabili sono influenzati da decisioni soggettive e discrezionali. L'esempio classico fornito dai testi è l'ammortamento (depreciation) e le spese in conto capitale (capital expenditures):

- Quando l'azienda acquista un costoso macchinario da 1 milione di euro, il contabile non registra quella spesa come una perdita contabile immediata, ma spalma quel costo lungo la vita utile del macchinario tramite l'ammortamento.

- Di conseguenza, **l'ammortamento abbassa il profitto contabile anno dopo anno, ma non rappresenta un'uscita fisica di denaro** in quegli anni.

2\. I Cash Flows (o Flussi di Cassa)

Il cash flow è la misura reale e oggettiva del denaro. Rappresenta semplicemente **la differenza tra il denaro (cash) fisicamente incassato e il denaro fisicamente pagato** in un dato periodo. Le fonti usano una frase molto pragmatica per spiegare perché contano solo i flussi di cassa: *"Il profitto non è denaro. Non puoi comprare cose con il profitto; compri cose con il denaro (cash)"*.

- Riprendendo l'esempio di prima: l'acquisto del macchinario da 1 milione di euro è un'uscita di cassa immediata (e quindi abbatte il cash flow di quest'anno), anche se a livello contabile il costo verrà spalmato nel futuro.

Come si passa dal Profitto Contabile al Flusso di Cassa?

Se per valutare la bontà di un progetto di investimento (calcolando il Valore Attuale Netto o NPV) ti basi sui profitti, otterrai un risultato sbagliato. Per trovare i veri flussi di cassa a partire dai profitti contabili, il manager finanziario deve effettuare delle rettifiche:

- **Aggiungere gli ammortamenti:** Poiché l'ammortamento ha abbassato il profitto ma non è una vera uscita di cassa, devi ri-sommarlo al profitto.

- **Sottrarre le spese in conto capitale e gli investimenti in capitale circolante:** Quando acquisti un asset fisico o investi in scorte di magazzino, il denaro esce davvero dalle casse. Pertanto, devi sottrarre questi importi per trovare il tuo vero flusso di cassa.

In sintesi, all'esame ricorda questa massima: **le spese in capitale influenzano i flussi di cassa ma non i profitti, mentre l'ammortamento influenza i profitti ma non i flussi di cassa**.

How do fixed costs specifically affect a company's Beta?

What is the difference between accounting and financial break-even?

How does sensitivity analysis help in project break-even planning?

Qual è la differenza tra break-even contabile e finanziario?

Il **break-even contabile** è l'approccio tradizionale che esamina i ricavi e i costi per **determinare il volume di vendite al quale i ricavi totali eguagliano esattamente i costi totali**. Da quel preciso punto in poi, l'azienda smette di essere in perdita e inizia a generare profitti contabili.

Il **break-even finanziario**, al contrario, è una variante che si concentra sul rendimento finanziario reale e **mira a identificare l'esatta quantità di output (o vendite) in corrispondenza della quale il Valore Attuale Netto (NPV) del progetto scende a zero**. In altre parole, questo punto di pareggio viene raggiunto quando il valore attuale dei flussi di cassa futuri scontati del progetto corrisponde perfettamente all'investimento di capitale iniziale.

La differenza sostanziale tra i due concetti risiede nel fatto che **il break-even contabile ignora il valore temporale del denaro**, accontentandosi di mostrare un utile "sulla carta". Il break-even finanziario, invece, si basa sulla regola d'oro del capital budgeting secondo cui solo i flussi di cassa sono rilevanti. Integrando il costo opportunità del capitale come tasso di attualizzazione, il break-even finanziario indica a un manager l'esatto margine di sicurezza di un progetto: mostra con esattezza di quanto possono calare le vendite o aumentare i costi prima che l'investimento inizi attivamente a distruggere la ricchezza degli azionisti.

What are sensitivity and scenario analysis?

How do managers use real options in project analysis?

How does operating leverage affect a company's Beta?

Overview audio

Presentazione

Overview video

Mappa mentale

Report

Flashcard

Quiz

Infografica

Tabella di dati

Risposta pronta.

App Google