-- ex1

-- -- select rating,count(*) from film group by rating
-- -- --select title from film where rating = 'G' or rating='PG-13';

-- -- --UPDATE customer set first_name='Danielle', last_name='Katzav' where customer_id =1;

-- -- --select * from customer where customer_id=1;

-- -- --update address 
-- -- -- set address='grinshpan' 
-- -- -- where  address_id = (select address_id from customer where first_name = 'Danielle' and last_name='Katzav');;

-- ex2:

-- update students
-- set birth_date = '1998-11-02'
-- where first_name = 'Lea';

-- -- 2. 
-- update students
-- set last_name = 'Guez'
-- where last_name = 'Grez';


-- -- 1. 
-- delete from students
-- where first_name = 'Lea' and last_name = 'Benichou';


-- -- 1. 
-- select count(*) from students;

-- -- 2. .
-- select count(*) from students where birth_date = '2000-01-01';




-- -- 1
-- -- alter table students add column math_grade smallint;

-- -- 2.
-- update students set math_grade = 80 where student_id = 1;

-- -- 3
-- update students set math_grade = 90 where student_id = 2 or student_id = 4;

-- -- 4.
-- update students set math_grade = 40 where student_id = 6;


-- 5
-- select count(*) from students where math_grade>83;
-- 6
-- insert into students(first_name,last_name,birth_date,math_grade)
-- values ('Omer', 'Simpson','1980-10-03',70);
-- select * from students;
-- select first_name, last_name, count(math_grade)
-- as total_grade from students group by (first_name,last_name);


-- -- -- SUM -- --
-- -- 1. Find the sum of all the students grades.
-- select sum(math_grade) from students
