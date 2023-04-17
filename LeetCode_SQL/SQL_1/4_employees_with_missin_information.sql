
select
	employees.employee_id
from
	employees
	left join salaries on employees.employee_id = salaries.employee_id
where
	salaries.employee_id is null
union
select
	salaries.employee_id
from
	salaries
	left join employees on employees.employee_id = salaries.employee_id
where
	employees.employee_id is null
Order by
	employee_id