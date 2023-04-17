select
	employee_id,
	if (
		employee_id % 2 != 0
		and name not like 'M%',
		salary,
		0
	) as bonus
from
	employees
order by
	employee_id

-- with case when then else 
select
	employee_id,
	case
		when employee_id % 2 = 0 then 0
		when name like 'M%' then 0
		else salary
	end as bonus
from
	employees
order by
	employee_id