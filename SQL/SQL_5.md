# 데이터 수정과 삭제

## 데이터 수정과 트랜잭션
* 데이터 수정
    * 데이터베이스의 레코드를 변경하는 작업을 수행하기 위해 `INSERT`, `UPDATE`, `DELETE`문을 사용할 수 있다.
        ```sql
        -- 'Sales'부서에 속하는 직원들의 급여를 5000으로 수정
        update employees
        set salary = 5000
        where department = 'Sales'
        ```
    * 데이터 수정은 데이터베이스의 상태를 변경하고, 필요에 따라 데이터의 일부 또는 전체를 수정할 수 있다.
* 트랜잭션 : 데이터 수정 작업을 논리적인 작업 단위로 묶어서 데이터의 일관성과 안정성을 보장하는 개념
    * 원자성(Atomicity), 일관성(Consistency), 격리성(Isolation), 지속성(Durability)의 특성을 가지며 이것을 ACID라고 한다.
    * 원자성(Atomicity) : 태랜잭션 내의 모든 작업이 전부 성공하거나 전부 실패하여 아무런 변화가 없는 상태를 보장하는 것을 의미한다. 트랜잭션 내에서 하나의 작업이라도 실패하면 이전 상태로 롤백되어야 한다.
    * 일관성(Consistency) : 트랜잭션이 실행되기 전과 후에 데이터베이스의 일관성이 유지되는 것을 의미한다. 트랜잭션은 데이터베이스의 무결성 규칙을 준수하고 데이터의 일관성을 유지해야 한다.
    * 격리성(Isolation) : 동시에 실행되는 여러 트랜잭션이 서로 영향을 주지 않고 독립적으로 실행되는 것을 의미한다. 한 트랜잭션이 다른 트랜잭션의 작업에 영향을 주지 않도록 격리 수준을 설정할 수 있다.
    * 지속성(Durability) : 트랜잭션이 성공적으로 완료되면 그 결과를 영구적으로 유지되는 것을 의미한다. 데이터베이스 시스템은 트랜잭션의 결과를 안정적으로 디스크에 기록하여 지속성을 보장해야 한다.
    ```sql
    -- 두 개의 계좌 간에 100달러를 이체하는 작업을 단일 트랜잭션으로 묶음
    -- 트랜잭션 시작
    start transaction
    -- update문을 이용하여 계좌의 잔액을 수정
    update accounts set balance = balance - 100 where account_id = 1234
    update accounts set balance = balance + 100 where account_id = 5678
    -- commit으로 트랜잭션 완료
    commit
    ```
    ```sql
    -- 트랜잭션 시작
    start transaction
    -- 상품의 재고 5개 감소한 것으로 변경
    update inventory set quantity = quantity - 5 where product_id = 123
    -- 주문 상태를 'Shipped'로 변경
    update orders set status = 'Shipped' where order_id = 456
    -- 하지만 rollback을 사용하여 트랜잭션을 롤백하여 이전상태로 되돌린다.
    rollback
    ```

## 데이터 삭제와 롤백
* 데이터베이스에서 불필요한 데이터를 삭제하여 공간을 절약하고 데이터베이스의 성능을 향상시킬수 있다.
    * `DELETE`문을 사용하여 데이터를 삭제할 수 있다.
        ```sql
        -- orders에서 order_id = 123 을 삭제
        delete from orders where order_id = 123
        ```
        ```sql
        -- 'HR'부서에서 50세 이상인 직원들을 삭제하는 작업 수행
        delete from employees where department = 'HR' and age > 50
        ```
        * `DELETE`문은 조건에 맞는 레코드를 삭제하는 작업을 수행한다.
        * 조건을 지정하지 않으면 모든 레코드가 삭제될 수 있으므로 주의가 필요하다.
        * `DELETE`문을 실행하기 전에 데이터의 백업을 수행하는 것이 좋다.
* 룰백 : 트랜잭션 내에서 작업이 실패하거나 오류가 발생할 경우 이전 상태로 복원하는 것
    * 데이터의 무결성과 일관성을 유지하는데에 도움을 준다.
    ```sql
    -- 트랜잭션 시작
    start transaction
    -- product_id = 456인 제품과 관련된 데이터를 삭제하는 작업
    delete from products where product_id = 456
    delete from inventory where product_id = 456
    -- 작업 중 오류가 발생한다면 이전 상태로 롤백
    rollback
    ```
    ```sql
    -- 트랜잭션 시작
    start transaction
    -- 데이터 삭제 : 2024-02-11 이전에 생성된 주문과 주문 상세 항목 삭제 
    delete from orders
    where order_date < '2024-02-11'
    delete from order_items
    where order_id in (select order_id
                        from orders
                        where order_date < '2024-02-11')
    -- 롤백하여 이전상태로 되돌린다.
    rollback
    ```