-- Database: bootcamp

-- DROP DATABASE bootcamp;

-- create table students(
-- student_id serial primary key,
-- last_name varchar(255) not NULL,
-- first_name varchar(255) not NULL,
-- birth_date date)


-- -- INSERT -- --
-- insert into students(first_name, last_name,birth_date)
-- values ('Marc','Benichou','1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03'),
-- ('Danielle', 'katzav','1993-02-09')


-- -- SELECT -- --

-- Fetch all of the data from the table.
-- select * from students

-- Fetch all of the students first_names and last_names.
-- select last_name, first_name from students


-- For the following questions, only fetch the first_names and last_names of the students.

-- Fetch the student which id is equal to 2.
-- select last_name, first_name from students where student_id = 2

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
-- select last_name, first_name from students where last_name = 'Benichou' and first_name = 'Marc'

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
-- select last_name, first_name from students where last_name = 'Benichou' or first_name = 'Marc'

-- Fetch the students whose first_names contain the letter a.
-- select last_name, first_name from students where first_name like '%a%'

-- Fetch the students whose first_names start with the letter a.
-- select last_name, first_name from students where first_name like 'a%'
-- select last_name, first_name from students where first_name ilike 'a%'

-- Fetch the students whose first_names end with the letter a.
-- select last_name, first_name from students where first_name like '%a'

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
-- select last_name, first_name from students where substr(first_name,2,1)='a'

-- Fetch the students whose id’s are equal to 1 AND 3 .
-- select last_name, first_name from students where student_id = 1 or student_id = 3


-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
-- select * from students where birth_date >= '2000-01-01'