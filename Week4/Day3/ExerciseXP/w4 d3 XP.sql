--Use the RANK() function to rank movies by their popularity within each genre.
--Display the genre name, movie title, and their rank based on popularity.

SELECT g.genre_name,
		m.title,
		RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
FROM movies.movie as m
JOIN movies.movie_genres as mg
ON m.movie_id = mg.movie_id
JOIN movies.genre as g
ON g.genre_id = mg.genre_id;

--Use the NTILE() function to divide the movies produced by each production company into quartiles 
--based on revenue. 
--Display the company name, movie title, revenue, and quartile.

SELECT pc.company_name,
		m.title,
		m.revenue,
		 NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile
FROM movies.production_company as pc
JOIN movies.movie_company as mc
ON pc.company_id = mc.company_id
JOIN movies.movie  as m
ON m.movie_id = mc.movie_id
WHERE m.revenue !=0;

--Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets 
--within each genre.
--Display the genre name, movie title, budget, and running total budget.

SELECT g.genre_name,
		m.title,
		m.budget,
		SUM(m.budget) OVER (PARTITION BY g.genre_name  ORDER BY m.release_date ) AS running_total
FROM movies.movie as m
JOIN movies.movie_genres as mg
ON m.movie_id = mg.movie_id
JOIN movies.genre as g
ON g.genre_id = mg.genre_id
WHERE m.budget >1000;

--Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date.
--Display the genre name, movie title, and release date.

WITH recent_movies AS (
    SELECT 
        g.genre_name,
        m.title,
        m.release_date,
        FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_release_date
    FROM 
        movies.movie AS m
    JOIN 
        movies.movie_genres AS mg ON m.movie_id = mg.movie_id
    JOIN 
        movies.genre AS g ON g.genre_id = mg.genre_id
)

SELECT 
    genre_name,
    title,
    release_date
FROM 
    recent_movies
WHERE 
    release_date = most_recent_release_date
ORDER BY 
    genre_name, release_date DESC;


--Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in.
--Display the actor’s name and their rank.
WITH counts AS(
SELECT p.person_name,
		count(mc.movie_id) as movie_count
FROM movies.movie_cast as mc
JOIN movies.person as p
ON p.person_id = mc.person_id
GROUP BY p.person_name)
	
	SELECT person_name,
		DENSE_RANK() OVER (ORDER BY movie_count DESC) AS dense_rank
	FROM counts;

--Use a CTE and the RANK() function to find the director with the highest average movie rating.
--Display the director’s name and their average rating.

WITH ratings AS(
SELECT p.person_name,
	 	m.movie_id,
		m.vote_average,
	ROUND(AVG(m.vote_average) OVER (PARTITION BY p.person_name), 2) AS avg_rating
FROM movies.movie_crew as mc
JOIN movies.person as p
ON p.person_id = mc.person_id
JOIN movies.movie as m
ON m.movie_id = mc.movie_id
WHERE mc.job = 'Director'),
	
ranked_directors AS (
    SELECT 
        person_name,
        avg_rating,
        RANK() OVER (ORDER BY avg_rating DESC) AS rating_rank
    FROM 
        ratings
)

-- Step 3: Select the director(s) with the highest average rating
SELECT 
    person_name,
    avg_rating
FROM 
    ranked_directors
WHERE 
    rating_rank = 1;
	;

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. 
--Display the actor’s name and the cumulative revenue.
WITH actor_revenues AS
(SELECT  p.person_name,
		m.title,
		m.revenue,
		SUM(m.revenue) OVER (PARTITION BY p.person_name  ORDER BY m.release_date ) AS cumulative_revenue
FROM movies.movie_cast as mc
JOIN movies.person as p
ON p.person_id = mc.person_id
JOIN movies.movie as m
ON m.movie_id = mc.movie_id
WHERE m.revenue !=0)
	
	SELECT DISTINCT
    person_name,
    LAST_VALUE(cumulative_revenue) OVER (PARTITION BY person_name ORDER BY m.release_date
                                         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS cumulative_revenue
FROM
    actor_revenues AS ar
JOIN
    movies.movie AS m ON ar.title = m.title;

--Use a CTE and a window function to find the director whose movies have the highest total budget.
--Display the director’s name and the total budget.

WITH director_budgets AS(
SELECT p.person_name,
	 	m.movie_id,
		m.budget,
	SUM(m.budget) OVER (PARTITION BY p.person_name  ORDER BY m.release_date ) AS total_budget
FROM movies.movie_crew as mc
JOIN movies.person as p
ON p.person_id = mc.person_id
JOIN movies.movie as m
ON m.movie_id = mc.movie_id
WHERE mc.job = 'Director' AND m.budget !=0)
	
	SELECT person_name,
		total_budget
	FROM director_budgets
	ORDER BY total_budget DESC
	LIMIT 1;