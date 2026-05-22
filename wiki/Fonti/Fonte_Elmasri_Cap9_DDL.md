---
tags: [database, SQL, DDL, constraints, foreign-key, table-creation, elmasri-navathe, study-notes]
aliases: [SQL DDL Mapping Notes, Elmasri Chapter 9 DDL]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 9-DDL: Practical SQL DDL Mapping & Constraints


## Chapter 9.DDL

What is DDL?

DDL commands define and modify the structure of database objects. Think of DDL as the "blueprint commands" - they create, modify, or destroy the containers that hold your data.

| Command | Purpose | Example |
| --- | --- | --- |
| CREATE | Create new database objects | CREATE TABLE customers (...); |
| ALTER | Modify existing objects | ALTER TABLE customers ADD COLUMN email VARCHAR(100); |
| DROP | Delete database objects | DROP TABLE old\_customers; |
| TRUNCATE | Remove all data, keep structure | TRUNCATE TABLE temp\_data; |

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]