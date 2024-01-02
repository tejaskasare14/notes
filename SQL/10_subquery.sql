-- when output of one query act as input to another query
-- we generay use subquery on single table
-- ex : show me empoyees getting salary more than rani
		-- here first we have to find rani's salary
		-- then use this as output to find other employees
        
use my_db;
-- show me empoyees getting salary more than rani
select salary from employee where name = "rani";
select * from employee where salary > 10000;

-- solution by subquery
select * from employee where salary > 
(select salary from employee where name = "rani");






































