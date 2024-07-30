-- Calculate the average budget growth rate for each production company across all movies they have produced.
--Use window functions to determine the budget growth rate and then calculate the average growth rate.
WITH budget_growth AS (
SELECT m.movie_id,
		m.title,
		mc.company_id,
		m.budget,
		LAG(m.budget, 1) OVER (PARTITION BY mc.company_id ORDER BY m.release_date) AS previous_budget,    
	    (m.budget - LAG(m.budget, 1) OVER (PARTITION BY mc.company_id ORDER BY m.release_date)) as growth_rate
FROM movies.movie as m
JOIN movies.movie_company as mc
ON m.movie_id = mc.movie_id
WHERE m.budget > 0)

SELECT 
    bg.company_id,
	pc.company_name,
    ROUND(AVG(growth_rate)) AS average_growth_rate
FROM 
    budget_growth as bg
JOIN movies.production_company as pc
	ON bg.company_id = pc.company_id
WHERE 
    growth_rate IS NOT NULL  
GROUP BY 
    bg.company_id, pc.company_name
ORDER BY 
    average_growth_rate DESC;

--Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.
--Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
WITH avg_rating AS(
SELECT ROUND(AVG(vote_average), 2) as avg_vote
FROM movies.movie),

high_avg AS (
	SELECT movie_id
FROM movies.movie as m
JOIN avg_rating AS ar
ON m.vote_average > ar.avg_vote)
	
SELECT mc.person_id,
	 p.person_name,
		count(*) as num_films
FROM movies.movie_cast as mc
JOIN high_avg as ha
ON ha.movie_id = mc.movie_id
JOIN movies.person as p
ON p.person_id = mc.person_id
GROUP by mc.person_id, p.person_name
ORDER BY count(*) DESC
LIMIT 1;

--Calculate the rolling average revenue for movies within each genre,
--considering only the last three movies released in the genre.
--Use window functions with the ROWS frame specification to achieve this.

SELECT m.movie_id,
	m.title,
	mg.genre_id ,
	g.genre_name,
	m.revenue,
    ROUND(AVG(m.revenue) OVER (
        PARTITION BY mg.genre_id 
        ORDER BY m.release_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS rolling_avg_revenue
FROM movies.movie as m
JOIN movies.movie_genres as mg
ON m.movie_id = mg.movie_id
JOIN movies.genre as g
	ON mg.genre_id = g.genre_id
WHERE m.revenue != 0;

--Identify the movie series (based on shared keywords) with the highest total revenue.
--Use window functions and CTEs to group movies by their series and calculate the total revenue.


-- The same keywords have different films!!!
SELECT *
FROM movies.keyword
WHERE keyword_name LIKE '%series%';

SELECT m.movie_id,
		m.title
FROM movies.movie as m
JOIN movies.movie_keywords as mk
ON m.movie_id = mk.movie_id
JOIN movies.keyword as k
ON k.keyword_id = mk.keyword_id
WHERE keyword_name LIKE '%series%'
ORDER by


