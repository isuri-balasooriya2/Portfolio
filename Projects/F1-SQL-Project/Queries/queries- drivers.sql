#Question 1
SELECT d.forename, d.surname, 
       COUNT(*) AS total_races,
       SUM(CASE WHEN r.position REGEXP '^[0-9]+$' THEN 1 ELSE 0 END) AS finishes,
       ROUND(100 * SUM(CASE WHEN r.position REGEXP '^[0-9]+$' THEN 1 ELSE 0 END) / COUNT(*), 2) AS finish_rate
FROM results r
JOIN drivers d ON r.driverId = d.driverId
GROUP BY d.driverId
HAVING total_races > 50
ORDER BY finish_rate DESC;

#Question2
SELECT d.forename,d.surname,
COUNT(*) AS race_entries,
SUM(r.points) AS total_points,
ROUND(SUM(r.points)/COUNT(*),2) AS points_per_race
FROM results r
JOIN drivers d ON d.driverId=r.driverId
GROUP BY d.driverId
HAVING race_entries>50
ORDER BY points_per_race DESC;

#Question 3
SELECT d.forename, d.surname, 
       COUNT(*) AS pole_positions,
       SUM(CASE WHEN r.position = '1' THEN 1 ELSE 0 END) AS wins_from_pole,
       ROUND(100 * SUM(CASE WHEN r.position = '1' THEN 1 ELSE 0 END)/COUNT(*), 2) AS conversion_rate
FROM qualifying q
JOIN results r ON q.driverId = r.driverId AND q.raceId = r.raceId
JOIN drivers d ON d.driverId = q.driverId
WHERE q.position = 1
GROUP BY d.driverId
HAVING pole_positions > 5
ORDER BY conversion_rate DESC;

#Question 4
SELECT d.forename, d.surname,
COUNT(*) AS total_qualis,
 ROUND(AVG(
           CAST(SUBSTRING_INDEX(q.q3, ':', 1) AS DECIMAL(10,3)) * 60 +
           CAST(SUBSTRING_INDEX(q.q3, ':', -1) AS DECIMAL(10,3))
       ), 3) AS avg_q3_seconds
FROM qualifying q
JOIN drivers d ON d.driverId=q.driverId
WHERE q.q3 IS NOT NULL AND q.q3 REGEXP '^[0-9]+:[0-9]{2}\\.[0-9]{3}$'
GROUP BY d.driverId
HAVING total_qualis>50
ORDER BY avg_q3_seconds ASC
LIMIT 10;

#Question 5
SELECT d.forename, d.surname,
COUNT(*) as total_entries,
ROUND(AVG(q.position),2) AS avg_grid_position,
ROUND(AVG( CAST(r.position AS UNSIGNED)),2) AS avg_race_position,
ROUND(AVG(q.position) - AVG(CAST(r.position AS UNSIGNED)), 2) AS racecraft_score
FROM qualifying q
JOIN drivers d ON d.driverId=q.driverId
JOIN results r ON r.raceId=q.raceId AND q.driverId = r.driverId
WHERE q.position>0
GROUP BY d.driverId
HAVING avg_race_position>0 AND total_entries>50
ORDER BY racecraft_score DESC;


