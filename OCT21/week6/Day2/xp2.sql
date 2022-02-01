

-- -- 1
-- select * from customer;

-- -- 2.
-- select concat(first_name,' ',last_name) as full_name from customer;

-- -- 
-- select distinct create_date from customer;

-- --4.
-- select * from customer order by first_name desc;

-- -- 5 
-- select film_id, title, description, release_year, rental_rate from film order by rental_rate asc;

-- -- 6
-- select address, phone from address where district = 'Texas';

-- --7.
-- select * from film where film_id = 15 or film_id = 150;


-- --9 
-- select film_id, title, description, length, rental_rate from film where title like 'Ti%';

-- --10
-- select * from film order by rental_rate asc limit 10;

-- --11
-- select * from film order by rental_rate asc limit 10 offset 10;

-- -- 
-- -- 
-- select * from film order by rental_rate offset 10 fetch first 10 row only;

-- --12. 
-- select payment.customer_id,amount, payment_date from payment inner join customer on payment.customer_id = customer.customer_id order by payment.customer_id;

-- -- 13
-- select * from film where film_id not in (select film_id from inventory);

-- --14.
-- select city.city , country.country from city inner join country on country.country_id = city.country_id;
