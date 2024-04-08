-- 조건에 맞는 사원 정보 조회하기

SELECT SUM(score) AS score, g.emp_no, e.emp_name, e.position, e.email
FROM hr_employees e JOIN hr_grade g USING (emp_no)
GROUP BY year, emp_no
HAVING g.year = '2022'
ORDER BY 1 DESC
LIMIT 1 ;