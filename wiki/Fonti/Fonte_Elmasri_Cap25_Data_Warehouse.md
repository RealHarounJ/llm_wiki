---
tags: [database, data-warehouse, OLAP, ETL, MDM, multidimensional-model, elmasri-navathe, study-notes]
aliases: [Data Warehousing Notes, Elmasri Chapter 25]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---

# ðŸ“– Database Systems - Capitolo 25: Data Warehousing and OLAP


## Data Warehouse

Traditional databases are created to handle current operations, however, they present limits for long term analysis.

Storage time: Transactional Database (called OLTP - Online Transaction Processing) has the aim to record transactions: Insert, update, or delete data quickly and without errors.

Main Features:

Current Data: Contains only the necessary data for the current operation

High Speed: (Read/Write)

Data Integrity

Decision-Making: The data warehouse keeps years of data precisely to allow historical analysis

A Data Warehouse is not only a bigger database, is created in a different way

Analysis Trio:

Data Warehousing

Is a collection of informations specifically designed to support business decisions.

Online Analytical Processing (olap)

DW supports applications as OLAP

Data Mining

### Definition of Data Warehouse

A subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management’s decision-making process.

Subject- Oriented means that focus on business area like the sales for instance

Integrated because integrate multiple sources systems

Time-Variant, you can keep historical data inside the dw

Non-volatile, it means once the data entered the dw is not deleted or modified

![](https://www.notion.so/image/attachment%3A170cde85-0dac-407e-9183-2d966b9a19d1%3Aimage.png?table=block&id=33c843e8-3372-8058-b8eb-ecd9b909ca8e&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1330&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Manual Scenario

![](https://www.notion.so/image/attachment%3Ad9a01556-adbf-410f-b8a6-537a46912db9%3Aimage.png?table=block&id=33c843e8-3372-8073-a008-d7f63a5d40e1&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

### Scenario Data Warehouse

We will have a very important component called ETL ( extract, transform, load ), then we can create multiple reports and as well we can create integrated reports from multiple sources

#### Data Modeling for Data Warehouses

Traditional databases usually handle data in two dimensions, just like a standard spreadsheet.

Ex: We might have rows for product and columns for sales regions. if we add a third dimension, such as Fiscal Quarters, we create a 3d matrix where each single cell represents the exact combination of these three pieces of information

![](https://www.notion.so/image/attachment%3Adbd1aa07-f2fd-41e4-b537-313cf84512c8%3Aimage.png?table=block&id=33c843e8-3372-806f-9452-c98a6decbcff&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1210&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A2ac5de18-98b5-4fe2-8127-780e3ef39288%3Aimage.png?table=block&id=33c843e8-3372-80d5-94c0-dfb52c5762aa&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

This models can have more than 3 dimensions, in this case we talk about hypercubes.

The big advantage of this structure is that the performance of queries are higher respect the relational model, as the system exploits the natural relationship already “embedded” in the data.

In order to manipulate the cube we use different methods:

| Operazione | Descrizione | Effetto Pratico |
| --- | --- | --- |
| Pivoting (Rotazione) | Cambia l'orientamento degli assi nel cubo. | Le Regioni che erano colonne possono diventare righe, mentre i Trimestri diventano colonne. |
| Slice (Fetta) | Estrae una "fetta" bidimensionale da un cubo a 3 o più dimensioni. | Vedere solo la tabella "Prodotto vs Regione" per un singolo trimestre specifico. |
| Slice and Dice | Riduzione sistematica dei dati in blocchi o viste più piccole. | Analizzare i dati da molteplici angolazioni per rendere visibili dettagli specifici. |
| Roll-up | Si muove verso l'alto in una gerarchia di dati. | Passare dalla visualizzazione delle vendite settimanali a quelle trimestrali o annuali (maggiore generalizzazione). |
| Drill-down | Si muove verso il basso per rivelare livelli di dettaglio crescenti. | È il complemento del roll-up: passare dai dati annuali a quelli mensili per vedere i dettagli. |

#### How Data Warehouse organize the data for analysis

Fact Table: contains the observed measures or variables, as the revenue or the selled quantity.

Dimension Tables: Represent the fac, for exampl if the fact is a sell, the dimension migh be product, region and fiscal period

Example:

Fact Table

![](https://www.notion.so/image/attachment%3Ab35f8448-8309-4e20-bbbb-492901109656%3Aimage.png?table=block&id=348843e8-3372-80c5-9e1e-fdbdd993bbc6&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Dimension Table (It is storing an extra information)

![](https://www.notion.so/image/attachment%3Af33a2f03-dd4c-427d-92de-ea4982776280%3Aimage.png?table=block&id=348843e8-3372-80d6-8109-c4d597e73d17&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A4ed8b3a6-40ac-4f83-b1d3-b518a884d3f5%3Aimage.png?table=block&id=33c843e8-3372-8050-91be-e8967bed39f3&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1220&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

There are three ways to link this tables:

Star Schema:

A central fact tabel surrounded by single tables for each dimension

Snowflake Schema:

is a variation on the star schema in which the dimensional tables from a star schema are organized into a hierarchy by normalizing them. (normalize means divide the table into subtables to avoid redundancy)

Fact Costellation: A set of fact tables that share some dimension tables.

In order to find informations quickly we use:

Bitmap Indexing: we use vectors of 0 and 1 to find information quickly

Join Indexing: This indexs keep the relationship between primary keys and foreign key.

#### Building a Data Warehouse

The process is divided into several critical stages:

Data Acquisition(ETL): ETL is a data integration process that combines data from multiple sources and loads it into a target system, like a database or data warehouse. The process consists of three stages: extraction, transformation and loading.

Extraction

In the extraction stage, raw data is extracted from one or more sources and moved to a staging area. The goal is to move data from its original location with as little impact on the source systems as possible.

Once extracted, the data is placed in a staging area. Staging areas are temporary and used to combine data from multiple sources. It can be a simple flat file or a relational database, as seen here.

This diagram uses a traditional ETL process in which the data is transformed and then loaded into the data warehouse. Transformation changes the data so that all data from all sources has the same structure and format. Common transformations include filtering, cleansing, and sorting data.

A data warehouse is a central repository of information that can be analyzed to make more informed decisions. The information can be from a wide variety of sources, as shown in this example, where customer, process, external, supplier, and product data are stored.

Specialized Storage

Design and Architecture:

![](https://www.notion.so/image/attachment%3Add6dcc22-2b6f-42d0-9f08-18b6d6be20eb%3Alicensed-image.jpg?table=block&id=33c843e8-3372-8072-8e52-ee87b1bc625f&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

#### Typical Functionality of a Data Warehouse

Data warehouse are designed to facilitate complex and frequent ‘ad hoc’ queries, offering much more powerful and efficient tools than transactional databases.

Multidimensional Navigation: Users can perform operations such as Roll-up to summarize data or Drill-down to reveal increasing details.

Tipi di sistemi OLAP

Partendo dai concetti di base appena descritti, si può precisare che esistono tre tipologie di sistemi OLAP: multidimensionale (MOLAP: Multidimensional OLAP), relazionale (ROLAP: Relational OLAP) e ibrido (HOLAP: Hybrid OLAP). Ciascuna di queste tipologie presenta i propri benefici, benché non vi sia una concordanza completa relativamente ad essi.

MOLAP è la tipologia più usata e ci si riferisce ad essa comunemente con il termine OLAP. Sfrutta un database di riepilogo avente un motore specifico per l'analisi multidimensionale e crea le dimensioni con un misto di dettaglio ed aggregazioni. Risulta la scelta migliore per quantità di dati ridotte, perché è rapido nel calcolare aggregazioni e restituire risultati; tuttavia crea enormi quantità di dati intermedi.

ROLAP lavora direttamente con [database relazionali](https://it.wikipedia.org/wiki/Database_relazionale); i dati e le tabelle delle dimensioni sono memorizzati come tabelle relazionali e nuove tabelle sono create per memorizzare le informazioni di aggregazione. È considerato più scalabile e presenta requisiti di archiviazione e memoria minori; tuttavia, è lento nella creazione delle tabelle e nel generare il rapporto circa le interrogazioni.

HOLAP utilizza tabelle relazionali per memorizzare i dati e le tabelle multidimensionali per le aggregazioni "speculative". Come dice il nome, questo sistema è un ibrido, poiché viene creato più velocemente di un sistema ROLAP ed è al tempo stesso più scalabile di MOLAP.

La difficoltà nell'implementazione di un database OLAP comincia dalle ipotesi delle possibili interrogazioni utente; scegliere la tipologia di OLAP, lo schema e creare una base dati completa e consistente è un'operazione complessa, decisamente complicata per una base di utenza ampia ed eterogenea.

Gli operatori base di uno strumento OLAP per fare analisi multidimensionale dei dati sono:

pivoting: è l'operazione di rotazione delle dimensioni di analisi. È un'operazione fondamentale per analizzare totali ottenuti in base a dimensioni diverse o se si vogliono analizzare aggregazioni trasversali;

slicing: è l'operazione di estrazione di un subset di informazioni dall'aggregato che si sta analizzando. L'operazione di slicing viene eseguita fissando uno specifico valore per una delle dimensioni del "cubo", estraendo quindi una "fetta" e ottenendo un nuovo cubo con una dimensione in meno rispetto a quello di partenza;

dicing: è l'operazione di estrazione di un subset di informazioni dall'aggregato che si sta analizzando. L'operazione di dicing viene eseguita quando l'analisi viene focalizzata su un sottoinsieme del "cubo" avente particolare interesse per l'analista. In alcuni casi l'operazione di dicing può essere "fisica" nel senso che non consiste solo nel filtrare le informazioni di interesse ma anche nell'estrarle dall'aggregato generale per distribuirne i contenuti;

drill-down: è l'operazione di "esplosione" del dato nelle sue determinanti. L'operazione di drill-down può essere eseguita seguendo due diversi percorsi: la gerarchia costruita sulla dimensione di analisi (p. es.: passaggio dalla famiglia di prodotti all'insieme dei prodotti che ne fanno parte) oppure la relazione matematica che lega un dato calcolato alle sue determinanti (p. es.: passaggio dal margine al ricavo e costo che lo generano). È comprensibile l'importanza di tale operazione ai fini analitici in termini di comprensione delle determinanti di un dato;

drill-across: è l'operazione mediante la quale si naviga attraverso uno stesso livello nell'ambito di una gerarchia. Come visto precedentemente, il passaggio dalla famiglia di prodotti alla lista dei prodotti è un'operazione di drill-down, il passaggio da una famiglia a un'altra famiglia è un'operazione di drill-across;

drill-through: concettualmente simile al drill-down, è l'operazione mediante la quale si passa da un livello aggregato al livello di dettaglio appartenente alla base dati normalizzata. Molti venditori proclamano che i loro prodotti hanno la capacità, mediante l'operazione di drill-through, di passare dal data warehouse ai sistemi transazionali alimentanti. Tale operazione, anche se tecnicamente fattibile sotto una serie di condizioni abbastanza rilevanti, è poco sensata per le problematiche di sicurezza e di performance indotti nei sistemi transazionali stessi.

### Master Data Management

The problem:

Imagine a company that has several softwares do not communicate with each other:

Il CRM (dove i venditori registrano i contatti) ha un cliente chiamato:

Mario Rossi, Telefono: 333-123456

.Il Sistema di Fatturazione (ERP) ha un cliente registrato come:

M. Rossi, Email: mario@email.it, Indirizzo: Via Roma 1

.Il Sistema di Assistenza Clienti ha un ticket aperto da:

Mario Rossi, Indirizzo: Via Roma 1/A

.

For a Data Warehouse they are different people

Solution: The Master Data Management

It’s not a single software, but a mix of human rules,processes and it algorithms with a unique goal: Create a unique,perfect,irrefutable “Truth machine”

Steps that do the MDM:

Cleansing: Corrects typos (”Via rOmA” in Via Roma)

Matching: Use complex algorithms to understand f the record that is in CRM and in the Invoice are the same person, even if they are written differently

Merging: Merge from each system the best pieces to create the golden record

#### Bitmap and Join Index

Bitmap converts datas into vectors composed by only 0 and 1(bit), since the computers are faster processing 0 and 1, the queries are much faster

![](https://www.notion.so/image/attachment%3A8dc76297-55ec-439f-9b14-ee8a8b6872a6%3Aimage.png?table=block&id=348843e8-3372-80c0-b951-f1f298cd4467&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

Advantages:

They offer huge advantages on domains with “ low cardinality”

Refers to how many unique value can have a column

Bassa Cardinalità: Pochi valori possibili. (es. Taglia dell'auto: 4 valori. Genere: 3 valori. Giorno della settimana: 7 valori).

Disadvantages:

Alta Cardinalità: Tantissimi valori unici, quasi uno diverso per ogni riga. (es. Codice Fiscale, Targa dell'auto, Indirizzo Email).

Join table resolve a problem:

With traditional databases when you have to get datas from different tables you use the join, but when you try to use the join in the datawarehouse, this operation will cost a lot in terms of time and computing power.

Instead of doing this we use an Join Index that creates an already computed map

Example in the real life:

![](https://www.notion.so/image/attachment%3A2c914a8d-ecfe-4fab-8a85-b80171a063ab%3Aimage.png?table=block&id=348843e8-3372-80a6-a116-e12eb95470c7&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2) ![](https://www.notion.so/image/attachment%3A3bc67729-6067-42d7-803e-a54a74bfdd17%3Aimage.png?table=block&id=348843e8-3372-80a3-8de1-fc6960736c01&spaceId=04f085f0-9964-4790-bc1b-a8c98d8d5b8a&width=1420&userId=192d872b-594c-8166-ae96-000202569c1b&cache=v2)

#### ETL

Extract: Data are extracted from multiple and heterogeneous sources

Transform - Standardization: the data must be made coherent.

Transform - Cleansing: This is identified as the component that requires the most work of all → this is linked with backflushing: Source system managers often want to receive clean data back from Data Warehouses to update and improve their operating systems.

Transform - Modeling: Datas must be converted from their original model to adapt at the Data Warehouse multidimensional model

Load: due to huge volume, they sometimes use an incremental update is usually used rather than reloading everything from scratch. The loading order is essential to avoid integrity errors: The master data (client, product) must be loaded before the transactions (invoice) that refer to it.

#### Storage and Refresh

The creation of efficient access routes.

The management of time-dependent (time-variant) data as new records arrive.

Partial refreshment (refreshing).

The elimination (purging) of data that is too old (e.g. discarding data older than three years every quarter to free up space).

#### The Design Components

DW needs to consider factors such as who will use it and how.

A central element is the meta-data repository that divides into two categories:

Tecnical: Details on acquisition, storage structure, operations and security

Business: Company ruless and organizational definitions

When you have to manage a DW that is located in many servers:

Distributed Warehouse: Offer several benefits like load balancing, scalability and the higher availability, facing classical problems of distributed databases

Federated Warehouse:A decentralized confederation of autonomous Data Warehouses (often smaller, such as Data Marts), each with its own independent metadata repository.

The piece concludes with a look at current trends. Companies are increasingly less satisfied with traditional systems. The rise of Big Data Analytics has led to the integration of technologies such as Hadoop, specialized graph databases, and key-value stores. The emergence of Data Virtualization platforms is also mentioned, which will allow the construction of purely logical Data Warehouses.

## Fonti
* [[raw/Fundamentals of Database Systems (Ramez Elmasri, Shamkant B. Navathe) (z-library.sk, 1lib.sk, z-lib.sk).md]]