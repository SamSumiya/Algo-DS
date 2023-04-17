select
	user_id,
	concat(upper(left(name, 1)), lower(substring(name, 2))) as name
from
	users
order by
	user_id;