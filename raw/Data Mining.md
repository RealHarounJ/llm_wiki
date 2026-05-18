To understand data mining, it is essential to differentiate between the systems that generate data and the systems that store it for analysis.

- **Operational Databases (OLTP) vs. Data Warehouses (OLAP)**
- **Operational Databases (OLTP):** These systems manage day-to-day, real-time business transactions. The provided Enterprise Resource Planning (ERP) Conceptual Data Model is an excellent example of an operational system. It structurally organizes entities like "Parties" (Customers/Suppliers), "Products" (catalogs and pricing), sales documents (Orders and Invoices), and physical "Warehouse Management". Note that in the ERP model, "Warehouse" refers to a _physical facility_ tracking the exact 3D coordinates of physical inventory (aisles, levels). Data is retrieved from these operational systems using structured SQL queries, such as calculating the total revenue of a product or finding the top-selling product in a category.
- **Data Warehouses (OLAP):** Unlike physical warehouses for goods, a **Data Warehouse** is a large, centralized digital repository that integrates data from multiple heterogeneous sources (like the aforementioned ERP operational databases) to support long-term, historical analysis. Instead of focusing on day-to-day operations, Data Warehouses use Online Analytical Processing (OLAP). They organize data using a multi-dimensional view called a **Data Cube** (e.g., analyzing sales across dimensions like time, product type, and location). This enables managers to perform operations like _drill-down_ (moving from yearly to monthly sales details) or _roll-up_ (summarizing city-level data into country-level data)

---

Each operation generate a huge quantity of “raw data” that will became the primary resources for Data mining.

**Fundamentals of Data Mining and the KDD Process(Extraction)**

The theoretical foundation of Data Mining is **`the discovery of implicit, previously unknown and useful patterns or information from immense amounts of data.`** Unlike a "simple search" (which only extracts exact results based on a predefined query) or "Expert Systems" (which apply static human rules), Data Mining learns from the data itself to discover hidden relationships **Data Mining** is actually a step within a larger fundamental process known as KDD (Knowledge Discovery from Data)

---

### Data Mining Goals

- **Prediction:** Show how certain attributes behave in the future, for instance anayzing transactions to forecast what consumers will buy for certain discounts.
- **Identification:** Using data models to identify the existence of an element,even or activity, for example useful to autenticate users.
- **Classification:** Divided and categorize databased on parameter combination, as the client division of a supermarket based on their shopping routine
- **Optimization:** Optimize the use of limited resources (time, space, money) to maximize the output variables, such as sales and profits.

---

### What are the algorithms looking for when they analyze data?

First we need to understand that: Data Mining is based on **inductive logic.**

In contrast with **deductive logic(** where it is we humans to apply logic predefined rules to data), in the Data Mining we give raw data to the machine and let her discover new rules and hidden patterns.

**5 types of “knowledge” that algorithms can extract**

- **Association Rules:** find some events that happen toghether, like someone bought a bag and is probable that also buy shoes

![image.png](attachment:3d394898-103f-46d7-9101-5965097f0986:image.png)

- **Classification hierarchies: Assign** data based on categories based on past events.
    
    - It is like a sorted, based on past data can sort for example people between high credit risk or low credit risk
    
    ![image.png](attachment:f21e9d45-a019-4340-8b5a-563889bd0c9a:image.png)
    
- **Sequential patterns: Find** a chain of events linked temporaly
    
    ![image.png](attachment:0eb02383-da2d-43d1-b54c-06a0ffd875f7:image.png)
    
- **Patterns within time series: They** identify similar trends measured at regular intervals, as stocks that move toghether similarly
    

![image.png](attachment:15bd8ba8-310e-48f2-bbc2-7600776b2d80:image.png)

- **Clustering: They Segment** a population into groups with “similar” elements to each other
    
    - It is like an explorer, they don’t sort but use an algorith to group subjects who act similar.
    
    ![image.png](attachment:3e3e787f-f050-45ca-9c71-1d65f0414449:image.png)
    

---

### Associative Rules

An example of **Data Mining is Market Basket Model,** used to show one of the main technologies: The discover of associative rules.

In this model, the database is seen as a collection of transactions. The market basket specifically represents the set of articles (**itemset**) ****that a consumer buys in a supermarket during a single visit.

An example is the rule “milk ⇒ juice” , used to understand how often those who buy milk also buy fruit juice,

So that these rules extracted from shopping carts are considered useful, they have to respect two fundamental metrics

- **Support**
    
    The frequency of how often it is in the database
    
- **Confidence**
    
    States the probability that the articles of the et Y are acquired, with the condition that the cllient have already bought the articles of the set X
    

---

### Antimonotonicity

But there is a big problem: in a supermaket with many articles, the possibile combination(itemset) are

$$ 2^m $$

Calculating them all would make any computer explode.

To avoid going crazy, the algorithm uses a mathematical shortcut called

**Antimonotonicity:**

If we discover for example that milk and sugar are rarely bought ( low support), the computer immeditately stop to calculate big operations that contain it as ( milk,sugar,eggs) or (milk,sugar,coffè)

![image.png](attachment:688c6804-9976-407f-be65-1b9418b79f92:image.png)

### Algorithms that resolve the Market Basket Model

- **Apriori Algorithm**
    
    - First algorithm that use the gold rule of **antimonotonicity**
    - Reads the entire database and counts how many times each individual object appears (Milk, Bread, etc.).
    - throws away all objects that appear very rarely (below the Support limit). The remaining ones are called "Frequent 1-itemsets" ($L_1$).
    - Use ONLY the surviving items to create pairs (Frequent 2-itemsets, $L_2$).
    
    Re-reads the entire database to count these pairs. Throw away the rare pairs and use the surviving ones to create trios ($L_3$). Rereads entire database. Stops when it fails
    
- **Sampling Algorithm**
    
    - To avoid reading millions of lines,this algorithm has a genius idea: take a small casual sample
        1. Use the Apriori only on that small sample to find perfect combinations
        2. As the sample could not be perfect, use the concept of **negative border, which** contains those combinations that the sample was almost frequent
        3. At the end it makes a single pass over the entire real database
- **FP-Tree Algorithm (Evolution that overcome Apriori)**
    
    - Frequent-Pattern Tree was born because, if you have 1000 products, Apriori have to generare almost half of a million of candidate pairs only to test it.
    - This algorithm completely eliminate the candidate generation phase
- So instead of bindly making combinations, this algorithm compresses the entire database into a kind of visual “family tree”.
    

![image.png](attachment:8fa9e97f-b3ee-423a-9639-5f23e3960309:image.png)

After the FP-Tree we have the **Partition Algorithm**

**The idea:**

- Divide the database in small blocks that are able to confortly stay in the computer’s Ram
- Step 1: The computer reads a single partition at a time and finds “local frequent rules” for that block. The union of all rules becomes the list of “global candidates”. In this phase, there could be **false positives (** a rule could be strict in block 1, but it does not exist in the rest of the db), but never **false negatives ( we don't lose any true rules)**
- Step 2: the entire database is reread one last time just to test the final list of candidates and discard false positives.
- **Association and hierarchy:**
    - **If a supermaket** discovers the rule Drinks → Desserts, nothing is done about it, it’s too generic. The magic happens by “crossing” very specific hierarchical as Yogurt Gelato marca "Healthy" => Acqua Minerale
- **Multidimensional associations**
    - So far we have only looked at “Items purchased” (one size only). But a database has many columns (Time, Day, Customer Age).
    - A multidimensional rule includes these variables: Time(6:30-8:00) → Subject(Milk). To handle this numbers (as hours and wages), the algorithm group the continous values in discrete “baskets” (Low Income,medium,high)
- **Negative Association**
    - Find the set of what people don’t buy, but it’s mathematical hard.

---

### Classification (or supervised learning)

Classification helps to make clear decisions

- **Should we give the rent to this client (yes) or should we reject it? (No)**

### **How to construct a decision tree**

Decisional tree works like the game “Guess who?”. You have several questions (attributes) to ask to isolate “good” customers from “bad” cuustomers:

- Is it married?
- How much does he earn?
- How old is he?

The computer does not ask these questions randomly in constrast use math to choce the “best” question,this “goodness” of a question is called **information gain** and is based on the concept of **Entropy.**

- **Entropy** measures the “caos” or the “disorder” of the data. If in a room there are 50 good clients and 50 bad clients, entropy is at its maximum. If there are 100 good clients, entropy is zero.
    
- **Information Gain** measures how much “caos” we eliminate by asking a certain question.
    
    The algorithm wil compute always the information gain for each column and will choose as “root” of the three the columns with the highest score
    

---

**Example:**

We analyze 6 clients

Make the calculations and discover that:

- Knowing if they are married reduces the chaos very little Gain = 0.08
- Knowing the age is a little better Gain = 0,46
- Knowing the salary splits custoers almost perfectly Gain = 0,67

![image.png](attachment:b4a4e32e-66d9-4119-94dd-0fd99987dcd4:image.png)

---

### Unsupervised Learning (K-Means)

**How does K-Means work? (La danza dei Centroidi)**

The algorithm is based entirely on a physical and geometric concept: the Euclidean distance (teorema di Pitagora). The closer two points are on the graph, the more “similar” they are considered.

**Steps:**

- **Choise of K:** Decide how many cluster you want to seek. For example K = 2
- **Casual Centroids:** The computer randomly drops 2 “Centroids.” into the middle of the data
- **Assignment:** each individual client looks at the two centroids, measures the distance with the ruler, and colors himself based on the centroids closest to him
- **The Recalculation**: Now that two groups have formed, the centroid mathematically moves to the true "exact center" of its new group.
- **Repetition**: By moving, the centroid may have moved closer to customers who were previously in the other group. Distances are redone and colors are changed. The process continues until the centroids stop moving.

![image.png](attachment:1a16b69d-8d1a-4780-a400-f6c9a152d7c0:image.png)

---

### The K-Means Limit and the BIRCH algorithm

With many clients the computer could not use this algortithm, in constrast, the **birch algorithm , instead of calculating distances between millions of points each time,** it builds a hierarchical tree (similar to the FP-Tree) that compresses groups of neighboring points into “micro-spheres”

![image.png](attachment:1e8a7c11-c3b8-4d40-984d-e0ac3c70e02a:image.png)

---

### Regression (Forecast the numbers)

So far we have seen the Classification, that divides things into predefinite categories (High risk, low risk), the regression takes a leap forward: **forecast a continuous and specific number.** Instead of telling you whether a patient will survive or not (Yes or No), it analyzes the clinical tests and gives you an exact percentage (survival percentage = 87.5%). Use mathematical functions ( as linear regression) to plot a trend line through the data

---

### Neural Links

Inspired by the functioning of human neurons, these networks learn from their mistakes (Supervised Learning). They are very powerful in recognizing complex patterns. However, the text highlights their biggest flaw: they are "black boxes". While a Decision Tree clearly shows you the logical path (e.g. If salary > 50k -> Mortgage Granted), a Neural Network gives you the correct answer but cannot explain how it got there.

---

### Genetic Algorithms

This is perhaps the craziest concept in the entire book. Instead of using rigid equations, Genetic Algorithms (GA) steals the idea from Charles Darwin. The text explains it like this:

Individuals (Strings): Possible solutions to a problem are translated into codes (like our DNA).

Fitness (Strength): You evaluate how good each solution is. The worst solutions die.

Cross-over (Reproduction): The best solutions survive and "mating", combining half of the "father" code and half of the "mother" to create a new generation.

Mutation: To prevent the species from stagnating, every now and then a piece of code changes at random.

![image.png](attachment:93e172b5-3205-4ee9-960e-b61ef7132679:image.png)

---

### Application of Data Mining

Now the question is “what is all this for and who uses it”?

1. **Practical Applications (The Real World)** The text makes us understand that the algorithms we have studied are the engine of decisions in the most profitable sectors in the world. If we connect the dots between the sectors listed and the techniques we have learned, we get this map:

**Marketing**: The analysis of purchasing behavior (e.g. catalog design and shelf layout) is the realm of the Association Rules (Market-Basket Model).

**Finance**: Creditworthiness analysis (deciding whether to give a mortgage) is the classic Classification problem (e.g. via Decision Trees), while fraud detection uses anomaly search techniques.

**Healthcare**: Clustering genes based on microarray experiments or finding patterns in drug side effects (where we don't know the answers in advance) is the perfect field for Clustering (Unsupervised Learning).

**Production (Manufacturing):** Optimizing the use of limited resources such as machines, personnel and materials often requires the exploratory and adaptive power of Genetic Algorithms or the statistical analysis of Regression.

1. Commercial Tools (How it really works) In real life, a Data Scientist does not write the K-Means algorithm from scratch every morning. Use commercial software (such as SAS Enterprise Miner or IBM Intelligent Miner). The text highlights two fundamental technical details for these tools:

**ODBC** interface (Open Database Connectivity): It is the universal standard that allows Data Mining software to "speak" and fish data from very different databases (Oracle, SQL Server, Access) without having to worry about how they are built internally.

GUI and API: While in the past we used textual commands (**UNIX**), today we use Graphical Interfaces (GUI) that allow you to view data. In some cases, programmers can use APIs (e.g. C libraries) to embed the Data Mining engine directly inside the company's apps.

1. **Future Directions (Big Data and Multimedia Data)** The text ends with a perfect prediction of what is happening in computing today:

The explosion of Big Data: Traditional databases are no longer enough. Data Mining is moving to huge clusters using technologies like Hadoop (and libraries like Mahout), parallel computing and Cloud.

Beyond the numbers: The future is not just analyzing tables or receipts, but doing Data Mining on non-standardized data, such as images, videos and medical texts (a very heavy operation for computers).