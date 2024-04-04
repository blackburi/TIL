-- 입양 시각 구하기(2)

SET @HOUR = -1;

SELECT (@HOUR := @HOUR +1) AS HOUR,
        (SELECT COUNT(*)
        FROM animal_outs
        WHERE HOUR(datetime)=@HOUR) AS COUNT
FROM animal_outs
WHERE @HOUR < 23
ORDER BY HOUR ;