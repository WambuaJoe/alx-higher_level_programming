-- list all records in second_table that fit the criteria
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;