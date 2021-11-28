-- Database: Hollywood

-- DROP DATABASE "Hollywood";

-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Dana','Mel','08/10/14970', 5),('nom','nom','06/08/1965', 2)

-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- select count(*) from actors

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- insert into actors(first_name, last_name)
-- values ('Brad','Pitt')
