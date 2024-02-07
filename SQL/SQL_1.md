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
    * 관계형 데이터베이스(RDBMS)
    * 비관계형 데이터베이스(NoSQL)
* 데이터 정의 언어(DDL)은 데이터베이스의 구조를 정의하고 조작하는 역할

### 데이터베이스 생성
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
5. 테이블 데이터 삽입(`INSERT INTO __ () VALUES ()`)
    ```sql
    /* 새로운 레코드와 값을 추가하였다 */
    INSERT INTO 'employees' ('id', 'name', 'age', 'department') VALUES (1234, 'John', 20, 'MX');
    ```
6. 테이블 데이터 삭제(`DELETE`)
    ```sql
    -- 먼저 SELECT문을 통해 지우고자 하는 레코드를 조회 후 삭제하는것을 권장
    SELECT * FROM 'employees';

    -- 테이블에 id = 1234인 행을 제거한다.
    DELETE FROM employees WHERE id = 1234;
    ```
(https://www.whatap.io/ko/blog/141/)

## 데이터 조작 언어(DML)


## 데이터 제어 언어(DCL)



