-- ============================================================
--  PIATTAFORMA STREAMING MUSICALE — Schema Relazionale
--  DDL Completo
-- ============================================================

-- ============================================================
--  ENTITÀ BASE
-- ============================================================

CREATE TABLE UTENTE (
    user_id            INT          NOT NULL AUTO_INCREMENT,
    username           VARCHAR(100) NOT NULL,
    email              VARCHAR(150) NOT NULL UNIQUE,
    data_registrazione DATE         NOT NULL,
    tipo_abbonamento   ENUM('free','premium','family') NOT NULL DEFAULT 'free',
    PRIMARY KEY (user_id)
);

CREATE TABLE ARTISTA (
    artista_id       INT          NOT NULL AUTO_INCREMENT,
    nome_arte        VARCHAR(100) NOT NULL,
    paese            VARCHAR(100),
    genere_principale VARCHAR(100),
    PRIMARY KEY (artista_id)
);

CREATE TABLE ALBUM (
    album_id           INT          NOT NULL AUTO_INCREMENT,
    titolo             VARCHAR(150) NOT NULL,
    anno_uscita        YEAR         NOT NULL,
    tipo               ENUM('singolo','EP','LP') NOT NULL,
    data_pubblicazione DATE,
    artista_id         INT          NOT NULL,   -- FK verso ARTISTA (relazione PUBBLICA 1:N)
    PRIMARY KEY (album_id),
    FOREIGN KEY (artista_id) REFERENCES ARTISTA(artista_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE CANZONE (
    canzone_id     INT          NOT NULL AUTO_INCREMENT,
    titolo         VARCHAR(150) NOT NULL,
    durata_secondi INT          NOT NULL,
    explicit       BOOLEAN      NOT NULL DEFAULT FALSE,
    numero_traccia INT          NOT NULL,       -- attributo di CONTIENE
    album_id       INT          NOT NULL,       -- FK verso ALBUM (relazione CONTIENE 1:N)
    PRIMARY KEY (canzone_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE PLAYLIST (
    playlist_id    INT          NOT NULL AUTO_INCREMENT,
    nome           VARCHAR(150) NOT NULL,
    data_creazione DATE         NOT NULL,
    pubblica       BOOLEAN      NOT NULL DEFAULT FALSE,
    user_id        INT          NOT NULL,       -- FK verso UTENTE (una playlist ha un owner)
    PRIMARY KEY (playlist_id),
    FOREIGN KEY (user_id) REFERENCES UTENTE(user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- ============================================================
--  RELAZIONI M:N
-- ============================================================

-- COLLABORA: artisti che collaborano in una canzone (feat., produttori, ecc.)
CREATE TABLE COLLABORA (
    artista_id INT          NOT NULL,
    canzone_id INT          NOT NULL,
    ruolo      VARCHAR(100) NOT NULL DEFAULT 'featured',
    PRIMARY KEY (artista_id, canzone_id),
    FOREIGN KEY (artista_id) REFERENCES ARTISTA(artista_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (canzone_id) REFERENCES CANZONE(canzone_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- ============================================================
--  RELAZIONI TERNARIE
-- ============================================================

-- AGGIUNGE: un utente aggiunge una canzone a una playlist
CREATE TABLE AGGIUNGE (
    user_id       INT  NOT NULL,
    canzone_id    INT  NOT NULL,
    playlist_id   INT  NOT NULL,
    data_aggiunta DATE NOT NULL,
    posizione     INT  NOT NULL,
    PRIMARY KEY (user_id, canzone_id, playlist_id),
    FOREIGN KEY (user_id)     REFERENCES UTENTE(user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (canzone_id)  REFERENCES CANZONE(canzone_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (playlist_id) REFERENCES PLAYLIST(playlist_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- ASCOLTA: storico degli ascolti — stessa canzone ascoltata più volte
CREATE TABLE ASCOLTA (
    user_id    INT      NOT NULL,
    canzone_id INT      NOT NULL,
    timestamp  DATETIME NOT NULL,
    completata BOOLEAN  NOT NULL DEFAULT FALSE,
    PRIMARY KEY (user_id, canzone_id, timestamp),
    FOREIGN KEY (user_id)    REFERENCES UTENTE(user_id)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (canzone_id) REFERENCES CANZONE(canzone_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- ============================================================
--  DATI DI ESEMPIO
-- ============================================================

INSERT INTO UTENTE (username, email, data_registrazione, tipo_abbonamento) VALUES
    ('mario_r',    'mario@email.it',   '2023-01-15', 'premium'),
    ('giulia_m',   'giulia@email.it',  '2023-03-22', 'free'),
    ('luca_t',     'luca@email.it',    '2024-06-01', 'family'),
    ('sara_b',     'sara@email.it',    '2022-11-10', 'premium'),
    ('marco_v',    'marco@email.it',   '2024-01-01', 'free');

INSERT INTO ARTISTA (nome_arte, paese, genere_principale) VALUES
    ('The Weeknd',    'Canada',     'R&B'),
    ('Dua Lipa',      'UK',         'Pop'),
    ('Kendrick Lamar','USA',        'Hip-Hop'),
    ('Måneskin',      'Italia',     'Rock'),
    ('Sfera Ebbasta', 'Italia',     'Trap');

INSERT INTO ALBUM (titolo, anno_uscita, tipo, data_pubblicazione, artista_id) VALUES
    ('After Hours',   2020, 'LP', '2020-03-20', 1),
    ('Future Nostalgia', 2020, 'LP', '2020-03-27', 2),
    ('Mr. Morale',    2022, 'LP', '2022-05-13', 3),
    ('Rush!',         2023, 'LP', '2023-01-20', 4),
    ('Famoso',        2020, 'LP', '2020-10-09', 5);

INSERT INTO CANZONE (titolo, durata_secondi, explicit, numero_traccia, album_id) VALUES
    ('Blinding Lights',  200, FALSE, 1, 1),
    ('Save Your Tears',  215, FALSE, 2, 1),
    ('Levitating',       203, FALSE, 1, 2),
    ('Physical',         194, FALSE, 2, 2),
    ('N95',              188, TRUE,  1, 3),
    ('Die Hard',         222, TRUE,  2, 3),
    ('Gossip',           195, FALSE, 1, 4),
    ('Supermodel',       210, FALSE, 2, 4),
    ('Nuovo Range',      178, TRUE,  1, 5),
    ('Hype',             165, TRUE,  2, 5);

INSERT INTO PLAYLIST (nome, data_creazione, pubblica, user_id) VALUES
    ('Chill Vibes',     '2024-01-10', TRUE,  1),
    ('Workout Mix',     '2024-02-15', FALSE, 1),
    ('Preferiti',       '2023-12-01', TRUE,  2),
    ('Domenica Mattina','2024-03-05', FALSE, 3);

INSERT INTO COLLABORA (artista_id, canzone_id, ruolo) VALUES
    (5, 6,  'featured'),   -- Sfera feat. in Die Hard
    (2, 1,  'featured'),   -- Dua Lipa feat. in Blinding Lights
    (3, 10, 'produttore'); -- Kendrick produttore in Hype

INSERT INTO AGGIUNGE (user_id, canzone_id, playlist_id, data_aggiunta, posizione) VALUES
    (1, 1, 1, '2024-01-11', 1),
    (1, 3, 1, '2024-01-11', 2),
    (1, 5, 2, '2024-02-16', 1),
    (2, 7, 3, '2024-01-05', 1),
    (3, 2, 4, '2024-03-06', 1);

INSERT INTO ASCOLTA (user_id, canzone_id, timestamp, completata) VALUES
    (1, 1, '2024-03-01 08:00:00', TRUE),
    (1, 1, '2024-03-01 18:30:00', TRUE),  -- stesso utente, stessa canzone, orario diverso ✅
    (1, 3, '2024-03-02 09:15:00', FALSE),
    (2, 5, '2024-03-03 14:00:00', TRUE),
    (3, 7, '2024-03-04 20:00:00', TRUE),
    (4, 2, '2024-03-05 07:45:00', TRUE);
