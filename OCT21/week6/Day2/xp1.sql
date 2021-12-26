-- Items And Customers


-- -- -- 1.

-- -- 
-- select * from items order by price asc;


-- select * from items where price >= 80 order by price desc;


-- select first_name, last_name from customers order by last_name asc limit 3;


-- select last_name from customers order by last_name desc;

-- -- -- 2. 

-- create table purchases (
-- item_id integer,
-- FOREIGN KEY(item_id) REFERENCES public.items (items_id),
-- customer_id integer,
-- FOREIGN KEY(customer_id) REFERENCES public.customers (customer_id)
-- );


-- Insert into purchases(customer_id) values 
-- ((SELECT customer_id from customers WHERE first_name='Greg'));


-- Insert into purchases(customer_id, item_id)values 
-- ((SELECT customer_id from customers WHERE first_name='Sandra'),(SELECT items_id from items WHERE price=300)),
-- ((SELECT customer_id from customers WHERE first_name='Scott'),(SELECT items_id from items WHERE price=80)),
-- ((SELECT customer_id from customers WHERE first_name='Trevor'),(SELECT items_id from items WHERE price=100)),
-- ((SELECT customer_id from customers WHERE first_name='Melanie'),(SELECT items_id from items WHERE price=300));


--------------------------------------------------------------------------------------

-- -- --  3.
-- select * from purchases;


-- select * from purchases inner join customers on purchases.customer_id = customers.customer_id;


-- select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id=4;
--  desk

-- select * from purchases inner join items on purchases.item_id = items.items_id where name='Small Desk' or name='Large Desk';



-- -- -- 4. 

-- Insert into customers(first_name, last_name) values ('Scott','Scott');
-- Insert into items(name,price) values('Hard Drive',200);
-- insert into purchases(customer_id , item_id) values
-- ((SELECT customer_id from customers WHERE first_name='Scott' and customer_id = 6),(SELECT items_id from items WHERE price=200));


-- select customers.first_name, customers.last_name, items.name from purchases join items on purchases.item_id = items.items_id join customers on purchases.customer_id = customers.customer_id;


