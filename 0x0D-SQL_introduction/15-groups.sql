-- scripts the number of record with the same score in the table
-- count number of score in apperance 
SELECT `score`, COUNT (*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
