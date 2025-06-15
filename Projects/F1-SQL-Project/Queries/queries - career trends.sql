SELECT 
    ci.name AS circuit_name,
    d.forename,
    d.surname,
    COUNT(*) AS fastest_laps
FROM results r
JOIN drivers d ON r.driverId = d.driverId
JOIN races ra ON r.raceId = ra.raceId
JOIN circuits ci ON ra.circuitId = ci.circuitId
WHERE r.ranking = '1'
GROUP BY ci.name, d.driverId
ORDER BY fastest_laps DESC;

