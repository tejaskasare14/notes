-- selecting database
use students;
show tables;

-- creating employee table with name column
create table emplyee (name varchar(20) not null);
show tables;
desc emplyee;

-- adding age column (by deafult added at the end)
alter table emplyee add column age int not null;
desc emplyee;

-- adding id column (add at the begining)
alter table emplyee add column id int primary key first;
desc emplyee;

-- adding "doj" column between name and age
-- there is only "after" command in sql. there is no "before"
alter table emplyee add column doj date after name;
desc emplyee;

-- adding multipe column at a time
alter table emplyee add column (phone varchar(15), gender enum('m','f'));
desc emplyee;

-- changing column structure size,data type, or add constraint
-- we can modify one column at time
alter table emplyee modify column phone varchar(20);
desc emplyee;

alter table emplyee modify column phone int unique;
desc emplyee;

-- remianing column
alter table emplyee rename column phone to phone_number;
desc emplyee;

-- remianing column
alter table emplyee rename to employee;
desc emplyee;
desc employee;


-- adding constraints - add uqiue  constraint on name column
alter table employee add constraint unique_name unique(name);
desc employee;

-- removing constraint
alter table employee drop constraint unique_name;
desc employee;

-- adding constraints - add check  constraint on age column
alter table employee add constraint check_age check(age>18 and age<35);
desc employee;

-- removing constraint
alter table employee drop constraint check_age;
desc employee;






