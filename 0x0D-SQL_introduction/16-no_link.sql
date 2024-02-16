-- list all record of the second_table from the database
-- result only list with names in a descending order
SELECT `score`, `name` 
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
