-- write script that displays top 3 cities temperature in a month range
-- in descending order
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;