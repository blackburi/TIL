-- 오프라인/온라인 판매 데이터 통합하기

select date_format(a.sales_date, '%Y-%m-%d'), a.product_id, a.user_id, a.sales_amount
from (select sales_date, product_id, user_id, sales_amount
      from online_sale
      union all
      select sales_date, product_id, null as user_id, sales_amount
      from offline_sale) as a
where month(a.sales_date) = 3
order by a.sales_date, a.product_id, a.user_id