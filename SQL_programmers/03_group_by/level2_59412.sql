-- 입양 시각 구하기(1)

SELECT DATE_FORMAT(datetime, '%H') as HOUR, COUNT(datetime)
FROM animal_outs
GROUP BY HOUR
HAVING HOUR BETWEEN 9 and 19
ORDER BY HOUR