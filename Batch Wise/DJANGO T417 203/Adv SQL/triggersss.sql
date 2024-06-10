create database trigers;
use trigers;

create table product (
id int primary key auto_increment,
name varchar(20) not null unique,
price double);

desc product;

create table costly_product (
pid int,
constraint fk_pid foreign key(pid) references product(id) on delete cascade);

desc costly_product;

-- create trigger after insertion in product table
create trigger costly_prodcut_after_insert
after insert on product
for each row
update costly_product set pid=
(select id from product where price=
(select max(price) from product));



select * from product;
select * from costly_product;

-- inserting null value in costly_product bcoz we cant update if there is no record
insert into costly_product values(null);

insert into product(name,price) values("shirt",500);
insert into product(name,price) values("pant",600);
insert into product(name,price) values("watch",1000);

select * from product;
select * from costly_product;

-- create trigger after updation in product table
create trigger costly_prodcut_after_update
after update on product
for each row
update costly_product set pid=
(select id from product where price=
(select max(price) from product));

select * from product;
select * from costly_product;

update product set price=6000 where id=2;

select * from product;
select * from costly_product;


-- create trigger before deletion in product table
create trigger costly_prodcut_before_delete
before delete on product
for each row 
insert into costly_product values(null);

-- create trigger after deletion in product table
create trigger costly_prodcut_after_delete
after delete on product
for each row 
update costly_product set pid=
(select id from product where price=
(select max(price) from product));

delete from product where id=2;
select * from product;
select * from costly_product;

delete from product where id=3;
select * from product;
select * from costly_product;














