select a.name as Employee 
from employee as a join employee as b
on a.managerId = b.id
and a.salary > b.salary; 