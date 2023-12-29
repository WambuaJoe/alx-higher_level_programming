-- display average temperature (F) by city in descending order
-- SELECT city, AVG(value) AS avg_temp
-- FROM temperatures
-- GROUP BY city
-- ORDER BY avg_temp DESC;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;