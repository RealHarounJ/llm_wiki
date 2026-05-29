-- =============================================
-- MUSIC STREAMING PLATFORM — Full Database
-- =============================================

-- =============================================
-- DDL — CREATE TABLES
-- =============================================

CREATE TABLE ARTIST (
    artist_id    INT PRIMARY KEY,
    stage_name   VARCHAR(100) NOT NULL,
    country      VARCHAR(50),
    founding_year INT
);

CREATE TABLE ALBUM (
    album_id     INT PRIMARY KEY,
    title        VARCHAR(100) NOT NULL,
    release_year INT,
    artist_id    INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES ARTIST(artist_id)
);

CREATE TABLE ALBUM_GENRE (
    album_id     INT,
    genre        VARCHAR(50),
    PRIMARY KEY (album_id, genre),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
);

CREATE TABLE SONG (
    track_number     INT,
    album_id         INT,
    title            VARCHAR(100) NOT NULL,
    duration_seconds INT NOT NULL CHECK (duration_seconds > 0),
    PRIMARY KEY (track_number, album_id),
    FOREIGN KEY (album_id) REFERENCES ALBUM(album_id)
);

CREATE TABLE COLLABORATES_ON (
    artist_id    INT,
    album_id     INT,
    PRIMARY KEY (artist_id, album_id),
    FOREIGN KEY (artist_id) REFERENCES ARTIST(artist_id),
    FOREIGN KEY (album_id)  REFERENCES ALBUM(album_id)
);

CREATE TABLE USER (
    user_id           INT PRIMARY KEY,
    username          VARCHAR(50)  NOT NULL UNIQUE,
    email             VARCHAR(100) NOT NULL UNIQUE,
    subscription_type VARCHAR(20)  NOT NULL DEFAULT 'free'
                      CHECK (subscription_type IN ('free', 'premium', 'family'))
);

CREATE TABLE USER_PHONE (
    user_id      INT,
    phone_number VARCHAR(20),
    PRIMARY KEY (user_id, phone_number),
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
);

CREATE TABLE FREE_USER (
    user_id      INT PRIMARY KEY,
    ads_enabled  BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
);

CREATE TABLE PREMIUM_USER (
    user_id      INT PRIMARY KEY,
    expiry_date  DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
);

CREATE TABLE PLAYLIST (
    playlist_id   INT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    creation_date DATE NOT NULL,
    user_id       INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
);

CREATE TABLE INCLUDES (
    playlist_id  INT,
    track_number INT,
    album_id     INT,
    position     INT NOT NULL,
    PRIMARY KEY (playlist_id, track_number, album_id),
    FOREIGN KEY (playlist_id)              REFERENCES PLAYLIST(playlist_id),
    FOREIGN KEY (track_number, album_id)   REFERENCES SONG(track_number, album_id)
);

-- =============================================
-- DML — INSERT DATA
-- =============================================

-- ARTISTS
INSERT INTO ARTIST VALUES (1, 'Taylor Swift',  'USA',    2004);
INSERT INTO ARTIST VALUES (2, 'The Weeknd',    'Canada', 2010);
INSERT INTO ARTIST VALUES (3, 'Dua Lipa',      'UK',     2015);
INSERT INTO ARTIST VALUES (4, 'Ed Sheeran',    'UK',     2004);
INSERT INTO ARTIST VALUES (5, 'Billie Eilish',  'USA',   2015);

-- ALBUMS
INSERT INTO ALBUM VALUES (1, 'Midnights',        2022, 1);
INSERT INTO ALBUM VALUES (2, 'After Hours',       2020, 2);
INSERT INTO ALBUM VALUES (3, 'Future Nostalgia',  2020, 3);
INSERT INTO ALBUM VALUES (4, 'Divide',            2017, 4);
INSERT INTO ALBUM VALUES (5, 'Happier Than Ever', 2021, 5);

-- ALBUM GENRES (multi-valued)
INSERT INTO ALBUM_GENRE VALUES (1, 'Pop');
INSERT INTO ALBUM_GENRE VALUES (1, 'Synth-pop');
INSERT INTO ALBUM_GENRE VALUES (2, 'R&B');
INSERT INTO ALBUM_GENRE VALUES (2, 'Synth-pop');
INSERT INTO ALBUM_GENRE VALUES (3, 'Pop');
INSERT INTO ALBUM_GENRE VALUES (3, 'Dance');
INSERT INTO ALBUM_GENRE VALUES (4, 'Pop');
INSERT INTO ALBUM_GENRE VALUES (4, 'Folk');
INSERT INTO ALBUM_GENRE VALUES (5, 'Pop');
INSERT INTO ALBUM_GENRE VALUES (5, 'Alternative');

-- SONGS (track_number, album_id, title, duration_seconds)
INSERT INTO SONG VALUES (1, 1, 'Lavender Haze',    202, 1);
INSERT INTO SONG VALUES (2, 1, 'Maroon',            213, 1);
INSERT INTO SONG VALUES (3, 1, 'Anti-Hero',         200, 1);
INSERT INTO SONG VALUES (1, 2, 'Alone Again',       234, 2);
INSERT INTO SONG VALUES (2, 2, 'Too Late',          239, 2);
INSERT INTO SONG VALUES (3, 2, 'Blinding Lights',   200, 2);
INSERT INTO SONG VALUES (1, 3, 'Future Nostalgia',  187, 3);
INSERT INTO SONG VALUES (2, 3, 'Levitating',        203, 3);
INSERT INTO SONG VALUES (1, 4, 'Eraser',            227, 4);
INSERT INTO SONG VALUES (2, 4, 'Castle on the Hill',261, 4);
INSERT INTO SONG VALUES (3, 4, 'Shape of You',      234, 4);
INSERT INTO SONG VALUES (1, 5, 'Getting Older',     264, 5);
INSERT INTO SONG VALUES (2, 5, 'Happier Than Ever', 294, 5);

-- COLLABORATIONS (guest features)
INSERT INTO COLLABORATES_ON VALUES (4, 3); -- Ed Sheeran on Dua Lipa album
INSERT INTO COLLABORATES_ON VALUES (2, 1); -- The Weeknd on Taylor Swift album
INSERT INTO COLLABORATES_ON VALUES (3, 4); -- Dua Lipa on Ed Sheeran album

-- USERS
INSERT INTO USER VALUES (1, 'alice99',   'alice@mail.com',   'premium');
INSERT INTO USER VALUES (2, 'brunorock', 'bruno@mail.com',   'free');
INSERT INTO USER VALUES (3, 'claire_d',  'claire@mail.com',  'premium');
INSERT INTO USER VALUES (4, 'david_uk',  'david@mail.com',   'free');
INSERT INTO USER VALUES (5, 'emma_b',    'emma@mail.com',    'family');

-- USER PHONES (multi-valued)
INSERT INTO USER_PHONE VALUES (1, '+39-333-1111111');
INSERT INTO USER_PHONE VALUES (2, '+39-333-2222222');
INSERT INTO USER_PHONE VALUES (2, '+39-333-9999999'); -- bruno has 2 phones
INSERT INTO USER_PHONE VALUES (3, '+33-612-345678');

-- ISA subtypes
INSERT INTO FREE_USER    VALUES (2, TRUE);
INSERT INTO FREE_USER    VALUES (4, TRUE);
INSERT INTO PREMIUM_USER VALUES (1, '2025-12-31');
INSERT INTO PREMIUM_USER VALUES (3, '2024-06-30');
-- user 5 is 'family' → neither FREE nor PREMIUM (partial ISA)

-- PLAYLISTS
INSERT INTO PLAYLIST VALUES (1, 'Chill Vibes',    '2024-01-10', 1);
INSERT INTO PLAYLIST VALUES (2, 'Workout Mix',    '2024-02-15', 2);
INSERT INTO PLAYLIST VALUES (3, 'Late Night',     '2024-03-01', 1);
INSERT INTO PLAYLIST VALUES (4, 'Top Hits 2024',  '2024-04-05', 3);
INSERT INTO PLAYLIST VALUES (5, 'Study Focus',    '2024-04-20', 5);

-- INCLUDES (playlist_id, track_number, album_id, position)
INSERT INTO INCLUDES VALUES (1, 3, 1, 1); -- Anti-Hero in Chill Vibes
INSERT INTO INCLUDES VALUES (1, 2, 3, 2); -- Levitating in Chill Vibes
INSERT INTO INCLUDES VALUES (1, 3, 2, 3); -- Blinding Lights in Chill Vibes
INSERT INTO INCLUDES VALUES (2, 3, 4, 1); -- Shape of You in Workout Mix
INSERT INTO INCLUDES VALUES (2, 2, 3, 2); -- Levitating in Workout Mix
INSERT INTO INCLUDES VALUES (3, 1, 1, 1); -- Lavender Haze in Late Night
INSERT INTO INCLUDES VALUES (3, 2, 2, 2); -- Too Late in Late Night
INSERT INTO INCLUDES VALUES (3, 2, 5, 3); -- Happier Than Ever in Late Night
INSERT INTO INCLUDES VALUES (4, 3, 1, 1); -- Anti-Hero in Top Hits
INSERT INTO INCLUDES VALUES (4, 2, 3, 2); -- Levitating in Top Hits
INSERT INTO INCLUDES VALUES (5, 1, 5, 1); -- Getting Older in Study Focus
INSERT INTO INCLUDES VALUES (5, 1, 4, 2); -- Eraser in Study Focus
