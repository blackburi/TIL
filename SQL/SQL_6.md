# 인덱스와 성능 최적화
* 인덱스와 성능 최적화는 데이터베이스의 성능을 향상시키는데 중요한 역할을 한다.

## 인덱스의 개념과 종류
* 인덱스는 데이터베이스에서 데이터를 빠르게 검색하기 위한 구조로, 특정 열 또는 열의 조합에 대한 정렬된 데이터 구조이다.
* 인덱스는 데이터베이스의 성능을 향상시키는데 중요한 역할을 하고, 일반적으로 인덱스는 테이블의 열에 대한 포인터를 제공하여 데이터를 더 빠르게 찾을 수 있도록 도와준다.
* 인덱스의 종류
    1. B-트리 인덱스
        * B-트리 인덱스는 가장 일반적으로 사용되는 인덱스 종류
        * 데이터베이스에서 기본적으로 제공되며, 이진트리의 변형인 B-트리 구조를 사용하여 데이터를 저장하고 검색한다.
        * B-트리 인덱스는 데이터의 정렬 순서를 유지하며, 범위 검색과 정렬된 결과 반환에 효율적이다.
            ```sql
            -- employees 테이블 생성
            CREATE TABLE employees (
                id INT PRIMARY KEY,
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            )

            -- last_name 컬럼에 대한 B-트리 인덱스 생성
            CREATE INDEX idx_last_name ON employees(last_name)
            ```
    2. 해시 인덱스
        * 해시 인덱스는 해시 함수를 사용하여 데이터를 저장하고 검색한다.
        * 해시 인덱스는 정확한 일치 검색에 효율적이지만, 범위 검색이나 정렬된 결과 반환에는 적합하지 않을 수 있다.
            ```sql
            -- employees 테이블 생성
            CREATE TABLE employees (
                id INT PRIMARY KEY,
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            )

            -- id 컬럼에 대한 해시 인덱스 생성
            CREATE INDEX idx_id ON employees(id) USING HASH
            ```
    3. 클러스터드 인덱스
        * 클러스터드 인덱스는 테이블의 데이터를 인덱스의 순서에 따라 물리적으로 정렬한다.
        * 클러스터드 인덱스는 데이터의 논리적인 순서와 물리적인 저장 순서를 일치시키므로, 범위 검색과 정렬된 결과 반환에 매우 효율적이다.
        * 하나의 테이블에는 하나의 클러스터드 인덱스만 생성할 수 있다.
            ```sql
            -- employees 테이블 생성
            CREATE TABLE employees (
                id INT PRIMARY KEY,
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            )

            -- id 컬럼을 기준으로 클러스터드 인덱스 생성
            CREATE CLUSTERED INDEX idx_id ON employees(id)
            ```
    4. 비클러스터드 인덱스
        * 비클러스터드 인덱스는 테이블의 데이터를 인덱스의 순서에 따라 물리적으로 정렬하지 않는다.
        * 비클러스터드 인덱스는 테이블의 열이나 열의 조합에 대한 별도의 데이터 구조를 생성하며, 데이터의 위치를 가리키는 포인터를 포함한다.
            ```sql
            -- employees 테이블 생성
            CREATE TABLE employees (
                id INT PRIMARY KEY,
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                age INT,
                department VARCHAR(50)
            )

            -- last_name 컬럼에 대한 비클러스터드 인덱스 생성
            CREATE NONCLUSTERED INDEX idx_last_name ON employees(last_name)
            ```
* 주의 사항
    * 인덱스는 데이터베이스의 성능을 향상시키는데 중요한 역할을 한다. 하지만 인덱스를 적절히 설계해야하며, 인덱스를 과도하게 생성하는 것은 오히려 성능을 저하시킬수 있다.
    * 인덱스를 설계할 때는 데이터의 특성과 접근 패턴을 고려하여 적절한 열 또는 열의 조합을 선택해야 한다.


## 인덱스의 효과와 성능 최적화 기법
* 인덱스의 효과
    * 데이터 검색 속도 향상 : 데이터베이스에서 데이터를 빠르게 검색하기 위한 구조로, 인덱스를 사용하면 데이터베이스 엔진은 인덱스를 통해 데이터를 직접 찾아내므로 검색 속도가 향상된다.
    * 정렬된 결과 반환 : 인덱스는 데이터를 정렬된 상태로 유지하기 때문에, 정렬된 결과를 반환하는 쿼리의 성능도 향상된다.
    * 범위 검색의 효율적인 처리 : 인덱스를 사용하면 특정 범위에 속하는 데이터를 효율적으로 찾을 수 있어 범위 검색의 성능이 향상된다.
* 성능 최적화 기법
    1. 적절한 인덱스 설계 : 인덱스를 설계할 때는 데이터의 특성과 접근 패턴을 고려해야 한다. 자주 검색되는 열이나 조건으로 사용되는 열에 인덱스를 생성하는 것이 좋다. 또한, 인덱스의 크기를 최소화하고 중복된 인덱스를 제거하여 성능을 최적화할 수 있다.
        ```sql
        -- employees 테이블 생성
        CREATE TABLE employees (
            id INT PRIMARY KEY,
            last_name VARCHAR(50),
            first_name VARCHAR(50),
            age INT,
            department VARCHAR(50)
        )

        -- 적절한 인덱스 설계
        -- 1. id 컬럼에 클러스터드 인덱스 생성
        CREATE CLUSTERED INDEX idx_id ON employees(id)

        -- 2. last_name 컬럼에 비클러스터드 인덱스 생성
        CREATE NONCLUSTERED INDEX idx_last_name ON employees(last_name)

        /* 'id'컬럼에는 클러스터드 인덱스를 생성하여 데이터 행을 인덱스의 정렬 순서와 동일하게 유지
        'last_name'컬럼에는 비클러스터드 인덱스를 생성하여 데이터 행을 별도로 유지
        -> 검색 성능을 최적화 한다.*/
        ```
    2. 인덱스 통계 유지 : 데이터베이스는 쿼리 실행 계획을 수립할 때 인덱스의 통계 정보를 사용한다. 따라서 인덱스의 통계 정보를 주기적으로 업데이트하여 최신 정보를 유지해야 한다.
        ```sql
        -- 인덱스 통계 유지
        -- employees 테이블의 인덱스 통계 갱신
        UPDATE STATISTICS employees

        /* 데이터베이스는 최신의 인덱스 통계를 유지하고
        쿼리 옵티마이저는 정확한 실행 계획을 수립할 수 있다.*/
        ```
    3. 인덱스의 갱신 비용 고려 : 인덱스를 생성하면 데이터의 갱신 작업(삽입, 수정, 삭제)에 대한 성능 저하가 발생할 수 있다. 따라서 인덱스의 갱신 비용을 고려하여 필요한 인덱스만 생성해야 한다.
        ```sql
        -- 인덱스 갱신 비용 고려
        -- employees 테이블의 데이터 삽입 작업 후 인덱스 갱신
        INSERT INTO employees (id, last_name, first_name, age, department)
        VALUES (1, 'Smith', 'John', 30, 'Sales')

        -- 인덱스 갱신
        UPDATE STATISTICS employees

        /* 'employees'테이블에 데이터를 삽입한 후 적절한 시점에 인덱스를 갱신
        삽입 작업 후에는 인덱스의 갱신을 고려하여 인덱스 통계를 갱신 */
        ```
    4. 쿼리의 재작성과 최적화 : 쿼리의 실행 계획을 분석하고 쿼리를 재작성하여 인덱스를 최대한 활용할 수 있도록 해야 한다. 불필요한 조인이나 조건식을 제거하고, 인덱스 스캔을 인덱스 범위 스캔으로 변경하는 등의 최적화 작업을 수행할 수 있다.
        ```sql
        -- last_name 컬럼을 이용한 검색 쿼리의 재작성과 최적화
        SELECT * FROM employees WHERE last_name = 'Smith'
        -- 첫 번째 쿼리는 인덱스를 사용하지 않고 전체 테이블을 스캔하여 검색

        -- 인덱스를 활용한 검색 쿼리의 재작성과 최적화
        SELECT * FROM employees WITH(INDEX(idx_last_name)) WHERE last_name = 'Smith'
        -- 두 번째 쿼리에서는 WITH문을 사용하여 'last_name'컬럼에 대한 비클러스터드 인덱스를 명시적으로 지정하여 검색기능 향상
        ```


## 쿼리 실행 계획과 성능 모니터링
* 쿼리 실행 계획 : 데이터베이스 엔진이 쿼리를 어떻게 실행할지를 결정하는 계획
* 성능 모니터링 : 데이터베이스틔 성능을 지속적으로 모니터링하고 문제를 해결하는 과정

### 쿼리 실행 계획
* 쿼리 옵티마이저
    * 데이터베이스 엔진은 쿼리를 최적화하는 옵티마이저를 가지고 있다. 옵티마이저는 쿼리 실행 계획을 수립하는데, 쿼리의 테이블과 인덱스 통계 정보, 데이터 분포 등을 고려하여 가장 효율적인 실행 계획을 선택한다.
* 실행 계획 확인
    * 실행 계획은 `EXPLAIN`이라는 명령을 사용하여 확인할 수 있다. 실행 계획을 확인하면 쿼리가 어떤 인덱스를 사용하고, 어떤 조인 방식을 사용하는지 등을 알 수 있다. 실행 계획을 분석하여 쿼리의 성능을 개선할 수 있다.
* 쿼리 실행 계획 확인
    ```sql
    -- 'employees'테이블에서 'department'컬럼이 'Sales'인 데이터를 검색하는 쿼리의 실행계획 확인
    EXPLAIN SELECT * FROM employees WHERE department = 'Sales'
    ```

### 성능 모니터링
* 성능 지표 모니터링
    데이터베이스의 성능을 모니터링하기 위해 CPU 사용량, 메모리 사용량, 디스크 I/O 등의 성능 지표를 모니터링한다. 이러한 성능 지표를 모니터링하여 성능 저하의 원인을 파악하고 조치할 수 있다.
* 쿼리 성능 모니터링
    * 성능 모니터링 도구를 사용하여 실행되는 쿼리의 성능을 모니터링할 수 있다. 쿼리의 실행 시간, I/O 비용, 인덱스 사용 여부 등을 확인하여 성능 저하의 원인을 찾고 최적화할 수 있다.
* 쿼리 실행 계획 추적
    * 쿼리 실행 계획을 추적하여 어떤 쿼리가 성능 저하를 일으키는지 파악할 수 있다. 쿼리 실행 계획 추적을 통해 성능 문제를 가진 쿼리를 식별하고 최적화할 수 있다.
* 성능 모니터링
    ```sql
    -- 성능 모니터링
    -- employees 테이블에서 department가 'Sales'인 데이터를 검색하는 쿼리 실행 시간 측정
    -- SET STATISTICS TIME ON 명령어로 성능 모니터링 시작
    SET STATISTICS TIME ON

    -- 쿼리 실행
    SELECT * FROM employees WHERE department = 'Sales';

    -- SET STATISTICS TIME OFF 명령어로 성능 모니터링 종료
    SET STATISTICS TIME OFF
    ```
