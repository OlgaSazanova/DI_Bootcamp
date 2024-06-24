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
    
-- All items, ordered by price (lowest to highest).

select item
from items
order by price;

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select item
from items
where price >= 80
order by price DESC;

-- The first 3 customers in alphabetical order of the first name (A-Z) 
-- – exclude the primary key column from the results.

select first_name, last_name
from  customers
order by first_name
limit 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name
from customers
order by last_name DESC;
