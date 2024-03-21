-- 저자 별 카테고리 별 매출액 집계하기

select car_type, count(*) as cars
from car_rental_company_car
where (options like '%통풍시트%') or
      (options like '%열선시트%') or
      (options like '%가죽시트%')
group by car_type
order by car_type asc