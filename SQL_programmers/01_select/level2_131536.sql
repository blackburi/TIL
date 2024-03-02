-- 재구매가 일어난 상품과 회원 리스트 구하기

select user_id, product_id
from online_sale
group by user_id, product_id
having count(user_id) >= 2
order by user_id, product_id desc