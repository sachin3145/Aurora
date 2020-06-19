CREATE DATABASE IF NOT EXISTS AURORA;
USE AURORA;


-- game_starts table, will we used as a primary table
CREATE TABLE IF NOT EXISTS game_stats(
    PLAYER_ID CHAR(10) PRIMARY KEY,
    PLAYER_NAME VARCHAR(30),
    LEVEL INT,
    SCORE INT DEFAULT 0,
    BADGES TEXT DEFAULT 'No badges earned yet!',
    PROGRESS VARCHAR(3) DEFAULT '0%'
                                       );

-- this table holds data for troops that player has unlocked
CREATE TABLE IF NOT EXISTS player_troops(
    PLAYER_ID CHAR(10) NOT NULL UNIQUE,
    DELTA INT DEFAULT 1,
    TARDIS INT DEFAULT 0,
    BENZAMITE INT DEFAULT 0,
    MANDALORE INT DEFAULT 0,
    NEMESIS INT DEFAULT 0,
    ARMADA INT DEFAULT 0,
    ELSYIUM  INT DEFAULT 0,
    DEMOGORGON INT DEFAULT 0,
    FOREIGN KEY (PLAYER_ID) REFERENCES GAME_STATS(PLAYER_ID)
                                         );

-- this table holds data for spells that player has unlocked
CREATE TABLE IF NOT EXISTS player_spells(
    PLAYER_ID CHAR(10) NOT NULL UNIQUE,
    RAY_OF_SICKNESS INT DEFAULT 1,
    INCINERATE INT DEFAULT 0,
    PLASMA_DISCHARGE  INT DEFAULT 0,
    GOD_OF_CHAOS INT DEFAULT 0,
    FOREIGN KEY (PLAYER_ID) REFERENCES GAME_STATS(PLAYER_ID)
                                         );

-- details of troops and spells attack defence and spells
CREATE TABLE IF NOT EXISTS STATS(
    NAME VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HP INT
);
INSERT INTO STATS VALUES ('DELTA', 0, 0, 0),
                         ('TARDIS', 0, 0, 0),
                         ('BENZAMITE', 0, 0, 0),
                         ('MANDALORE', 0, 0, 0),
                         ('NEMESIS', 0, 0, 0),
                         ('ARMADA', 0, 0, 0),
                         ('ELSYIUM', 0, 0, 0),
                         ('DEMOGORGON', 0, 0, 0),
                         ('RAY_OF_SICKNESS', 0, 0, NULL),
                         ('INCINERATE', 0, 0, NULL),
                         ('PLASMA_DISCHARGE', 0, 0, NULL),
                         ('GOD_OF_CHAOS', 0, 0, NULL);

-- Table holds data of enemy planets
CREATE TABLE IF NOT EXISTS PLANETS(
    PLANET_ID CHAR(10) PRIMARY KEY,
    NAME VARCHAR(10),
    ATTACK INT,
    DEFENCE INT,
    HP INT
                                  );
INSERT INTO PLANETS VALUES (1, 'Mercury', 0, 0,0),
                           (2, 'Venus', 0, 0, 0),
                           (3, 'Earth', 0, 0,0),
                           (4, 'Mars', 0, 0,0),
                           (5, 'Jupiter', 0, 0,0),
                           (6, 'Saturn', 0, 0,0),
                           (7, 'Uranus', 0, 0,0),
                           (8, 'Neptune', 0, 0,0);


CREATE TABLE IF NOT EXISTS SPELLS(
    PLAYER VARCHAR(20) UNIQUE,
    RAY_OF_SICKNESS INT,
    INCINERATE INT,
    PLASMA_DISCHARGE INT,
    GOD_OF_CHAOS INT
);

CREATE TABLE IF NOT EXISTS DELTA(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS TARDIS(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS BENZAMITE(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS MANDALORE(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS NEMESIS(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS ELYSIUM(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS ARMADA(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);

CREATE TABLE IF NOT EXISTS DEMOGORGON(
    PLAYER VARCHAR(20) UNIQUE,
    ATTACK INT,
    DEFENCE INT,
    HEALTH INT
);
