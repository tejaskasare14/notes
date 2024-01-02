-- always use aggrigate function with group by.
-- never ever use single column. dont write group by query without aggrigate function

use my_db;
drop table employee;

create table employee(
id int primary key ,
name varchar(20),
city varchar(20),
gender varchar(2),
salary double
);

insert into employee values
(1,"raj","pune","m",25000),
(2,"aniket","thane","m",20000),
(3, "rani","pune","f",10000),
(4,"rajat","thane","m",8000);

select * from employee;
select city from employee;
select gender from employee;
select distinct city from employee;
select distinct gender from employee;
select city from employee group by city;
select gender from employee group by gender;

-- show me city wise max salary
select * from employee;
select max(salary),city from employee;
select max(salary),city from employee group by city;
select city,name from employee group by city; -- dont write queries like this

-- show me gender wise max salary
select max(salary),gender from employee group by gender;

-- city wise min salary
select min(salary),city from employee group by city;
-- city wise total salary
select sum(salary),city from employee group by city;
-- city wise total employees
select city,count(*) from employee group by city;

-- how many m and f are there in each city
select city,gender,count(gender) from employee group by city,gender;

-- show city name where company spending total salary more than 30000 
-- sum(salary)>30000;
select city, sum(salary) from employee group by city having sum(salary)>30000;

-- check which gender getting max salary
select max(salary), gender from employee;


























