--Identify the top 5 movies in each genre based on the revenue growth rate 
--compared to the previous movie released in the same genre.
--Use window functions to calculate the growth rate and rank the movies.
--Then, list the movies with their rank and revenue growth rate.
WITH previous_r AS(
SELECT g.genre_name,
		m.movie_id,
		m.title,
		m.revenue,
		LAG(m.revenue, 1) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS previous_revenue
		
FROM movies.movie as m
JOIN movies.movie_genres as mg
ON m.movie_id = mg.movie_id
JOIN movies.genre as g
ON g.genre_id = mg.genre_id
WHERE m.revenue != 0)
,

growth_rates AS (

SELECT genre_name,
		movie_id,
		title,
		revenue,
		previous_revenue,
		revenue - previous_revenue as growth_rate,
		RANK() OVER (PARTITION BY genre_name ORDER BY (revenue - previous_revenue)DESC ) AS rank
FROM previous_r
	WHERE previous_revenue IS NOT NULL)


SELECT genre_name,
       movie_id,
       title,
       revenue,
       previous_revenue,
       growth_rate,
       rank
FROM growth_rates
WHERE rank <= 5;

--Calculate the cumulative average rating for each movie in each genre,
--but only include movies that have at least 50 votes.
--Use the AVG() function with windowing and filter the results.

SELECT g.genre_name,
		m.movie_id,
		m.title,
	ROUND(AVG(vote_average) OVER (PARTITION BY g.genre_name ORDER BY m.release_date 
							ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW),2) as cum_avg_rating
FROM movies.movie as m
JOIN movies.movie_genres as mg
ON m.movie_id = mg.movie_id
JOIN movies.genre as g
ON g.genre_id = mg.genre_id
WHERE m.vote_count >= 50;

--  Determine the directors who have consistently produced movies in the top 10% of popularity within their genre.
--Use CTEs and window functions to calculate the required values and display the director’s name,
--the titles of their top movies, and their popularity ranks.

WITH cum_pop AS(
SELECT m.movie_id,
		m.title,
		mg.genre_id,
		m.popularity,
		SUM(m.popularity) OVER (PARTITION BY mg.genre_id	ORDER BY m.popularity DESC) cum_popularity
FROM movies.movie as m
JOIN movies.movie_genres as mg
	ON m.movie_id = mg.movie_id),

genre_pop_total AS (
    SELECT 
        mg.genre_id,
        SUM(m.popularity) AS genre_total_popularity
    FROM 
        movies.movie AS m
    JOIN 
        movies.movie_genres AS mg ON m.movie_id = mg.movie_id
    GROUP BY 
        mg.genre_id
),
	
ten_perc AS (
	   SELECT 
        cp.movie_id,
        cp.title,
        cp.genre_id,
        cp.popularity,
        cp.cum_popularity,
		RANK () OVER (PARTITION BY cp.genre_id ORDER BY cp.popularity DESC ) AS rank
    FROM 
        cum_pop AS cp
    JOIN 
        genre_pop_total AS gpt 
	ON cp.genre_id = gpt.genre_id
    WHERE 
        cp.cum_popularity <= gpt.genre_total_popularity * 0.1)

	SELECT 
	p.person_name,

    tc.title,
    tc.genre_id, 
	tc.rank
FROM 
    ten_perc as tc
JOIN movies.movie_crew as mc
	ON tc.movie_id = mc.movie_id
JOIN movies.person as p
ON p.person_id = mc.person_id

WHERE mc.job = 'Director'
ORDER BY tc.genre_id, tc.rank
;

	



