---
tags: [database, relational-algebra, relational-calculus, query-languages, elmasri-navathe, study-notes]
aliases: [Relational Algebra Notes, Elmasri Chapter 5]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 5: Basic Relational Algebra and Calculus


## Chapter 5)The Relational Data Model and Relational Database Constraints

#### Constrainsts:

Are the restrictions or the limitations on data in the database

Constraints on databases can be divided into three categories:

Inherent model-based or implicit constrainsts: Inherent in the data model

Examples of implicit (inherent) constraints in the pure Relational Model

Values must be atomic (1NF Rule): The basic relational model dictates that a single “cell” in a table can only hold one single (scalar) value.

The ordering of columns (attributes) does not matter

There can be no identical rows (no duplicate tuples)

The ordering of rows(tuples) does not matter

Schema-based: Defined directly in the schemas of the data model

Examples of explicit constraint:

Domain Constraints:

What it is: Specifying exactly what type of data is allowed in a column.

Example: You declare that the

Age

column must be an integer (

INT

). If someone tries to type the word "Twenty-two", the database blocks the operation. You can also enforce a range, like Age > 18.![](https://www.notion.so/image/attachment%3A416eaa85-4c18-416d-a1c5-7aaf61ede5ed%3Aimage.png?table=block&id=30d843e8-3372-8039-af3f-c63b28b5aaad&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1310&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Key Constraints:

What it is: The requirement of uniqueness for certain attributes.

Example: You declare that the

StudentID

column is a key (

UNIQUE

or

PRIMARY KEY

). From that moment on, the database will never allow the insertion of two students with the exact same ID number.

Superkey specifies that no two tuples can have the same value

Every relation has at least one superkey → set of all attributes

![](https://www.notion.so/image/attachment%3Ae3e9adc8-b467-4f02-aaa0-0d91978b1860%3Aimage.png?table=block&id=30d843e8-3372-80e6-829a-c2e387463feb&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1310&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

A relation schema can have more than one key:

Candidate key

What is a Candidate Key? A Candidate Key is an attribute (or a set of attributes) that possesses two fundamental properties:

Uniqueness: It uniquely identifies a single row (tuple) within the table. There will never be two rows with the exact same value for this key.

Minimality: It is the smallest possible set of attributes needed to guarantee that uniqueness. If you remove even a single "piece" from this key, you lose the uniqueness.

The "Election" Process (The vital difference for your exam): Imagine the

STUDENT

table. Which attributes or combinations of attributes are strictly unique for every student?

The is unique. (It is a candidate key).

The

Student ID

is unique. (It is a candidate key).The

University Email

is unique. (It is a candidate key).

All of these attributes are candidates for the role of the table's official identifier. You, as the database designer (the Database Administrator), look at all the "candidates" and elect exactly one.

![](https://www.notion.so/image/attachment%3A79f311c8-e747-496e-af6f-dc2db0fab8ab%3Aimage.png?table=block&id=30d843e8-3372-8098-ad7a-e9019d1769a3&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=540&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Entity Integrity:

What it is: A strict rule regarding primary keys.

Example: No part of a Primary Key can ever have an empty value (

NULL

). If you are registering a new student, you cannot leave their Student ID blank; otherwise, you would never be able to identify them.

Referential Integrity (Foreign Key Constraint):

What it is: The constraint that holds tables together (the famous Foreign Key we discussed earlier). It ensures that references between different tables are always valid.

Example: If you record in the

EXAMS

table that a student passed the course "CS101", that exact code "CS101" must absolutely exist in the parent

COURSES

table. You cannot reference a ghost course.![](https://www.notion.so/image/attachment%3Aca2f67fe-19b7-4dd2-8b2f-971608d6e3bf%3Aimage.png?table=block&id=311843e8-3372-8035-8206-f8ad3683ebd3&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1310&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Foreign Key: must satisfy the following

Same domain

Application-based or semantic constraints: Must be expressed and enforced by the application programs.

Example:

The Salary Rule: "An employee's salary can never exceed the salary of their direct manager."

Why is it semantic? Because to verify this, the system must first read the employee's row, then find out who their manager is, read the manager's row, compare the two salaries, and finally decide whether to block the insertion. A basic SQL table constraint cannot make this "journey". You need external software logic to perform this check before saving the data.

The VIP Bank Rule: "A customer cannot withdraw more money than they have in their account, unless they have been a VIP customer for over 5 years, in which case they can overdraw up to €10,000."

Why is it semantic? There are far too many conditional variables ("if... then... unless...") for a simple schema constraint. The banking application (the software) must process all these logical calculations and then tell the database "Okay, update the balance" or "No, decline the transaction."

Update Operations:

There are three basic operations,they are insert,delete and modify.

#### Insert Operations:

Is used to insert or add a new tuple

![](https://www.notion.so/image/attachment%3A2bb862e8-e054-417e-9a67-d532974e6ce8%3Aimage.png?table=block&id=314843e8-3372-80a2-bc89-d29ba24ed608&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

this operation “insert” can violate any of the four constraints:

Domain constraints

can be violated if the given attribute value doesn’t appear in the corresponding domain.

![](https://www.notion.so/image/attachment%3A3e4549f4-6190-4e1b-a2b9-90409baf40a0%3Aimage.png?table=block&id=314843e8-3372-807e-b5ae-fb7c98f5ea59&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=970&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Entity Integrity Constraint

![](https://www.notion.so/image/attachment%3A99db88e5-0a0d-473f-8ad6-bf2a88ff5602%3Aimage.png?table=block&id=314843e8-3372-8015-901c-e5c72df8ef6f&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=970&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

#### Delete Operation:

The operation “delete” can violate refential integrity

To resolve this violation the database react with 4 strategies

#### Restrict:

The RESTRICT constraint prevents the deletion of a parent record because doing so would violate Referential Integrity, immediately generating orphaned records with dangling foreign keys. Instead of automatically modifying or destroying the dependent child records (as seen with Cascade or Set Null), RESTRICT acts as a strict, proactive safeguard. It forces the database administrator to manually resolve the dependencies first. To successfully execute the deletion, you must perform a bottom-up removal: first, manually delete or reassign all associated child records in the referencing table. Only when the parent record has zero dependencies will the RDBMS permit the DELETE transaction to proceed.

\> Loading JavaScript code…

How to resolve?

\> Loading JavaScript code…

\> Loading JavaScript code…

#### Cascade:

is to attempt to cascade (or propagate) the deletion by deleting tuples that reference the tuple that is being deleted.

Table 1:

RESEARCHER

(L'entità forte)

| id (PK) | Full\_Name | email\_address | |:--- |:--- |:--- | | 10 | Alan Turing | turing@cambridge.edu | | 11 | Marie Curie | curie@sorbonne.fr |

Table 2:RESEACH\_PAPER

Active rule: The columns

researcher\_id

is a foreign key

ON DELETE CASCADE

.

| id (PK) | title | researcher\_id (FK) |
| --- | --- | --- |
| 101 | Computing Machinery | 10 |
| 102 | Enigma Logic | 10 |
| 103 | Radioactivity | 11 |

\> Loading JavaScript code…

Answer:

\> Loading JavaScript code…

#### ON DELETE SET DEFAULT

Imagine you have configured the database to never lose the authorship of the documents, automatically reassigning them to a dummy account (for example, ID

0000

, named "Deleted Author") when the original author is removed from the system.

Current Database State (Before the command)

Table 1: RESEARCHER (Parent): Contains ID

10

(Alan Turing), ID

11

(Marie Curie), and ID

0000

(Deleted Author).Table 2: RESEARCH\_PAPER (Child): Contains papers

101

and

102

, both linked to

researcher\_id = 10

. The active rule on the Foreign Key is

ON DELETE SET DEFAULT

.

The User's Action You execute the command:

SQL

DELETE FROM RESEARCHER WHERE id = 10;

My internal process (How I act as a DBMS)

Interception: I receive the deletion command for ID 10. I scan the dependent table and find two child records (101 and 102) that rely on this ID.

Policy Reading: I read the rule set on the Foreign Key:

ON DELETE SET DEFAULT

.Execution: I perform the operation in a single safe transaction. First, I modify the child records: I replace ID

10

with the predefined default value (which is

0000

). Immediately after, having secured them, I permanently delete the parent record (Alan Turing).The Final Result The command succeeds without returning errors. Turing's papers still exist, but they are now officially assigned to the "Deleted Author" user (

0000

). The database remains perfectly consistent, referential integrity is preserved, and no record is orphaned.

#### ON DELETE SET NULL

Current Database State (Before the command)

Table 1: RESEARCHER (Parent): Contains ID

10

(Alan Turing) and ID

11

(Marie Curie).Table 2: RESEARCH\_PAPER (Child): Contains papers

101

and

102

, both linked to

researcher\_id = 10

. The active rule on the Foreign Key is

ON DELETE SET NULL

.

The User's Action You execute the command:

SQL

DELETE FROM RESEARCHER WHERE id = 10;

My internal process (How I act as a DBMS)

Interception: I receive the deletion command for ID 10. I scan the dependent table and find two child records (101 and 102) that rely on this author.

Policy Reading: I read the rule set on the Foreign Key:

ON DELETE SET NULL

.Execution: I perform the operation in a single safe transaction to gently sever the tie. First, I access the child records (the papers) and replace ID

10

with the empty value

NULL

(which in database jargon means "unknown" or "no value"). Immediately after safely unlinking them, I permanently delete the parent record (Alan Turing).The Final Result The command succeeds without returning errors. Turing's papers still exist intact in the database, but they are now officially anonymous documents (their author is

NULL

). Referential integrity is preserved, and there are no pointers to non-existent records (orphans).

Question:

When we have to use this strategies to avoid violation?

Restrict

Use

RESTRICT

for mission-critical data where automated cascading actions pose a severe risk of accidental data loss (e.g., financial transactions, audit trails, or active contracts)

Cascade

Use

CASCADE

for Weak Entities or strict compositional relationships where the child entity is entirely intrinsically dependent on the parent for its logical existence Real-world example: Deleting a

User\_Account

should automatically trigger a cascade delete of their

Account\_Preferences

and

Saved\_Passwords

, as these configuration files are completely useless without the core user profile.

On Delete Set null

Use

SET NULL

to comply with data retention policies when dealing with independent entities that generate valuable historical records. It is the optimal strategy when the child entity holds intrinsic business or academic value and must remain in the system for auditing or historical reporting, even if the primary stakeholder is removed.Real-world example: If a

Sales\_Manager

resigns and their profile is deleted, the

Closed\_Deals

they generated must not be deleted. Instead, the manager ID is set to

NULL

, preserving the company's quarterly revenue reports while anonymizing the instigator.

On Delete Set Default

Use

SET DEFAULT

to ensure uninterrupted workflow continuity in systems where the child entity possesses a mandatory participation constraint (a

NOT NULL

foreign key). It provides a smooth operational transition by dynamically reallocating orphaned assets to a pre-configured generic placeholder or administrative queue.Real-world example: In a logistics tracking system, if a

Delivery\_Driver

is removed from the active roster, all their pending

Delivery\_Routes

are automatically reassigned to the default

Unassigned\_Pool\_ID

to ensure no shipments are dropped from the daily schedule.![](https://www.notion.so/image/attachment%3Abef4dcbd-eb0f-4487-b407-bc38abd7199c%3Aimage.png?table=block&id=317843e8-3372-806f-a796-f0c5dc656155&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

\> Loading JavaScript code…

Check data constraint on primary key RegNo

1004 match with the data type

Check key constraint (no value duplicated)

There is no duplication on the primary key

Check Integrity Constraints (No null value)

The value of the primary key is not null therefore the entity integrity constraint is also not violated

Check refential integrity constraint (which states that the value of the foreign key should refer to an existing tuple in the relation it refers to or it should be null)

Solution:

No constraint violation.

\> Loading JavaScript code…

domain constraint is not violated!

key constraint is not violated!

integrity constraint is not violated!

Referential integrity constaint is violated!!

Because the value of the foreign key must refer to an existing tuple in the relation it refers to.

\> Loading JavaScript code…

The key constraint is violated because there already exists a primary key with the same value.

\> Loading JavaScript code…

Integrity constraint is violated because we cannot accept null values

Referential integrity is also violated since we don’t have a tuble contains the same value of the foreign key!

![](https://www.notion.so/image/attachment%3A324d8909-cd04-4351-acab-6f30a8dd7702%3Aimage.png?table=block&id=317843e8-3372-8012-9a43-c35f60a613a6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

\> Loading JavaScript code…

It’s possible

\> Loading JavaScript code…

referential integrity constraint is violated because we don’t have a foreign key with value 7

\> Loading JavaScript code…

Integrity constraint is violated

\> Loading JavaScript code…

integrity constraint and referential integrity constraint

\> Loading JavaScript code…

The Referential Integrity constraint is violated. If we delete John, we will create orphaned records in both the

DEPARTMENT

and

WORKS\_ON

tables. To resolve this, we must apply different referential actions: for the

DEPARTMENT

table, we can apply ON DELETE SET NULL (leaving the department temporarily without a manager) or ON DELETE RESTRICT (preventing John's deletion until the administrator assigns a new manager to department 1). For the

WORKS\_ON

table, we must apply ON DELETE CASCADE to automatically remove his logged hours.

\> Loading JavaScript code…

No integrity constraints are violated. The deletion is successful because works\_on is a dependent (child) table. Removing a tuple from this relation does not create orphaned records in any other table, therefore it does not trigger any referential integrity violations.

\> Loading JavaScript code…

Referential integrity constraint is violated because Sarah and Smith have records in the table works\_on linked with PNo = 10.

\> Loading JavaScript code…

Referential integrity

\> Loading JavaScript code…

No constraint is violated, unless there is a domain constraint that restricts the maximum number of working hours

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]