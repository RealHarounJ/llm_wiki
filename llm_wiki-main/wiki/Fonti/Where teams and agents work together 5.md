---
title: "Where teams and agents work together"
source: "https://www.notion.so/Chapter-6-Basics-SQL-311843e83372805fb1e1c0b94c6992e8"
author:
published:
created: 2026-05-05
description: "A collaborative AI workspace, built on your company context. Build and orchestrate agents right alongside your team's projects, meetings, and connected apps."
tags:
  - "clippings"
---
## Chapter 6) Basics SQL

#### 6.3.4 Tables as Sets in SQL

In pure mathematics (the Relational Algebra on which SQL is based), a set cannot have duplicates. If you have a basket with an apple and you put another identical, by pure mathematics you still have “ the concept of an apple”.

But SQL breaks this mathematical rule and uses Multisets, where duplicates are allowed. If you query to extract the Continent from our State table, SQL will return Europe,North America, Africa… and if we had 10 states in Europe, it would return Europe 10 times.

Why this choice?

Computational cost (Performance)

Eliminate duplicates is really slowly

Aggregation Functions(Statitics)

if we want to compute an average for ex: (AVG(Salary)), and three people earn 25.000$, we need all three 25.000$ to make the correct mathematical average. If SQL eliminated duplicates automatically, the statistics would be destroyed.

#### Distinct

When we want to force SQL to behave as the pure mathematics (eliminating duplicates), we have to use the DISTINCT clause.

SELECT DISTINCT: if a ship visited the same port 5 times, the sql engine works more, filter data, and shows you which port only once.

#### Set Operations

These operations eliminates duplicates automatically.

UNION ( A U B ): Merges the results of two different queries into a single column, removing duplicates.

INTERSECT ( A ∩ B): Find only the rows that are present in both queries at the same time.

EXCEPT ( A \\ B): Subtract the results of the second query from the first ( show me what there is in the first that are not in the SECOND).

#### UNION VS UNION ALL

Union

He controls every single line. If it sees a duplicate, it discards it. This requires a huge computational effort.

Union All

Takes the two queries and glues them one under the other without looking anyone in the face. If there are 5 duplicates, it shows you all

#### PATTERN MATCHING (LIKE, %, \_)

When you are not searching an exact identity (’ = ‘), but a “blueprint”, you uses the LIKE operator.

%

Substitute every number of caracters.

Esempio:

WHERE PName LIKE '%Miami%'

trova "Port of Miami", "Miami Beach", o semplicemente "Miami"

The underscore ( \_ )

Substitute exactly a caracter.

Esempio:

WHERE Hull LIKE '\_ouble'

troverà "Double" ma non "Trouble" (perché 'Trouble' ha due lettere prima della 'o').

#### VIRTUAL COLUMNS (as)

L'Esempio del Libro:

1.1 \* E.Salary AS Increased\_sal

non modifica il database (non è un

UPDATE

). Crea semplicemente un report visivo temporaneo in cui i dipendenti sembrano più ricchi del 10%.

#### BETWEEN

The between operator is what in it we call Syntactic Sugar. It doesn’t add a new power to the database, but make the ode more readable for the humans.

Architectural Detail:

Salary BETWEEN 30000 AND 40000

is the exact trasnlation of

\>= 30000 AND <= 40000

.

It works also with DATA type

#### ORDER BY

With order by we force the engine to make an extra work of sorting.

ASC (Ascending)

Invisible default. Goes from A to Z, or from the smallest number to the biggest

DESC ( Descending)

Goes from Z to A, or goes from the biggest number to the smallest

CASCADING (Multi-Column) Sorting:

If you write ORDER BY State\_Name ASC, PName DESC,SQL first puts the states in alphabetical order.Then only for the ports that are in the same state,it orders them in reverse order.

CREATE Table vehicle( vin int primary key, model varchar(20) not null, Price float not null, category enum('Engine\_size','No\_seats','Tonnage')

); CREATE TABLE salesperson( sid int primary key, name varchar(20) not null

); CREATE TABLE customer( ssn int primary key, name varchar(20) not null, city varchar(20) not null, state varchar(20) not null, street varchar(20) not null, sid int not null UNIQUE, Foreign key (sid) REFERENCES salesperson(sid) on UPDATE CASCADE on delete cascade

); CREATE TABLE sale(

data

date not null, sid int not null unique, ssn int not null unique, vin int not null UNIQUE, foreign key(sid) REFERENCES salesperson(sid), foreign key(ssn) REFERENCES vehicle(ssn), foreign key(vin) REFERENCES customer(vin)

);

use medici; CREATE TABLE school( name varchar(20) primary key, city varchar(20) ); CREATE TABLE department( dep\_name varchar(20) primary key, id\_employee int not null unique ); CREATE TABLE employee( id\_employee int primary key, address varchar(20), phone varchar(20), name varchar(20), start\_date date, dep\_name varchar(20) not null unique, FOREIGN KEY (dep\_name) REFERENCES department(dep\_name) on UPDATE CASCADE on DELETE CASCADE ); ALTER TABLE department ADD CONSTRAINT fk\_dep\_emp FOREIGN KEY (id\_employee) REFERENCES employee(id\_employee) on UPDATE CASCADE on DELETE CASCADE; CREATE TABLE profession( name varchar(20) not null unique, code1 int primary key, description varchar(20), foreign key (name) REFERENCES school(name) on UPDATE CASCADE on DELETE cascade ); CREATE TABLE physician( license\_no int primary key, specialization varchar(20), id\_physician int not null unique, id\_employee int not null unique, FOREIGN key (id\_employee) REFERENCES employee(id\_employee) ); CREATE TABLE study( date1 date, name\_school varchar(20) not null unique, code\_profession int not null unique, license\_no int not null unique, FOREIGN key (name\_school) REFERENCES school(name) on update cascade on delete CASCADE, FOREIGN key (code\_profession) REFERENCES profession(code) on UPDATE CASCADE on DELETE CASCADE, FOREIGN key (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE schedule1( day int primary key, from\_time TIME, to\_time TIME, license\_no int not null UNIQUE, FOREIGN KEY (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADe ); CREATE TABLE visit( date1 date primary key, diagnosis varchar(20), license\_no int not null unique, id\_patient int not null unique, FOREIGN KEY (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE medicine( name varchar(20), med\_code int primary key ); CREATE TABLE prescription( no\_of\_days int, qty\_per\_day int, med\_code int not null unique, date1 date not null unique, FOREIGN KEY (date1) REFERENCES visit(date1) on UPDATE CASCADE on DELETE CASCADE, FOREIGN KEY (med\_code) REFERENCES medicine(med\_code) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE patient( id\_patient int primary key, name varchar(20), address varchar(20), phone varchar(20) ); CREATE TABLE nurse( id\_employee int not null unique, degree varchar(20), job\_description varchar(20), id\_nurse int primary key, FOREIGN KEY (id\_employee) REFERENCES employee(id\_employee) on UPDATE CASCADE on DELETE CASCADE ); Solution----- DROP DATABASE IF EXISTS medici; CREATE DATABASE medici; USE medici; -- 1. CREAZIONE TABELLE INDIPENDENTI (Genitori assoluti) CREATE TABLE school ( name varchar(20) primary key, city varchar(20) ); CREATE TABLE medicine ( name varchar(20), med\_code int primary key ); CREATE TABLE patient ( id\_patient int primary key, name varchar(20), address varchar(20), phone varchar(20) ); CREATE TABLE profession ( name varchar(20) not null unique, code1 int primary key, description varchar(20), foreign key (name) REFERENCES school(name) on UPDATE CASCADE on DELETE cascade ); -- 2. RISOLUZIONE DIPENDENZA CIRCOLARE (Employee / Department) -- Prima creiamo department SENZA la foreign key CREATE TABLE department ( dep\_name varchar(20) primary key, id\_employee int not null unique ); -- Ora creiamo employee CON la foreign key verso department (Sistemato id\_employee) CREATE TABLE employee ( id\_employee int primary key, address varchar(20), phone varchar(20), name varchar(20), start\_date date, dep\_name varchar(20) not null unique, FOREIGN KEY (dep\_name) REFERENCES department(dep\_name) on UPDATE CASCADE on DELETE CASCADE ); -- Ora "saldiamo" la foreign key mancante su department ALTER TABLE department ADD CONSTRAINT fk\_dep\_emp FOREIGN KEY (id\_employee) REFERENCES employee(id\_employee) on UPDATE CASCADE on DELETE CASCADE; -- 3. CREAZIONE TABELLE DIPENDENTI (Figli) CREATE TABLE nurse ( id\_nurse int primary key, degree varchar(20), job\_description varchar(20), id\_employee int not null unique, FOREIGN KEY (id\_employee) REFERENCES employee(id\_employee) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE physician ( license\_no int primary key, specialization varchar(20), id\_physician int not null unique, id\_employee int not null unique, FOREIGN key (id\_employee) REFERENCES employee(id\_employee) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE schedule1 ( day int primary key, from\_time TIME, to\_time TIME, license\_no int not null UNIQUE, FOREIGN KEY (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADE ); -- 4. TABELLE ASSOCIATIVE / COMPLESSE CREATE TABLE study ( date1 date, name\_school varchar(20) not null unique, code\_profession int not null unique, license\_no int not null unique, FOREIGN key (name\_school) REFERENCES school(name) on update cascade on delete CASCADE, FOREIGN key (code\_profession) REFERENCES profession(code1) on UPDATE CASCADE on DELETE CASCADE, FOREIGN key (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE visit ( date1 date primary key, diagnosis varchar(20), license\_no int not null unique, id\_patient int not null unique, FOREIGN KEY (license\_no) REFERENCES physician(license\_no) on UPDATE CASCADE on DELETE CASCADE, FOREIGN KEY (id\_patient) REFERENCES patient(id\_patient) on UPDATE CASCADE on DELETE CASCADE ); CREATE TABLE prescription ( no\_of\_days int, qty\_per\_day int, med\_code int not null unique, date1 date not null unique, FOREIGN KEY (date1) REFERENCES visit(date1) on UPDATE CASCADE on DELETE CASCADE, FOREIGN KEY (med\_code) REFERENCES medicine(med\_code) on UPDATE CASCADE on DELETE CASCADE );