-- 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기

SELECT e.emp_no,
        e.emp_name,
        CASE
            WHEN AVG(g.score) >= 96 THEN 'S'
            WHEN AVG(g.score) >= 90 THEN 'A'
            WHEN AVG(g.score) >= 80 THEN 'B'
            ELSE 'C'
        END AS grade,
        CASE
            WHEN AVG(g.score) >= 96 THEN e.sal*0.2
            WHEN AVG(g.score) >= 90 THEN e.sal*0.15
            WHEN AVG(g.score) >= 80 THEN e.sal*0.1
            ELSE 0
        END AS bonus
FROM hr_department d JOIN hr_employees e ON e.dept_id=d.dept_id
                     JOIN hr_grade g ON g.emp_no=e.emp_no
GROUP BY e.emp_no
ORDER BY 1 ;