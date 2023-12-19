-- defFult database where all users information is stored
show databases;

-- selecting mysql database
use mysql;

-- showing all tables present isnide mysql database
show tables;

-- using user table
select * from user; -- * means all columns in user table
select User from user; -- here User is column name present inside user table

-- creating our own users
create user 'tom'@'localhost' identified by 'tom@123';
select User from user;
create user 'jerry'@'localhost' identified by 'jerry@123';
select User from user;

-- check current user
select current_user();
select user();

-- checking permission for perticular user
show grants for 'root'@'localhost';
show grants for 'tom'@'localhost';
show grants for 'jerry'@'localhost';

-- giving permissions to users
-- GRANT permission_name(s) ON DATABASE_NAME.TABLE_NAME TO user_name
use students;
show tables;
select * from book;

use mysql;

-- one permission on one table at a time
GRANT insert ON students.book TO 'tom'@'localhost';
show grants for 'tom'@'localhost';

-- multiple permissions on one table at a time
GRANT select,update ON students.book TO 'tom'@'localhost';
show grants for 'tom'@'localhost';

-- all permissions on one table at a time
GRANT all ON students.book TO 'tom'@'localhost';
show grants for 'tom'@'localhost';

-- all permissions on all tables at a time
GRANT all ON students.* TO 'tom'@'localhost';
show grants for 'tom'@'localhost';

-- all permissions on all databases and all tables at a time
GRANT all ON *.* TO 'tom'@'localhost';
show grants for 'tom'@'localhost';

-- removing permissions
grant insert,update,delete on students.book to 'jerry'@'localhost';
show grants for 'jerry'@'localhost';

revoke insert on students.book from 'jerry'@'localhost';
show grants for 'jerry'@'localhost';











