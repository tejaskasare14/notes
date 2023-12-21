create database my_db;

use my_db;

create table employee(
id int primary key auto_increment,
name varchar(20),
per_day int,
total_leaves int,
bouns int
);

alter table employee rename column bouns to bonus;

show tables;

desc employee;

insert into employee
(name,per_day,total_leaves,bonus) 
values
("raj",1000,5,4500),
("rani",2500,3,1000),
("aniket",3000,8,null),
("sumit",500,2,800);

select * from employee;

-- SELECT WITH ARITHMATIC OPERATORS : +,-,*,/
-- show monthly salary of each employee
select name,per_day*30 as salary from employee;

-- show salary after giving bonus
select name, per_day*30+bonus as salary_bonus from employee;
select name,per_day*30 as salary, per_day*30+bonus as salary_bonus from employee;

-- show salary after removing leaves
select name, per_day*(30-total_leaves) as final_salary from employee;

-- make salary half of each employee
select name,(per_day*30)/2 as half_salary from employee;

-- SELECT WITH COMPARISION OP
select * from employee where per_day<1000;
select * from employee where per_day>1000;
select * from employee where per_day<=1000;
select * from employee where per_day>=1000;
select * from employee where per_day=1000;
select * from employee where per_day!=1000;
select * from employee where per_day<>1000;

-- show employees who are getting salary more than 30k
select * from employee where per_day*30>30000;


-- SELECT WITH LOGICAL OPRATOR : and, or, not

-- show employees who are getting per_day more than 1000 as well as  has leaves more than 5 days
select * from employee where per_day>1000 and total_leaves>5;

-- show employees who are getting either per_day more than 1000 or has leaves more than 5 days
select * from employee where per_day>1000 or total_leaves>5;

-- show employees who are getting either per_day more than 5000 or has leaves more than 5 days
select * from employee where per_day>5000 or total_leaves>5;

-- show me employees whos name is not raj
select * from employee where not name = "raj";

-- SLEECT WITH IN , NOT IN OPERATOR
-- show empoyees getting per_day either 1000 or 2500 or 3000
select * from employee where per_day=1000 or per_day=2500 or per_day=3000;
-- instead of using multiple OR statements, use IN operator
select * from employee where per_day in(1000,2500,3000);
select * from employee where per_day not in(1000,2500,3000);

-- SELECT WITH RANGE OPERATOR (BETWEEN)
-- show employees getting per_day in range 500-2500
select * from employee where per_day between 500 and 2500;
-- IMPORTANT : here 500 and 2500 both values will be included

-- show employees who are not getting per_day in range 500-2500
select * from employee where per_day not between 500 and 2500;




