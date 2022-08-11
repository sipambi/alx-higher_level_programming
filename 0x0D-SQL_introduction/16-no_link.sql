-- lists all records of second_table in hbtn_0c_0,list rows with name value
-- display the score and the name (in this order), descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
