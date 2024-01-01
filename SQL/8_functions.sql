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
select avg(salary) as avg_sal from employee;
select sum(salary) from employee;

select * from employee where salary =(select min(salary) from employee);
select * from employee where salary = 45000;
-- select * from employee where salary = max(salary); ERROR

-- math function
-- abs() gives absolute value / remove sign 
select abs(90);
select abs(-90);

select ceil(40.01);
select ceil(40.99);

select floor(40.01);
select floor(40.99);

select round(40.12);
select round(40.52);

select round(40.125,2);
select round(40.512,2);
select truncate(5.236,1);
select truncate(5.236,2);
select truncate(542,1);
select truncate(542,-1);
select truncate(52.236,-1);
select pow(2,4);
select sqrt(49);
select sqrt(35);
select pow(5.916079783099616,2);
select truncate((select sqrt(35)),2);
select truncate(sqrt(35),2);


-- Date realted functions
select curdate();
select now();
select sysdate();

select year('2025-03-20');
select year(curdate());
select month(curdate());
select day(curdate());
select yearweek('2024-01-08');
select yearweek('2023-12-05');
select last_day(curdate());


select datediff('2024-01-31','2024-01-01');
select datediff('2024-02-14','2024-01-01');
select datediff(last_day(curdate()),curdate())














