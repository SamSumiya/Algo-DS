select
	name,
	bonus
from
	bonus
	left join employee
where
	employee.empId = bonus.empId;