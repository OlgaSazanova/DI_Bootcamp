create table items(
    id serial primary key,
    item varchar,
    price integer);
    
insert into items(item, price)
    VALUES
    ('Small Desk', 100),
    ('Large desk', 300),
    ('Fan', 80)
    ;
    
 create table customers(
    id serial primary key,
    first_name varchar,
    last_name varchar);
    
    insert into customers(first_name, last_name)
    VALUES
    ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson')
    ;
    
--     All the items.

select * from items;
select * from customers;

-- All the items with a price above 80 (80 not included).
select * from items
where price > 80;

-- All the items with a price below 300. (300 included)

select * from items
where price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
select * from customers
where last_name = 'Smith';

-- All customers whose last name is ‘Jones’.
select * from customers
where last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’.
select * from customers
where first_name = 'Scott';


--Create a table named purchases. It should have 3 columns :
--id : the primary key of the table
--customer_id : this column references the table customers
--item_id : this column references the table items
--quantity_purchased : this column is the quantity of items purchased by a certain customer

create table purchases(
    id serial primary key,
	customer_id INTEGER,
	item_id INTEGER,
    FOREIGN KEY  (customer_id) REFERENCES customers (id),
    FOREIGN KEY  (item_id) REFERENCES items (id),
	quantity_purchased integer);

--Insert purchases for the customers, use subqueries:
--Scott Scott bought one fan
--Melanie Johnson bought ten large desks
--Greg Jones bougth two small desks

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
    (SELECT id FROM items WHERE item = 'Fan'),
    1
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
    (SELECT id FROM items WHERE item = 'Large desk'),
    10
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
    (SELECT id FROM items WHERE item = 'Small Desk'),
    2
);

SELECT *
FROM purchases;

DELETE from purchases
WHERE id > 3;

UPDATE  purchases
SET item_id = 2
WHERE id = 2;

UPDATE  purchases
SET item_id = 1
WHERE id = 3;

--All purchases, joining with the customers table.

SELECT *
FROM purchases as p
JOIN  customers as c
ON c.id = p.customer_id;

--Purchases of the customer with the ID equal to 5.
SELECT *
FROM purchases
WHERE customer_id = 5;

--Purchases for a large desk AND a small desk
SELECT *
FROM purchases as p
JOIN items as i
ON p.item_id = i.id
WHERE i.item = 'Small Desk' or i.item = 'Large desk';


SELECT c.first_name,
       c.last_name,
       i.item
FROM customers as c
JOIN purchases as p
ON c.id = p.customer_id
JOIN items as i
ON i.id = p.item_id;

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 5)


--Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
SELECT first_name,
       last_name
FROM customers
ORDER by first_name DESC
LIMIT 2;

--Use SQL to delete all purchases made by Scott.
DELETE FROM purchases
WHERE customer_id = (
    SELECT id
    FROM customers
    WHERE first_name = 'Scott'
);

--Does Scott still exist in the customers table, even though he has been deleted? Try and find him.

SELECT *
FROM customers;
--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear,
--although instead of the customer’s first and last name, you should only see empty/blank.
--(Which kind of join should you use?).

SELECT *
FROM purchases as p
FULL JOIN customers as c
ON c.id = p.customer_id;
--Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear.
--(Which kind of join should you use?)

SELECT *
FROM purchases as p
JOIN customers as c
ON c.id = p.customer_id;