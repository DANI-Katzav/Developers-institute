#
# --  Basic Select Statement
#
# select first_name as "First Name", last_name as "Last Name" from employees;
#
# select distinct employee_id from employees;
#
# select * from employees order by first_name desc;
#
# select first_name, last_name, salary, 0.15*salary as "PF" from employees;
#
# select employee_id , first_name, last_name, salary from employees order by salary asc;
#
# select sum(salary) from employees;
#
# select max(salary), min(salary) from employees;
#
# select avg(salary) from employees;
#
# select count(*) from employees;
#
# select UPPER(first_name) from employees;
#
# select left(first_name,3) from employees;
#
# select concat(first_name,' ',last_name) as "Full Name" from employees;
#
# select first_name, last_name, length(concat(first_name,last_name)) from employees;
#
# SELECT first_name, last_name , REGEXP_MATCHES(first_name,'([0-9_]+)','g') FROM employees;
#
# select * from employees limit 10;
#
#
#
# --- Restricting And Sorting
#
# select first_name, last_name, salary from employees where salary between 10000 and 15000;
#
# select first_name, last_name, hire_date from employees where hire_date between '1987-01-01' and '1987-12-31';
#
# select first_name, last_name from employees where first_name ilike '%c%' and first_name ilike '%e%';
#
# select last_name, job_title, salary
# from employees inner join jobs on jobs.job_id = employees.job_id;
#
# from employees inner join jobs on jobs.job_id = employees.job_id
# where job_title != 'Programmer' and job_title != 'Shipping Clerk';
#
# from employees inner join jobs on jobs.job_id = employees.job_id
# where salary not in (4500,10000,15000);
#
# select last_name from employees where length(last_name)=6;
#
# select last_name from employees where substr(last_name,3,1)='e';
#
# select distinct job_title
# from employees inner join jobs on jobs.job_id = employees.job_id;
#
# -- Write a query to select all information of employees whose last name is either ‘JONES’ or ‘BLAKE’ or ‘SCOTT’ or ‘KING’ or ‘FORD’.
# select * from employees where upper(last_name) in ('JONES','BLAKE','SCOTT','KING','FORD');