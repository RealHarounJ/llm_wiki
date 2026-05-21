---
tags: [database, relational-model, constraints, keys, primary-key, elmasri-navathe, study-notes]
aliases: [Relational Model Notes, Elmasri Chapter 4]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 4: The Relational Data Model and Relational Database Constraints


## Chapter 4) Relational Data Model

First introduced by Ted Codd (in 1970)

[www.seas.upenn.edu](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)

Relational Data Model use concept of mathematical relation

### Terminologies

Relational model represents data as a collection of tables

A table is also called a relation

Each row is called tuple

![](https://www.notion.so/image/attachment%3A4e6fc0e0-f887-4472-a61f-727329ed3a15%3Aimage.png?table=block&id=30b843e8-3372-805f-9c2b-e62d9d539bfd&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Each column headers → Attributes

![](https://www.notion.so/image/attachment%3Aa71f6738-8820-488f-89ef-b610b5f2350b%3Aimage.png?table=block&id=30b843e8-3372-80c1-91bb-d8d530ae94ed&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Terminologies Part 2

Domain:

Set of possibile values allowed for an attribute

Example

Name: string of characters that represent name of persons.

Employee\_ages: Possible ages of employees of a company (values between 20 and 70 years old)

Relation schema:

Used to describe a relation or a table

Made up of a relation name R and a list of attributes A1,A2,A3,An.

![](https://www.notion.so/image/attachment%3A1a716272-cc6c-414c-8cb0-9a9879e6cfa2%3Aimage.png?table=block&id=30b843e8-3372-80d4-b8d5-fd4aba41ec41&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Degree (or arity) of a relation:

Number of attributes in a relation schema.

![](https://www.notion.so/image/attachment%3A89645d86-469b-421f-8616-e20ef081514a%3Aimage.png?table=block&id=30b843e8-3372-8004-9840-d1ee526ca8b7&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Cardinality:total number of tuples present in a relation.

![](https://www.notion.so/image/attachment%3A186f4ab4-1dfa-4267-9e88-5df142148359%3Aimage.png?table=block&id=30b843e8-3372-803b-b5fc-ecf0a69b41d9&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Relational database schema: is a set of relation schemas and a set of integrity constraints.

Relation state: a set of tuples at a given moment of time

### Characteristics of Relations

Notice!

Set → {1,2,3,4}

A relation is a set of tuples

Tuples in a relation need not have any particular order

Ordering of Values within a Tuple:

An n-tuple is an ordered list of n values,so ordering of values in a tuple is important

Tuple: A set of attribute value pair, then ordering of attributes is not important

Each value in a tuple is an atomic value

### Characteristics of Relations

Interpretation of a Relation:

The relation schema can be represented as a declaration or assertion.

Each tuple can be interpreted as a fact.

![](https://www.notion.so/image/attachment%3A105ad460-026b-4d45-a78b-e51bb67239aa%3Aimage.png?table=block&id=30c843e8-3372-804d-9c84-e0cb02a2d495&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1400&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Specialization and Generalization

## Specialization

An entity set may include sub-group of entities in some way

Example: The entity set Person may be further classified as Employee or Student

Specialization follow a top-down approach in which a higher level entity is classified into subtypes that has different attributes

It is basically disjoint) a person must be a thing or another= in nature and has is-a relationship

![](https://www.notion.so/image/attachment%3Ab1d100c0-7d67-49eb-af39-672f26db7587%3Aimage.png?table=block&id=30c843e8-3372-804d-a10f-f7530a606933&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1130&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Generalization

Two or more lower level entities combine to form a higher level entity if they have common attributes.

It is a bottom-up approach

Example: The entity set instructor with attributes instructor\_id, instructor\_name, instructor\_salary, and rank can be generalized with the entity set employee with attributes employee\_id, employee\_name. employee\_salary and hrs\_per\_week.

![](https://www.notion.so/image/attachment%3Acfeac8d2-8d9c-4323-aaf8-8b702b7d752b%3Aimage.png?table=block&id=30c843e8-3372-809c-9028-e74a7de1b228&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=860&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Aggregation

One limitation with the E-R model is that it cannot express relationship among relationships

The relation between two entities is treated as a single entity

It is an abstraction trough which relationships are treated as higher-level entities

![](https://www.notion.so/image/attachment%3A4bc674bc-ca1e-4dde-94ac-315cf4d87b23%3Aimage.png?table=block&id=30c843e8-3372-805d-bc8d-d1003b148b37&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1180&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Inheritance

Higher-level and lower-level entity sets also mayu be designed by the terms superclass and subclass, respectively.

When we talk about person entity we know it’s the super class or the higher level entity whereas the employee and student subclasses

A crucial property of the higher-level and lower-level entities created by specialization and generalization is attribute inheritance (eredietarità)

The attributes of the higher-level entity sets are said to be inherited by the lower-level entity sets.

### Exercises

Specialization Disjoint Total

![](https://www.notion.so/image/attachment%3A829cea11-22b9-4751-a62a-e45edb3b6991%3Aimage.png?table=block&id=30c843e8-3372-8029-9e39-c0931e299435&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1320&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Specialization Overlapping Partial

![](https://www.notion.so/image/attachment%3Acd8ab296-7fd2-40cd-b663-15aea0d5ca76%3Aimage.png?table=block&id=30c843e8-3372-8059-8818-ed6f1b67c5e5&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1290&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Specialization Disjoint and Partial

![](https://www.notion.so/image/attachment%3Ab653149b-0718-4903-8504-6cb690531f4f%3Aimage.png?table=block&id=30c843e8-3372-80d8-b762-d4fa357d96db&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1230&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Specialization Overlapping and Total

![](https://www.notion.so/image/attachment%3Ab997db0c-3ca6-4bf1-b5a4-a611e51fc25a%3Aimage.png?table=block&id=30c843e8-3372-80f0-9934-ea6f2e3417d8&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1140&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3Aeaf193d3-94cc-4fa3-acc7-8a116aecb01f%3ADiagramma_senza_titolo.drawio_(3).png?table=block&id=312843e8-3372-8064-97c1-d8de6fa12ae5&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3Aeb2f681a-eb6c-4f7a-97c5-d8bfb1b392e4%3ADiagramma_senza_titolo.drawio_(7).png?table=block&id=313843e8-3372-8032-b31b-f6f1c0d13f07&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Specializzazione e Generalizzazione non sono simboli grafici diversi, ma sono i due percorsi mentali opposti (le due facce della stessa medaglia logica) che un progettista di database usa per arrivare a disegnare quelle gerarchie che hai appena completato.

Ecco la scomposizione definitiva dei due approcci, applicata al tuo esame.

La Specializzazione (L'approccio Top-Down / Dall'alto verso il basso):

Prendi un'entità generale già esistente e la "spacchi" in sottogruppi più specifici per poterne gestire i dettagli unici.

L'esempio nel tuo esame: Il testo partiva dicendo che ci sono degli

USER

(Utenti). Poi, per esigenze amministrative, ci ha costretto a scendere nel dettaglio e a specializzare questa entità in

STUDENT

e

PROFESSOR

, aggiungendo matricole e dipartimenti. Sei partito dal generale e sei sceso nello specifico.

La Generalizzazione (L'approccio Bottom-Up / Dal basso verso l'alto):

Osservi diverse entità specifiche sul campo, ti accorgi che hanno molti attributi in comune e decidi di "estrarre" questi dati comuni portandoli al piano di sopra, in una nuova superclasse inventata da te, per evitare di scrivere le stesse cose due volte.

L'esempio nel tuo esame: Immagina se la biblioteca avesse iniziato a catalogare separatamente i

PHYSICAL\_BOOKS

(con Titolo e Anno) e gli

AUDIOVISUAL\_MEDIA

(anch'essi con Titolo e Anno). Per non sprecare memoria ripetendo le colonne "Titolo" e "Anno" in decine di tabelle diverse, hai generalizzato il concetto creando la superclasse

RESOURCE

e ci hai spostato dentro gli attributi condivisi.![](https://www.notion.so/image/attachment%3A19b3e6e9-9bdc-423e-b4cf-649a640879a3%3A1.drawio.png?table=block&id=314843e8-3372-80bc-89f6-d17e9afad3f5&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1310&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]