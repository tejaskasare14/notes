

create table department 
( did int primary key , 
department_name varchar (20)  ,
department_head varchar (20) ) ; 

desc department ; 


insert into department 
( did , department_name , department_head )  
values 
( 1 , 'hr' , 'amit' ) ,
( 2 , 'trainer ' ,'sumit ' ) ,
( 3 , 'accounts ' , 'pranit ' ) ,
( 4 , 'it' , 'pratik' ) ,
( 5 , 'infra ' ,'sunita ' ); 
 



select * from department ; 

drop table employee ; 
create table employee 
( eid int primary key , 
name varchar (20 ) , 
phone int unique , 
did int , 
constraint did_fk foreign key(did) 
references department(did) ) ; 

insert into employee values 
( 10 , 'raj' , '123' , 1 ) ,
( 11 , 'rani' , '456' ,2 ) , 
( 12 , 'rajat' ,'126' ,3 ) , 
(13 ,'aniket' ,'359' ,4 ) ,
(14 ,'john' , '128' , null ); 

select * from employee ; 
select * from department;

-- inner join : to get common records from both table
-- SELECT column_name_from_both_table
-- FROM table1_name
-- join_name table2_name
-- ON common_column_name

select eid,name,phone,department_name,department_head
from employee
inner join department
on employee.did = department.did;

-- left join : aal records from left table and matching record from right table

select eid,name,phone,department_name,department_head
from employee
left join department
on employee.did = department.did;

select eid,name,phone,department_name,department_head
from employee
right join department
on employee.did = department.did;

-- full outer join : there is no full outer join in mysql. but we can achive it by 
-- taking unioun of left join and right join

select eid,name,phone,department_name,department_head
from employee
left join department
on employee.did = department.did
union
select eid,name,phone,department_name,department_head
from employee
right join department
on employee.did = department.did;

-- self join : when there is relation between entties is present inside same table, we have to use self join
-- ex : employee table. there are some employees who are manager


create table emp 
( id int primary key ,
name varchar (20) ,
phone varchar (20) , 
manager_id int ) ; 

insert into emp values
( 1 , ' raj ', '123' , 3 ) , 
( 2 , 'rani' ,'456' , 3 ) , 
( 3 , 'punit' ,'126' , null ) , 
( 4 , 'aniket' , '359' , 1 ) ; 

select *  from emp ; 

select employeee.id, employeee.name as emp_name, employeee.phone, manager.name as manager_name
from emp employeee
join emp manager
on employeee.manager_id = manager.id;


-- join with sorting and condition
select eid,name,phone,department_name,department_head
from employee
inner join department
on employee.did = department.did
order by name;

select eid,name,phone,department_name,department_head
from employee
inner join department
on employee.did = department.did
where phone in(123,359);

select eid,name,phone,department_name,department_head
from employee
inner join department
on employee.did = department.did
where phone in(123,359) order by name;


 