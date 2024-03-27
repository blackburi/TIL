-- 카테코리 별 도서 판매량 집계하기

select category, sum(sales) as total_sales
from book b join book_sales s using (book_id)
where s.sales_date between "2022-01-01" and "2022-01-31"
group by b.category
order by category