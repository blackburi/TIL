# 집계 함수의 그룹화

## 집계 함수의 개념과 종류
* 집계 함수 : 데이터베이스에서 그룹 단위로 데이터를 집계하고 통계적인 값을 게산하기 위해 사용되는 함수
    * 여러 개의 행을 하나의 결과로 반환
    * 데이터의 합계, 평균, 개수, 최댓값, 최솟값 등의 계산을 할 수 있다.
    * 집계함수는 보통 SELECT문장의 SELECT 절이나 HAVING 절에서 사용된다.
* 집계 함수의 종류
    1. `SUM` 함수
        ```sql
        SELECT SUM(sales) AS total_sales
        FROM orders
        ```
        * 숫자 데이터의 합계를 계산
        * 슷자형 열에서 사용되며 `NULL`값을 제외하고 합계를 계산
    2. `AVG` 함수
        ```sql
        SELECT AVG(price) AS average_price
        FROM products
        ```
        * 데이터의 평균을 계산
        * 숫자형 열에서 사용되며 `NULL`값을 제외하고 평균을 계산
    3. `COUNT` 함수
        ```sql
        SELECT COUNT(*) AS total_orders
        FROM orders
        ```
        * 행의 개수를 계산
        * 열이나 테이블에서 사용될 수 있으며 `NULL`값을 포함한 모든 행의 개수를 반환
    4. `MAX` 함수
        ```sql
        SELECT MAX(quantity) AS max_quantity
        FROM products
        ```
        * 숫자나 문자열 데이터의 최댓값을 반환
        * 숫자형 열이나 문자열 열에서 사용될 수 있으며 `NULL`값을 제외한 최댓값을 반환
    5. `MIN` 함수
        ```sql
        SELECT MIN(quantity) AS min_quantity
        FROM products
        ```
        * 숫자나 문자열 데이터의 최솟값을 반환
        * 숫자형 열이나 문자열 열에서 사용될 수 있으며 `NULL`값을 제외한 최솟값을 반환
    6. `GROUP_CONCAT` 함수
        ```sql
        SELECT department, GROUP_CONCAT(employee_name) AS employees
        FROM employees
        GROUP By department
        ```
        * 문자열 데이터를 그룹화하여 하나의 문자열로 결합
        * 그룹 내에서 문자열을 결합하고, 구분자를 지정하여 결과를 반환
    7. `DISTINCT` 함수
        ```sql
        SELECT DISTINCT department
        FROM employees
        ```
        * 중복된 값을 제거한 후 유일한 값을 반환
        * 주로 집계 함수와 함께 사용되어 그룹화된 데이터에 중복을 제거한 결과를 얻을 수 있다.

## 그룹화와 HAVING 절
* 그룹화 : SQL에서 데이터를 그룹 단위로 묶어서 집계 함수를 적용하는 기능
    * 그룹화를 통해 특정 기준에 따라 데이터를 분류하고, 그룹 내에서 집계 함수를 사용하여 그룹별로 계산된 결과 추출
* `HAVING`절 : 그룹화된 데이터에 대한 조건을 지정하는 역할
    * `HAVING`절 vs `WHERE`절
        * `WHERE`절 : 개별 레코드에 대한 필터링을 수행
        * `HAVING`절 : 그룹화된 데이터에 대한 필터링을 수행
    * `HAVING`절은 집계함수와 함꼐 사용되며, 그룹화된 데이터의 결과를 조건에 맞게 제한
    * `HAVING`절의 특징
        * `HAVING`절은 `SELECT`문의 `GROUP BY`절과 함께 사용된다.
        * `HAVING`절은 `WHERE`절과 비슷한 문법을 가지며, 조건을 지정할 수 있다.
        * `HAVING`절은 집계 함수를 사용 가능하다.
        * `HAVING`절은 그룹화된 데이터의 결과를 필터링하므로, 결과로 출력되는 그룹의 수를 제한하거나 특정 조건을 만족하는 그룹만 선택할 수 있다.

```sql
-- 2. 각 그룹의 평균 salary를 계산
SELECT department, AVG(salary) AS average_salary
-- 1. employees 테이블을 department로 그룹화
FROM employees
GROUP BY department
-- 3. 평균 salary가 5000보다 큰 그룹만 선택
HAVING AVG(salary) > 5000
-- 이를 통해 평균 salary가 5000보다 큰 부서에 대한 정보를 얻을 수 있다.
```


## 데이터 분석과 집계 함수 응용
* 데이터 분석 작업 수행
    * 데이터 요약 및 통계 : 집계 함수를 사용하여 데이터의 요약 정보와 통계량을 계산할 수 있다. 예를 들어 평균, 합계, 개수, 최댓값, 최솟값 등의 집계 함수를 활용하여 데이터의 특성을 파악할 수 있다. 이를 통해 데이터의 분포, 중심 경향성, 변동성 등을 알 수 있다.
    * 그룹별 분석 : 데이터를 그룹화하여 그룹별로 분석을 수행할 수 있다. 이를 통해 그룹간의 차이나 패턴을 확인하고 비교할 수 있다.
    * 필터링 및 조건부 분석 : 집계 함수와 그룹화를 활용하여 필터링과 조건부 분석을 수행할 수 있다. HAVING절을 사용하여 그룹화된 데이터를 조건에 따라 필터링할 수 있다. 이를 통해 특정 조건을 만족하는 그룹만 분석하는 등의 작업을 수행할 수 있다.
    * 다중 열 그룹화 및 다차원 분석 : 여러 열을 기준으로 데이터를 그룹화하여 다차원 분석을 수행할 수 있다. 예를 들어 부서와 직책별로 평균 급여 계산, 지역과 연도별로 판매량 비교 등 다중 열 그룹화를 통해 다차원적인 분석 수행이 가능하다.
* 일반적으로 사용되는 집계 함수와 그룹화 종류
    1. `GROUP BY`절
        ```sql
        SELECT department, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        ```
    2. `HAVING`절
        ```sql
        SELECT department, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        HAVING average_salary > 5000
        ```
    3. `WITH ROLLUP`절
        ```sql
        /* GROUP BY 절에서 계층적인 그룹화를 수행하고
        각 계층에서의 집계 결과를 포함하여 결과를 반환 */
        SELECT department, job_title, SUM(salary) AS total_salary
        FROM employees
        GROUP BY department, job_title WITH ROLLUP
        ```
    4. 집계 함수의 중첩
        ```sql
        SELECT AVG(MAX(salary)) AS average_max_salary
        FROM employees
        ```
    5. 집계 함수의 조건적 사용
        ```sql
        SELECT AVG(salary) AS average_salary
        FROM employees
        WHERE department = 'Sales'
        ```
    6. 집계 함수의 결과 정렬
        ```sql
        SELECT department, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        ORDER BY average_salary DESC
        ```
    7. 집계 함수의 `NULL`처리
        ```sql
        SELECT department, COUNT(salary) AS employee_count
        FROM employees
        GROUP BY department
        ORDER BY employee_count
        ```
    8. 집계 함수의 별칭(Alias)
        ```sql
        SELECT department, AVG(salary) AS avg_salary, COUNT(*) AS total_count
        FROM employees
        GROUP BY department
        ```
    9. 집계 함수의 종류
        ```sql
        SELECT COUNT(*) AS total_rows,
                SUM(quantity) AS total_quantity,
                AVG(price) AS average_price,
                MAX(date) AS latest_date,
                MIN(date) AS earliest_date
        FROM orders
    10. 그룹화 된 데이터의 필터링
        ```sql
        SELECT department, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        HAVING average_salary > 5000
        ```
    11. 그룹화된 데이터의 정렬
        ```sql
         SELECT department, AVG(salary) AS average_salary
         FROM employees
         GROUP BY department
         ORDER BY average_salary DESC
         ```
    12. 그룹화된 데이터의 조건적 집계
        ```sql
        SELECT department,
                SUM(CASE WHEN salary > 5000 THEN 1 ELSE 0 END) AS high_salary_count,
                SUM(CASE WHEN salary <= 5000 THEN 1 ELSE 0 END) AS low_salary_count
        FROM employees
        GROUP BY department
        ```
    13. 그룹화된 데이터의 다중 열 그룹화
        ```sql
        SELECT department, job_title, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department, job_title
        ```
    14. 그룹화된 데이터의 연산
        ```sql
        SELECT department, SUM(salary) AS total_salary
        FROM employees
        GROUP BY department
        HAVING total_salary > 100000
        ```
    15. 그룹화된 데이터의 복수 열 반환
        ```sql
        SELECT department, job_title,
                AVG(salary) AS average_salary,
                COUNT(*) AS employee_count
        FROM employees
        GROUP BY department, job_title
        ```
    16. 그룹화된 데이터의 결과 제한
        ```sql
        SELECT department, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        ORDER BY average_salary DESC LIMIT 5
        ```
    17. 그룹화된 데이터의 `NULL`철
        ```sql
        SELECT department, COUNT(salary) AS employee_count
        FROM employees
        GROUP BY department
        ORDER BY employee_count
        ```
    18. 그룹화된 데이터의 결과 표현
        ```sql
        SELECT department,
                AVG(salary) AS average_salary,
                CONCAT('$', FORMAT(AVG(salary), 2)) AS formatted_salary
        FROM employees
        GROUP BY department
        ```
    19. 그룹화된 데이터의 다중 조건 필터링
        ```sql
        SELECT department, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        HAVING employee_count > 10 AND AVG(salary) > 5000
        ```
    20. 그룹화된 데이터의 결과 정렬
        ```sql
        SELECT department, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        ORDER BY average_salary DESC
        ```
    21. 그룹화된 데이터의 계층적 그룹화
        ```sql
        SELECT department, job_title, AVG(salary) AS average_salary
        FROM employees
        GROUP BY department, job_title WITH ROLLUP
        ```
    22. 그룹화된 데이터의 결과 제한
        ```sql
        SELECT department, COUNT(*) AS employee_count
        FROM employees
        GROUP BY department
        ORDER BY employee_count DESC LIMIT 5
        ```
    23. 그룹화된 데이터의 결과 조인
        ```sql
        SELECT department, AVG(salary) AS average_salary, department_info.location
        FROM employees
        INNER JOIN department_info ON employees.department = department_info.department
        GROUP BY department
        ```