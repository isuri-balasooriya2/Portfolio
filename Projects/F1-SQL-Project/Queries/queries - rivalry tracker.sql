SELECT 
    CONCAT(a.forename, ' ', a.surname) AS driver_a,
    CONCAT(b.forename, ' ', b.surname) AS driver_b,
    COUNT(*) AS races_together,
    SUM(CASE WHEN ra.position < rb.position THEN 1 ELSE 0 END) AS a_beats_b,
    SUM(CASE WHEN ra.position > rb.position THEN 1 ELSE 0 END) AS b_beats_a
FROM results ra
JOIN results rb ON ra.raceId = rb.raceId AND ra.driverId != rb.driverId
JOIN drivers a ON ra.driverId = a.driverId
JOIN drivers b ON rb.driverId = b.driverId
WHERE a.driverId = 102 AND b.driverId = 117
GROUP BY a.driverId, b.driverId;
