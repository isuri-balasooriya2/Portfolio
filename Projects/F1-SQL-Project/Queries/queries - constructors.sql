#Question 1
SELECT c.name,
SUM(CASE WHEN q.position='1' THEN 1 ELSE 0 END) AS total_poles,
SUM(CASE WHEN r.position='1' THEN 1 ELSE 0 END) AS total_wins,
ROUND(100*SUM(CASE WHEN q.position='1' THEN 1 ELSE 0 END)/SUM(CASE WHEN r.position='1' THEN 1 ELSE 0 END),2 ) AS pole_to_win_rate
FROM constructors c
JOIN results r ON c.constructorId=r.constructorId
JOIN qualifying q ON r.driverId = q.driverId AND r.raceId = q.raceId
GROUP BY c.constructorId
HAVING total_poles>50
ORDER BY pole_to_win_rate DESC;

#Question 2
SELECT c.name AS Constructor, ci.name AS Circuit,
COUNT(*) AS total_wins
FROM results r
JOIN constructors c ON c.constructorId=r.constructorId
JOIN races ra ON ra.raceId=r.raceId
JOIN circuits ci ON ci.circuitId=ra.circuitId
WHERE r.position='1'
GROUP BY c.name,ci.name
HAVING total_wins>5 
ORDER BY total_wins DESC;

#Question 3
SELECT c.name, r.year, SUM(cs.points) AS season_points
FROM constructor_standings cs
JOIN constructors c ON c.constructorId = cs.constructorId
JOIN races r ON r.raceId = cs.raceId
GROUP BY c.name, r.year
HAVING season_points>50
ORDER BY c.name, r.year;


