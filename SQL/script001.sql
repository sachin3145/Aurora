CREATE DATABASE IF NOT EXISTS AURORA;
USE AURORA;

CREATE TABLE IF NOT EXISTS GAME_STATS(
    PLAYER_ID CHAR(10) PRIMARY KEY,
    PLAYER_NAME VARCHAR(30),
    SCORE INT DEFAULT 0,
    BADGES TEXT DEFAULT 'No badges earned yet!',
    PROGRESS VARCHAR(3) DEFAULT '0%'
                                       );

-- The table definitions below are incomplete,
-- more data fields are required to complete them.


CREATE TABLE IF NOT EXISTS HIGH_SCORE(
    PLAYER_ID CHAR(10) NOT NULL UNIQUE,
    /*
    MORE CODE HERE
    */
    FOREIGN KEY (PLAYER_ID) REFERENCES GAME_STATS(PLAYER_ID)
                                         );

CREATE TABLE IF NOT EXISTS PLANETS(
    PLANET_ID CHAR(10) PRIMARY KEY,
    NAME VARCHAR(10),
    RADIUS FLOAT DEFAULT 1
    /*
     MORE CODE HERE
     */
                                  );