-- 성분으로 구분한 아이스크림 총 주문량

select ingredient_type, sum(total_order) as total_order
from first_half join icecream_info on first_half.flavor = icecream_info.flavor
group by icecream_info.ingredient_type
order by sum(total_order) asc