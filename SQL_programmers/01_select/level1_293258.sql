-- 잔챙이 잡은 수 구하기

select count(*) as fish_count
from fish_info
where ifnull(length, 0) < 10