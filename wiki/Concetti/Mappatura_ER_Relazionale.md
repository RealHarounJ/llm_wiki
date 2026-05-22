---
tags: [concept, theory]
aliases: [Mappatura ER Relazionale]
date_created: 2026-05-21
last_modified: 2026-05-21
source_count: 1
---
# 🗺️ Mappatura ER-Relazionale (I 9 Step)

Processo per trasformare uno schema concettuale (ER/EER) in uno schema logico (Tabelle SQL).

## Gli Step di Base
1. **Entità Forti**: Ogni entità diventa una tabella.
2. **Entità Deboli**: Creare una tabella includendo la PK dell'owner come Foreign Key (FK) con `ON DELETE CASCADE`.
3. **Relazioni 1:1**: Usare l'approccio FK nella tabella con partecipazione totale per evitare valori NULL.
4. **Relazioni 1:N**: Inserire la PK del lato "1" come FK nel lato "N".
5. **Relazioni M:N**: Creare una tabella ponte (Junction Table) con la combinazione delle PK delle due entità.
6. **Attributi Multivalore**: Estrarli in una nuova tabella dedicata per rispettare la 1NF.
7. **Relazioni N-arie**: Trasformarle sempre in una tabella associativa con FK verso tutte le entità partecipanti.

## Step 8: Mappatura della Specializzazione (EER)
Esistono 4 opzioni principali:
- **8A (Separate Tables)**: Una tabella per la superclasse e una per ogni sottoclasse. La PK delle sottoclassi è anche FK verso la superclasse. (Funziona sempre).
- **8B (Subclasses Only)**: Solo tabelle per le sottoclassi, con attributi della superclasse duplicati. (Solo per partecipazione Totale e Disjoint).
- **8C (Single Table + Type)**: Una sola mega-tabella con una colonna "Discriminatore" per indicare il tipo. (Solo per Disjoint).
- **8D (Single Table + Flags)**: Una sola mega-tabella con flag Booleani per ogni sottoclasse. (Ottimo per Overlapping).

## Step 9: Mappatura delle Categorie (Union Types)
Quando le superclassi hanno chiavi primarie diverse (es. Persona con SSN e Azienda con Partita IVA):
- Si crea una **Chiave Surrogata** (es. `Owner_id`) come PK della tabella Categoria.
- Si aggiunge la chiave surrogata come FK nelle tabelle delle superclassi.

---
*Vedi anche: [[Modellazione_ER]], [[SQL_Esempi_Pratici]]*

## Fonti
* [[wiki/Fonti/Fonte_Database_Systems_Elmasri.md]]
