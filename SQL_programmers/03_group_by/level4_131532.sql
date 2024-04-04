-- 년, 월, 성별 별 상품 구매 회원 수 구하기

SELECT YEAR(sales_date) AS 'YEAR',
        MONTH(sales_date) AS 'MONTH',
        user_info.gender AS 'GENDER',
        count(DISTINCT online_sale.user_id) AS 'USERS'
FROM user_info, online_sale
WHERE user_info.user_id = online_sale.user_id
    AND user_info.gender IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER