-- Get a list of all the languages, from the language table.
 SELECT name
 FROM language;
SELECT *
FROM language;

-- Get a list of all films joined with their languages – select the following details :
-- film title, description, and language name.

SELECT f.title,
       f.description,
        l.name
 FROM film AS f
INNER JOIN language AS l
ON f.language_id = l.language_id;

-- Get all languages, even if there are no films in those languages –
-- select the following details : film title, description, and language name.

-- SELECT l.name,
--        f.title,
--        f.description
-- FROM language AS l
-- LEFT JOIN film AS f
-- ON f.language_id = l.language_id;


-- Create a new table called new_film with the following columns : id, name.
-- Add some new films to the table.
-- CREATE table new_film(
-- 	id  SERIAL PRIMARY KEY,
-- 	name varchar (50));

-- INSERT into new_film(name)
-- VALUES 
-- ('Home'),
-- ('Cat'),
-- ('Star WARS');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,
--     film_id INTEGER,
--     FOREIGN KEY(film_id) REFERENCES new_film(id) ON DELETE CASCADE ON UPDATE CASCADE,
--     language_id INTEGER,
--     FOREIGN KEY(language_id) REFERENCES language(language_id) ON DELETE CASCADE ON UPDATE CASCADE,
--     title VARCHAR,
--     score INTEGER CHECK (score >= 1 AND score <= 10),
--     review_text TEXT,
--     last_update DATE
-- );
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- INSERT into customer_review(film_id, language_id, title, score, review_text, last_update)
-- VALUES (1, 1, 'WOW!', 9, 'It was great!', '2024-06-26'),
-- (2, 1, 'Not for me', 4, 'It was boring', '2024-06-25');



-- Delete a film that has a review from the new_film table, what happens to the customer_review table?

-- DELETE FROM new_film
-- WHERE id = 1;
-- review also was deleted (on this film)


-- 2.
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.



-- UPDATE film
-- SET language_id = 2
-- WHERE film_id IN (1, 2);


-- SELECT film_id, title, language_id
-- FROM film
-- WHERE film_id IN (1, 2);


-- Which foreign keys (references) are defined for the customer table?
-- address_id in address

-- How does this affect the way in which we INSERT into the customer table?
-- address_id shoould already exist before inserting new customer


-- We created a new table called customer_review. Drop this table. 
-- DROP TABLE customer_review;
-- Is this an easy step, or does it need extra checking?

-- we should check all our keys, how dropping will affect another tables

-- Find out how many rentals are still outstanding 
-- (ie. have not been returned to the store yet).

-- SELECT count(rental_id)
-- FROM rental
-- where return_date IS NULL;

-- Find the 30 most expensive movies which are outstanding
-- (ie. have not been returned to the store yet)

-- SELECT f.title,
--        MAX(p.amount) AS amount
-- FROM film AS f
-- INNER JOIN inventory AS i
-- ON f.film_id = i.film_id
-- INNER JOIN rental AS r
-- ON i.inventory_id = r.inventory_id
-- INNER JOIN payment AS p
-- ON r.rental_id = p.rental_id
-- WHERE r.return_date IS NULL
-- GROUP BY f.title
-- ORDER BY amount DESC
-- LIMIT 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies,
-- but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT f.title
-- FROM film as f
-- INNER JOIN film_actor as fa
-- ON f.film_id = fa.film_id
-- INNER JOIN actor as a
-- ON fa.actor_id = a.actor_id
-- WHERE a.first_name ILIKE '%Penelope%'
-- 	and a.last_name ILIKE '%Monroe%'
-- 	and f.description ILIKE '%sumo%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT  f.title,
-- 		c.name,
-- 		f.length,
-- 		f.rating
-- FROM film as f
-- INNER JOIN film_category as fc
-- ON f.film_id = fc.film_id
-- INNER JOIN category as c
-- ON fc.category_id = c.category_id
-- WHERE c.name ILIKE '%documentary%' and f.length <60 and f.rating = 'R';


-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
-- and he returned it between the 28th of July and the 1st of August, 2005.

SELECT DISTINCT f.title
FROM film as f
INNER JOIN inventory as i
	ON f.film_id = i.film_id
INNER JOIN rental as r
	ON i.inventory_id = r.inventory_id
INNER JOIN customer as c
	ON r.customer_id = c.customer_id
INNER JOIN payment as p
	ON c.customer_id = p.customer_id
WHERE c.first_name ILIKE '%Matthew%' and c.last_name ILIKE '%Mahan%' 
	and p.amount > 4.00 and (r.return_date BETWEEN '2005-07-29' AND '2005-08-01');
		

-- The 4th film : His friend Matthew Mahan watched this film, as well.
-- It had the word “boat” in the title or description, 
-- and it looked like it was a very expensive DVD to replace.

SELECT DISTINCT f.title,
				f.replacement_cost
FROM film as f
INNER JOIN inventory as i
	ON f.film_id = i.film_id
INNER JOIN rental as r
	ON i.inventory_id = r.inventory_id
INNER JOIN customer as c
	ON r.customer_id = c.customer_id
INNER JOIN payment as p
	ON p.rental_id = r.rental_id
WHERE c.first_name ILIKE '%Matthew%' and c.last_name ILIKE '%Mahan%'
		and (f.title ILIKE '%boat%' or f.description ILIKE '%boat%') 
ORDER by f.replacement_cost DESC
	LIMIT 1;
