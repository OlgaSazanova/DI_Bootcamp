--Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
SELECT *
FROM rental
WHERE return_date is NULL
;

-- Get a list of all customers who have not returned their rentals. Make sure to group your results.

SELECT DISTINCT c.customer_id,
		c.first_name,
  		c.last_name
FROM customer as c
JOIN rental as r
ON c.customer_id = r.customer_id
WHERE return_date is NULL;

-- Get a list of all the Action films with Joe Swank.

SELECT f.title

FROM film as f
INNER JOIN film_actor as fa
ON f.film_id = fa.film_id
INNER JOIN actor as a
ON fa.actor_id = a.actor_id
INNER JOIN film_category as fc
ON f.film_id = fc.film_id
INNER JOIN category as c
ON fc.category_id = c.category_id
WHERE c.name ILIKE '%action%' 
 	and a.first_name ILIKE '%Joe%'
     and a.last_name ILIKE '%Swank%';

-- How many stores there are, and in which city and country they are located.
SELECT co.country,
		c.city,
		count(s.store_id)
FROM store as s
JOIN address as a
ON s.address_id = a.address_id
JOIN city as c
ON a.city_id = c.city_id
JOIN country as co
ON c.country_id = co.country_id
GROUP BY co.country_id, c.city;



-- How many hours of viewing time there are in total in each store – in other words,
--the sum of the length of every inventory item in each store.
--Make sure to exclude any inventory items which are not yet returned.
SELECT s.store_id,
       sum(f.length),
	ROUND(SUM(f.length) / 60.0, 2) AS total_general_viewing_time_hours,
    ROUND(SUM(f.length) / 1440.0, 2) AS total_general_viewing_time_days
FROM store as s
JOIN inventory as i
ON i.store_id = s.store_id
JOIN film as f
ON f.film_id = i.film_id
JOIN rental as r
ON r.inventory_id = i.inventory_id
WHERE r.return_date IS not NULL
GROUP by s.store_id;



--A list of all customers in the cities where the stores are located.

SELECT c.customer_id,
		c.first_name,
		c.last_name,
		c.store_id
FROM customer as c
JOIN store as s
ON c.store_id= s.store_id;

--A list of all customers in the countries where the stores are located.

SELECT c.customer_id,
		c.first_name,
		c.last_name,
		c.store_id
FROM customer as c
JOIN store as s
ON c.store_id= s.store_id;


-- Create a ‘safe list’ of all movies. Get the sum of their viewing time (length).

--For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).

SELECT  SUM(f.length) AS total_safe_viewing_time_minutes,
    ROUND(SUM(f.length) / 60.0, 2) AS total_safe_viewing_time_hours,
    ROUND(SUM(f.length) / 1440.0, 2) AS total_safe_viewing_time_days
FROM film as f
JOIN film_category as fc
	ON fc.film_id = f.film_id
JOIN category as c
	ON c.category_id = fc.category_id
WHERE c.name != 'Horror'
  AND f.title NOT ILIKE '%beast%'
  AND f.title NOT ILIKE '%monster%'
  AND f.title NOT ILIKE '%ghost%'
  AND f.title NOT ILIKE '%dead%'
  AND f.title NOT ILIKE '%zombie%'
  AND f.title NOT ILIKE '%undead%'
  AND f.description NOT ILIKE '%beast%'
  AND f.description NOT ILIKE '%monster%'
  AND f.description NOT ILIKE '%ghost%'
  AND f.description NOT ILIKE '%dead%'
  AND f.description NOT ILIKE '%zombie%'
  AND f.description NOT ILIKE '%undead%';


--Retrieve all films with a rating of G or PG, which are are not currently rented 

SELECT f.title,
		f.rating
FROM film as f
JOIN inventory as i
ON f.film_id = i.film_id
LEFT JOIN rental as r
ON r.inventory_id = i.inventory_id
WHERE (f.rating = 'G' OR f.rating = 'PG')
     AND r.return_date IS NOT NULL OR  r.rental_date IS NULL;



CREATE TABLE waiting_list (
    waiting_list_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    film_id INT NOT NULL,
    waiting_since DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (film_id) REFERENCES film(film_id)
);

-- Adding test data
INSERT INTO waiting_list (customer_id, film_id) VALUES (1, 101);
INSERT INTO waiting_list (customer_id, film_id) VALUES (2, 101);
INSERT INTO waiting_list (customer_id, film_id) VALUES (3, 102);
INSERT INTO waiting_list (customer_id, film_id) VALUES (4, 103);
INSERT INTO waiting_list (customer_id, film_id) VALUES (1, 103);

-- Query to retrieve the number of people waiting for each children’s DVD
SELECT f.title, COUNT(wl.customer_id) AS waiting_count
FROM waiting_list AS wl
JOIN film AS f
  ON wl.film_id = f.film_id
JOIN film_category AS fc
  ON f.film_id = fc.film_id
JOIN category AS c
  ON fc.category_id = c.category_id
WHERE f.film_id =101
GROUP BY f.title;
