---
tags: [concept, theory]
aliases: [Modellazione ER]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---
# 🗂️ Conceptual Database Modeling (ER)

## 1. Introduzione: L'Astrazione dei Dati
Il modello **Entity-Relationship (ER)** è un modello concettuale ad alto livello. Serve per descrivere la struttura del database in modo indipendente dal software che verrà usato (DBMS). 
Lo scopo è fare una mappatura del "Mini-World" (la porzione di realtà che vogliamo modellare) identificando concetti chiari e privi di ambiguità.

---

## 2. Entità e Attributi

### Entità (Entities)
Un'entità è un "oggetto" del mondo reale che ha una sua esistenza indipendente.
*   **Strong Entity (Entità Forte):** Esiste da sola. Ha sempre una chiave primaria (Primary Key) che la identifica in modo univoco. *(Rappresentazione: Rettangolo singolo)*
*   **Weak Entity (Entità Debole):** Non ha una vera chiave primaria e non può esistere senza un'entità "Padre" (Owner Entity). Viene identificata tramite una **Partial Key** e la chiave del padre. *(Rappresentazione: Doppio Rettangolo)*

### Attributi (Attributes)
Le proprietà che descrivono un'entità.
*   **Simple Attribute:** Indivisibile (es. `Age`, `Gender`). *(Rappresentazione: Ovale)*
*   **Composite Attribute:** Divisibile in sotto-parti (es. `Address` diviso in `Street`, `City`, `Zip`). *(Rappresentazione: Ovale con altri ovali attaccati)*
*   **Multi-valued Attribute:** Può avere più valori per la stessa entità (es. `Phone_Numbers`, `Degrees`). Rischia di violare la First Normal Form (1NF) nel modello relazionale. *(Rappresentazione: Doppio Ovale)*
*   **Derived Attribute:** Il suo valore viene calcolato da altri attributi (es. `Age` calcolato da `Birth_Date`). Non viene salvato fisicamente. *(Rappresentazione: Ovale tratteggiato)*
*   **Key Attribute (Primary Key):** Identifica univocamente l'entità. *(Rappresentazione: Ovale con nome sottolineato. Partial Key: Sottolineatura tratteggiata).*

---

## 3. Relazioni (Relationships)
Una relazione è un'associazione tra due o più entità. *(Rappresentazione: Rombo)*

### Tipi di Relazione
*   **Identifying Relationship:** La relazione che lega una Weak Entity alla sua Owner Entity. *(Rappresentazione: Doppio Rombo)*
*   **Recursive Relationship:** Un'entità si relaziona con se stessa (es. Employee supervisiona Employee). È fondamentale specificare i **Role Names** (es. "Supervisor" e "Supervised").

### Cardinalità: Notazione (Min, Max)
I numeri tra parentesi vicino all'entità indicano quante volte una singola istanza di quell'entità può partecipare alla relazione.
*   **Min = 0:** Partecipazione **Parziale** (Opzionale).
*   **Min > 0 (es. 1):** Partecipazione **Totale** (Obbligatoria).
*   **Max = 1:** Indica che la chiave esterna andrà in questa tabella (l'entità "vede" al massimo 1 controparte).
*   **Max = N:** Può relazionarsi infinite volte.

*(Ricorda: Se entrambe le entità hanno Max=N, è una relazione M:N e nel modello relazionale servirà una tabella di collegamento - Junction Table).*

---

## 4. Gerarchie ISA (Specialization / Generalization)
Si usa quando un'entità (Superclass) può essere divisa in sottocategorie (Subclasses) che ereditano tutti i suoi attributi, ma hanno attributi o relazioni proprie.

Si definisce tramite due vincoli fondamentali (Constraints):

### 1. Disjointness Constraint (D/O)
*   **Disjoint (`d`):** Un'istanza della superclasse può appartenere a **una sola** sottoclasse alla volta. (es. Un impiegato può essere o Segretario o Ingegnere, non entrambi).
*   **Overlapping (`o`):** Un'istanza della superclasse può appartenere a **più** sottoclassi contemporaneamente. (es. Una persona può essere sia Studente che Dipendente dell'università).

### 2. Completeness Constraint (Single/Double Line)
*   **Total Specialization (Doppia Linea):** Ogni istanza della superclasse **DEVE** appartenere ad almeno una sottoclasse. Non esistono "Superclassi pure".
*   **Partial Specialization (Singola Linea):** Alcune istanze della superclasse possono **NON** appartenere a nessuna delle sottoclassi descritte.

---

## 5. Regole d'oro per l'esame
1.  **Se ha un ID Univoco:** È SEMPRE un'entità (forte), non può mai essere una relazione o un attributo.
2.  **Weak Entities:** Hanno sempre una Partial Key (tratteggiata) e un identifying relationship (doppio rombo) `(1,1)` verso il padre.
3.  **Relazioni su Relazioni:** Non puoi attaccare un'entità direttamente a un rombo (salvo nei modelli estesi tramite *Aggregation*).
4.  **Mappatura FK in (Min, Max):** L'entità che ha un `Max = 1` verso la relazione, "cattura" la Foreign Key. Se entrambe hanno `Max = N`, si crea una nuova tabella.

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
