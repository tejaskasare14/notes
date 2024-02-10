use my_db;
show tables;
drop table employee;

create table employee(
id int primary key auto_increment,
name varchar(20),
per_day int,
total_leaves int,
bonus int
);

-- starting transaction
start transaction;

insert into employee
(name,per_day,total_leaves,bonus) 
values
("raj",1000,5,4500),
("rani",2500,3,1000),
("aniket",3000,8,null),
("sumit",500,2,800);

-- creating insert savepint 
savepoint insertion_step;
select * from employee;

-- updating 1 record
update employee set name="raju" where id = 1;
select * from employee;

-- undo update and go to insert savepoint
rollback to insertion_step;
select * from employee;

-- deleting record
delete from employee where id=1;
select * from employee;

-- undoing delete command
rollback to insertion_step;
select * from employee;

-- deleting record
delete from employee where id=1;
select * from employee;

-- commit is used to make permenant change
commit;

-- we cant rollback since we have made commit
rollback to insertion_step;















































