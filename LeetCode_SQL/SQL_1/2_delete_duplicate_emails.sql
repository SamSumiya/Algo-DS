delete from person 
where id not in ( select * from (select min(id) from person group by email) as p )