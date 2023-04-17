select
	a1.player_id,
	a1.device_id
from
	activity a1
where
(a1.player_id, a1.event_date) in (
		select
			a2.player_id,
			min(a2.event_date)
		from
			activity as a2
		group by
			player_id
	)