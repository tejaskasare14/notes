create database sp;
use sp;

create table employee(
id int primary key auto_increment,
name varchar(10),
salary float
);

insert into employee(name,salary) values
("raj",25000),("rani",30000),("rajat",28000);

select * from employee;
call all_employees;

call employee_count();

insert into employee(name,salary) values
("rakshit",20000);

call employee_count();

call employeeById(1);

call outAvgSalary(@avgSalary);
select @avgSalary;

call in_id_out_name(2,@empname);
select @empname;

call conditional_sp();







