-- 가격대 별 상품 개수 구하기

SELECT TRUNCATE(price, -4) AS price_group, count(*) AS products
FROM product
GROUP BY price_group
order by price_group