- Items And Customers


-- -- 1.Use SQL to get the following from the database:-- --

-- All items, ordered by price (lowest to highest).
select * from items order by price asc;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items where price >= 80 order by price desc;

-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
select first_name, last_name from customers order by last_name asc limit 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name from customers order by last_name desc;

----------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

-- --  3.Use SQL to get the following from the database: -- --

-- All purchases. Is this information useful to us? Not useful
select * from purchases;

-- All purchases, joining with the customers table.
select * from purchases inner join customers on purchases.customer_id = customers.customer_id;

-- Purchases of the customer with the ID equal to 5.
select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id=5;

-- Purchases for a large desk AND a small desk
select * from purchases inner join items on purchases.item_id = items.items_id where name='Small Desk' or name='Large Desk';

------------------------------------------------------------------------------------------
