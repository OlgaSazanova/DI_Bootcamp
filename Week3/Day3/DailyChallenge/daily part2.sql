CREATE table book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	author VARCHAR(50) NOT NULL);

INSERT INTO book(title, author)
	VALUES 
	('Alice In Wonderland', 'Lewis Carroll'),
	('Harry Potter', 'J.K Rowling'),
	('To kill a mockingbird', 'Harper Lee');

CREATE table student ( 
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE, 
	age integer CHECK (age <= 15));

INSERT into student(name, age)
	VALUES
	('John', 12 ),
	('Lera', 11 ),
	('Patrick', 10 ),
	('Bob', 14 );

CREATE table library(
	book_fk_id INTEGER,
    student_fk_id INTEGER,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id , student_fk_id) , 
    FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO library(book_fk_id, student_fk_id, borrowed_date)
	VALUES
	((SELECT book_id from book where title = 'Alice In Wonderland'),
	(SELECT student_id from student where name = 'John'), '2022-02-15'),
	 ((SELECT book_id from book where title = 'To kill a mockingbird'),
	(SELECT student_id from student where name = 'Bob'), '2021-03-03'),
	((SELECT book_id from book where title = 'Alice In Wonderland'),
	(SELECT student_id from student where name = 'Lera'), '2021-05-23'),
	((SELECT book_id from book where title = 'Harry Potter'),
	(SELECT student_id from student where name = 'Bob'), '2021-08-12');

-- Select all the columns from the junction table
SELECT *
FROM library;

-- Select the name of the student and the title of the borrowed books

SELECT s.name, b.title
FROM student as s
JOIN library as l
ON s.student_id=l.student_fk_id
JOIN book as b
ON l.book_fk_id = b.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland

SELECT AVG(s.age) as average_age
FROM student as s
JOIN library as l
ON s.student_id=l.student_fk_id
JOIN book as b
ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';


-- Delete a student from the Student table, what happened in the junction table ?
DELETE 
	FROM student 
WHERE name = 'Bob';

SELECT *
FROM library;







 