SELECT
	weather.id as 'Id'
FROM
	weather
	JOIN weather w ON DATEDIFF(weather.recordDate, w.recordDate) = 1
	and weather.temperature > w.temperature