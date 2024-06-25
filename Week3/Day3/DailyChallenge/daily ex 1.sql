-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean),
-- 	customer_id (a reference to the Customer table)

CREATE table customer(
	customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (100) NOT NULL
);

CREATE table customer_profile(
	profile_id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT false, 
	customer_id int references customer(customer_id) unique not null
    
);

INSERT INTO customer (first_name, last_name)
	VALUES
        ('John', 'Doe'),
		('Jerome', 'Lalu'),
		('Lea', 'Rive');

INSERT INTO customer_profile (isloggedIn, customer_id)
	VALUES
        (true,
	(SELECT customer_id 
	 FROM customer
	 WHERE first_name = 'John')),
	(false,
	(SELECT customer_id
	FROM customer
	WHERE first_name = 'Jerome'));
	    
		

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers

SELECT cus.first_name
FROM customer as cus
INNER JOIN customer_profile as c_p
ON cus.customer_id = c_p.customer_id
WHERE c_p.isLoggedIn = true;

-- All the customers first_name and isLoggedIn columns -
-- even the customers those who don’t have a profile.
SELECT cus.first_name, 
  	 	c_p.isLoggedIn
FROM customer as cus
LEFT JOIN customer_profile as c_p
ON cus.customer_id = c_p.customer_id;

-- The number of customers that are not LoggedIn

SELECT count(sub_cust_profile.customer_id)
FROM
(SELECT cus.customer_id,
      cus.first_name, 
  	 	c_p.isLoggedIn
FROM customer as cus
LEFT JOIN customer_profile as c_p
ON cus.customer_id = c_p.customer_id) as sub_cust_profile
WHERE isLoggedIn = false OR isLoggedIn is Null;
