---
tags: [data-mining, esercitazione, kdd, association-rules, classification, clustering, exam-prep]
date_created: 2026-05-19
source: Elmasri & Navathe — Chapter 28, Data Mining Concepts
---

# 🔍 Data Mining — Full Study Session (Chapter 28)

> **Exam Score After Re-Test:** All weak points resolved ✅
> **Source:** Elmasri & Navathe, *Fundamentals of Database Systems*, Chapter 28

---

## 📋 Quick Reference Cheat Sheet

```
KDD Pipeline (6 steps):
Selection → Cleansing → Enrichment → Transformation → Mining → Reporting

Association Rules:
  Support    = how FREQUENT is the itemset (prevalence)
  Confidence = P(Y | X already bought) (strength)
  Antimonotonicity: superset of a SMALL itemset is also SMALL → prune immediately
  Algorithms: Apriori → Sampling → FP-Tree → Partition

Classification (Supervised):
  Entropy         = measures chaos (1.0 = max, 0.0 = pure)
  Information Gain = I(initial) - E(attribute) → pick highest = root node
  Output          = predefined CATEGORY

Regression (Supervised):
  Output = continuous NUMBER: Y = f(X1...Xn)
  Linear Regression = straight trend line through data

Clustering (Unsupervised):
  K-Means: Euclidean distance, terminates at Squared Error Criterion
  BIRCH:   sequential reads, hierarchical tree, 2 params:
           → Available RAM + Radius Threshold

Genetic Algorithms (inspired by Darwin):
  4 mechanisms: Strings → Fitness Function → Cross-over → Mutation

Big Data Stack:
  Hadoop (distributes data across servers) + Mahout (mining on top of Hadoop)
```

---

## 🧠 Block 1: KDD Pipeline & Theoretical Foundations

### What is Data Mining?
Data Mining is the **discovery of implicit, previously unknown, and useful patterns** from large amounts of data. It uses **inductive logic** — the machine discovers rules from raw data, without being told what to look for. This is different from:
- **SQL queries** → only retrieve exact, predefined results.
- **Expert Systems** → apply static, human-written rules.

### The 6 Phases of KDD (Knowledge Discovery in Databases)
Data Mining is only **Step 5** of the full KDD pipeline:

| Step | Phase | Example |
|------|-------|---------|
| 1 | **Data Selection** | Select sales data from a specific region |
| 2 | **Data Cleansing** | Fix invalid zip codes, remove bad records |
| 3 | **Enrichment** | Append external credit rating or income data |
| 4 | **Transformation/Encoding** | Group items into categories (Audio, Video, Camera) |
| 5 | **Data Mining** | Run Apriori, K-Means, Decision Tree algorithms |
| 6 | **Reporting & Display** | Visualize discovered patterns as charts and tables |

### The 4 Goals of Data Mining
- **Prediction** — Forecast future behavior (e.g., what consumers will buy under a discount).
- **Identification** — Detect an event or entity (e.g., intrusion detection, authentication).
- **Classification** — Partition data into categories (e.g., customer segments).
- **Optimization** — Maximize output variables under constraints (like Operations Research objective functions).

### 5 Types of Knowledge Discovered
1. **Association Rules** — {Milk} ⇒ {Juice} (items bought together).
2. **Classification Hierarchies** — Partition population into credit risk levels.
3. **Sequential Patterns** — Camera → Supplies (within 3 months) → Accessory (within 6 months).
4. **Time Series Patterns** — Two stocks showing identical closing price trends.
5. **Clustering** — Group patients by similarity of drug side effects.

---

## 🛒 Block 2: Association Rules

### Formal Definition
An association rule has the form: **$X \Rightarrow Y$** (LHS ⇒ RHS)
- The set $X \cup Y$ is called an **itemset**.
- The rule states: *"If a customer buys X, they are likely to also buy Y."*

### Two Key Metrics
| Metric | Formula | Also Called |
|--------|---------|-------------|
| **Support** | % of transactions containing $X \cup Y$ | Prevalence |
| **Confidence** | $\frac{\text{Support}(X \cup Y)}{\text{Support}(X)}$ | Strength |

### The Combinatorial Problem
A supermarket with $m$ items has $2^m$ possible itemsets — computationally impossible to test all.

### Antimonotonicity Property (Key Exam Answer)
> **"A superset of a small (infrequent) itemset is also small."**

If {Caviar, Champagne} is below the minimum support threshold, then **ANY itemset containing them** — {Caviar, Champagne, Bread}, {Caviar, Champagne, Milk}, etc. — is **immediately pruned** without scanning the database.

Twin property: **Downward Closure** — "A subset of a large (frequent) itemset is also large."

### Algorithms for Association Rules

#### 1. Apriori Algorithm
- First algorithm to use Antimonotonicity and Downward Closure.
- Works in **multiple passes** (one full database scan per pass).
- **Pass 1:** Count all individual items → create $L_1$ (frequent 1-itemsets).
- **Pass k:** Extend $L_{k-1}$ to create candidates $C_k$ → scan database → create $L_k$.
- Stops when $L_k$ is empty.
- **Weakness:** Generates too many candidates. With 1,000 frequent items → $\binom{1000}{2} = 499,500$ candidate pairs for Pass 2 alone.

#### 2. FP-Tree (Frequent-Pattern Tree) — Apriori's Successor
- **Eliminates candidate generation entirely.**
- Reads the database **exactly twice**:
  1. First pass → finds frequent 1-itemsets.
  2. Second pass → builds the compressed FP-Tree in memory.
- Mining uses **FP-Growth** with a divide-and-conquer strategy on conditional FP-trees.

#### 3. Sampling Algorithm
- Takes a small random sample that fits in RAM.
- Runs Apriori on the sample with lower minimum support.
- Uses the **negative border** concept to catch missed frequent itemsets.
- Makes one final pass over the full database to verify.

#### 4. Partition Algorithm
- Divides the database into non-overlapping partitions that fit in RAM.
- Finds **local frequent itemsets** for each partition (no false negatives).
- Merges all local results into global candidates (may have false positives).
- One final pass to verify global candidates and eliminate false positives.

### Other Association Rule Types
- **Hierarchical Associations** — cross-hierarchy rules (e.g., "Healthy-brand Frozen Yogurt ⇒ Bottled Water").
- **Multidimensional Associations** — include non-item dimensions: `Time(6:30–8:00) ⇒ Items_bought(Milk)`. Quantitative attributes are discretized into buckets (Low/Medium/High Income).
- **Negative Associations** — e.g., "60% of customers who buy chips do NOT buy bottled water." Very hard to compute due to exponential combinations.

---

## 🌳 Block 3: Classification (Supervised Learning)

### What is Classification?
Learning a model from **pre-labeled training data** to assign new records to predefined classes (e.g., Loanworthy: Yes/No). Also called **supervised learning**.

### Algorithm 28.3: Decision Tree Induction
1. Start with all training records at the root.
2. If all records belong to the same class → create a leaf node.
3. Select attribute $A_i$ with the **highest Information Gain**.
4. Label the node with $A_i$ and branch for each value of $A_i$.
5. Recurse on each subset until all leaves are pure.

### The Math: Entropy and Information Gain

**Entropy** (measures chaos/disorder):
$$I(s_1, s_2, \dots, s_n) = -\sum_{i=1}^{n} p_i \log_2(p_i) \quad \text{where } p_i = s_i/s$$

| Entropy Value | Meaning |
|---|---|
| **1.0** | Maximum chaos — perfectly split between classes (e.g., 50% Yes, 50% No) |
| **0.0** | Perfect purity — all records are the same class |

**Expected Entropy of attribute A:**
$$E(A) = \sum_{j=1}^{m} \frac{|S_j|}{s} \times I(s_{1j}, \dots, s_{nj})$$

**Information Gain:**
$$\text{Gain}(A) = I(s_1, \dots, s_n) - E(A)$$

→ **The attribute with the HIGHEST Gain becomes the root node.**

### Textbook Example (6 Loan Applicants)

| Attribute | Gain | Result |
|---|---|---|
| Married | 0.08 | ❌ Weak |
| **Salary** | **0.67** | ✅ **Root Node** |
| Acct_balance | 0.08 | ❌ Weak |
| Age | 0.46 | 🟡 Second split |

Final Decision Tree:
```
         [Salary?]
        /    |    \
     <20K  20-50K  ≥50K
      |       |       |
   Class:No [Age?] Class:Yes
           /     \
         <25     ≥25
          |        |
       Class:No  Class:Yes
```

---

## ⚙️ Block 4: Clustering (Unsupervised Learning)

### What is Clustering?
Partitioning data into groups where **records within a group are similar** and **records across groups are dissimilar**. No predefined labels — hence **unsupervised learning**.

### When MUST you use Clustering instead of Classification?
When **no labeled training data exists**. Example: analyzing gene expression data from a new disease where no prior categorization exists.

### Euclidean Distance (Similarity Metric)
$$\text{Distance}(r_j, r_k) = \sqrt{\sum_{i=1}^{n}(r_{ji} - r_{ki})^2}$$
Smaller distance = more similar points.

### Algorithm 28.4: K-Means
**Input:** Database of $m$ records, desired number of clusters $k$.

```
1. Randomly choose k records as initial centroids
2. REPEAT:
   a. Assign each record to the cluster with the nearest centroid (min Euclidean distance)
   b. Recalculate each centroid as the mean of all records in its cluster
3. UNTIL convergence (Squared Error Criterion stops decreasing)
```

**Termination — Squared Error Criterion:**
$$\text{Error} = \sum_{i=1}^{k} \sum_{r_j \in C_i} \text{Distance}(r_j, m_i)^2$$

**Limitation:** Assumes entire dataset fits in RAM → fails for very large databases.

### BIRCH Algorithm (Scalable Clustering)
**Two input parameters (vs. K-Means's one):**
1. **Available Main Memory** (hardware constraint)
2. **Initial Radius Threshold** (geometric constraint — defines micro-sphere size)

**How it works:**
- Reads records **sequentially**, one at a time.
- Inserts each record into a compact **hierarchical tree** in memory.
- Each leaf node = a **micro-cluster** (sphere defined by center + radius).
- If memory runs out → **increase radius threshold** → neighboring micro-spheres merge → fewer clusters → memory freed.
- **Linear computational complexity** — scales proportionally with number of records.

---

## 📈 Block 5: Advanced Models & Big Data

### Regression
- A special case of Classification where the output is a **continuous number** instead of a category.
- Formula: $Y = f(X_1, X_2, \dots, X_n)$
- When $f$ is linear → **Linear Regression** (most common statistical technique).
- Example: Predicting exact survival probability (87.5%) vs. Classification's Yes/No.

> **Key distinction:** Classification draws a **boundary** between groups. Regression draws a **trend line** to predict a number.

### Neural Networks
- Inspired by biological neurons.
- Can be supervised or unsupervised.
- Very powerful for pattern recognition.
- **Critical flaw → "Black Box":**

| | Decision Trees | Neural Networks |
|---|---|---|
| **Accuracy** | Good | Excellent |
| **Explainability** | ✅ Clear logical path | ❌ Cannot explain output |
| **Output format** | Human-readable rules | Highly quantitative numbers |
| **Time Series** | OK | ❌ Poor |

### Genetic Algorithms
Inspired by **Charles Darwin's theory of natural selection**. Introduced by Holland (1975).

**4 Biological Mechanisms:**

| Biological Concept | GA Equivalent | Description |
|---|---|---|
| Individual organism | **Strings** | Possible solutions encoded as character strings |
| Survival of the fittest | **Fitness Function** | Scores each solution — weak ones die |
| Reproduction | **Cross-over** | Combine half of solution A + half of solution B |
| Random DNA change | **Mutation** | Randomly alter one piece of the code |

**Drawbacks:** Large overproduction of candidate solutions, randomized search, requires substantial computing power.

### Big Data: Hadoop + Mahout
For petabyte-scale Data Mining across distributed server clusters:

```
Raw Data (petabytes, distributed across hundreds of servers)
        ↓
   [HADOOP] — splits & processes data in parallel across the cluster
        ↓
   [MAHOUT] — Data Mining library running on top of Hadoop
              (brings K-Means, clustering, classification to Big Data scale)
        ↓
  Discovered Knowledge
```

### Commercial Tools & Interfaces
- **ODBC** (Open Database Connectivity) — universal standard allowing mining tools to connect to any database (Oracle, SQL Server, Access).
- **GUI** — graphical interfaces for data visualization.
- **API** — C libraries and DLLs for embedding mining engines into applications.

---

## 🔗 Related Notes
- [[Data_Mining_Hub]] — Central hub for all Data Mining concepts
- [[Clustering_KMeans]] — K-Means deep dive
- [[Classificazione_Decision_Tree]] — Decision Trees deep dive
- [[Regole_di_Associazione]] — Association Rules deep dive
- [[Data_Warehouse]] — OLTP vs OLAP foundations
- [[Fonte_Data_Warehouse_Mining_Notes]] — Source notes

---

*Session completed: 2026-05-19 | Source: Elmasri & Navathe Ch.28 + personal notes*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
