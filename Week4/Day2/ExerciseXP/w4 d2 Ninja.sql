--Identify competitors who have won medals in both individual and team events, 
--and calculate the total number of medals they have won in each category.
--Create a temporary table to store the results and ensure it includes their full name,
--total medals in individual events, and total medals in team events.
SELECT *
from olympics.event
LIMIT 20;
SELECT *
FROM olympics.sport
LIMIT 20;

--Create a temporary table to store the competitors who have won medals in exactly 3 different sports.
--Then, using this temporary table, identify the top 3 competitors with the highest total number of medals
--across all sports. 
--Use nested subqueries and aggregation

WITH three_sports AS (
SELECT 
	 p.full_name,
 	 
	  count(DISTINCT e.sport_id)
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
JOIN olympics.event as e
ON  ce.event_id = e.id
JOIN olympics.person as p
	ON p.id = gc.person_id
WHERE ce.medal_id != 4
GROUP by p.full_name
HAVING count(DISTINCT e.sport_id) = 3)

SELECT p.full_name,
 	 gc.person_id,
	count(ce.medal_id)
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
JOIN olympics.event as e
ON  ce.event_id = e.id
JOIN olympics.person as p
	ON p.id = gc.person_id
WHERE ce.medal_id != 4
GROUP by p.full_name, gc.person_id
ORDER by count(ce.medal_id) DESC
LIMIT 3;

--Find the regions that have competitors who have won medals in both the Summer and Winter games, 
--and calculate the average age of these competitors. 


with SummerMedals as(
select gc.person_id,
		ROUND(AVG(gc.age)) as avg_age,
	count(*) as summer_medals
from olympics.games_competitor gc
join olympics.competitor_event ce on gc.id = ce.competitor_id  
join olympics.games g on gc.games_id = g.id
where ce.medal_id<=3 and g.season='Summer'
group by gc.person_id
	
),

WinterMedals as(
select gc.person_id,
	ROUND(AVG(gc.age)) as avg_age,
	count(*) as winter_medals
from olympics.games_competitor gc
join olympics.competitor_event ce on gc.id = ce.competitor_id  
join olympics.games g on gc.games_id = g.id
where ce.medal_id<=3 and g.season='Winter'
group by gc.person_id
	
)

select p.id as person_id,
	p.full_name,
	ROUND((wm.avg_age +sm.avg_age)/2)  as absolute_avg_age,
	nr.region_name,
	wm.winter_medals,
	sm.summer_medals
from SummerMedals sm
join WinterMedals wm on sm.person_id =wm.person_id
join olympics.person p on p.id =sm.person_id
JOIN olympics.person_region as pr
	ON p.id = pr.person_id
JOIN olympics.noc_region as nr
	ON nr.id = pr.region_id
where sm.summer_medals>0 and wm.winter_medals>0;
