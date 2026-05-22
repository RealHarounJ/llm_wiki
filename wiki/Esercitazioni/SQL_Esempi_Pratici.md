---
tags: [exercise, practice]
aliases: [SQL Esempi Pratici]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---
# 🚢 Esempi Pratici SQL (Database Navi)

Questi esempi mostrano l'applicazione pratica dei vincoli di integrità e della mappatura delle entità deboli.

## 1. Definizione delle Tabelle (DDL)
Le tabelle devono essere create seguendo l'ordine gerarchico (Genitori prima dei Figli).

```sql
-- 1. Anagrafiche Forti (Genitori)
CREATE TABLE SHIP_TYPE (
    Type VARCHAR(255) PRIMARY KEY,
    Tonnage VARCHAR(255) NOT NULL,
    Hull VARCHAR(255) NOT NULL
);

CREATE TABLE STATE (
    Name VARCHAR(255) PRIMARY KEY,
    Continent VARCHAR(255)
);

-- 2. Entità Debole (Porto dipende da Stato)
CREATE TABLE PORT (
    PName VARCHAR(255),
    State_Name VARCHAR(255),
    Water_Name VARCHAR(255),
    PRIMARY KEY (PName, State_Name, Water_Name),
    FOREIGN KEY (State_Name) REFERENCES STATE(Name)
);

-- 3. Entità Forte con FK (Nave)
CREATE TABLE SHIP (
    SName VARCHAR(255) PRIMARY KEY,
    Owner VARCHAR(255),
    Type VARCHAR(255) NOT NULL,
    Home_PName VARCHAR(255),
    State_Name VARCHAR(255),
    Water_Name VARCHAR(255),
    FOREIGN KEY (Type) REFERENCES SHIP_TYPE(Type),
    FOREIGN KEY (Home_PName, State_Name, Water_Name) REFERENCES PORT(PName, State_Name, Water_Name)
);
```

## 2. Inserimento Dati (DML)
È fondamentale rispettare l'ordine per non violare i vincoli di Foreign Key.

1. Inserire i tipi di nave e gli stati.
2. Inserire i porti.
3. Inserire le navi (che ora hanno porti validi a cui riferirsi).

## 3. Vincoli Complessi: Entità Deboli Associative
La tabella `VISITS` è un esempio di entità debole che lega una Nave a un Porto:
- Chiave Primaria Composta: `(StartDate, SName, PName, State_Name, Water_Name)`.
- Questa struttura assicura che una nave non possa essere in due porti diversi nello stesso momento (StartDate).

---
*Vedi anche: [[Mappatura_ER_Relazionale]]*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
