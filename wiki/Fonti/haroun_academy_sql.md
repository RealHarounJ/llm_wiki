---
tags: [sql, database, ddl, er_mapping]
aliases: [Haroun Academy SQL]
date_created: 2026-05-14
last_modified: 2026-05-14
source_count: 1
---
# Haroun Academy SQL Script

## Sintesi
Questo file contiene lo script SQL DDL per la creazione del database "Haroun Academy", una piattaforma globale di e-learning.
Il livello accademico è universitario e mostra la traduzione da schema concettuale (ER) a schema logico/fisico relazionale.

## Concetti Chiave Applicati
- **Gerarchia ISA**: L'entità base `USER_ACCOUNT` ha le sottoclassi `INSTRUCTOR` e `STUDENT` (gestite tramite foreign key `user_id` con `ON DELETE CASCADE`).
- **Attributi Multivalore**: La tabella `STUDENT_INTERESTS` modella un attributo multivalore con una chiave primaria composta `(user_id, interest)`.
- **Relazione Ricorsiva M:N**: La tabella `PREREQUISITE` mappa la relazione tra un corso e i suoi corsi propedeutici `(main_course_code, prereq_course_code)`.
- **Entità Debole**: L'entità `LESSON` dipende da `COURSE`, e la sua chiave primaria è composta dalla chiave forte e dalla chiave parziale `(course_code, lesson_number)`.

## Fonti
- `haroun_academy.sql` (in root workspace)
