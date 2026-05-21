---
tags: [database, ER-model, conceptual-design, entities, relationships, elmasri-navathe, study-notes]
aliases: [ER Model Notes, Elmasri Chapter 3]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 3: Data Modeling Using the Entity-Relationship (ER) Model


## Chapter 3 ) Data Modeling Using the Entity-Relationship (ER) Model

![](https://www.notion.so/image/attachment%3A94d37536-09d9-4317-93e9-dce02a5eca27%3AScreenshot_2026-02-13_160143.png?table=block&id=306843e8-3372-80ed-a5a8-ef080cc57c42&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=960&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

The first step in the design of the database is Requirements Collection and Analysis:

Database designers understand and document the data requirements of the database users.

The result is the Data Requirements written consisely or written in brief

Also Functional Requirements have to be specified

Consist of user-defined operations

Once this data is collected and analyzed, the next step is to create a conceptual schema for the database using high level or conceptual data model

A high-level data model is a data model that provides concepts close to the way how users persist data or how users see data, and this step is called conceptual design.

CONCEPTUAL DESIGN:

this step is for creating conceptual schema

CONCEPTUAL SCHEMA:

Is a concise description of the data requirements and detailed description of the entity types, relationships and constraints

Conceptual schema is easier to understand because do not contain the implementation details and also they can be communicated easily with the non-technical users

The next step is logical design:

Is the actual implementation of the database, using commercial DBMS.

Most commercial DBMS(Oracle) uses an implementation data model

The result of the step is a database schema

The last step is the PHYSICAL DESIGN

the internal storage structures, indexes, access path - specified

along with these activities application programs are designed and implemented as transactionsù

## Weak Entity Types

Entity types that do not have key attributes of their own

Identify themselves by relating to another entity type called the identifying or the owner entity type

Relationship between weak entity type to its owner is called identifying relationship

## Symbols used in ER Diagram:

Entity

Is a thing or an object that has existence

Weak Entity

Attribute

Describe an entity

Key Attribute

Helps in identifying an entity uniquely

Multivalued Attribute

that contains a set of values for a particular entity and it is represented by double oval

Composite Attribute

An attribute that can be divided into further attributes

Derived Attribute

Which is an attribute whose value is derived from another attribute

Identifyin Relationship

a relationship between a weak entity type and the owner entity type or the strong entity type

![](https://www.notion.so/image/attachment%3A9eb687e0-d366-4024-9148-c00c4bd1aede%3Aimage.png?table=block&id=30c843e8-3372-8014-85c4-fe2a37d9ed5c&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=820&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

## Sample Database Application

Database application, called Company

Requirements gathered:

The company is organized into departments. Each department has a unique name, a unique number, and a particular employee who manages the department. We also track the manager’s start date. A department may have several locations.

A department controls number of projects, each of which has a unique name, unique number and a single location.

Employee details: name, SSN, sex, salary. We keep track of number of hours per week on each project

![](https://www.notion.so/image/attachment%3Ac358a8d6-6c6a-426c-b6a2-8411db5612e2%3Aimage.png?table=block&id=306843e8-3372-80a3-a891-fc99d7217561&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A41fb76ea-fd2a-4313-a12d-943c48770c7b%3Aimage.png?table=block&id=306843e8-3372-8055-9a55-e99993e74afd&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A4a878f80-0e62-4786-bf1e-9c89edefa8f7%3Aimage.png?table=block&id=306843e8-3372-8011-a553-e51c5a830954&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

## Relationship

association among 2 or more entities

Teacher teaches student

Degree of Relationship

Denotes the number of entity types that partecipate in a relationship

Unary relationship: exists when there is an association with only one entity

![](https://www.notion.so/image/attachment%3A9f50961c-291e-4873-bf25-024d089e11b4%3Aimage.png?table=block&id=307843e8-3372-80c3-a60c-d6bd86901e82&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=790&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Binary relationship

Exists when there is an association among two entities

![](https://www.notion.so/image/attachment%3A2532e903-31de-471a-8488-1b5ce6f66342%3Aimage.png?table=block&id=307843e8-3372-80be-b729-f5149d4e2101&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1240&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Ternary relationship:

Exists when there is an association among three entities

![](https://www.notion.so/image/attachment%3A42d4c471-72fb-4926-8b53-41869ee00ac3%3Aimage.png?table=block&id=307843e8-3372-802e-8457-e15b2ffe07b6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1240&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Relationship Constraint

Cardinality Ratio

The maximum number of relationship instances that an entity can partecipate in.

Possibile cardinality ratios for binary relationship are

1:1

1:N

N:1

M:N

![](https://www.notion.so/image/attachment%3A72a89cf1-3398-4d25-9e6f-adadaddc0bb5%3Aimage.png?table=block&id=307843e8-3372-8062-b652-dcd98266716e&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=660&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

We have two types of partecipation constraint

Total partecipation and Partial partecipation

![](https://www.notion.so/image/attachment%3A37e43fd4-00ba-4295-a7ba-8cf62edcb447%3Aimage.png?table=block&id=307843e8-3372-80d1-9f99-fc981ba9bdd5&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1070&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Complete ER Diagram

![](https://www.notion.so/image/attachment%3A184396bc-fe61-49d3-8926-92f213e7b06c%3Aimage.png?table=block&id=307843e8-3372-80e0-b775-e7b6c56c6ec6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Attributes of Relationship Types

Attributes of 1:1 or 1:N relationship types can be migrated to one of the participating entity types

In 1:1 relationship, attributes can be migrated to either of the entity types.

In a 1:N or N:1 relationship type, attributes are migrated only to the entity type on the N-side of the relationship.

In M:N relationship type, some attributes can be determined by a combination of participating entiteis

Role Names

Signifies the role tha a participating entity plays in each realtionship instance

Used to remove ambiguity

EMPLOYEE (Supervisor) | SUPERVISES | EMPLOYEE (Subordinate)

Supervisor and Subordinate are role names

recursive relationship (unary relationship)

> A relationship where the same entity type participates more than once.

QUESTION

Why are role names necessary in recursive relationships?

Because without them the model is unclear, we cannot distinguish the two participations.

![](https://www.notion.so/image/attachment%3Ad058c1a9-0619-4a05-b657-beeb02f69444%3Aimage.png?table=block&id=309843e8-3372-8029-9abc-efd171b814f6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=480&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

## Alternative Notations for ER Diagrams

Associates a pair of integer numbers (min, max) with each participation of an entity type in a relationship type, where 0 ≤ min ≤ max and max ≥ 1.

What is the notation (min, max)?

Instead of writing

1:1

1:N

M:N

We write for each side of the relation

> (min, max)

Why is it better respect the 1:N?

Because distinguish between optional and mandatory

Is more precise

Example:

EMPLOYEE (0,1) PROJECT (1,N)

An employee can participate in the relation:

min 0 times

max 1 time

Remember 1

The cardinality (min, max) does not measure the number of events during the time

Measure the enitity’s number linked in the relation.

Remember 2

(1: N) = mandatory participation

(0: N) = optional participation

## Enhanced ER Model

Generalization:

Bottom-up approach: where two lower-level entities combine to form a higher level entity

Specialization:

Top-down approach: where it defines set of subclasses of an entity type

![](https://www.notion.so/image/attachment%3Af26fcbae-6121-4a5d-964a-3f77cc932c0a%3Aimage.png?table=block&id=309843e8-3372-8095-b7f3-d78997bccc0c&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=660&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Ridundant → Ridondante

An information that could be fetched (derived) from already existing informations.

Example

Data\_nascita

Età

→ Età è ridondante perchè puo essere già calcolata tramite data\_nascita

### Loss of Semantics

![](https://www.notion.so/image/attachment%3Aa43cf415-b7cc-47d0-b4c9-45bced06ad04%3Aimage.png?table=block&id=30c843e8-3372-8060-9a7f-ee0d06b5bf33&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Explain better the problem of loss of semantic

![](https://www.notion.so/image/attachment%3Aa17fc972-f647-4a88-9372-93232a5d1589%3Aimage.png?table=block&id=30c843e8-3372-800f-9bbd-e447f1f3ddde&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Context: Teacher,Course and Semester

Instructor (Teacher) Course Semester

Notice!

We have a ternary relation called Offers

Three separated binary relation: CAN\_TEACH, TAUGHT\_DURING, E OFFERED\_DURING

Each relation explain something

The nutshell of the question

The ternary relation offers rappresent an instance in which a specific teacher offers a specific course in a specific semester

Dalla ternaria alle binarie (Vero): Se sai che esiste un'istanza in

OFFERS

(es. Il Prof. Rossi insegna Basi di Dati nel 1° Semestre), allora puoi dedurre logicamente che le singole coppie esistono anche nelle relazioni binarie (Rossi può insegnare Basi di Dati, Rossi ha insegnato nel 1° semestre, Basi di Dati è stato offerto nel 1° semestre).Dalle binarie alla ternaria (Falso): Il contrario non è sempre vero! Potresti avere le tre singole istanze binarie separate senza avere l'istanza corrispondente in

OFFERS

. Ad esempio, Rossi può insegnare Basi di Dati, Basi di Dati è offerto nel 1° semestre, e Rossi insegna nel 1° semestre... ma magari nel 1° semestre Rossi sta insegnando "Reti", mentre "Basi di Dati" lo sta tenendo il Prof. Bianchi!

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]