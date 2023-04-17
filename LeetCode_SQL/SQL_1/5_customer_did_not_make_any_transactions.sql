select
	a.customer_id,
	count(*) as count_no_trans
from
	(
		select
			customer_id,
			count(transaction_id) as count_no_trans
		from
			visits
			left join transactions on visits.visit_id = transactions.visit_id
		group by
			visits.visit_id,
		having
			count_no_trans = 0
	) as a
group by
	customer_id


SELECT
	customer_id,
	COUNT(Visits.visit_id) AS count_no_trans
FROM
	visits
LEFT JOIN Transactions
	ON Visits.visit_id = Transactions.visit_id
WHERE 
	Transactions.visit_id IS NULL
GROUP BY customer_id