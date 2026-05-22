---
tags: [database, DBMS, database-users, elmasri-navathe, study-notes]
aliases: [Database Users Notes, Elmasri Chapter 1]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 1: Databases and Database Users


## Chapter 1 Database and Database Users

These are the foundational concepts. Do not move forward until these are clear.

Data

• Database

• Mini-world

• DBMS (Database Management System)

• Database system

• Application

• Metadata

• Database approach

• Program–data independence

• Data abstraction

• Concurrency

• Transaction

• Actors on the scene

• Workers behind the scene

We begin from the most abstract level. In computer science, data are not numbers or words by themselves; data are known facts that can be recorded and that have meaning only with respect to some portion of reality. This immediately implies that databases are not about “files” or “tables” first, but about representation. Before any technical system exists, there is a cognitive act: we decide what part of the real world is relevant. This selected portion is called the mini-world. The mini-world is not accidental; it is a deliberate abstraction. When an institution decides to store information about citizens, patients, students, or taxpayers, it is defining a mini-world governed by institutional rules and objectives.

Once the mini-world is fixed, data emerge as recorded facts about it. A database is then defined, at the theoretical level, as a collection of related data describing that mini-world. The word “related” is essential: databases are not arbitrary repositories, but structured representations in which relationships among facts matter as much as the facts themselves. At this stage, however, nothing has been said about how data are stored or managed. A database, in pure theory, can exist on paper.

The problem arises when databases are implemented in real institutions. Institutions do not merely store data; they use, modify,, and protect them over time. This creates a qualitative shift. The moment data must be accessed by multiple users, updated continuously, and kept consistent under institutional constraints, managing the database manually or through isolated files becomes untenable. This necessity gives rise to the Database Management System, or DBMS. The DBMS is defined as software whose role is to create, maintain, and control access to a database. Conceptually, the DBMS is not part of the data; it is the governing layer that enforces rules over data.

At this point, a crucial theoretical distinction appears. The database system is not just the database, and not just the DBMS, but the combination of the database and the DBMS (and, in practice, the applications that interact with them). This distinction matters because most institutional failures occur when these layers are confused. In a university, for example, grades are not changed directly in files; they are changed through controlled interactions with the database system, mediated by the DBMS.

The theoretical power of the database approach lies in three tightly linked concepts. The first is the self-describing nature of a database system. A DBMS does not merely store data; it also stores metadata, which are data describing the structure, types, and constraints of the database itself. Metadata explain what a “student number” is, which values are allowed, and which relationships are valid. This means the system knows its own structure. In institutional terms, this is equivalent to embedding organizational rules directly into the information system rather than relying on human memory or informal procedures.

The second concept is program–data independence. This expresses a separation between what data mean and how they are physically stored. Programs interact with the database through the DBMS, not through the storage itself. As a result, changes in storage structure or internal optimization do not require rewriting institutional applications. In a public administration, this allows technological evolution without disrupting services, which is why this concept is foundational for large-scale systems.

The third concept is data abstraction. Abstraction means that users do not interact with raw storage details but with conceptual representations of data. Different users see different abstractions, or views, of the same database. A clerk, a manager, and an auditor may access the same institutional database but perceive different structures and permissions. This is not a technical convenience; it is a direct translation of institutional hierarchy into system design.

Once multiple users operate on the same data, another theoretical requirement emerges: transaction processing. A transaction is defined as a logical unit of work that must be executed completely or not at all. This concept ensures institutional reliability. If a hospital registers a patient admission, all related updates must succeed together; partial execution would violate institutional consistency. Closely connected to this is concurrency control, which guarantees that simultaneous transactions do not corrupt shared data. Concurrency is not an exceptional case; it is the normal condition of institutional systems.

Finally, Chapter 1 introduces a sociotechnical perspective through the classification of database users. The system is not neutral; it reflects roles. Actors on the scene are those who design, control, and use the database content within the institution: administrators, designers, end users. Workers behind the scene are those who design and maintain the DBMS itself. This separation mirrors the division between institutional governance and technological infrastructure.

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]