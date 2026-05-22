---
tags: [dbms, database, relational-mapping, exam-prep, car-dealer]
aliases: [Car_Dealer_Mapping]
date_created: 2026-05-20
last_modified: 2026-05-20
source_count: 1
---

# 🚗 Esercizio 2 (Mappatura) — Car Dealer EER Diagram

Questo documento contiene la risoluzione ufficiale per la mappatura nel modello relazionale dell'**Esercizio 2 (Car Dealer)** rappresentato nel diagramma stampato.

---

## 1. Analisi dello Schema EER di Partenza

Lo schema EER presenta le seguenti componenti:
*   **Superclasse `VEHICLE`**:
    *   Attributi: `Vin` (Chiave Primaria), `Price`, `Model`.
    *   Specializzazione disjoint e totale (simbolo `d` con doppia linea): si divide nelle sottoclassi `CAR`, `TRUCK` e `SUV`.
*   **Sottoclasse `CAR`**: Attributo specifico `Engine_size`.
*   **Sottoclasse `TRUCK`**: Attributo specifico `Tonnage`.
*   **Sottoclasse `SUV`**: Attributo specifico `No_seats`.
*   **Entità `SALESPERSON`**: Attributi `Sid` (Chiave Primaria), `Name`.
*   **Entità `CUSTOMER`**: Attributi `Ssn` (Chiave Primaria), `Name` e l'attributo composto `Address` (`State`, `Street`, `City`).
*   **Relazione Ternaria `SALE`**:
    *   Collega `VEHICLE` (cardinalità $N$, partecipazione $0 \dots N$), `SALESPERSON` (cardinalità $1$, partecipazione $1 \dots N$) e `CUSTOMER` (cardinalità $1$, partecipazione $1 \dots 1$).
    *   Attributo della relazione: `Date`.

---

## 2. Processo di Mappatura (Step-by-Step)

### Step 1: Mappatura delle Entità Regolari e Composte
L'attributo composto `Address` di `CUSTOMER` viene "appiattito" nei suoi componenti semplici.
*   **`SALESPERSON`** (<u>`Sid`</u>, `Name`)
*   **`CUSTOMER`** (<u>`Ssn`</u>, `Name`, `State`, `Street`, `City`)

### Step 2: Mappatura della Specializzazione (`VEHICLE` $\rightarrow$ `CAR`, `TRUCK`, `SUV`)
Applichiamo l'**Opzione 8A** (relazioni multiple per superclasse e sottoclassi). Questa opzione è la migliore perché la superclasse `VEHICLE` partecipa a una relazione esterna (`SALE`).

*   **`VEHICLE`** (<u>`Vin`</u>, `Price`, `Model`)
*   **`CAR`** (<u>`*Vin*`</u>, `Engine_size`)
    *   *`Vin` è sia Chiave Primaria che Chiave Esterna riferita a `VEHICLE(Vin)` con eliminazione/aggiornamento in cascata (`ON DELETE CASCADE`).*
*   **`TRUCK`** (<u>`*Vin*`</u>, `Tonnage`)
    *   *`Vin` è sia Chiave Primaria che Chiave Esterna riferita a `VEHICLE(Vin)`.*
*   **`SUV`** (<u>`*Vin*`</u>, `No_seats`)
    *   *`Vin` è sia Chiave Primaria che Chiave Esterna riferita a `VEHICLE(Vin)`.*

### Step 3: Mappatura della Relazione Ternaria `SALE`
La relazione `SALE` collega `VEHICLE` ($N$), `SALESPERSON` ($1$) e `CUSTOMER` ($1$).
*   Tutte le chiavi primarie delle entità partecipanti entrano come chiavi esterne in `SALE`.
*   Poiché la partecipazione di `CUSTOMER` è `(1,1)`, ogni cliente effettua esattamente una sola transazione nel sistema. Di conseguenza, `Ssn` non si ripete mai in `SALE`.
*   La **Chiave Primaria** di `SALE` è quindi **`Ssn`** (oppure, se si considera che un veicolo fisico reale `Vin` viene venduto al massimo una volta, anche `Vin` o la coppia `(Vin, Sid)` possono essere candidati chiavi. Lo standard accademico per la cardinalità $1:1:N$ predilige `Ssn` o la coppia `(Vin, Sid)`).

Utilizzando la tabella di giunzione separata:
*   **`SALE`** (<u>`*Ssn*`</u>, `*Vin*`, `*Sid*`, `Date`)
    *   *`Ssn` è PK e FK che punta a `CUSTOMER(Ssn)`*
    *   *`Vin` è FK che punta a `VEHICLE(Vin)`*
    *   *`Sid` è FK che punta a `SALESPERSON(Sid)`*

---

## 3. Schema Relazionale Finale (Codice DDL SQL)

```sql
-- 1. Tabella Superclasse Veicoli
CREATE TABLE VEHICLE (
    Vin VARCHAR(50) PRIMARY KEY,
    Price DECIMAL(10, 2) NOT NULL,
    Model VARCHAR(100) NOT NULL
);

-- 2. Tabelle Sottoclassi (Ereditarietà Option 8A)
CREATE TABLE CAR (
    Vin VARCHAR(50) PRIMARY KEY,
    Engine_size DECIMAL(4, 2) NOT NULL,
    FOREIGN KEY (Vin) REFERENCES VEHICLE(Vin) ON DELETE CASCADE
);

CREATE TABLE TRUCK (
    Vin VARCHAR(50) PRIMARY KEY,
    Tonnage DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (Vin) REFERENCES VEHICLE(Vin) ON DELETE CASCADE
);

CREATE TABLE SUV (
    Vin VARCHAR(50) PRIMARY KEY,
    No_seats INT NOT NULL,
    FOREIGN KEY (Vin) REFERENCES VEHICLE(Vin) ON DELETE CASCADE
);

-- 3. Tabella Venditori
CREATE TABLE SALESPERSON (
    Sid VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

-- 4. Tabella Clienti (Address appiattito)
CREATE TABLE CUSTOMER (
    Ssn VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    State VARCHAR(50),
    Street VARCHAR(100),
    City VARCHAR(50)
);

-- 5. Tabella Relazione Ternaria (SALE)
CREATE TABLE SALE (
    Ssn VARCHAR(50) PRIMARY KEY, -- PK per via della cardinalità (1,1) di CUSTOMER
    Vin VARCHAR(50) NOT NULL,
    Sid VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (Ssn) REFERENCES CUSTOMER(Ssn) ON DELETE CASCADE,
    FOREIGN KEY (Vin) REFERENCES VEHICLE(Vin),
    FOREIGN KEY (Sid) REFERENCES SALESPERSON(Sid)
);
```

---

## Fonti
*   *Elmasri & Navathe, Fundamentals of Database Systems*, Capitolo 9 (Mappatura da modello ER/EER a Relazionale), Step 8 (Mappatura relazioni n-arie) e Step 4 (Mappatura specializzazioni).
