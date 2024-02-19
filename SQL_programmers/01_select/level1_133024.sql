-- 인기있는 아이스크림

select flavor
from first_half
order by total_order desc, shipment_id asc