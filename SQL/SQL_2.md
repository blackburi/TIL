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
        * 
    2. 중복 데이터 처리
    3. 효율적인 쿼리 작성
    4. 보안
    5. 정확한 조건 사용
    6. 성능 모니터링


# 데이터 필터링과 정렬


