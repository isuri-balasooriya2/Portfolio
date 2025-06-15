SELECT c.name AS constructor, ROUND(AVG(p.milliseconds), 2) AS avg_pit_time,
COUNT(*) AS total_entries
FROM pit_stops p
JOIN results r ON p.raceId = r.raceId AND p.driverId = r.driverId
JOIN constructors c ON r.constructorId = c.constructorId
GROUP BY c.name
HAVING total_entries>100
ORDER BY avg_pit_time ASC;
