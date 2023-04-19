select
	activity_date as day,
	count(distinct user_id) as active_users
from
	activity
where
	activity_date >= '2019-07-28' - INTERVAL 1 MONTH and activity_date < '2019-07-29'
group by
	activity_date