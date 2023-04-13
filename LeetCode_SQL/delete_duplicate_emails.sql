delete person from person 
where id not in 
	(select * from 
		(select min(id) from person group by email) as p )



delete p1 
from person p1, person p2
where p1.email = p2.email and p1.id > p2.id; 