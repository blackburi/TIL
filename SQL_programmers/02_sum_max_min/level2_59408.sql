-- 중복 제거하기

select count(distinct(name))
from animal_ins
where name <> 'NULL'