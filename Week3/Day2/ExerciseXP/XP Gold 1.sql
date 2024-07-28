--Find out how many films there are for each rating.
SELECT rating,
	    count (film_id)
FROM film
GROUP by rating;


--Get a list of all the movies that have a rating of G or PG-13.

SELECT 
	title,
	rating
FROM film
WHERE rating = 'G' or rating = 'PG-13';

--Filter this list further: look for only movies that are under 2 hours long,
--and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

SELECT 
	title,
	rating,
	length
FROM film
WHERE (rating = 'G' or rating = 'PG-13') AND length < 120 AND rental_rate <3
ORDER BY  title;

--Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
SELECT *
FROM customer
LIMIT 3;

UPDATE customer
SET first_name = 'Olga',
    last_name = 'Sazanova',
    email = 'olga.sazanova.da@gmail.com'
WHERE customer_id = 1;

--Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).

SELECT *
from address as a
INNER JOIN customer as c
ON a.address_id = c.address_id
WHERE customer_id = 1;

UPDATE address
SET address = 'HaShitta 5',
	district = 'Tsafon',
	city_id = 45,
	postal_code = '24421'
WHERE address_id = 5;