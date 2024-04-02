-- 동명 동물 수 찾기

SELECT name, count(*)
FROM animal_ins
WHERE name IS NOT NULL
GROUP BY name
HAVING count(*) >= 2
ORDER BY name