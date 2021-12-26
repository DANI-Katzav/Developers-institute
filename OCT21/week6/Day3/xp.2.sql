
-- -- 1. 
-- update film
-- set language_id = 3
-- where film_id between 25 and 30;


-- -- . 
-- drop table if exists customer_review;

-- 4.
-- select count(*) from rental where return_date is NULL;

-- -- 5.
-- select film.title, film.rental_rate
-- from (film join inventory on film.film_id = inventory.film_id)
-- join rental on rental.inventory_id = inventory.inventory_id
-- where rental.return_date is NULL
-- order by rental_rate desc
-- limit 30;

-- -- The 1st film
-- select film.title
-- from (film join film_actor on film.film_id = film_actor.film_id)
-- join actor on actor.actor_id = film_actor.actor_id
-- where actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and description ilike '%wrestler%';

-- -- The 2nd film 
-- select film.title 
-- from (film join film_category on film.film_id = film_category.film_id)
-- join category on category.category_id = film_category.category_id
-- where category.name = 'Documentary' and length <60 and rating='R';


-- -- The 3rd film : 

-- select film.title
-- from (film join inventory on film.film_id = inventory.film_id join customer on customer.store_id = inventory.store_id)
-- join rental on rental.inventory_id = inventory.inventory_id
-- where customer.first_name= 'Matthew' and customer.last_name='Mahan' and rental_rate>4.00 and return_date between '2005-07-28' and '2005-08-01';



-- -- The 4th film : 
-- select film.title
-- from (film join inventory on film.film_id = inventory.film_id join customer on customer.store_id = inventory.store_id)
-- join rental on rental.inventory_id = inventory.inventory_id
-- where customer.first_name= 'Matthew' and customer.last_name='Mahan' and rental_rate>4.00 and description ilike '%boat%' or title ilike '%boat%';

