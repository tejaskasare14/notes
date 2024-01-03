-- when there are muiltple entities in one table, it may create 
-- duplicate records (like patient and doctor data in one table)
-- so it is better to separate those 2 entities and make a new tables
-- for them. and to maintain a relationship between those tables we use primary 
-- key of one table as foreign key in another table

use my_db;
 create table doctor(
 did int primary key,
 dname varchar(20),
 dcity varchar(20),
 dphone varchar(20)
);

insert into doctor values
(1,"Dr Amit","pune","9856985695"),
(2,"Dr Sumit","thane","9856985625");

select * from doctor;

 create table patient(
 pid int primary key,
 did int, -- this will be my column act as FK to maintain ralationship between doctor and patient
 pname varchar(20),
 pcity varchar(20),
 pphone varchar(20),
 constraint fk_did foreign key(did)
 references doctor(did)
);

desc patient;

insert into patient values
(10,1,"raj","delhi","4585698563"),
(12,2,"rani","pune","4585698545"),
(13,1,"kumar","thane","4585698561"),
(14,1,"rajat","delhi","4585698512"),
(18,2,"ritesh","thane","4585698564");

select * from patient;



