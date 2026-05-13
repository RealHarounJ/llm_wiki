# NoSQL Databases & Big Data Systems

NoSQL (Not Only SQL) databases are designed to handle the 3 Vs of Big Data: **Volume, Velocity, and Variety**. Unlike traditional RDBMS (SQL), they offer flexible schemas and horizontal scalability.

## 1. The 4 Main Types of NoSQL

| Type | Data Model | Use Case | Example |
| :--- | :--- | :--- | :--- |
| **Key-Value** | Simple key-to-value mapping | Caching, User Sessions | Redis, DynamoDB |
| **Document** | Hierarchical documents (JSON/BSON) | Content Management, E-commerce | MongoDB, CouchDB |
| **Column-Family** | Rows with many, dynamic columns | Time-series data, Web analytics | Cassandra, HBase |
| **Graph** | Nodes and Edges (Relationships) | Social Networks, Fraud Detection | Neo4j, Amazon Neptune |

## 2. Theoretical Foundations: CAP vs. ACID

### ACID (Traditional SQL)
Focuses on data integrity and reliable transactions.
*   **Atomicity**: All or nothing.
*   **Consistency**: Data follows all rules.
*   **Isolation**: Transactions don't interfere.
*   **Durability**: Changes are permanent.

### BASE (Modern NoSQL)
Focuses on availability and scalability.
*   **Basically Available**: The system works even if parts are failing.
*   **Soft State**: Data can change even without input (due to eventual consistency).
*   **Eventually Consistent**: The system will be consistent given enough time.

### The CAP Theorem
In a distributed system, you can only pick **two** out of three:
1.  **Consistency (C)**: Every read receives the most recent write.
2.  **Availability (A)**: Every request receives a response (without guarantee of latest data).
3.  **Partition Tolerance (P)**: The system continues to operate despite network failures.

## 3. Business Context (BIS)
Modern Business Information Systems use **Polyglot Persistence**: using the best database type for each specific part of the application (e.g., SQL for transactions, Graph for recommendations, Key-Value for performance).

---
*Reference: Elmasri & Navathe, Chapter 24*
