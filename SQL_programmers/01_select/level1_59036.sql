-- 아픈 동물 찾기

select animal_id, name
from animal_ins
where intake_condition = 'Sick'
order by animal_id