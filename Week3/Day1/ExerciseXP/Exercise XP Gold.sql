create table bootcamp(id serial primary key
       );
       
       
create table students(id serial primary key,
      first_name varchar,
      last_name varchar,
      birth_date date  );
      
      
insert into students(first_name, last_name, birth_date)
VALUES('Marc', 'Benichou', '1998-02-11'),
       ('Yoan', 'Cohen', '2010-03-12'),
       ('Lea', 'Benichou', '1987-07-07'),
       ('Amelia', 'Dux', '1996-04-07'),
       ('David', 'Grez', '2003-06-14'),
       ('Omer', 'Simpson', '1980-10-03'),
       ('Olga', 'Sazanova', '1988-03-30');
       
-- Fetch all of the data from the table.

select *
from students;

-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

-- Fetch the first four students. You have to order the four students alphabetically by last_name.

select first_name, last_name, birth_date
from students
order by last_name
limit 4;

-- Fetch the details of the youngest student.

select first_name, last_name, birth_date
from students
order by birth_date desc
limit 1;


-- Fetch three students skipping the first two students.
select first_name, last_name, birth_date
from students
where id >2
limit 3;


--‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates.
--Update both their birth_dates to 02/11/1998.


UPDATE students
SET birth_date = '1998-11-02'
WHERE last_name = 'Benichou';

--Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET last_name = 'Guez'
WHERE last_name = 'Grez';

--Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';

--	Count how many students are in the table.
SELECT count(*)
FROM students;

--Count how many students were born after 1/01/2000.
SELECT count(*)
FROM students
WHERE birth_date > '2000-01-01';


--Add a column to the student table called math_grade.

ALTER TABLE students
ADD COLUMN math_grade INTEGER;

-- Add 80 to the student which id is 1.
UPDATE students
SET math_grade = 80
WHERE id = 1;


--Add 90 to the students which have ids of 2 or 4.

UPDATE students
SET math_grade = 90
WHERE id = 2 OR id = 4;

--Add 40 to the student which id is 6.
UPDATE students
SET math_grade = 40
WHERE id = 6;

--Count how many students have a grade bigger than 83
SELECT count(*)
FROM students
WHERE math_grade >83;

-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table.
--Give him a grade of 70
insert into students(first_name, last_name, birth_date, math_grade )
VALUES('Omer', 'Simpson', '1980-10-03', 70);

DELETE FROM students
WHERE id = 9;

UPDATE  students
SET math_grade = 70
WHERE id = 8;

-- Count how many grades each student has.

SELECT first_name,
	   last_name,
	count(math_grade) as total_grade 
FROM students
GROUP by first_name, last_name;

SELECT sum(math_grade)
FROM students;