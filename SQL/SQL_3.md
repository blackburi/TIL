# 관계형 데이터베이스와 조인
* 관계형 데이터베이스는 데이터를 테이블로 구조화하여 저장하고 관리하는 시스템
* 조인은 두 개 이상의 테이블을 연결하여 데이터를 조회하는 방법
    * 내부 조인 : 일치하는 값만 반환
    * 외부 조인 : 일치하지 않는 값도 포함하여 결과를 반환
    * 다중 조인 : 세 개 이상의 테이블을 연결하여 데이터를 조회
* 서브쿼리 : 주 쿼리의 결과에 영향을 주는 임시 쿼리
* 이러한 것을 이용하여 데이터베이스에서 필요한 정보를 효율적으로 추출하고 관리할 수 있다.

## 관계형 데이터베이스의 개념
* 관계형 데이터베이스
    * 데이터를 테이블 형태로 구조화하여 저장하고 관리하는 데이터베이스 시스
    * 테이블 간의 관계를 활용하여 데이터를 구성
    * 데이터의 일관성과 무결성을 보장
    * 테이블은 열(column)과 행(row)으로 구성
        * 열(column) : 데이터의 속성
        * 행(row) : 실제 데이터 레코드
* 관계형 데이터베이스는 SQL을 사용하여 데이터를 조작하고 조회한다.
    * SQL = Structured Query Language
    * SQL은 데이터 베이스에 대한 작업을 수행하기 위한 표준화된 쿼리 언어
        * 데이터의 삽입, 업데이트, 삭제, 검색 등 다양한 작업 수행
* 테이블 간의 관계는 기본 키(Primary Key)와 외래 키(Foreign Key)를 사용하여 정의
    * 기본 키 : 각 행을 고유하게 식별하기 위한 열로 테이블의 첫 번째 열로 정의
    * 외래 키 : 다른 테이블의 기본 키와 연결되는 열로, 테이블 간의 관계를 설정하는데 사용
* 관계형 데이터베이스의 장점
    * 데이터의 일관성과 무결성 유지
    * 데이터의 중복을 최소화하여 효율적인 데이터 관리가 가능
    * SQL을 사용하여 데이터를 다룰수 있어 다양한 쿼리와 조작을 통해 원하는 정보를 추출하고 처리 가능
* 관계형 데이터베이스의 개념을 위한 예시 코드
    ```sql
    -- 'Employees' 테이블 생성
    CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    );

    -- 'Departments' 테이블 생성
    CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
    );

    -- 'Employees' 테이블에 데이터 삽입
    INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID)
    VALUES (1, 'John', 'Doe', 1),
           (2, 'Jane', 'Smith', 2),
           (3, 'David', 'Johnson', 1),
           (4, 'Sarah', 'Williams', 2);

    -- 'Departments' 테이블에 데이터 삽입
    INSERT INTO Departments (DepartmentID, DepartmentName)
    VALUES (1, 'Sales'),
           (2, 'Marketing');

    -- 'Employees' 테이블과 'Departments' 테이블을 조인하여 데이터 조회
    SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
    FROM Employees
    JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
    ```
    1. 'Employees', 'Departments' 테이블을 생성
    2. 두 테이블을 'DepartmentID'를 기준으로 연결하고 해당하는 열을 선택하여 조회
        * 이를 통해 각 직원의 ID, 이름, 소속 부서명을 조회할 수 있다.

## 내부 조인과 외부 조인
* 내부 조인(inner join)과 외부 조인(outer join)은 관계형 데이터베이스에서 테이블 간의 연결과 데이터 조회를 위해 사용되는 두 가지 조인 방법
    * 내부 조인(inner join) : 내부 조인은 두 개 이상의 테이블을 연결하여 일치하는 값을 기준으로 데이터를 조회하는 방법이다. 내부 조인은 연결된 테이블들 간에서 일치하는 값을 가진 행만을 결과로 반환한다. 즉 조인하는 테이블 간에 일치하는 값이 없는 행은 제외된다.
        ```sql
        -- 'Employees' 테이블과 'Departments' 테이블을 내부 조인하여 데이터 조회
        SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
        /* 'Employees' 테이블과 'Departments' 테이블을 내부 조인하여 일치하는 DepartmentID를 기준으로 데이터를 조회
        조인 결과로는 직원의 ID, 이름, 소속 부서명이 반환된다. */
        ```
    * 외부 조인(outer join) : 외부 조인은 내부 조인과느 ㄴ달리 일치하는 값이 없는 행까지도 결과에 포함시키는 조인 방법이다. 외부 조인은 연결된 테이블 중에서 일치하는 값이 없는 행을 기준으로 결과를 생성한다. 이를 통해 일치하지 않는 데이터도 포함하여 조회할 수 있다.
    * 왼쪽 외부 조인(left outer join) : 왼쪽 외부 조인은 왼쪽 테이블을 기준으로 우측 테이블과 조인하여 일치하는 값이 없어도 왼쪽 테이블의 모든 행을 결과에 포함시킨다. 우측 테이블의 일치하는 갑이 없는 경우 NULL 값이 할당된다.
        ```sql
        -- 'Employees' 테이블과 'Departments' 테이블을 왼쪽 외부 조인하여 데이터 조회
        SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
        /* 'Employees' 테이블을 기준으로 'Departments' 테이블을 왼쪽 외부 조인하여 데이터를 조회
        왼쪽 테이블인 'Employees' 테이블의 모든행이 결과에 포함
        우측 테이블인 'Departments' 테이블과 일치하는 값이 없는 경우에는 NULL값을 할당한다. */
        ```
    * 오른쪽 외부 조인(right outer join) : 오른쪽 외부 조인은 오른쪽 테이블을 기준으로 왼쪽 테이블과 조인하여 일치하는 값이 없어도 오른쪽 테이블의 모든 행을 결과에 포함시킨다. 왼쪽 테이블의 일치하는 값이 없는 경우에는 NULL값이 할당된다.
        ```sql
        -- 'Employees' 테이블과 'Departments' 테이블을 오른쪽 외부 조인하여 데이터 조회
        SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        RIGHT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
        /* 'Employees' 테이블을 기준으로 'Departments' 테이블을 오른쪽 외부 조인하여 데이터를 조회
        오른쪽 테이블인 'Departments' 테이블의 모든 행이 결과에 포함
        왼쪽 테이블인 'Employees' 테이블과 일치하는 값이 없는 경우에는 NULL값을 할당한다. */
        ```
    * 전체 외부 조인(full outer join) : 전체 외부 조인은 왼쪽 테이블과 오른쪽 테이블 모두의 일치하는 값과 일치하지 않는 값을 모두 결과에 포함시킨다. 따라서 왼쪽과 오른쪽 테이블의 모든 행을 결과로 반환하며, 일치하지 않는 경우에는 NULL값이 할당된다.
        ```sql
        -- 'Employees' 테이블과 'Departments' 테이블을 전체 외부 조인하여 데이터 조회
        SELECT Employees.EmployeeID, Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
        /* 두 테이블을 전체 외부 조인하여 데이터를 조회
        양쪽 테이블의 모든 행이 결과에 포함되며, 일치하는 값이 없는 경우 NULL값을 할당한다. */
        ```

## 다중 조인과 서브 쿼리
* 다중 조인(Multiple Joins)과 서브 쿼리(Subquery)는 관계형 데이터베이스에서 데이터를 연결하고 조회하는데 사용
    * 다중 조인(Multiple Joins) : 다중 조인은 세 개 이상의 테이블을 연결하여 데이터를 조회하는 방법이다. 다중 조인은 여러 테이블 간의 관계를 이해하고 조인 조건을 정확하게 설정하여 데이터를 연결한다. 다중 조인을 사용하면 복잡한 데이터 구조에서 필요한 정보를 효율적으로 추출할 수 있다.
        ```sql
        /* 'Customers', 'Orders', 'OrderDetails'라는 세 개의 테이블을 다중 조인하여 데이터를 조회
        'Customers' 테이블과 'Orders' 테이블을 'CustomerID' 열을 기준으로 내부 조인
        그 결과를 'OrderDetails' 테이블과 'OrderID'열을 기준으로 다시 내부 조인 */
        SELECT *
        FROM Customers
        JOIN Orders ON Customers.CustomerID = Orders.CustomerID
        JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
        ```
    * 서브 쿼리(Subquery) : 서브 쿼리는 SQL 문장 내에 사용되는 중첩된 쿼리이다. 서브쿼리는 주로 다른 쿼리의 조건이나 결과를 기반으로 보조적인 데이터를 조회하거나 조건을 설정하는 데 사용된다. 주쿼리(외부쿼리)와 서브쿼리(내부쿼리)는 서로 독립적으로 실행되며, 서브쿼리의 결과를 기반으로 주쿼리의 동작이 수행된다. 서브쿼리는 `SELECT`, `FROM`, `WHERE`, `HAVING` 절 등 다양한 위치에서 사용할 수 있다. 서브쿼리를 사용하면 복잡한 조건과 데이터 처리를 수행할 수 있으며, 집계 함수나 비교 연산자를 활용하여 원하는 결과를 도출할 수 있다.
        ```sql
        /* 'Products' 테이블에서 'SupplierID' 열의 값이 'Suppliers' 테이블에서 'Country'가 'USA'인 'SupplierID'와 일치하는 경우 'ProductName'을 조회
        서브 쿼리는 WHERE 절 내에 사용되었다.
        'Suppliers' 테이블에서 'Country'가 'USA'인 'SupplierID'를 서브쿼리로 활용하여 'Products' 테이블에서 필터링을 수행
        서브쿼리를 사용하면 다른 쿼리의 조건이나 결과를 기반으로 원하는 데이터를 조회하거나 조건 설정이 가능해진다. */
        SELECT ProductName
        FROM Products
        WHERE SupplierID IN (SELECT SupplierID FROM Suppliers WHERE Country = 'USA')
        ```
