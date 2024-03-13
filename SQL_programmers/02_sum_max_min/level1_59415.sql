-- 최댓값 구하기

select max(datetime)
from animal_ins

-- 또다른 풀이
select datetime
from animal_ins
order by datetime desc limit 1