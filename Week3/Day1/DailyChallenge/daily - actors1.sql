CREATE TABLE actors(
  actor_id SERIAL PRIMARY KEY,
  first_name VARCHAR (50) NOT NULL,
  last_name VARCHAR (100) NOT NULL,
  age DATE NOT NULL,
  number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Matt','Damon','08/10/1970', 5),
('George','Clooney','06/05/1961', 2),
('Brad', 'Pitt', '1980-04-22', 1),
('Matt', 'Damon', '1982-11-22', 2),
('Patrick', 'Jolie', '1980-04-22', 1),
('Marc', 'Benichou', '1998-11-02',0), 
('Yoan', 'Cohen', '2010-12-03',0), 
('Lea',	'Benichou', '1987-07-27',0), 
('Amelia', 'Dux', '1996-04-07',0), 
('David', 'Grez', '2003-06-14',0), 
('Omer', 'Simpson', '1980-10-03',1); 

select *
from actors;
-- 1. Count how many actors are in the table.

select Count (*) as actors_num
from actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

 INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Nicole', 'Kidman', '', 0);
-- psql:commands.sql:33: ERROR:  invalid input syntax for type date: ""
-- LINE 2: VALUES ('Nicole', 'Kidman', '', 0);