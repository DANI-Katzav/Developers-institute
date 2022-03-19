-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- select count(*) from actors

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
insert into actors(first_name, last_name)
values ('Brad','Pitt')
-- --  output error 'age' has to received an input not null 