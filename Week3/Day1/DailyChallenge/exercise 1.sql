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