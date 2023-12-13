-- to check all databases
show databases;

-- to create database
-- create database database_name;
create database students;

-- check students databases created or not
show databases;

-- to drop/delete database
drop database students;

-- create students database 
create database students;

-- to select database for creating table
use students;

-- creating table inside students database
-- create table table_name (column_name datatype[(size)] [constraints]);
create table student(name varchar(10),age int);

-- to check all tables in selected database (students)
show tables;

-- checking structure of newly created table
describe student;

-- to drop/deleting table
drop table student;

-- inserting record into table
-- insert into table_name(column1, column2 ....) values (value1, value2.....)
insert into student(name,age) values("raj", 30);

-- to check all data inside table
-- select * from table_name
select * from student;
































































































































