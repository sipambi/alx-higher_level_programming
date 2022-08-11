-- lists the no" of records with the same score in second_table of hbtn_0c_0
-- score,the no" of records for this score wth the label no",order(descending)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
