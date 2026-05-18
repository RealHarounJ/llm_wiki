---
tags: [sql, database, ddl, er_mapping, healthcare]
aliases: [Healthcare DB SQL]
date_created: 2026-05-14
last_modified: 2026-05-14
source_count: 1
---
# Healthcare DB SQL Script

## Sintesi
Questo script definisce lo schema relazionale in SQL DDL per il "Metropolitan Healthcare System", applicando regole avanzate di progettazione per basi di dati a livello universitario.

## Concetti Chiave Applicati
- **Gerarchia ISA**: L'entità base `MEDICAL_STAFF` ha come sottoclassi `DOCTOR` e `NURSE`.
- **Relazione Ricorsiva 1:N**: Un dottore supervisiona un altro dottore (`supervisor_id` in `DOCTOR` come Foreign Key ricorsiva su `staff_id`, con `ON DELETE SET NULL`).
- **Relazione Obbligatoria 1:1**: Il vincolo `NOT NULL` e la Foreign Key su `manager_id` nella tabella `HOSPITAL` garantiscono che ogni ospedale abbia un manager (che è un dottore).
- **Attributo Multivalore**: Tabella `PATIENT_PHONES` associata a `PATIENT`.
- **Entità Debole**: `ADMISSION` usa come chiave la combinazione di un paziente, un ospedale e la data `(patient_ssn, hospital_id, admission_date)`.
- **Relazione Ternaria/Complessa**: `PRESCRIBES` collega il dottore, il farmaco e la specifica ammissione ospedaliera (che include paziente, ospedale e data), dimostrando come mappare associazioni M:N che coinvolgono entità deboli.

## Fonti
- `healthcare_db.sql` (in root workspace)
