-- constraints : read notes from notebook
-- book : 
-- id : int : PK, auto_increment,
-- book_name : varchar(50) : not null, unique
-- author_name: varchar(50) : default 'NA',
-- price : int : check -> 99-999
-- genre : enum : comedy,horror
-- available_in : set : online,offline,audio

-- selecting table in which we want to create table
use students;

-- creating book table with proper constraints
create table book(
id int primary key auto_increment,
book_name varchar(50) not null unique,
author_name varchar(50) default 'NA',
price int check(price>99 and price<999) not null,
genre enum('comedy','horror'),
available_in set('online','offline','audio')
);

-- getting all tables from database
show tables;

-- getting structure of newly created table - book
desc book;

-- inserting one correct record 
insert into book(book_name,author_name,price,genre,available_in)values("sql","tejas k",250,'comedy','online,offline');

-- use below command if you have entered wrong data
-- by running below command you are going to remove all records from table
truncate book;

-- getting all records from table
select * from book;

-- adding wrong data and checking whta types of error we get

-- adding duplicate book_name (voilating uniue constraint)
insert into book(book_name,author_name,price,genre,available_in)values("sql","tejas k",250,'comedy','online,offline');
-- Error Code: 1062. Duplicate entry 'sql' for key 'book.book_name'

-- not adding book_name (voilating not null constraint)
-- wrong way
insert into book(book_name,author_name,price,genre,available_in)values("tejas k",250,'comedy','online,offline');
-- Error Code: 1136. Column count doesn't match value count at row 1

-- not adding book_name (voilating not null constraint)
-- correct way
-- not passing value to column means not specifing column name
insert into book(author_name,price,genre,available_in)values("tejas k",250,'comedy','online,offline');
-- Error Code: 1364. Field 'book_name' doesn't have a default value
-- IMPORTANT : if there is NOT NULL cnstraint on any column then either specify default value or pass value































