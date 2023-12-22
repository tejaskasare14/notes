use my_db;
drop table employee;

create table employee(
id int primary key auto_increment,
fname varchar(20),
lname varchar(20),
salary int,
total_leaves int,
bonus int
);


insert into employee
(fname,lname,salary,total_leaves,bonus) 
values
("raj","kumar",30000,5,4500),
("rani","shinde",45000,3,1000),
("aniket","jadhav",15000,8,null),
("sumit","kumar",7500,2,800);

select * from employee;

-- Built in functions
-- Built in functions always use with SELECT
-- STRING FUNCTION
select concat("python","java");
select concat("python","java") as new_column;
select concat(fname,lname) as full_name from employee;
select concat(fname," ",lname) as full_name from employee;
select upper(fname) from employee;
select lower(fname) from employee;
select reverse(fname) from employee;

-- using separator with concat
select concat(fname," ",lname," ",salary) as full_name from employee;
select concat_ws(" ",fname,lname,salary) as full_name from employee;

-- from 2nd character to next 3 characters
-- 2nd character is a, next 3 characters including a are a,h,a
select insert("maharashtra",2,3,"*");
select insert(fname,1,2,"-") from employee;

-- Aggrigate functions
select min(salary) from employee;
select least(20,30,10,50);
select max(salary) from employee;
select greatest(20,30,10,50);
select avg(salary) from employee;
select sum(salary) from employee;

select * from employee where salary =(select min(salary) from employee);















