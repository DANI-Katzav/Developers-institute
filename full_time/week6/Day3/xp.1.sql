--  Exercise 1

-- --1. Get a list of all film languages.
-- select distinct name from language;

-- -- 2. 
-- select title, description, name from film inner join language on film.language_id = language.language_id;
-- -- Get all films, even if they don’t have languages.
-- select title, description, name from film left outer join language on film.language_id = language.language_id;
-- -- Get all languages, even if there are no films in those languages.
-- select title, description, name from film right outer join language on film.language_id = language.language_id;

-- --3.
-- id serial primary key,
-- name varchar(255));

-- insert into new_film(name) values ('Shrek'),('Avatr'),('Metrix'),('Nemo');

-- -- 4. 

-- create table customer_review (
-- review_id serial primary key NOT NULL,
-- film_id INTEGER REFERENCES new_film (id) ON DELETE CASCADE,
-- language_id INTEGER REFERENCES language (language_id) ON DELETE CASCADE,
-- title varchar(50),
-- score smallint,
-- review_text text,
-- last_update date
-- )


-- --5
--  insert into customer_review (film_id,language_id,title, score, review_text, last_update)
--  values ((select id from new_film where name = 'Shrek'), (select language_id from language where name='English'),'Titanic', 9,
--  'Shrek is a 2001 American computer-animated fantasy comedy film loosely based on the 1990 fairy tale picture book of the same name by William Steig,'2001-01-01'),
--  ((select id from new_film where name = 'Avatar'),(select language_id from language where name='English'), 'Avatar', 8,

--6
-- delete from new_film where name = 'Metrix';
-- select * from customer_review

