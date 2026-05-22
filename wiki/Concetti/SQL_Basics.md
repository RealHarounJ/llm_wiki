---
tags: [database, sql, basics]
date_created: 2026-05-07
source: "raw/SQL_Overview.md, wiki/Script/ikea_project.sql, wiki/Script/streaming_musicale.sql"
---

# 💾 SQL — Structured Query Language

## 🎯 Cos'è SQL?
SQL è il linguaggio standard per interagire con database relazionali. Tutti i principali RDBMS lo usano: Oracle, MySQL, PostgreSQL, SQL Server, SQLite.

## 📐 Comandi Fondamentali (DDL + DML)

### DDL — Data Definition Language
```sql
CREATE TABLE Clienti (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE
);

ALTER TABLE Clienti ADD COLUMN telefono VARCHAR(20);
DROP TABLE Clienti;
```

### DML — Data Manipulation Language
```sql
-- Inserimento
INSERT INTO Clienti (id, nome, email) VALUES (1, 'Haroun', 'haroun@email.com');

-- Lettura
SELECT nome, email FROM Clienti WHERE id = 1;

-- Aggiornamento
UPDATE Clienti SET email = 'nuovo@email.com' WHERE id = 1;

-- Cancellazione
DELETE FROM Clienti WHERE id = 1;
```

## 📐 SELECT Avanzato

### Aggregazioni
```sql
SELECT paese, COUNT(*) AS num_clienti, AVG(fatturato) AS media_fatturato
FROM Clienti
GROUP BY paese
HAVING COUNT(*) > 10
ORDER BY media_fatturato DESC;
```

### JOIN — Collegare Tabelle
```sql
-- INNER JOIN: solo le righe che hanno match in entrambe le tabelle
SELECT O.id_ordine, C.nome, O.totale
FROM Ordini O
INNER JOIN Clienti C ON O.id_cliente = C.id;

-- LEFT JOIN: tutti i clienti, anche senza ordini
SELECT C.nome, O.id_ordine
FROM Clienti C
LEFT JOIN Ordini O ON C.id = O.id_cliente;
```

### Subquery
```sql
-- Clienti con fatturato superiore alla media
SELECT nome FROM Clienti
WHERE fatturato > (SELECT AVG(fatturato) FROM Clienti);
```

## 🔑 Concetti Chiave
| Concetto | Descrizione |
|---|---|
| **Primary Key** | Identificatore unico per ogni riga |
| **Foreign Key** | Collega una tabella a un'altra |
| **Index** | Struttura che accelera le query di ricerca |
| **View** | Query salvata come tabella virtuale |
| **Transaction** | Gruppo di operazioni atomiche (ACID) |

## 💼 Esempi dal Tuo Vault
- `wiki/Script/ikea_project.sql` — Progetto IKEA con schema database completo
- `wiki/Script/streaming_musicale.sql` — Database streaming musicale

## 🔗 Collegato a
- [[Modellazione_ER]]
- [[Architettura_DBMS]]
- [[Data_Mining_Hub]]

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
