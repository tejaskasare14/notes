create database emp_trigger;
use emp_trigger;
create table emp(
				id int primary key auto_increment,
                name varchar(20) null,
                age int not null);
insert into emp(name,age)values("raj",20),("rani",25),("amit",26);
select * from emp;
select avg(age) from emp;

create table avg_emp_age(avg_age float not null);
insert into avg_emp_age(avg_age)values((select avg(age) from emp));
select * from avg_emp_age;

insert into emp(name,age)value("radha",30);
select * from emp;
select avg(age) from emp;

update avg_emp_age set avg_age = (select avg(age) from emp);
select * from avg_emp_age;

-- creating trigger to update table after inster

-- CREATE TRIGGER trigger_name
-- BEFORE/AFTER INSERT/UPDATE/DELETE ON table_name
-- FOR EACH ROW
-- your_query;

CREATE TRIGGER avg_emp_age_after_insert
AFTER INSERT ON emp
FOR EACH ROW
update avg_emp_age set avg_age = (select avg(age) from emp);

select * from emp;
select * from avg_emp_age;
insert into emp(name,age)value("shital",35);
select * from emp;
select * from avg_emp_age;


DELIMITER $$
CREATE TRIGGER emp_before_insert
BEFORE INSERT ON emp
FOR EACH ROW
IF new.age<18 then set new.age=0;
END IF $$

DELIMITER ;

insert into emp(name,age)value("sidhhu",15);
select * from emp;

drop trigger emp_before_insert;

-- create trigger after updating record from emp table
-- task : to update avg_age in emp_avg_age table
CREATE TRIGGER avg_emp_age_after_update
AFTER UPDATE ON emp
FOR EACH ROW
update avg_emp_age set avg_age = (select avg(age) from emp);

select * from emp;
select * from avg_emp_age;
update emp set age = 40 where id = 1;
select * from emp;
select * from avg_emp_age;

-- create trigger before updating record from emp table
-- task : to set age=0 if age<18
DELIMITER $$
CREATE TRIGGER emp_before_update
BEFORE UPDATE ON emp
FOR EACH ROW
IF new.age<18 then set new.age=0;
END IF $$

DELIMITER ;

update emp set age = 14 where id = 1;
select * from emp;

-- before deleting record from emp
create table emp_archive(name varchar(20) null,age int not null);

CREATE TRIGGER emp_archive_before_delete
BEFORE DELETE ON emp
FOR EACH ROW
insert into emp_archive(name,age)value(old.name,old.age);

select * from emp_archive;
delete from emp where id = 1;

select * from emp;
select * from emp_archive;












