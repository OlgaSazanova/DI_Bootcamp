-- Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. 
--Create a temporary table to store these competitors and their medal counts for each season,
--and then display the contents of this table.

with SummerMedals as(
select gc.person_id,count(*) as summer_medals
from olympics.games_competitor gc
join olympics.competitor_event ce on gc.person_id = ce.competitor_id  
join olympics.games g on gc.games_id = g.id
where ce.medal_id<=3 and g.season='Summer'
group by gc.person_id
	
),

WinterMedals as(
select gc.person_id,count(*) as winter_medals
from olympics.games_competitor gc
join olympics.competitor_event ce on gc.person_id = ce.competitor_id  
join olympics.games g on gc.games_id = g.id
where ce.medal_id<=3 and g.season='Winter'
group by gc.person_id
	
)

select p.id as person_id, p.full_name, wm.winter_medals,sm.summer_medals
from SummerMedals sm
join WinterMedals wm on sm.person_id =wm.person_id
join olympics.person p on p.id =sm.person_id
where sm.summer_medals>0 and wm.winter_medals>0

--2. Create a temporary table to store competitors who have won medals in exactly two different sports,
--and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports.
	--Display the contents of this table.
WITH two_sports AS (
SELECT ce.competitor_id,
	  count(DISTINCT e.sport_id)
FROM olympics.competitor_event as ce
JOIN olympics.event as e
ON  ce.event_id = e.id
WHERE ce.medal_id != 4
GROUP by ce.competitor_id
HAVING count(DISTINCT e.sport_id) = 2)
	
SELECT two_sports.competitor_id,
	 count(medal_id)
FROM two_sports
JOIN olympics.competitor_event as ce
	ON two_sports.competitor_id = ce.competitor_id
WHERE ce.medal_id != 4
GROUP by two_sports.competitor_id
ORDER by count(medal_id) DESC
LIMIT 3;


-- ex2 task 1  Retrieve the regions that have competitors who have won the highest number of medals
--in a single Olympic event. 
--Use a subquery to determine the event with the highest number of medals for each competitor,
--and then display the top 5 regions with the highest total medals.
-- doesn't work correctly
WITH max_medal AS (
	SELECT competitor_id,
        MAX(medal_count) AS max_medal_count
FROM
   	(SELECT 
		ce.competitor_id,
		e.id  as event_id,
	   count(ce.medal_id) as medal_count
	FROM olympics.event as e
	JOIN olympics.competitor_event as ce
	ON e.id = ce.event_id
	WHERE ce.medal_id !=4
	GROUP by ce.competitor_id, e.id)

GROUP by competitor_id
ORDER by MAX(medal_count) DESC )
	

	
SELECT mm.competitor_id,
	   pr.region_id,
		nr.region_name,
		mm.max_medal_count
FROM max_medal as mm
JOIN olympics.games_competitor as gc
	ON mm.competitor_id = gc.id
JOIN olympics.person as p
	ON p.id = gc.person_id
JOIN olympics.person_region as pr
	ON p.id = pr.person_id
JOIN olympics.noc_region as nr
	ON pr.region_id = nr.id
WHERE mm.max_medal_count > 2;


--Create a temporary table to store competitors who have participated in more than three Olympic Games 
--but have not won any medals. Retrieve and display the contents of this table,
--including their full names and the number of games they participated in.


WITH no_medals AS (
	SELECT p.id,
	    count(medal_id) as no_medal
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
JOIN olympics.person as p
	ON p.id = gc.person_id
WHERE medal_id = 4
GROUP by p.id),

all_medals_id AS (
	SELECT  p.id,
	    count(ce.medal_id) as all_medals
FROM olympics.competitor_event as ce
JOIN olympics.games_competitor as gc
	ON gc.id = ce.competitor_id
JOIN olympics.person as p
	ON p.id = gc.person_id
GROUP by  p.id)
,	
	
no_medals_id AS (	
	SELECT nm.id
	FROM  no_medals  as nm
	JOIN  all_medals_id as am
	ON nm.id = am.id
	WHERE nm.no_medal = am.all_medals ) 
	
SELECT 
		 p.id,
		p.full_name,
		count(DISTINCT gc.games_id)
FROM no_medals_id 
LEFT JOIN olympics.games_competitor as gc
	ON no_medals_id.id = gc.person_id
JOIN  olympics.person as p
	ON p.id = gc.person_id
GROUP by p.id, p.full_name
HAVING count(DISTINCT gc.games_id) > 3	
ORDER BY count(DISTINCT gc.games_id) DESC ;


