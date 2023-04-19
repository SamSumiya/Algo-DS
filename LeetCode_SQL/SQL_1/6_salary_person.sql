select
	s.name
from
	salesperson as s
	left join orders as o1 on s.sales_id = o1.sales_id
where
	o1.com_id is null
union
select
	a.name
from
	(
		select
			s.name,
			o.com_id
		from
			salesperson as s
			left join orders as o on s.sales_id = o.sales_id
		group by
			s.sales_id
		having
			o.com_id not in (
				select
					c.com_id
				from
					company as c
				where
					c.name = 'Red'
			)
	) as a