# SQL 기초
* 데이터 베이스 : 데이터를 구조화하고 저장하는 공간
* 테이블 : 데이터의 집합을 나타내는 구조.

## 데이터베이스와 테이블 생성
* 데이터베이스 생성
    ```sql
    -- my_database를 생성
    CREATE DATABASE my_database;
    ```
* 테이블 생성
    ```sql
   CREATE TABLE employees (
        id INT,
        name VARCHAR(50),
        age INT,
        department VARCHAR(50)
    );
    ```
    * `INT`는 정수형 데이터 타입, `VARCHAR`는 가변길이 문자열 데이터 타입을 의미한다.

* 주의 사항
    1. 데이터베이스 이름 중복 방지
        * 데이터베이스의 이름은 중복되지 않은 고유한 이름을 선택해야 한다.
        * 중복된 데이터베이스의 이름은 데이터베이스 간의 혼동을 발생, 데이터의 일관성과 정확성에 영향을 줄 수 있다.
    2. 테이블 구조 정확성
        * 각 열(Column)의 이름과 데이터 타입을 정확하게 지정해야 한다.
        * 데이터 타입은 해당 열에 저장될 데이터의 특성에 맞게 선택되어야 한다.
        * 잘못된 열의 이름이나 데이터 타입은 데이터의 저장과 조회에 오류를 발생시킨다.
    3. 제약 조건 설정
        * 테이블 생성시 필요한 제약조건(Constrains)을 설정해야한다.
        * 제약조건은 데이터의 무결성을 유지하기 위해 사용된다.
            * 특정열에는 `NULL`값이 들어갈 수 없도록 `NOT NULL` 제약 조건 설정 가능
            * 특정 열의 값이 다른 테이블의 값과 관계를 유지해야 하는 외래키(Foreign Key) 제약조건
            * 다양한 제약 조건 설정 가능
        * 제약 조건을 통해 데이터의 일관성과 정확성을 보장할 수 있게 된다.
    4. 보안과 권한 설정
        * 액세스 권한을 적절하게 설정하지 않으면 불법적인 접근이나 수정, 삭제 등의 보안 위협 발생 가능성이 있다.

* 네이밍 규칙
    1. 명확하고 의미 있는 이름 사용
        * 데이터베이스나 테이블의 이름은 해당 데이터의 내용이나 용도를 명확하게 나타낼수 있도록 해야 한다.
        * 직관적으로 이해하기 쉽고 다른 사용자들이 이름을 보고 내용을 파악할 수 있도록 해야 한다.
    2. 소문자와 언더스코어 사용
        * 일반적으로 데이터베이스와 테이블의 이름은 소문자와 under bar를 이용하여 작성하는 것을 권장 -> 가독성이 높아짐
    3. 짧고 간결한 이름 선택
        * 긴 이름은 코딩이나 쿼리 작성시 번거로움을 초래할 가능성이 있음
        * 필요한 내용을 충분히 담고 있는 짧은 이름을 선택하여 짧고 간결하면서 명확한 의미를 전달할 수 있어야 한다.
    4. 복수형 사용
        * 테이블 이름은 테이블이 담고 있는 데이터의 복수형으로 작성하는 것을 권장
    5. 일관성 유지
        * 데이터베이스와 테이블의 이름을 일관성 있게 작성하는 것이 중요
        * 비슷한 유형의 테이블은 비슷한 네이밍 페턴을 따르는 것을 권장
        * 데이터베이스 구조를 이해하기 쉽고 일관성 있는 쿼리 작성이 가능해 진다.
    6. 예약어 피하기
        * 데이터베이스 시스템에서 사용되는 예약어는 테이블 이름으로 사용해서는 안된다.
        * 예약어를 사용하면 오류가 발생할 수 있기 때문에 예약어는 피하고 대체어를 사용하는것을 권장

```sql
-- 데이터 베이스 생성
CREATE DATABASE mydatabase;

-- 테이블 생성
CREATE TABLE customers (
  -- 여기부터는 column을 정의
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  email VARCHAR(100),
  phone_number VARCHAR(20)
);

-- 테이블 제약 조건 추가
CREATE TABLE orders (
  -- order 테이블을 생성하고 Forign Key 제약조건을 추가
  order_id INT PRIMARY KEY,
  order_date DATE,
  order_amount DECIMAL(10, 2),
  customer_id INT,
  -- orders 테이블의 customer_id열은 customers테이블의 customer_id열과 연결
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 테이블 인덱스 추가
-- products 테이블의 product_name열에 인덱스를 추가
CREATE INDEX idx_product_name ON products (product_name);
```

## 데이터 입력과 조회
* 데이터 입력
    ```sql
    -- 형태
    INSERT INTO 테이블명 (열1, 열2, 열3, ...)
    VALUES (값1, 값2, 값3, ...);

    INSERT INTO employees (first_name, last_name, age, department)
    VALUES ('John', 'Doe', 30, 'Sales');
    ```
* 데이터 조회
    ```sql
    -- 형태
    SELECT 열1, 열2, 열3, ...
    FROM 테이블명;

    SELECT first_name, last_name, department
    FROM employees;
    ```
* 주의 사항
    1. 데이터 유효성 검사
        * 데이터를 입력하기 전에 유효성 검사를 해야 한다.
        * 데이터베이스 스키마에 정의된 제약 조건을 준수하고 테이터 타입, 길이, 형식, 등의 유효성 확인
        * 잘못된 데이터 입력시 데이터의 무결성이 손상될 수 있다.
    2. 중복 데이터 처리
        * 중복된 데이터는 피해야 한다. -> 효율성을 떨으뜨리기 때문
        * 데이터 입력전 중복 여부를 확인하고 필요한 조치가 필요하다.
    3. 효율적인 쿼리 작성
        * 적절한 인덱스를 활용하고, 필요한 열만 선택하여 조회하는 방법을 사용하여 실행 속도를 향상시킬수 있다.
    4. 보안
        * 인증과 권한 설정을 통해 불법적인 접근을 방지하고 데이터 노출을 예방해야 한다.
        * 민감한 정보를 다룰 때는 데이터 암호화 등의 보안 조치를 적용해야 한다.
    5. 정확한 조건 사용
        * 데이터 조회시에는 정확한 조건을 사용해야 한다.
        * 잘못된 조건을 사용하면 원하는 결과를 얻지 못하거나 부정확한 결과를 얻을 수 있다.
        * 쿼리 작성시 조건을 신중하게 검토하고 필요한 경우 조건을 조합하여 정확한 결과를 얻을 수 있도록 해야 한다.
    6. 성능 모니터링
        * 성능 이슈를 식별하고 최적화를 위해 필요한 조치를 취해야 한다.
        * 쿼리 실행 계획을 확인하고 인덱스의 사용 여부오 ㅏ효율성을 평가하는 등의 작업을 수행해야 한다.


# 데이터 필터링과 정렬
* SQL에서 데이터 필터링과 정렬은 중요한 작업이다.
* 데이터베이스에서 원하는 데이터를 선택하고, 필요한 조건에 따라 정렬하여 결과를 얻을 수 있다.
1. `WHERE`절
    * `WHERE`절은 데이터를 필터링하는데 사용된다.
        ```sql
        -- age열의 값이 30보다 큰  cutomers 테이블의 모든데이터를 가져옵니다
        SELECT *
        FROM customers
        WHERE age>30 
        ```
2. 비교 연산자
    * `WHERE`절에서 사용되는 비교 연산자에는 `=`, `<>`, `<`, `>`, `<=`, `>=` 등이 있다.
        ```sql
        SELECT *
        FROM products
        WHERE price>1000
        ```
3. 논리 연산자
    * `WHERE`절에서 논리 연산자인 `AND`, `OR`, `NOT`을 사용하여 여러 조건을 조합할 수 있다.
        ```sql
        /* age열의 값이 30보다 크고 department열의 값이 'Sales'에 해당되는
        'employees'테이블의 데이터를 반환한다. */
        SELECT *
        FROM employees
        WHERE age>30 AND department = 'Sales'
        ```
    * 이 외에도 `NAND`, `XOR`, `NOR`등 복합 논리연산자도 사용 가능
    * `LIKE`와 같이 뒤에 나오는 형태가 동일하다면 출력하는 연산자도 존재
        * `'_'` : 1글자
        * `'%'` : 들어가도 되고 안들어가도 되는 경우
        * `' '` : 공백이 있어야 하는 경우
            ```sql
            -- (공백, 1글자 이상)n City로 이루어진 name을 가진것이 조건이 된다.
            WHERE name LIKE '%_n City'
            ```
4. 정렬
    * 데이터를 정렬하기 위해 `ORDER BY`구문을 사용
        * 기본적으로 오름차순(`ASC`)로 정렬되며 내림차순(`DESC`)으로 정렬 또한 가능하다.
        ```sql
        -- name열을 오름차순으로 정렬하여 customers 테이블의 모든 데이터를 반환한다.
        SELECT *
        FROM customers
        ORDER BY name ASC
        ```
5. 다중 정렬
    * 여러 열을 기준으로 데이터를 정렬할 수 있다. 각 열은 쉼표로 구분하여 지정하며, 첫 번째 열을 기준으로 먼저 졍렬되고, 동일한 값이 있는 경우 두 번째 열을 기준으로 정렬한다.
        ```sql
        /*  category열을 오름차순으로 먼저 정렬
        동일한 category값이 있는 경우 price열을 내림차순으로 정렬 */
        SELECT *
        FROM products
        ORDER BY category ASC, price DESC
        ```
* 주의 사항
    1. 정확한 조건 사용
        * 잘못된 조건을 사용할 경우 원하는 결과가 나오지 않거나 부정확한 결과가 나옴
    2. 인덱스 활용
        * 적절한 열에 인덱스를 생성하여 데이터 검색 및 정렬 속도를 향상 시키고, 쿼리의 실행 속도를 개선할 수 있다.
    3. 조건의 순서
        * 여러 개의 조건을 사용하여 데이터를 필터링할 경우 조건의 순서에 따라 결과가 달라지므로 조건의 순서를 신중하게 결정해야 한다.
    4. 정렬의 영향
        * 정렬 기준 열이나 순서에 따라 결과가 달라질 수 있다. 조건과 마찬가지로 원하는 결과에 따라 정확하게 정렬을 해야 한다.
    5. 성능 모니터링
        * 데이터베이스의 성능 이슈를 식별하고 최적화를 위해 필요한 조치를 취해야 한다.
        * 쿼리 실행 계획을 확인하고 인덱스의 사용 여부와 효율성을 평가하는 등의 작업을 수행
    6. 데이터 양 고려
        * 대량의 데이터를 필터링하고 정렬하는 경우, 성능 문제가 발생할 수 있다.
        * 필요한 데이터만 선택하고 최소한의 정렬을 수행하여 처리 속도를 향상시키는 것이 중요
        * 필요한 경우 페이징이나 조인 등의 기술을 사용하여 데이터 처리를 최적화해야 한다.
* 네이밍 규칙
    * 네이밍 규칙은 데이터베이스의 일관성과 가독성을 유지하는데 중요한 역할
    * 명확하고 일관된 네이밍 규칙을 사용하면 데이터베이스 구조와 쿼리의 이해와 유지보수가 용이
    * 향후 작업에서 혼동과 오류를 방지
    1. 열(Column)의 네이밍
        * 열의 이름은 해당 열이 나타내는 데이터의 의미를 명확하게 표현
        * 가능한 한 간결하고 명확하게 작성. 긴이름이나 약어보다는 읽기 쉽고 이해하기 쉬운 이름을 사용하는 것을 권장
        * 열의 이름은 대소문자를 구분하는 경우가 많으며, 관례적으로 소문자와 under bar를 사용하여 작성
    2. 테이블(table) 네이밍
        * 테이블이 담고 있는 데이터의 의미를 잘 반영해야 한다.
        * 테이블의 이름은 단수형으로 작성하는 것이 일반적이다.
        * 테이블의 이름 또한 간결하고 명확하게 작성 -> 어떤 데이터를 담고 있는지 알기 쉽게
    3. 쿼리(Query) 네이밍
        * 해당 쿼리가 수행하는 작업을 간략하게 설명해야 한다.
        * 해당 쿼리의 목적이나 결과를 잘 나타내도록 작성

```sql
-- 데이터 필터링
SELECT *
FROM orders
WHERE order_amount >= 100;

-- 다중 조건 필터링
SELECT *
FROM products
WHERE category = '의류' AND price >= 5000;

-- 정렬
SELECT *
FROM customers
ORDER BY customer_name ASC;

-- 다중 열 정렬
SELECT *
FROM orders
-- 주문일자를 내림차순으로 정렬 후 주문 금액을 오름차순을 정렬
ORDER BY order_date DESC, order_amount ASC;
```