-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Check to see if Database exists, if so, drop this database and create it new

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Players table used for unique player id (primary ket), name and date created 
CREATE TABLE players (id serial primary key,
                      name text not null,
                      created_at timestamp default current_timestamp);


-- Matches table, holds match id, winner and loser information (related to player id from players table)
CREATE TABLE matches (id serial primary key,
                      winner int,
                      loser int,
                      foreign key (winner) references players(id),
                      foreign key (loser) references players(id));
