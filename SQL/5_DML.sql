drop database employee_db;

create database employee_db;

use employee_db;

create table employee(
	id int primary key,
    name varchar(20) not null,
    age int check(age>18 and age<35) not null,
    gender enum('m','f') not null,
    doj date not null,
    salary int default 0,
    skills set('java','sql','python'),
    phone varchar(20) unique not null
);
-- since we have not added auto incremet to id, so we have to pass id manually

-- INSERT
-- insert into table_name(column1,column2....) values(value1, value2......)

-- inserting without specifiying column name
--     when you are inserting data without specifing column name, 
--     you have to pass data for all columns with maintaining order of column
insert into employee values(101,"raj",20,"m","2020-11-30",350000,'java,sql',9856365248);
select * from employee;

-- inserting with specifiying all column names
insert into employee (id,name,age,gender,doj,salary,skills,phone)
values(102,"rani",25,"f","2020-10-28",300000,'java',9856365245);
select * from employee;

-- inserting without specifiying some column names
-- here specify only those column names on which there is no NOT NULL
-- here we have two columns - salary and skills
insert into employee (id,name,age,gender,doj,phone)
values(104,"aniket",32,"m","2020-09-28",9856365235);
select * from employee;

-- inserting wmultiple values at a time - for all columns
insert into employee 
(id,name,age,gender,doj,salary,skills,phone)
values
(105,"punit",31,"m","2019-08-25",210000,'java,sql',8956365245),
(106,"radha",30,"f","2022-07-10",200000,'java,python',7556365245),
(107,"sanjay",28,"m","2022-10-07",380000,'java,sql,python',8656365245);
select * from employee;

-- inserting data from one table to another
-- creating table with some imp details of employee (not all details)
create table employee_test(
	id int primary key,
    name varchar(20) not null,
    gender enum('m','f') not null,
    phone varchar(20) unique not null
);
select * from employee_test;
insert into employee_test select id,name,gender,phone from employee;
select * from employee_test;
select * from employee;

-- UPDATE
-- UPDATE table_name SET column_to_be_modify = value WHERE column_name_with_pk = value

-- udpdate one column at a time
select * from employee;
update employee set name = "raju" where id = 101;
select * from employee;

-- udpdate mutiple column at a time
select * from employee;
update employee set name = "raj",salary=40000 where id = 101;
select * from employee;

-- udpdate without where condition
-- not recommonded to use
update employee set name = "raj";
select * from employee;

-- DELETE
-- DELETE FROM table_name WHERE column_name = value

-- delete one record/row at a time
delete from employee where id=101;
select * from employee;
-- delete one record/row at a time with wrong id
-- if id does not exist, then our command will not give any error
delete from employee where id=201;
select * from employee;
-- delete muliple row/record at a time
delete from employee where gender='m';
select * from employee;
-- delete without where condition
delete from employee;
select * from employee;






























































