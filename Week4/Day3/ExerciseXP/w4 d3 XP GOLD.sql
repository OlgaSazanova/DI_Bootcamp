--Use the LEAD() and LAG() functions to identify movies where the budget increased 
--compared to the previous movie but decreased compared to the next movie, 
--in order of their release dates. 
--Display the movie title, release date, and budget, along with the previous and next budgets.

SELECT
		title,
		release_date,
		budget,
		LEAD(budget	, 1) OVER (ORDER BY release_date) AS next_budget,
		LAG	(budget	, 1) OVER (ORDER BY release_date) AS previous_budget
FROM movies.movie
WHERE budget >1000
ORDER BY release_date;

--Create a CTE to calculate the moving average rating of movies over a 5-year window for each genre.
--Display the genre, movie title, release year, and the moving average rating.

WITH rating_year AS(
SELECT
		g.genre_name,
        m.title,
       EXTRACT(YEAR FROM m.release_date) AS year,
		m.vote_average
       
FROM 
        movies.movie AS m
JOIN 
	    movies.movie_genres AS mg ON m.movie_id = mg.movie_id
JOIN 
        movies.genre AS g ON g.genre_id = mg.genre_id),

	avg_years AS(
	SELECT
		genre_name,
        title,
      	year,
		vote_average,
		AVG(vote_average) OVER (PARTITION BY genre_name, year ORDER BY year) as genre_year_avg
	FROM rating_year
	)

	SELECT	genre_name,
			title,
			year,
			AVG(genre_year_avg) OVER (PARTITION BY genre_name, year 
									ORDER BY year 
        							ROWS BETWEEN 4 PRECEDING AND CURRENT ROW ) AS avg_rating
	FROM avg_years
	ORDER by genre_name, year;

--Use the ROW_NUMBER(), RANK(), and DENSE_RANK() functions to create a comprehensive ranking system
--for movies based on revenue within each genre. 
--Display the genre, movie title, revenue, and their respective row number, rank, and dense rank.

SELECT g.genre_name,
        m.title,
		m.revenue,
		ROW_NUMBER() OVER (PARTITION BY g.genre_name  ORDER BY m.revenue DESC) AS row_num,
		RANK() OVER (PARTITION BY g.genre_name ORDER BY m.revenue DESC) AS rank,
		DENSE_RANK() OVER (PARTITION BY g.genre_name ORDER BY m.revenue DESC) AS dense_rank
       
FROM 
        movies.movie AS m
JOIN 
	    movies.movie_genres AS mg ON m.movie_id = mg.movie_id
JOIN 
        movies.genre AS g ON g.genre_id = mg.genre_id
WHERE m.revenue !=0;

--Use the FIRST_VALUE() and LAST_VALUE() functions to find the first and last movie each actor appeared in.
--Display the actor’s name, first movie title, first movie release date, 
--last movie title, and last movie release date.

SELECT DISTINCT p.person_name,
		FIRST_VALUE(m.title) OVER (PARTITION BY person_name ORDER BY m.release_date
                                         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
											AS first_movie_title,
		FIRST_VALUE(m.release_date) OVER (PARTITION BY person_name ORDER BY m.release_date
                                         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
											AS first_movie_release_date,
		LAST_VALUE(m.title) OVER (PARTITION BY person_name ORDER BY m.release_date
                                         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
											AS last_movie_title,
		LAST_VALUE(m.release_date) OVER (PARTITION BY person_name ORDER BY m.release_date
                                         RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
											AS last_movie_release_date
FROM movies.movie_cast as mc
JOIN movies.person as p
ON p.person_id = mc.person_id
JOIN movies.movie as m
ON m.movie_id = mc.movie_id;

-- Create a nested subquery to identify genres where the average movie revenue is above the overall average 
--movie revenue. Within those genres, use a window function to rank movies by their popularity.
--Display the genre, movie title, revenue, and rank.

WITH
genre_revenues AS (
	SELECT g.genre_name,
		ROUND(AVG(m.revenue)) as genre_rev
	FROM 
        movies.movie AS m
JOIN 
	    movies.movie_genres AS mg ON m.movie_id = mg.movie_id
JOIN 
        movies.genre AS g ON g.genre_id = mg.genre_id
WHERE m.revenue !=0
GROUP by g.genre_name
HAVING ROUND(AVG(m.revenue)) > (
	SELECT ROUND(AVG(revenue))
FROM movies.movie
WHERE revenue !=0) 
)
	
SELECT gr.genre_name,
		m.title,
		m.revenue,
		RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
FROM genre_revenues as gr
JOIN movies.genre as g
ON g.genre_name = gr.genre_name
JOIN movies.movie_genres as mg
ON mg.genre_id = g.genre_id
JOIN movies.movie as m
on mg.movie_id = m.movie_id;


--Use a combination of window functions and CTEs to find actors
--who have appeared in movies that have collectively grossed in the top 10% of all movie revenues.
--Display the actor’s name and the total revenue of the movies they have appeared in.


WITH cum_revenues AS(
SELECT movie_id,
		title,
		revenue,
		SUM(revenue) OVER (ORDER BY revenue DESC) cum_revenue
FROM movies.movie),

ten_perc AS (
	SELECT 
    movie_id,
    title,
    revenue,
    cum_revenue
FROM 
    cum_revenues
WHERE 
    cum_revenue <= (
        SELECT SUM(revenue) * 0.1
        FROM movies.movie
    )
ORDER BY 
    revenue DESC
	)

SELECT
	DISTINCT p.person_name,
	SUM(tc.revenue) OVER (PARTITION BY p.person_name) as total_revenue
FROM ten_perc as tc
JOIN movies.movie_cast as mc
	ON mc.movie_id = tc.movie_id
JOIN movies.person as p
	ON p.person_id = mc.person_id
ORDER BY total_revenue DESC

;

