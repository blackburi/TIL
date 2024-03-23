-- 저자 별 카테고리 별 매출액 집계하기

select author_id, author_name, category, sum(sales * price) as total_sales
from author join book using author_id
            join book_sales using book_id
where date_format(sales_date, '%Y-%m') = '2022-01'
group by author_id, category
order by author_id, category desc