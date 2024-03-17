-- 조건에 맞는 아이템들의가격의 총합 구하기

select sum(price) as total_price
from item_info
where rarity = 'LEGEND'