-- 조건에 맞는 회원수 구하기

select count(user_id) as users
from user_info
where year(joined) = 2021 and
      (20 <= age <= 29 or age = 'NULL')