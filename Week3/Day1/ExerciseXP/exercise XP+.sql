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

-- Fetch all of the students first_names and last_names.

select first_name, last_name
from students;


-- Fetch the student which id is equal to 2.
select first_name, last_name
from students
where id = 2;

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
select first_name, last_name
from students
where last_name = 'Benichou' and  first_name = 'Marc';

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
select first_name, last_name
from students
where last_name = 'Benichou' or  first_name = 'Marc';

-- Fetch the students whose first_names contain the letter a.
select first_name, last_name
from students
where first_name  LIKE '%a%';

-- Fetch the students whose first_names start with the letter a.
select first_name, last_name
from students
where first_name  LIKE 'A%';

-- Fetch the students whose first_names end with the letter a.
select first_name, last_name
from students
where first_name  LIKE '%a';

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select first_name, last_name
from students
where first_name  SIMILAR TO '%a_';

-- Fetch the students whose id’s are equal to 1 AND 3 .
select first_name, last_name
from students
where id = 1 or id = 3;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select *
from students
where birth_date >= '2000-01-01' ;