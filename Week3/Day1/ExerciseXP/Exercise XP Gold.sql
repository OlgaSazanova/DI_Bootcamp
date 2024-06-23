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