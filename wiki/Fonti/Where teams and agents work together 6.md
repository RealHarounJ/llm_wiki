---
title: "Where teams and agents work together"
source: "https://www.notion.so/Chapter-9-Relational-Database-Design-by-ER-and-EER-to-Relational-Mapping-319843e8337280ff8c0beb882a55bca6"
author:
published:
created: 2026-05-05
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
## Chapter 9)Relational Database Design by ER- and EER-to-Relational Mapping

#### Mapping Cardinalities

Also known as Cardinality Ratio. Because is used to express the number of entities to which another entity can be associated via relationship set.

most useful in describing binary relationship sets

There are four types of mapping cardinalities

One-to-One

![](https://www.notion.so/image/attachment%3A921d28cd-3db1-4e40-ae2a-6c8a72ebe82b%3Aimage.png?table=block&id=319843e8-3372-8048-85b2-de9c74bae1fa&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=480&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

One-to-Many

![](https://www.notion.so/image/attachment%3Ada1b47f4-fa31-4a47-b7a8-737fcdc9b5da%3Aimage.png?table=block&id=319843e8-3372-8033-bef7-c64317ebde5f&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=480&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Many-to-One

![](https://www.notion.so/image/attachment%3A136ac108-f845-45b6-830f-b544bf99c0bc%3Aimage.png?table=block&id=319843e8-3372-80c8-8907-d3f3516c14c9&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=480&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Many-to-Many

![](https://www.notion.so/image/attachment%3A0e36a2c5-db51-42af-b94d-949bcdbbbf0c%3Aimage.png?table=block&id=319843e8-3372-8008-8934-d0c7f41239e0&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=480&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 1: Mapping of Regular entity Types

For each regular entity type, create a relation (table) that includes all its simple attributes. The key attribute of the entity translates directly into the Primary key of the new relation.

Step 2:Mapping of Weak Entity Types

Create a relation for the weak entity. Its Primary Key is formed by combining its own partial key with the Primary Key of its identifying owner entity, which acts as a Foreign Key equipped with a mandatory

ON DELETE CASCADE

constraint.

Step 3:Mapping of 1:1 Relation Types

The standard approach is the Foreign Key approach. Identify the entity with total participation (mandatory existence) and embed the Primary Key of the other entity within it as a Foreign Key.

Step 4: Mapping of 1:N Relation Types

Implement the relationship by placing a Foreign Key on the "N-side" (the child entity). This Foreign Key references the Primary Key of the relation on the "1-side" (the parent entity).

Step 5: Mapping of M:N Relation Types

A many-to-many relationship cannot be mapped directly. It mandates the creation of a new, distinct relation (a junction table). Its Primary Key is a composite key derived from the Primary Keys of the two participating entities.

Step 6: Mapping of Multivalued Attributes (Ovali con doppia linea)

To preserve the First Normal Form (1NF), multivalued attributes are extracted and mapped into a separate, newly created relation.

Step 7: Mapping of N-ary Relationship Types (Relazioni Ternarie)

N-ary relationships are consistently translated into a dedicated associative relation containing Foreign Keys pointing to the Primary Keys of all participating entities.

![](https://www.notion.so/image/attachment%3A2bbc199e-a987-4c47-acb0-9802e5a40678%3Aimage.png?table=block&id=319843e8-3372-8057-93f5-f6f574bc7b6e&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Practical Example

Step 1:Mapping of Regular Entity Types (Entità Forti)

EMPLOYEE ( underline{Ssn}, Fname, Minit, Lname, Bdate, Address, Salary, Sex ) DEPARTMENT ( underline{Dnumber}, Dname ) PROJECT ( underline{Pnumber}, Pname, Location )

![](https://www.notion.so/image/attachment%3A65dea437-1b38-43d5-8b6f-72fa9000143c%3Aimage.png?table=block&id=319843e8-3372-804d-8667-d4b1f8b51fef&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 2: Mapping of Weak Entity types (Entità Deboli)

![](https://www.notion.so/image/attachment%3Afe9c94a3-2b1e-4051-be30-825a56792d80%3Aimage.png?table=block&id=319843e8-3372-8025-96fc-cc095fefe85d&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=860&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 3:Mapping of binary 1:1 Relation Types

![](https://www.notion.so/image/attachment%3A9f777561-085e-4c7a-a2e6-711ba25ed7be%3Aimage.png?table=block&id=319843e8-3372-800c-87af-c8720e5c508e&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) To map the 1:1 relationship

MANAGES

, we employ the Foreign Key approach. We evaluate the structural constraints and identify that

DEPARTMENT

exhibits total participation (mandatory existence). Therefore, we embed the Primary Key of the

EMPLOYEE

relation into the

DEPARTMENT

relation as a Foreign Key (

Mgr\_ssn

), alongside any simple attributes attached directly to the relationship diamond (

Mgr\_start\_date

). This avoids the proliferation of

NULL

values that would occur if the Foreign Key were placed on the partial participation side. Step 4:Mapping of Binary 1:N Relation Types For each regular 1:N relationship type (

WORKS\_FOR

,

CONTROLS

,

SUPERVISION

), we identify the relation representing the entity type on the N-side (the 'many' side) of the relationship. We then embed the Primary Key of the entity on the 1-side into this N-side relation as a Foreign Key. This establishes the directional linkage. In the specific case of the recursive relationship

SUPERVISION

, we map it by adding a Foreign Key (

Super\_ssn

) within the

EMPLOYEE

relation that directly self-references its own Primary Key (

Ssn

![](https://www.notion.so/image/attachment%3A42ee77dc-44af-42af-af77-b9096d20b813%3Aerdplus.png?table=block&id=319843e8-3372-80a9-9b54-edd2ef9209b8&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 5:Mapping of Binary M:N Relation Types

For each binary many-to-many (M:N) relationship type, the mapping algorithm mandates the creation of a new, independent relation, commonly referred to as a Junction Table or Associative Entity. We cannot embed a Foreign Key in either of the participating entities without violating the First Normal Form (1NF).

Instead, we extract the Primary Keys from the two participating entity types and include them as Foreign Keys in the newly created relation. These Foreign Keys are then concatenated to form the Composite Primary Key of this junction table. Any descriptive attributes attached directly to the M:N relationship are incorporated as simple, non-key attributes.

Step 6: Mapping of Multivalued Attributes (Attributi multivalore)

For each Multivalued Attribute (identified by a double oval in the conceptual schema), the algorithm requires the creation of a distinct, dedicated relation to maintain 1NF compliance. This prevents the storage of arrays or lists within a single database cell.

This new relation is constructed by including the multivalued attribute itself alongside the Primary Key of its parent entity, which acts as a Foreign Key. To ensure that each tuple is uniquely identifiable, the Foreign Key and the attribute value are combined to form a Composite Primary Key. Additionally, a strict ON DELETE CASCADE constraint is inherently applied to the Foreign Key, ensuring that if the parent entity is deleted, all its associated multivalued entries are automatically purged.

![](https://www.notion.so/image/attachment%3Af1dd63a3-dd16-47b0-8f12-593de97b8bcc%3Aimage.png?table=block&id=31f843e8-3372-80b3-bea5-de74885affc0&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 7: Mapping of N-ary Relationship Types (relazione ternaria)

[8-ER-to-Relational.pdf](https://cs.clarku.edu/~cs220/slides/8-ER-to-Relational.pdf)

#### Mapping of Specialization or Generalization

![](https://www.notion.so/image/attachment%3Ad8ae01a7-82a3-49f0-8590-98b0f40c9042%3Aslide19-n.jpg?table=block&id=31a843e8-3372-8043-ad55-c32a2f15523a&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A80194633-064b-460a-b5c7-e922776ba87f%3Aimage.png?table=block&id=31a843e8-3372-8013-bcac-fb2d372482c2&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A1a9b68bf-26da-400b-a243-54c0b0fadac4%3Aimage.png?table=block&id=31a843e8-3372-806a-b989-c04f3bf209a2&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=800&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3Afcf727be-817e-4779-ab77-93c9e4310ade%3Aslide22-n.jpg?table=block&id=31a843e8-3372-8089-957b-d91733c88278&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Step 8: Options for Mapping Specialization or Generalization

The algorithm provides you with 4 options for translating a Superclass C and his subclasses.

Step 8A: Multiple Relations- superclass and subclasses.

Create the table L for the superclass with his attributes and the primary key.

Create the tables Li for each subclass

Enter each Subclass with its specific attributes, plus the Superclass key.

The Key Trick: In the Subclass, the key acts simultaneously as the Primary Key and as a Foreign Key pointing to the Superclass. When to use it: Always. It works with any constraint (Full/Partial, Disjoint/Overlapping). The cost: To see all the data of an entity, the database must perform an EQUIJOIN operation (join two tables by key), which consumes computing power.

Step 8B: Multiple Relations(only subclasses)

Here the Superclass is literally made to disappear.

How it is build: You create only the table for the subclasses. Take all the Superclass’s attributes and you push them down, copying it withing each subclass.

When to use it: Works well ONLY if the participation is Total and the constraint is Disjoint.

The fatal risk:

If it’s partial: if an entity belong to the superclass but does not have a subclass, that entity is lost(erased from the database)

If it’s overlapping: If an entity belongs to multiple subclasses at the same time, all its inherited data will be duplicated in multiples tables, creating redundancy.

Step 8C: Single Relation with one type attribute.

How to build it:

Create a single table L. You put in it all the attributes of the Superclass and all the attributes of all the Subclasses

Discriminator:

Add an extra column called type attribute (t), which is used to write which subclass that row belongs

When to use it: ONLY for disjoint hierarchies

The cost: Generate a vast amount of values NULL

Step 8D: Single Relation with multiple type attributes

It is the evolution of Option 8C, designed to manage overlaps.How to build it: A mega-table with all the attributes of all the classes.The Discriminators: Instead of just one "Type" column, you create as many Boolean columns (True/False) as there are Subclasses ($t\_1, t\_2,..., t\_m$).When to use it: It is designed specifically for Overlapping hierarchies (but also works for Disjoints). If a person is both a Technician and an Engineer, put "True" in the is\_Technician column and "True" in the is\_Engineer column, filling the relevant fields without conflicts.

#### Real Example of every option

![](https://www.notion.so/image/attachment%3A0775877d-4fb1-4417-92a7-b531d9a3dcb7%3Aimage.png?table=block&id=31f843e8-3372-80ba-ad40-e6a6a9807852&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

The Decision Diagram (How to choose in the exam) To arrive at the perfect choice when you have to design from scratch, ask yourself these 3 questions in sequence:

Question 1: Does the circle have an "o" (Overlapping)?

YES: Discard 8B and 8C immediately. You are forced to use 8A (Separate Tables) or 8D (Mega-Table with Multiple Flags).

Question 2: Is participation Partial (single line towards the circle)?

YES: Discard 8B immediately. If you delete the superclass, you would lose the generic entity data. You can use 8A, 8C or 8D.

Question 3: Do subclasses have tons of specific attributes?

YES: Discard the 8C and 8D. If you create a mega-table, 80% of the cells will remain empty (NULL), wasting a huge amount of memory on your hard drive. Use 8A.

#### 9.2.2 Mapping of Shared Subcllasses (Multiple inheritance)

![](https://www.notion.so/image/attachment%3A78fb6594-c06e-492b-9009-33c4a3fb55b3%3Aimage.png?table=block&id=31f843e8-3372-80d6-a540-caf5eca4bf90&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Mapping of Shared Subclasses (Ereditarietà Multipla)

The Logical Problem: Imagine a university assistant (STUDENT\_ASSISTANT). This person is simultaneously a Student (therefore he has a study plan) and an Employee (therefore he receives a salary). In the EER diagram, its rectangle has two lines going up, pointing to two different superclasses (STUDENT and EMPLOYEE).

The Golden Rule (What the text says): The book sets an ironclad constraint: you can only do this if both superclasses have the exact same Primary Key at the root. Looking at Figure 9.6, you notice that both EMPLOYEE and STUDENT derive from PERSON, so they all share the Ssn identifier.

The Physical Solution: Since the keys match, there is no need to invent anything new. The rules of Step 8 that we just studied simply apply! In the text example, they used a crazy combination: Option 8C (the Employee\_type column) to handle the work side and Option 8D (the Student\_assist\_flag boolean flag) to handle the student side.

#### 2\. Lo Step 9: Mapping of Categories (Union Types)

![](https://www.notion.so/image/attachment%3A40ec9d98-0e03-4a1c-9a88-97d4d2b7e97d%3Aimage.png?table=block&id=31f843e8-3372-80a0-8a1d-fad8a760a85e&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=530&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Logical Problem:

Imagine you have to manage the “OWNERS” of a registered vehicle (OWNER).

Who can own a car?

A physical person(

PERSON

\- Key: Codice Fiscale / SSN).A bank(

BANK

\- Key: Codice ABI).A company (

COMPANY

\- Key: Partita IVA).

These three entities are the “Superclass” of the OWNER category. But unlike multiple inheritance, the primary keys are all different!

If you created the OWNER table, what primary key would you import? You cannot import them all, because you would exclude the others.

PHYSICAL SOLUTION! (SURROGATE KEY)

This is Step 9. When the superclasses have different keys, the algorithm tells to invent a fake key.

The table for the

OWNER

category is created.

A totally new attributed is created, called Surrogate Key (Chiave surrogata). For example: Owner\_id

This

OWNER\_id

become the primary key of the OWNER table.This

OWNER\_id

will then be added as a Foreign Key into the PERSON, BANK, and COMPANY tables, in order to link the vehicle to its true owner, regardless of who he or she is

se hai pero una participazione partziale o totale e un diskoint o un overlapping create una single table risolve sempre giusto?

### Gemini ha detto

Alt! Sirene spiegate nel database!

È un'intuizione logica eccellente, ma la risposta da vero Senior Architect è NO, la Single Table non è una bacchetta magica universale.

Anzi, se provi a usare la struttura esatta che abbiamo appena scritto per risolvere un diagramma Overlapping (Sovrapposto), il tuo database va letteralmente in crash logico.

Smontiamo chirurgicamente questa architettura per vedere come reagisce alle 4 diverse combinazioni teoriche (Step 8 dell'algoritmo).

#### 1\. La Single Table con il DISJOINT (Perfetta)

Il vincolo Disjoint significa "O l'uno o l'altro". La Single Table è l'arma perfetta per questo:

Disjoint Totale: Usi

ruolo ENUM('Dev', 'Sales') NOT NULL

. Sei obbligato a scegliere un solo ruolo. Perfetto.Disjoint Parziale: Togli il

NOT NULL

. La colonna

ruolo

può essere lasciata vuota (l'impiegato esiste, ma non è né Dev né Sales). Perfetto.

#### 2\. La Single Table con l'OVERLAPPING (Il Tallone d'Achille)

Il vincolo Overlapping significa "Può essere ENTRAMBI contemporaneamente". Immagina che Bob sia sia un programmatore Java sia un venditore eccezionale.

Il Crash Logico: Se usi la colonna discriminatrice

ruolo ENUM('Developer', 'Salesperson')

, cosa scrivi nella riga di Bob? L'

ENUM

accetta un solo valore alla volta. Non puoi scrivere "Tutti e due". Il database ti obbliga fisicamente a scegliere, rompendo il vincolo Overlapping!Il "Cerotto" Architetturale (Come risolvere l'Overlapping in Single Table): Per far funzionare l'Overlapping in una Single Table, l'Architetto deve distruggere la colonna

ruolo

e sostituirla con tante flag Booleane (Vero/Falso) quanti sono i figli:

SQL

\- Esempio di Single Table per OVERLAPPINGCREATE TABLE employee\_all\_overlapping ( emp\_id INT PRIMARY KEY, name VARCHAR(20), - Niente più colonna "ruolo". Usiamo flag separate! is\_developer BOOLEAN NOT NULL DEFAULT FALSE, is\_salesperson BOOLEAN NOT NULL DEFAULT FALSE, -... );

Con questa struttura, la riga di Bob avrebbe

is\_developer = TRUE

e

is\_salesperson = TRUE

.Ma attenzione al prezzo da pagare! Se hai 10 sottoclassi Overlapping, la tua Single Table diventerà un mostro largo 50 colonne, di cui il 90% saranno

NULL

(una Sparse Matrix estrema). Ecco perché, quando il diagramma ER dice Overlapping, quasi tutti i Data Architect scelgono la Strategia B (Tabelle Separate), perché gestisce le sovrapposizioni in modo molto più pulito.![](https://www.notion.so/image/attachment%3Af951d646-a9fb-47c2-890a-b2c57a1a16f5%3Aimage.png?table=block&id=322843e8-3372-807a-bbe7-cff37a7389d0&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

You have to consider important things to not get wrong!

SHIP, PORT AND VISITS DO NOT CREATE A TERNARY RELATIONSHIP

Why? Because SHIP AND PORT and in the middle a weak entity VISITS. It’s a binary relationship

\- 1. LE ANAGRAFICHE DI BASE (Entità Forti) CREATE TABLE IF NOT EXISTS

SHIP\_TYPE

(

Type

VARCHAR(255) NOT NULL,

Tonnage

VARCHAR(255) NOT NULL,

Hull

VARCHAR(255) NOT NULL, PRIMARY KEY(

Type

) );CREATE TABLE IF NOT EXISTS

STATE

(

Name

VARCHAR(255) NOT NULL,

Continent

VARCHAR(255), PRIMARY KEY(

Name

) );CREATE TABLE IF NOT EXISTS

SEA\_OCEAN\_LAKE

(

Name

VARCHAR(255) NOT NULL, PRIMARY KEY(

Name

) );- 2. IL PORTO (Entità Debole) CREATE TABLE IF NOT EXISTS

PORT

(

PName

VARCHAR(255) NOT NULL,

State\_Name

VARCHAR(255) NOT NULL,

Water\_Name

VARCHAR(255) NOT NULL, PRIMARY KEY(

PName

,

State\_Name

,

Water\_Name

) -- Corretto: La Super-Chiave! );- 3. LA NAVE (Entità Forte con FK composte) CREATE TABLE IF NOT EXISTS

SHIP

(

SName

VARCHAR(255) NOT NULL,

Owner

VARCHAR(255),

Type

VARCHAR(255) NOT NULL,

Home\_PName

VARCHAR(255) NOT NULL,

State\_Name

VARCHAR(255) NOT NULL,

Water\_Name

VARCHAR(255) NOT NULL, PRIMARY KEY(

SName

) -- Corretto: La nave è forte, ha solo il suo nome come PK! );- 4. I MOVIMENTI (Entità Debole della Nave) CREATE TABLE IF NOT EXISTS

SHIP\_MOVEMENT

(

date

DATE NOT NULL,

time

TIME NOT NULL,

Longitude

FLOAT NOT NULL,

Latitude

FLOAT NOT NULL,

SName

VARCHAR(255) NOT NULL, PRIMARY KEY(

date

,

time

,

SName

) );- 5. LE VISITE (Entità Debole Associativa) CREATE TABLE IF NOT EXISTS

VISITS

(

StartDate

DATE NOT NULL,

EndDate

DATE, -- Togliamo il NOT NULL, la visita potrebbe essere ancora in corso!

SName

VARCHAR(255) NOT NULL,

Pname

VARCHAR(255) NOT NULL,

State\_Name

VARCHAR(255) NOT NULL,

Water\_Name

VARCHAR(255) NOT NULL, PRIMARY KEY(

StartDate

,

SName

,

Pname

,

State\_Name

,

Water\_Name

) -- Il Boss Finale! );

\- ========================================== -- CREAZIONE DELLE FOREIGN KEYS (LA DIREZIONE GIUSTA: Dal Figlio al Genitore) -- ==========================================

\- PORT dipende da STATE e SEA ALTER TABLE

PORT

ADD CONSTRAINT

fk\_port\_state

FOREIGN KEY(

State\_Name

) REFERENCES

STATE

(

Name

); ALTER TABLE

PORT

ADD CONSTRAINT

fk\_port\_sea

FOREIGN KEY(

Water\_Name

) REFERENCES

SEA\_OCEAN\_LAKE

(

Name

);- SHIP dipende da SHIP\_TYPE e da PORT (Nota la sintassi a 3 colonne per il Porto!) ALTER TABLE

SHIP

ADD CONSTRAINT

fk\_ship\_type

FOREIGN KEY(

Type

) REFERENCES

SHIP\_TYPE

(

Type

); ALTER TABLE

SHIP

ADD CONSTRAINT

fk\_ship\_homeport

FOREIGN KEY(

Home\_PName

,

State\_Name

,

Water\_Name

) REFERENCES

PORT

(

PName

,

State\_Name

,

Water\_Name

);- SHIP\_MOVEMENT dipende da SHIP ALTER TABLE

SHIP\_MOVEMENT

ADD CONSTRAINT

fk\_movement\_ship

FOREIGN KEY(

SName

) REFERENCES

SHIP

(

SName

);- VISITS dipende da SHIP e da PORT (La doppia FK dell'entità debole associativa) ALTER TABLE

VISITS

ADD CONSTRAINT

fk\_visits\_ship

FOREIGN KEY(

SName

) REFERENCES

SHIP

(

SName

); ALTER TABLE

VISITS

ADD CONSTRAINT

fk\_visits\_port

FOREIGN KEY(

Pname

,

State\_Name

,

Water\_Name

) REFERENCES

PORT

(

PName

,

State\_Name

,

Water\_Name

);

\================================================================= -- FASE 1: I GENITORI ASSOLUTI (Nessuna Foreign Key, si inseriscono per primi) -- =================================================================

INSERT INTO

SHIP\_TYPE

(

Type

,

Tonnage

,

Hull

) VALUES ('Cargo', '150000', 'Double'), ('Passeggeri', '85000', 'Single'), ('Cisterna', '200000', 'Double');INSERT INTO

STATE

(

Name

,

Continent

) VALUES ('Italia', 'Europa'), ('USA', 'Nord America'), ('Egitto', 'Africa');INSERT INTO

SEA\_OCEAN\_LAKE

(

Name

) VALUES ('Mare Adriatico'), ('Oceano Atlantico'), ('Mar Rosso');

\- ================================================================= -- FASE 2: I FIGLI DI PRIMO LIVELLO (Dipendono dalla Fase 1) -- =================================================================

\- Il Porto dipende da Stato e Mare INSERT INTO

PORT

(

PName

,

State\_Name

,

Water\_Name

) VALUES ('Porto di Ancona', 'Italia', 'Mare Adriatico'), ('Port of Miami', 'USA', 'Oceano Atlantico'), ('Porto di Suez', 'Egitto', 'Mar Rosso');

\- ================================================================= -- FASE 3: I FIGLI DI SECONDO LIVELLO (Dipendono dalla Fase 1 e 2) -- =================================================================

\- La Nave dipende dal Tipo e dal suo Porto di Base INSERT INTO

SHIP

(

SName

,

Owner

,

Type

,

Home\_PName

,

State\_Name

,

Water\_Name

) VALUES ('Ever Given', 'Evergreen Marine', 'Cargo', 'Porto di Suez', 'Egitto', 'Mar Rosso'), ('MSC Seaview', 'MSC Cruises', 'Passeggeri', 'Port of Miami', 'USA', 'Oceano Atlantico'), ('Eurocargo', 'Grimaldi Lines', 'Cargo', 'Porto di Ancona', 'Italia', 'Mare Adriatico');

\- ================================================================= -- FASE 4: LE ENTITÀ DEBOLI E ASSOCIATIVE (L'ultimo anello della catena) -- =================================================================

\- I Movimenti (Dipendono solo dalla Nave) INSERT INTO

SHIP\_MOVEMENT

(

date

,

time

,

Longitude

,

Latitude

,

SName

) VALUES ('2026-03-10', '08:00:00', 13.51, 43.61, 'Eurocargo'), ('2026-03-10', '09:30:00', 13.65, 43.70, 'Eurocargo'), ('2026-03-15', '14:00:00', -80.19, 25.76, 'MSC Seaview');- Le Visite (Dipendono da Nave e Porto. Nota il NULL sulla EndDate della MSC, significa che è ancora attraccata!) INSERT INTO

VISITS

(

StartDate

,

EndDate

,

SName

,

Pname

,

State\_Name

,

Water\_Name

) VALUES ('2026-03-01', '2026-03-05', 'Ever Given', 'Porto di Ancona', 'Italia', 'Mare Adriatico'), ('2026-03-16', NULL, 'MSC Seaview', 'Port of Miami', 'USA', 'Oceano Atlantico');

#### ON UPDATE/ ON DELETE

The commands ON UPDATE and ON DELETE are real triggers linked with foreign keys.

They answer to a question: “if i modify or destroy the identity of the parent, What should the database do to the Children who depend on it?

#### 4 Possible Reactions

Restrict (or No Action)

This is the default behaviour if you don’t write anything. The database protect the child blocking the parent.

Example:

DELETE FROM PORT WHERE PName = 'Porto di Ancona’

Messaggio di MySQL:

This image couldn’t be found.

[Learn more](https://www.notion.com/help/images-files-and-media)

localhost (Error 404)

#1451 - Cannot delete or update a parent row: a foreign key constraint fails (\`ship\_tracking1\`.\`ship\`, CONSTRAINT \`fk\_ship\_homeport\_final\` FOREIGN KEY (\`Home\_PName\`, \`State\_Name\`, \`Water\_Name\`) REFERENCES \`port\` (\`PName\`, \`State\_Name\`, \`Water\_Name\`))

Solution:

DELETE FROM VISITS WHERE PName = 'Porto di Ancona' DELETE FROM PORT WHERE PName = 'Porto di Ancona'

CASCADE - Domino Effect

The database propagates the parent's action to all children instantly, invisibly and unstoppably.

Example:

CONSTRAINT

fk\_visits\_port

FOREIGN KEY (

Pname

,

State\_Name

,

Water\_Name

) REFERENCES

PORT

(

PName

,

State\_Name

,

Water\_Name

) ON UPDATE CASCADE ON DELETE CASCADE

SET NULL

The parent vanishes or changes, and the child remains “orphan”

Where don’t you have to insert it?

We can’t use ON DELETE SET NULL in any weak entity

Technical Reason:

Remember that the weak entity use the foreign key as part of their primary key. So In the case of visits table, port can’t be null

Where do you have to insert it?

It’s perfect for the strong entities that has an optional foreign key

Like Ship, for example:

\- 1. Togliamo il divieto di "NOT NULL" dalle colonne del porto nella tabella SHIP ALTER TABLE

SHIP

MODIFY

Home\_PName

VARCHAR(255) NULL; ALTER TABLE

SHIP

MODIFY

State\_Name

VARCHAR(255) NULL; ALTER TABLE

SHIP

MODIFY

Water\_Name

VARCHAR(255) NULL;- 2. Applichiamo il vincolo con il SET NULL ALTER TABLE

SHIP

ADD CONSTRAINT

fk\_ship\_homeport\_null

FOREIGN KEY (

Home\_PName

,

State\_Name

,

Water\_Name

) REFERENCES

PORT

(

PName

,

State\_Name

,

Water\_Name

) ON UPDATE CASCADE ON DELETE SET NULL;![](https://www.notion.so/image/attachment%3Ab9af90c9-2d02-46ad-8f48-65f9c630cfe9%3Aimage.png?table=block&id=325843e8-3372-801b-a98b-db0ef75444d6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

SET DEFAULT

If the Parent disappears, the child is automatically reassigned to a “backup” parent.

To let it works we need two elements:

The declaration of Default in the column

The trigger “On delete set default” on the foreing key

Example:

![](https://www.notion.so/image/attachment%3Aa30ea9bb-70be-4cbd-878d-4e5815b74701%3Aimage.png?table=block&id=325843e8-3372-8042-b57b-f9fcf8f4d123&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=450&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Phase 1: Create the parachute

When you define the TYPE column inside the table SHIP you need to tell it what its save value is.

ALTER TABLE

SHIP

MODIFY

Type

VARCHAR(255) DEFAULT 'Cargo';

Phase 2: Trigger

Now you apply the foreign key telling to the database to use that parachute in case of emergency

ALTER TABLE

SHIP

ADD CONSTRAINT

fk\_ship\_type\_def

FOREIGN KEY (

Type

) REFERENCES

SHIP\_TYPE

(

Type

) ON DELETE SET DEFAULT

ON UPDATE CASCADE O RESTRICT!;