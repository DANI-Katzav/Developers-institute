-- -- -- Exercise 1: DVD Rental -- -- --

-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.
select rating, count(rating) as num_films from film group by rating;

-- Get a list of all the movies that have a rating of G or PG-13.
select title from film where rating = 'G' or rating='PG-13';

-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
select title from film where rating in ('G','PG-13') and length<120 and rental_rate<3.00 order by film asc;


-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
update customer
set first_name = 'Yona', last_name = 'David'
where first_name = 'Jared' and last_name = 'Ely';

-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
update address
set address = '3 yad haroutsim'
where address_id = (select address_id from customer where first_name = 'Yona' and last_name='David');
------------------------------------------------------------------------------
-- -- -- Exercise 2: Students Table -- -- --


-- -- Update -- --
-- 1.‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
update students
set birth_date = '1998-11-02'
where first_name = 'Lea';

-- 2. Change the last_name of David from ‘Grez’ to ‘Guez’.
update students
set last_name = 'Guez'
where last_name = 'Grez';


-- -- Delete -- --
-- 1. Delete the student named ‘Lea Benichou’ from the table.
delete from students
where first_name = 'Lea' and last_name = 'Benichou';


-- -- Count -- --
-- 1. Count how many students are in the table.
select count(*) from students;

-- 2. Count how many students were born after 1/01/2000.
select count(*) from students where birth_date = '2000-01-01';



-- -- Insert / Alter -- --
-- 1. Add a column to the student table called math_grade.
-- alter table students add column math_grade smallint;

-- 2.Add 80 to the student which id is 1.
update students set math_grade = 80 where student_id = 1;

-- 3. Add 90 to the students which have ids of 2 or 4.
update students set math_grade = 90 where student_id = 2 or student_id = 4;

-- 4. Add 40 to the student which id is 6.
update students set math_grade = 40 where student_id = 6;

-- 5. Count how many students have a grade bigger than 83
select count(*) from students where math_grade>83;

-- 6.Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
insert into students(first_name,last_name,birth_date,math_grade) values ('Omer', 'Simpson','1980-10-03',70);
select * from students;

-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
-- Hint : Use GROUP BY.
select first_name, last_name, count(math_grade) as total_grade from students group by (first_name,last_name);


-- -- SUM -- --
-- 1. Find the sum of all the students grades.
select sum(math_grade) from students