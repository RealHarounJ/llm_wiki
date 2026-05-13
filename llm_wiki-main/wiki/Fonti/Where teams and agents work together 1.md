---
title: "Where teams and agents work together"
source: "https://www.notion.so/Fundamentals-of-Database-Systems-2f4843e8337280ed9da6fe65eb396bb6"
author:
published:
created: 2026-05-05
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
## Fundamentals of Database Systems

#### 1) Data model

IT (esaustivo): Un modello dei dati è un insieme di concetti per descrivere struttura (tipi, relazioni, vincoli) e spesso anche operazioni (query/aggiornamenti) di un database. Serve a parlare in modo standardizzato dei dati, dal design all’implementazione.

EN: A data model is a set of concepts to describe a database’s structure (types, relationships, constraints) and often operations (retrieval/updates). It is the foundation for design and implementation.

Pratica (azienda): scegli il modello relazionale → userai tabelle, PK/FK.

Esempio mini-schema:

CREATE TABLE Customer( customer\_idINTPRIMARY KEY, emailVARCHAR(255)UNIQUE );

#### 2) Database schema

IT: Lo schema è la descrizione del database (tabelle, attributi, vincoli, viste). È “il progetto” e cambia raramente.

EN: The schema is the description of the database (tables, attributes, constraints, views). It changes infrequently.

Pratica: lo schema è ciò che metti in Git come migration:

ALTER TABLE CustomerADDCOLUMN birthdateDATE;

#### 3) Database state (instance)

IT: Lo stato (o istanza) è il contenuto attuale: le righe presenti “oggi”. Cambia ogni insert/update/delete.

EN: The database state/instance is the current content (the rows currently stored). It changes with every insert/update/delete.

Pratica: righe reali:

INSERT INTO Customer(customer\_id,email)VALUES (1,'luca@x.com');

#### 4) Internal schema

IT: Descrive come i dati sono memorizzati fisicamente (file, pagine, indici, partizioni).

EN: Describes how data is stored physically (files, pages, indexes, partitions).

Pratica (DBA):

CREATE INDEX idx\_customer\_emailON Customer(email);

#### 5) Conceptual schema

IT: Descrizione logica globale dell’intero database (entità/relazioni o tabelle/relazioni), indipendente dal fisico.

EN: The global logical description of the whole database, independent of physical storage.

Pratica: “tutte le tabelle + vincoli” del sistema (Customer, Order, Product, …).

#### 6) External schema (view)

IT: Descrive le viste per gruppi di utenti: ognuno vede solo la parte che gli serve.

EN: Describes views for user groups; each sees only what they need.

Pratica: vista per customer care:

CREATEVIEW CustomerCareViewASSELECT customer\_id, emailFROM Customer;

#### 7) Data independence

IT: Capacità di cambiare uno schema a un livello senza rompere i livelli superiori.

EN: Ability to change the schema at one level without requiring changes at higher levels.

Pratica: aggiungo un indice (fisico) senza cambiare query/app.

#### 8) DDL (Data Definition Language)

IT: Linguaggio per definire strutture: CREATE/ALTER/DROP, vincoli, viste.

EN: Language to define structures: CREATE/ALTER/DROP, constraints, views.

Pratica:

CREATE TABLE

,

ALTER TABLE

,

CREATE VIEW

.

#### 9) DML (Data Manipulation Language)

IT: Linguaggio per interrogare e modificare dati: SELECT/INSERT/UPDATE/DELETE.

EN: Language to query and modify data: SELECT/INSERT/UPDATE/DELETE.

Pratica:

SELECT\*FROM CustomerWHERE emailLIKE'%@x.com';

#### 10) SDL (Storage Definition Language)

IT: Concetti/comandi per definire strutture di memorizzazione (oggi spesso “comandi DBA” più che un linguaggio separato).

EN: Concepts/commands to define storage structures (often DBA-specific commands today).

Pratica: partizionamento/indici/comandi storage (dipende dal DBMS).

#### 11) VDL (View Definition Language)

IT: Parte del linguaggio per definire viste (spesso inglobato in SQL).

EN: The part used to define views (often integrated into SQL).

Pratica:

CREATE VIEW...

.

#### 12) Query language

IT: DML ad alto livello usato “standalone” per fare query (SQL).

EN: A high-level DML used standalone to query (SQL).

Pratica: un analista usa solo SELECT.

#### 13) Host language

IT: Linguaggio generale (Java/Python/JS) che incorpora la DML (embedded SQL / API).

EN: A general-purpose language (Java/Python/JS) that embeds DML via APIs or embedded SQL.

Pratica (pseudo):

cursor.execute("SELECT \* FROM Customer WHERE customer\_id=%s", (1,))

#### 14) Data sublanguage

IT: Sotto-linguaggio per dati dentro un host language (tipicamente SQL + API).

EN: The data-oriented sublanguage within a host language (typically SQL + DB API).

Pratica: “SQL dentro Python”.

#### 15) Database utility

IT: Strumenti di supporto (backup, restore, import/export, monitor).

EN: Support tools (backup, restore, import/export, monitoring).

Pratica: dump/restore, tool di migrazione, analyzer indici.

#### 16) Catalog

IT: Il catalogo contiene metadati: descrizione di tabelle, vincoli, viste, indici.

EN: The catalog stores metadata: table definitions, constraints, views, indexes.

Pratica: il DBMS consulta il catalogo quando esegui una query.

#### 17) Client/server architecture

IT: Separazione tra client (UI/app) e server (DBMS) che gestisce i dati.

EN: Separation between client (UI/app) and server (DBMS) managing data.

Pratica: app mobile → API → DB server.

#### 18) Three-tier architecture

IT: Presentation (client) → Application server → Database server.

EN: Presentation (client) → Application server → Database server.

Pratica (flusso):

Mobile/Web → Backend (API) → DB

#### 19) N-tier architecture

IT: Estensione a più livelli (API gateway, microservizi, cache, ecc.) per scalare e separare responsabilità.

EN: Extension to multiple layers (API gateway, microservices, cache, etc.) for scalability and separation of concerns.

Pratica:

Client → Gateway → ServiceA/B → Cache → DB Cluster

### 2.2 Categorie di data model + differenze relazionale/object/XML

IT (esaustivo):

Relazionale: dati in tabelle, relazioni via PK/FK, query SQL set-oriented.

Object model: dati come oggetti con attributi e (spesso) comportamento/metodi; mapping più naturale con OOP.

XML model: dati gerarchici/semistrutturati (documenti), schema più flessibile.

EN:

Relational: tables, PK/FK relationships, set-oriented SQL queries.

Object: objects with attributes (and often behavior/methods); natural for OOP.

XML: hierarchical/semi-structured document data, flexible schema.

Pratica:

E-commerce “ordine/prodotti” → relazionale.

CAD/oggetti complessi → più naturale object.

Documenti scambiati tra sistemi (payload) → XML/JSON-like.

### 2.3 Differenza schema vs state

IT: schema = struttura/progetto; state = contenuto attuale.

EN: schema = structure/blueprint; state = current content.

Pratica:

Migrazione

ALTER TABLE

cambia schema.

INSERT/UPDATE/DELETE

cambia state.

### 2.4 Three-schema architecture + perché servono mapping + ruolo dei linguaggi

IT (esaustivo):

External: viste utenti

Conceptual: schema logico globale

Internal: memorizzazione fisica

Servono mapping per tradurre richieste/risultati tra livelli (da vista → schema logico → storage e ritorno).

EN:

External views, conceptual global schema, internal storage schema. Mappings translate requests/results between levels.

Pratica (esempio):

Utente fa

SELECT

su una VIEW (external)

DBMS riscrive la query sulle tabelle (conceptual)

Optimizer decide indici/piani (internal)

Risultato torna all’utente.

### 2.5 Logical vs Physical data independence + quale è più difficile

IT:

Physical: cambi fisico (indici, file) senza cambiare schema logico/viste → più “facile”.

Logical: cambi schema logico senza cambiare viste/programmi → più difficile perché le app spesso dipendono dalla struttura logica.

EN:

Physical independence is usually easier; logical independence is harder because applications/views depend on the logical structure.

Pratica:

Aggiungo indice → app invariata.

Rinomino una colonna usata dall’app → rischio di rompere tutto.

### 2.6 Procedural vs nonprocedural DML

IT:

Procedurale: dici come ottenere il risultato (passo-passo, record-oriented).

Non procedurale: dici cosa vuoi (set-oriented), il DBMS decide come.

EN:

Procedural = specify how; nonprocedural = specify what.

Pratica: SQL è nonprocedurale:

SELECT emailFROM CustomerWHERE customer\_id=1;

### 2.7 Interfacce user-friendly + utenti tipici

IT + pratica:

GUI report: manager

Query tool (SQL): analisti/sophisticated users

Program API: sviluppatori

Natural language: utenti occasionali (limitato)

EN: same mapping: menu/forms for naive users, SQL tools for analysts, APIs for developers, etc.

### 2.8 Con quali altri software interagisce un DBMS

IT: OS, file system, rete, application server, strumenti di sviluppo, sistemi di sicurezza/backup.

EN: OS, file system, networking, app servers, dev tools, security/backup systems.

Pratica: il DBMS legge/scrive su disco via OS e comunica via rete con l’app server.

### 2.9 Two-tier vs Three-tier

IT:

Two-tier: client ↔ DB (client “pesante”)

Three-tier: client ↔ app server ↔ DB (più sicuro e scalabile)

EN:

Two-tier: client directly talks to DB; three-tier: client talks to app server which talks to DB.

Pratica: web app moderna quasi sempre three-tier.

### 2.10 Esempi di utilities/tools

IT: backup/restore, import/export, monitor performance, rebuild indici, migrazioni schema, auditing.

EN: backup/restore, import/export, performance monitoring, index rebuild, schema migrations, auditing.

Pratica: “ieri notte backup automatico”, “oggi analyzer indici perché query lenta”.

### 2.11 Cosa aggiunge N-tier (n > 3)

IT: più livelli = più specializzazione: gateway, microservizi, cache, message queue, replica/cluster, load balancer.

EN: additional layers: gateway, microservices, cache, queues, replication/cluster, load balancing.

Pratica (pipeline):

Client → API Gateway → Auth Service → Orders Service → Cache → DB Cluster

## Extra: 2.15 “Unique constraints” (metodo pratico)

Regola pratica: qualsiasi ID/chiave naturale che identifica univocamente un’entità deve essere UNIQUE.

Esempi tipici (oltre a Student\_number):

COURSE:

Course\_number

UNIQUESECTION: combinazione (

Course\_number

,

Section\_number

,

Semester

,

Year

) UNIQUE (se identifica una sezione in modo univoco)PREREQUISITE: (

Course\_number

,

Prereq\_number

) UNIQUEGRADE\_REPORT / ENROLLMENT: (

Student\_number

,

Section\_identifier

) UNIQUE (uno studente non può iscriversi due volte alla stessa sezione)