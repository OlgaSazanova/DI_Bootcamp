-- Task 1: Identify competitors who have won medals in both individual and team events.
--Use subqueries to distinguish between individual and team events and correlate with medal records.

SELECT ce1.competitor_id
FROM olympics.competitor_event ce1
JOIN olympics.event e1 ON ce1.event_id = e1.id
WHERE e1.event_name LIKE '%Individual%'
AND ce1.medal_id IS NOT NULL
SELECT *
	FROM olympics.event
LIMIT 10
;
SELECT *
	FROM olympics.event
WHERE event_name LIKE '%Individual%'
;
SELECT *
	FROM olympics.event
WHERE event_name LIKE '%team%'
;
-- Create a temporary table to store the cumulative medal count for each region, 
--then find the top 3 regions with the highest cumulative medal count.
--Use nested subqueries and aggregation.

SELECT nr.id,
		nr.region_name,
	count(ce.medal_id) as medal_count
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
ON gc.id = ce.competitor_id
JOIN olympics.person as p
ON p.id = gc.person_id
JOIN olympics.person_region as pr
ON p.id = pr.person_id
JOIN olympics.noc_region as nr
ON nr.id = pr.region_id
WHERE medal_id !=4
GROUP by nr.id,
		nr.region_name
ORDER by count(ce.medal_id) DESC;

--Task 3: Insert records into a temporary table for competitors who have won at least one gold medal 
--and participated in more than 2 different games.
--Use subqueries to aggregate the data.

SELECT p.id,
		p.full_name,
		count(ce.medal_id) as count_medal,
		count(DISTINCT games_id) as count_games
FROM  olympics.person as p
JOIN olympics.games_competitor as gc
	ON p.id = gc.person_id
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
WHERE ce.medal_id = 1
GROUP by p.id,
		p.full_name
HAVING count(DISTINCT games_id) >2;


 --Update the weights of competitors who have won medals in multiple games,
--setting it to the average weight of all medal winners. Use subqueries within the UPDATE statement.


WITH avg_medal_winner_weight AS(
 SELECT round(avg(p.weight)) avg_weight
FROM olympics.person as p
JOIN olympics.games_competitor as gc
	ON p.id = gc.person_id
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
WHERE ce.medal_id !=4	
),
	competitors_with_multiple_medals AS (
	SELECT p.id as person_id,
	count(DISTINCT gc.games_id)
FROM olympics.person as p
JOIN olympics.games_competitor as gc
	ON p.id = gc.person_id
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
WHERE ce.medal_id !=4
GROUP by p.id
HAVING count(DISTINCT gc.games_id) >1)

UPDATE olympics.person p
	
SET weight = (SELECT avg_weight FROM avg_medal_winner_weight)
WHERE id in (SELECT  person_id FROM competitors_with_multiple_medals );


 
-- Create a temporary table to store the number of events participated by each competitor,
--then identify those who have participated in events across different seasons.
--Use complex subqueries for filtering.

SELECT p1.id,
	p1.full_name,
	count(ce.event_id)
FROM (SELECT p.id,
	p.full_name,
	count(DISTINCT g.season)
FROM olympics.person as p
JOIN olympics.games_competitor as gc
	ON p.id = gc.person_id
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
join olympics.games g 
	ON gc.games_id = g.id
GROUP by p.id,
	p.full_name
HAVING count(DISTINCT g.season) >1)  as p1
JOIN olympics.games_competitor as gc
	ON p1.id = gc.person_id
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
GROUP BY p1.id,
		p1.full_name;


--Find the average height of competitors from each region who have won at least one medal,
--and compare it to the average height of all competitors. 
--	Use nested subqueries and temporary tables for calculations.

SELECT nr.id,
	nr.region_name,
	round(avg(p.height))
FROM olympics.noc_region as nr
JOIN olympics.person_region as pr
ON nr.id = pr.region_id
JOIN olympics.person as p
ON p.id = pr.person_id
GROUP by nr.id,
	nr.region_name;

SELECT round(avg(p.height))
FROM olympics.person as p;
