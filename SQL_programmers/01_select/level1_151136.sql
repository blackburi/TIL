-- 평균 일일 대여 요금 구하기

select round(sum(daily_fee)/count(daily_fee), 0) as average_fee
from car_rental_company_car
where car_type = 'SUV'