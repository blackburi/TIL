-- 고양이와 개는 몇 마리 있을까

select animal_type, count(*)
from animal_ins
group by animal_type
order by animal_type