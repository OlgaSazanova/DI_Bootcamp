--1. Find the average age of competitors who have won at least one medal, grouped by the type of medal they won.
--Use a correlated subquery to achieve this.


WITH comp_medals AS (
    SELECT 
        ce.competitor_id,
        ce.medal_id,
        m.medal_name
    FROM olympics.competitor_event AS ce
    JOIN olympics.medal AS m
        ON ce.medal_id = m.id
    WHERE ce.medal_id != 4
)
SELECT 
    cm.medal_name,
    AVG(gc.age) 
FROM comp_medals AS cm
JOIN olympics.games_competitor AS gc
    ON gc.id = cm.competitor_id
GROUP BY cm.medal_name;


-- Identify the top 5 regions with the highest number of unique competitors who have participated
--in more than 3 different events.
--Use nested subqueries to filter and aggregate the data.




SELECT nr.region_name,
	COUNT(comp_id)	
FROM	
(SELECT DISTINCT  comp_id
FROM (SELECT  p.id as comp_id,
		count(ce.event_id) as num_events
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
ON ce.competitor_id = gc.id
JOIN olympics.person as p
	ON gc.person_id = p.id
GROUP by p.id)
WHERE num_events >3) as a

JOIN olympics.person_region as pr
	ON comp_id = pr.person_id
JOIN olympics.noc_region as nr
	ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY count DESC
LIMIT 5
;
-- 3. Create a temporary table to store the total number of medals won by each competitor
--and filter to show only those who have won more than 2 medals.
--Use subqueries to aggregate the data.



CREATE TEMPORARY TABLE TempTable (
    person_id INT,
    medal_count INT
);


INSERT INTO TempTable
SELECT person_id,
       COUNT(medal_id) AS medal_count
FROM olympics.games_competitor as gc
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
	
WHERE medal_id != 4
GROUP BY person_id;


SELECT *
FROM TempTable
WHERE medal_count > 2;

-- Use a subquery within a DELETE statement to remove records of competitors who have not won any medals 
-- from a temporary table created for analysis.

CREATE TEMPORARY TABLE TempTable2 (
    person_id INT,
    medal_id INT
);


INSERT INTO TempTable2
SELECT person_id,
       medal_id
FROM olympics.games_competitor as gc
JOIN olympics.competitor_event as ce
	ON gc.id = ce.competitor_id
;

DELETE FROM TempTable2
WHERE medal_id = 4;



--Exercise 2: 
-- 1. Update the heights of competitors based on the average height of competitors from the same region.
--Use a correlated subquery within the UPDATE statement.

WITH all_heights AS (SELECT  gc.id,
		gc.person_id,
		p.height,
		pr.region_id
FROM olympics.games_competitor AS gc
JOIN olympics.person as p
ON gc.person_id = p.id
JOIN olympics.person_region as pr
ON p.id = pr.person_id),

avg_heights AS (	SELECT region_id,
						round(AVG(height)) as avg_height
   					 FROM all_heights
   			 		WHERE height != 0
    				GROUP by region_id)
	
	--  doesn't work UPDATE, I tried:

	
UPDATE olympics.person
SET height = 
    (SELECT avg_height
    FROM avg_heights
    WHERE avg_heights.region_id = (
        SELECT all_heights.region_id
        FROM all_heights as al
        WHERE pr.person_id = olympics.person.id
    )
)
WHERE olympics.person.height = 0;




UPDATE olympics.person p
SET height = (
    SELECT AVG(p2.height)
    FROM olympics.person p2
    JOIN olympics.person_region pr ON p2.id = pr.person_id
    WHERE pr.region_id = (SELECT pr2.region_id FROM olympics.person_region pr2 WHERE pr2.person_id = p.id)
)
WHERE p.height = 0;


WITH avg_heights AS (
    SELECT pr.region_id,
           ROUND(AVG(p.height)) AS avg_height
    FROM olympics.games_competitor gc
    JOIN olympics.person p ON gc.person_id = p.id
    JOIN olympics.person_region pr ON p.id = pr.person_id
    WHERE p.height != 0
    GROUP BY pr.region_id
)
UPDATE olympics.person p
SET height = (
    SELECT ROUND(AVG(ah.avg_height))
    FROM avg_heights ah
    JOIN olympics.person_region pr ON p.id = pr.person_id
    WHERE pr.region_id = ah.region_id
)
WHERE p.height = 0;

--Insert new records into a temporary table for competitors who participated in more than one event
--in the same games and list their total number of events participated. 
--Use nested subqueries for filtering.

CREATE TEMPORARY TABLE TempTable4 (
    competitor_id INT,
	games_id INT,
    event_count INT
);


INSERT INTO TempTable4
SELECT *
	FROM
	(SELECT ce.competitor_id,
	   gc.games_id,
       COUNT(ce.event_id) AS event_count
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
GROUP BY ce.competitor_id, games_id)
WHERE event_count > 1
;

SELECT *
FROM TempTable4
Limit 4;


-- 3. Identify regions where the average number of medals won per competitor is greater than the overall average.
--Use subqueries to calculate and compare averages.

WITH overall AS
(SELECT (count(ce.medal_id) / count(DISTINCT gc.person_id)) as overall_avg
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
WHERE medal_id !=4),

regional_avg AS 
( SELECT pr.region_id,
	   nr.region_name,
	(count(ce.medal_id) / count(DISTINCT gc.person_id)) as region_avg
FROM olympics.person_region as pr
JOIN olympics.noc_region as nr
ON nr.id = pr.region_id
JOIN olympics.person as p
ON p.id = pr.person_id
JOIN olympics.games_competitor as gc
ON gc.person_id = p.id
JOIN olympics.competitor_event as ce
ON gc.id = ce.competitor_id

GROUP BY pr.region_id, nr.region_name)
	
SELECT region_id, region_name, region_avg
FROM regional_avg
WHERE region_avg > (SELECT overall_avg FROM overall);


--4 Create a temporary table to track competitors’ participation across different seasons
-- and identify those who have participated in both Summer and Winter games.



CREATE TEMPORARY TABLE TempTable5 (
    id INT,
    count_seasons INT
);


INSERT INTO TempTable5
SELECT p.id,
       count(DISTINCT g.season) as count_seasons
FROM olympics.games_competitor as gc
JOIN olympics.games as g
	ON gc.games_id =g.id
JOIN olympics.person as p
	ON p.id = gc.person_id
GROUP BY p.id
HAVING count(DISTINCT g.season) > 1 ;



SELECT *
FROM TempTable5
LIMIT 5;




