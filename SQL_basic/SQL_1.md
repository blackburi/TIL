# SQL과 데이터베이스의 기본 개념
* SQL = Structured Query Language
* SQL은 데이터베이스를 조작하고 관리하는데 사용되는 표준화된 언어이다.
    * 데이터베이스는 구조화된 데이터를 저장하고 관리하는 시스템으로, 기업이나 조직에서 중요한 정보를 보관하고 활용하는 데에 사용된다.
* SQL은 데이터베이스와 상호 작용하기 위해 사용되며 삽입, 조회, 수정, 삭제 등 다양한 직업을 수행할 수 있다.
* SQL은 직관적이고 간단한 문법으로 구성되어 있어 데이터베이스 관리에 필수적인 기술이다.

* SQL 주요 요소
    1. 데이터 정의 언어(DDL) : 데이터베이스, 테이블, 컬럼 등의 구조를 정의하는데 사용
    2. 데이터 조작 언어(DML) : 데이터를 검색하거나 조작하기 위해 사용되며 여러 구문이 존재 한다.
    3. 데이터 제어 언어(DCL) : 데이터 접근 권한을 관리하기 위해 사용되며 여러 구문이 존재 한다.

## 주석
* 주석은 SQL 내에서 다양한 설명을 넣을수 있다.
    1. `--`를 사용하는 방법 : 보통 한줄 정도의 단순한 주석을 쓸 때 사용한다.
        ```sql
        CREATE my -- 이곳은 주석입니다
        ```
    2. `/* */`를 사용하는 방법 : 여러 줄의 긴 주석을 쓸 때 사용한다.
        ```sql
        /* 이곳부터 주석 시작입니다
        CREATE my
        이곳 주석이 마지막입니다. */
        ```

## 데이터 정의 언어(DDL)
* 데이터베이스는 데이터의 구조와 유지, 관리를 담당
* 효율적인 데이터 접근 및 관리를 위해 인덱스 , 트랜잭션, 보안 등의 기능을 제공
* 데이터베이스의 종류
    * 관계형 데이터베이스(RDBMS) : 행과 열이 있는것
    * 비관계형 데이터베이스(NoSQL) : 행과 열이 없는것
* 데이터 정의 언어(DDL)은 데이터베이스의 구조를 정의하고 조작하는 역할
1. 데이터 베이스의 생성(`CREATE DATABASE`)
    ```sql
    -- 'my_database'라는 이름의 데이터베이스를 생성한다.
    CREATE DATABASE my_database;
    ```
2. 테이블 생성(`CREATE TABLE`)
    ```sql
    /* "employees"라는 이름의 테이블을 생성하는 구문이다. 이 테이블에는 id, name, age, department라는 열(Column)이 정의되어 있다. 각열의 데이터 타입과 크기도 함께 정의되어 있다. */
    CREATE TABLE employees (
        id INT,
        name VARCHAR(50),
        age INT,
        department VARCHAR(50)
    );
    ```
3. 테이블 변경(`ALTER TABEL __ ADD __`) : 열(Column)추가
    ```sql
    /* "employees"테이블에 "salary"라는 열을 추가하는 구문이다. 열의 데이터 타입과 크기도 함께 정의되어 있다.*/
    ALTER TABLE employees
    ADD COLUMN salary DECIMAL(10, 2);
    ```
4. 테이블 삭제
    ```sql
    /* employees 테이블을 삭제하는 구문이다. 해당 테이블과 관련된 모든 데이터도 함께 삭제된다.*/
    DROP TABLE employees;
    ```


## 데이터 조작 언어(DML)
* 데이터 조작 언어(DML)는 데이터베이스에서 데이터를 검색하거나 조작하는 역할을 한다.
1. 데이터 삽입(`INSERT INTO`)
    ```sql
    /* employees 테이블에 새로운 데이터를 삽입하는 구문
    id, name, age, department 열에 해당하는 값들을 지정하여 데이터 삽입 */
    INSERT INTO employees (id, name, age, department)
    VALUES (1, 'John Doe', 30, 'IT')
    ```
2. 데이터 조회(`SELECT _ FROM _`)
    ```sql
    /* '*'는 모든 열을 의미하며
    데이터 베이스에서 모든 행과 열을 반환한다. */
    SELECT * FROM employees;
    ```
3. 테이블 데이터 변경(`UPDATE`)
    ```sql
    /* 테이블의 UPDATE를 진행하는데 에러가 발생했다면 safe mode를 초기화 세팅해 주면 된다.
    에러가 발생하면 이 쿼리를 실행해 보는것을 권장 */
    --safe mode 초기화 세팅 방법
    SET sql_safe_updates = 0;

    -- id = 1234인 데이터의 age값을 35로 update
    UPDATE employees
    SET age = 35
    WHERE id = 1234
    ```
4. 테이블 데이터 삭제(`DELETE`)
    ```sql
    -- 먼저 SELECT문을 통해 지우고자 하는 레코드를 조회 후 삭제하는것을 권장
    SELECT * FROM 'employees';

    -- 테이블에 id = 1234인 행을 제거한다.
    DELETE FROM employees WHERE id = 1234;
    ```


## 데이터 제어 언어(DCL)
* 데이터 제어 언어(DCL)는 데이터베이스에 대한 접근 권한을 관리하는 역할을 한다.
1. 사용자에게 권한 부여(`GRANT`)
    ```sql
    /* employees테이블에 대한 SELECT와 INSERT 권한을 user1에게 부여
    user1은 해당 테이블에서 데이터를 조회하고 삽입할 수 있게 된다. */
    GRANT SELECT, INSERT ON employees TO user1;
    ```
2. 사용자의 권한 취소(`REVOKE`)
    ```sql
    /* employees 테이블에 대한 UPDATE 권한을 user2로부터 취소한다.
    user2는 해당 테이블에서 데이터를 UPDATE할수 없게 된다. */
    REVOKE UPDATE ON employees FROM user2;
    ```
3. 롤(Role) 생성(`CREATE`)
    ```sql
    /* 'manager'라는 이름의 role을 생성하는 구문이다.
    role은 여러 사용자에게 동일한 권한을 일괄적으로 부여하기 위해 사용한다. */
    CREATE ROLE manager;
    ```
4. 롤(Role)에 권한 부여(`GRANT`)
    ```sql
    /* 'manager' role에게 employees 테이블에 대한 SELECT와 UPDATE 권한을 부여
    manager role의 모든 사용자는 해당 테이블에서 데이터를 조회하고 업데이트 할수 있게 된다.*/
    GRANT SELECT, UPDATE ON employees TO manager;
    ```