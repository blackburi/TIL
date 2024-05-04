# Java 기본 문법

## Java 기본
* main method
    * 실행 명령인 java를 실행 시 가장 먼저 호출 되는 부분
    * 만약, Application에서 `main()` 메서드가 없다면 절대로 실행 될 수 없음
    * Application의 시작 -> 특정 클래스의 `main()` 실행
    * 형태 (고정된 형태)

        ```java
        public static void main(String [ ] args) { }
        ```
* 출력문
    * `print()` : 그대로 출력
    * `println()` : 출력 + 한줄 띄어씀
    * `printf()` : 형식에 맞춰서 출력
        * `%d` : 정수
        * `%f` : 실수
        * `%c` : 문자
        * `%s` : 문자열
    * 출력 예시

        ```java
        System.out.print("Hello World");

        // \n을 사용하면 줄바꿈이 된다.
        System.out.print("Hello World\n");

        System.out.println("Hello World!!!");
        System.out.println("Hello World!!!");

        // \를 1개사용하면 출력되지 않는다 -> 의미를 갖는 기호이기 때문에
        // \는 기호를 출력하기 위해 사용된다.
        System.out.println("\\"); // \ 1개 출력
        System.out.println("\""); // " 1개 출력

        // %는 값이 들어갈 자리
        System.out.printf("%d\n", 10); // 정수 10진수
        System.out.printf("%o\n", 10); // 정수 8진수
        System.out.printf("%x\n", 10); // 정수 16진수(소문자)
        System.out.printf("%X\n", 10); // 정수 16진수(대문자)

        System.out.printf("%4d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지
        System.out.printf("%-4d\n", 10); // 4칸을 확보한 뒤 왼쪽부터 차지
        System.out.printf("%04d\n", 10); // 4칸을 확보한 뒤 오른쪽부터 차지(남는 부분은 0으로 채워 넣는다.)

        System.out.printf("%f\n", 10.12345); // 실수 6자리까지 출력
        System.out.printf("%.2f\n", 10.12345); // 실수 소수점 아래 2번째까지 반올림 하여 출력
        System.out.printf("%.2f\n", 10.125);

        System.out.printf("%s", "싸피"); // 문자열
        System.out.printf("%c", "A"); // 문자

        /*
        Hello WorldHello World
        Hello World!!!
        Hello World!!!
        \
        "
        10
        12
        a
        A
            10
        10
        0010
        10.123450
        10.12
        10.13
        싸피A
        */
        ```


## 변수와 자료형
* 변수(Variable)
    * 데이터를 저장할 메모리의 위치를 나타내는 이름
    * 메모리 상에 데이터를 보관할 수 있는 공간을 확보
    * 적절한 메모리 공간을 확보하기 위해서 변수의 타입 등장
    * `=`를 통해서 CPU에게 연산작업을 의뢰
    * 대소문자를 구분한다.
    * 공백은 허용되지 않는다.
    * 숫자로 시작할수 없다.
    * `$`와 `_`를 변수 이름에 사용할 수 있다. 이외의 특수문자는 허용되지 않는다.
    * 예약어(keyword : 자바문법을 위해서 미리 지정되어 있는 단어)는 사용할 수 없다.
    * 합성어의 경우 주로 camelCase를 활용한다.
    * 한글을 이용한 변수 작명 가능(권장X)
* 자료형 (Data Type)
    1. 기본 자료형 : 미리 정해진 크기의 Memory Size 표현, 변수 자체에 값 저장
    2. 참조 자료형
* 선언
    * `자료형 변수명;`
    * ex) `int age;`, `String name;`
* 저장(할당)
    * `변수명 = 저장할 값;`
    * ex) `age = 30;`, `name='철수';`
* 초기화
    * `자료형 변수명 = 저장할 값;`
    * ex) `int age = 30;`
* 형 변환 (Type Casting)
    * 자동(묵시적, 암묵적) 형변환이 가능한 방향

        ![java_01_type_casting](../image/Java/01/java_01_type_casting.png)

    * 데이터 형 변환
        * 묵시적(암묵적) 형변환 : Implicit Casting
            * 범위가 넓은 데이터 형에 좁은 데이터 형을 대입하는 것
            * ex) `byte b = 100 ; int i = b ;`
        * 명시적 형변환 : Explicit Casting
            * 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것
            * 형 변환 연산자 사용 - `(타입) 값`
            * ex) `int i = 100; byte b = i; (X), byte b = (byte) i;`
    * 예시

        ```java
        // 묵시적 형변환
        int n1 = 10;
        long n2 = n1;

        // 명시적 형변환 : 범위가 큰 자료형 -> 범위가 작은 자료형
        byte b = (byte) n2;
        ```



## 연산자
* 연산자 종류

    ![java_01_operator](../image/Java/01/java_01_operator.png)

    * 단항 연산자의 우선순위가 제일 높다.

* 단항 연산자
    * 증감 연산자 `++`, `--`
        * 피연산자의 값을 1증가, 감소 시킨다.
        * 전위형(prefix) `++i` : 먼저 값을 증감시키고 그 값을 사용
        * 후위형(postfix) `i++` : 먼저 값을 사용하고 그 값을 증감
    * 부호 연산자 `+`, `-`
        * 숫자가 양수임을 표시 `+`
        * 피연산자의 부호를 반대로 변경한 결과 반환 `-`
    * 논리 부정 연산자 `!`
        * 논리 값을 반전
    * 비트 부정 연산자 `~`
        * 비트 값을 반전
    * 형 변환 연산자 (type)

        ```java
        int a = 5;
        System.out.println(a++); // 5
        // 이후 a = 6
        System.out.println(++a); // 7
        System.out.println(--a); // 6
        System.out.println(a); // 6
        System.out.println(a--); // 6
        // 이후 a = 5
        System.out.println(a++); // 5
        // 이후 a = 6

        System.out.println(-a); // -6
        System.out.println(~a); // -7

        System.out.println(!false); // true
        ```

* 산술 연산자 (이항 연산자)
    * 곱하기 연산자 `*`
    * 나누기 연산자 `/`
    * 나머지 연산자 `%`
    * 더하기 연산자 `+`
    * 빼기 연산자 `-`
    * 정수와 정수의 연산 = 정수
    * 실수가 들어간 연산 = 실수

    ```java
    int a = 10;
    int b = 6;

    System.out.println(a + b); // 16
    System.out.println(a - b); // 4
    System.out.println(a * b); // 60
    // 정수의 나눗셈 => 소수점 이하를 버린다.
    System.out.println(a / b); // 1
    System.out.println(a % b); // 4

    // 정수와 실수의 연산 => 실수
    System.out.println(double(a) / b); // 1.666666666666667
    System.out.println(a / double(b)); // 1.666666666666667
    // 정수 나눗셈 연산 이후 실수로 형변환
    System.out.println(double(a / b)); // 1.0

    double c = 2.3;

    System.out.println(a / c); // 4.347826086956522
    System.out.println(a / (int) c); // 5
    ```

* 비교 연산자
    * 대소 비교 연산 : `>`, `<`, `>=`, `<=`
    * 동등 비교 연산 : `==`, `!=`
        * 단 String 변수 비교는 `equals()`로 한다.
    * 객체 타입 비교 연산 : `instanceof`

    ```java
    int a = 10;

    System.out.println(a > 10); // false
    System.out.println(a <= 10); // true
    System.out.println(a >= 10); // true
    System.out.println(a == 10); // true
    System.out.println(a != 10); // false

    // 자바에서 문자열은 어떻게 비교 하는가?
    String c = "Hi";
    String d = "Hi";
    String e = new String("Hi");

    // 자바에서 문자열의 비교는 ==, != 연산자로 하지 않는다.
    // 문자열에서 ==, != : 참조값(주소값) 비교
    // 문자열에서 .equals : 값 비교
    System.out.println(c == d); // true
    System.out.println(c == e); // false
    System.out.println(c.equals(e)); // == : true
    System.out.println(!c.equals(e)); // != : false
    ```

* 논리 연산자
    * `&&` : 논리곱(AND), 피연산자 모두가 true일 경우에만 true
    * `||` : 논리합(OR), 피연산자 중 하나라도 true일 경우 true
    * `!` : 논리 부정(NOT), 피연산자의 결과를 반대로 바꾼다.

    ```java
    System.out.println(true && true); // true
    System.out.println(false && true); // false
    System.out.println(true && false); // false
    System.out.println(false && false); // false

    System.out.println(true || true); // true
    System.out.println(true || false); // true
    System.out.println(false || true); // true
    System.out.println(false || false); // false

    // Short circuit evaluation(단축 평가) => 효율적인 연산이 가능
    // && 연산일 경우 : 앞이 false인 경우 => 전체 결과가 false
    //    => 뒤는 고려하지 않고 바로 false

    // || 연산일 경우 : 앞이 true => 전체 결과가 true
    //    => 뒤는 고려하지 않고 바로 true

    int b = 20;
    int a = 10;

    System.out.println(a > b && a++ > b); // false
    System.out.println(a); // 10
    System.out.println(a < b && a++ < b); // true
    System.out.println(a); // 11

    System.out.println(a > b || a++ > b); // false
    System.out.println(a); // 12
    System.out.println(a < b || a++ < b); // true
    System.out.println(a); // 12

    // 연산자가 2개가 아닌 1개인 경우 (& or |) 단축평가를 하지 않고 전부 실행
    int b = 20;
    int a = 10;

    System.out.println(a > b & a++ > b); // false
    System.out.println(a); // 11
    System.out.println(a < b & a++ < b); // true
    System.out.println(a); // 12

    System.out.println(a > b | a++ > b); // false
    System.out.println(a); // 13
    System.out.println(a < b | a++ < b); // true
    System.out.println(a); // 14
    ```

* 삼항 연산자
    * `조건식 ? 식1 : 식2`
    * 조건식이 참일 경우 식1 수행
    * 조건식이 거짓일 경우 식2 수행
* 복합 대입 연산자
    * `+=`, `-=`, `*=`, `/=`

## 제어문(조건문 & 반복문)

### 조건문(if, switch)
* if 문

    ```java
    if (조건식) {
        실행할 문장1;
        실행할 문장2;
        ...
    }
    ```

    * 조건식의 결과에 따라 블록 실행 여부가 결정
    * 조건식 : true/false 값을 산출할 수 있는 연산식 또는 boolean 타입 변수가 올 수 있음
    * 조건식이 참일 경우 문장들을 실행하고, 거짓일 경우 실행하지 않음
    * 실행할 문장이 하나라면 중괄호 생략 가능
* if-else 문

    ```java
    if (조건식) {
        실행할 문장1;
        실행할 문장2;
        ...
    } else {
        실행할 문장a;
        ...
    }
    ```

    * 조건식의 결과에 따라 실행할 블록 결정
    * 조건식이 참일 경우 if 블록의 문장들을 실행하고, 거짓일 경우 else 블록의 문장을 실행
    * 실행할 문장이 하나라면 중괄호 생략 가능
* 중첩 if 문

    ```java
    if (조건식A){
        if (조건식B){
            조건식 A, B 모두 참일 경우 수행할 문장;
        } else {
            조건식 A는 참, B는 거짓일 경우 수행할 문장;
        }
    } else {
        조건식 A가 거짓일 경우 수행할 문장;
    }
    ```

    * 중첩의 횟수에는 제한이 없음
* if-else if-else 문

    ```java
    if (조건식){
        실행할 문장1;
        ...
    } else if(조건식){
        실행할 문장a;
        ...
    } ...{
        ...
    } else {
        실행할 문장 A;
        ...
    }
    ```

    * 조건식이 참일 경우 해당 블록의 문장들을 실행하고, 거짓일 경우 다음 조건식을 실행
* 예시

    ```java
    // 중괄호가 있는 경우
    int n = 15;
    if (n > 10) {
        System.out.println("블록 내부를 수행한다.");
    }

    // 중괄호가 없는 경우
    if (n > 10)
        System.out.println("해당 문장을 수행한다.");
        System.out.println("얘도 수행?"); // 이 문장은 if문과 관계 없다 => 실행된다.

    
    // 90점 이상 A
    // 80점 이상 90점 미만 B
    // 70점 이상 80점 미만 B
    // 70점 미만 A

    int score = 97;
    if (score >= 90) {
        System.out.println("A");
    } else {
        if(score >= 80) {
            System.out.println("B");
        } else {
            if(score >= 70) {
                System.out.println("C");
            } else {
                System.out.println("F")
            }
        }
    }

    int score = 97;
    if (score >= 90) {
        System.out.println("A");
    } else if (score >= 80) {
        System.out.println("B");
    } else if (score >= 70) {
        System.out.println("C");
    } else {
        System.out.println("F")
    }
    ```

* switch 문

    ```java
    switch (수식) {
        case 값1 :
            실행문 A;
            break;
        case 값2 :
            실행문 B;
            break;
        default :
            실행문 C;
    }
    ```

    * 인자로 선택변수를 받아 변수의 값에 따라서 실행문이 결정
    * 주의 사항
        1. 수식에 올 수 있는 것
            - 1.4버전 까지는 byte, short, char, int
            - 1.5버전 부터 enum 클래스 타입
            - 1.7버전 부터 String 클래스 타입
        2. break문 없이도 사용이 가능하다.
        3. default => else의 역할과 동일하다.

    ```java
    int month = 12;

    switch (month) {
        case 1 :
        case 3 :
        case 5 :
        case 7 :
        case 8 :
        case 10 :
        case 12 :
            System.out.println("31일");
            break;
        case 4 :
        case 6 :
        case 9 :
        case 11 :
            System.out.println("30일");
            break;
        case 2 :
            // 4로 나누어 떨어지는 해는 윤년이다.
            // 4, 100으로 나누어 떨어지는 해는 평년이다.
            // 4, 100, 400으로 나누어 떨어지는 해는 윤년이다.
            System.out.println("28일, 윤년 고려해봐야함");
            break;
        default :
            System.out.println("그런 월은 존재하지 않음.")
    }
    ```


### 반복문(for, while, do~while)
* for 문

    ```java
    for (1.초기화식; 2.조건식; 4.증감식) {
        3.반복 수행할 문장
    }
    ```

    * 초기화는 반복문이 시작될 때 한 번 실행됨
    * 조건식이 false이면, 반복문 종료
    * 증감식은 반복문의 반복이 끝나면 실행됨
    * 초기화식, 증감식은 `,`를 이용하여 둘 이상을 작성할 수 있음
    * 필요하지 않은 부분은 생략할 수 있음. ex) `for(;;)` : 무한 루프
    * 반복횟수를 알고 있을 때 유용
* 중첩 for 문

    ```java
    for (초기화식; 조건식; 증감식) {
        for (초기화식; 조건식; 증감식) {
            반복 수행할 문장
        }
    }
    ```

* while 문

    ```java
    while (1. 조건식) {
        2. 반복 수행할 문장;
    }
    ```

    * 조건식이 true일 경우에 계속해서 반복
    * 조건식이 거짓이 될 때까지 문장을 반복 수행
    * 조건식 생략 불가능
* do ~ while 문

    ```java
    do {
        1. 반복수행할 문장;
    } while (2. 조건식);
    ```

    * 블록 내용을 먼저 수행 후 조건식 판단. (최소 한번은 수행)
    * 조건식이 true일 경우에 계속해서 반복
    * 조건식이 거짓이 될 때까지 문장을 반복 수행
    * 조건식 생략 불가능
* break & continue
    * break
        * switch, while, do-whlie, for 문의 블록에서 빠져나오기 위해서 사용
        * 반복문에 이름(라벨)을 붙여 한번에 빠져 나올 수 있음
    * continue
        * 반복문의 특정지점에서 제어를 반복문의 처음으로 보냄
        * 반복문에 이름(라벨)을 붙여 제어할 수 있음
* 예시

    ```java
    // for 문
    // 0부터 9까지 출력
    for (int i = 0; i < 10; i++) {
        System.out.println(i);
    }

    for (int i = 0, j = 30; i < 10 && j >=20; i += 10, j += 2) {
        System.out.println(i + " " + j);
    }

    // 중첩 for 문
    // 중첩 반복문 (구구단)
    for (int i = 2; i <= 9; i++) {
        System.out.println(i+"단");
        for (int j = 1; j <= 9; j++) {
            System.out.println("%d * %d = %d\n", i, j, i*j);
        }
    }

    // while 문
    int n = 10;

    while (n > 5) {
        System.out.println("이거 실행되나?" + n);
        n--;
    }
    

    // do-while 문
    Scanner sc = new Scanner(System.in);
    int num;

    do {
        System.out.println("숫자를 입력하세요. (0이면 종료)");
        num = sc.nextInt();
    } while (num != 0);

    // continue - 짝수 구구단 출력
    for (int i = 2; i <= 9; i++) {
        if (i % 2 == 1)
            continue;
        System.out.println(i+"단");
        for (int j = 1; j <= 9; j++) {
            System.out.println("%d * %d = %d\n", i, j, i*j);
        }
    }

    // break - 구구단 4단까지 출력
    for (int i = 2; i <= 9; i++) {
        if (i > 5)
            break;
        System.out.println(i+"단");
        for (int j = 1; j <= 9; j++) {
            System.out.println("%d * %d = %d\n", i, j, i*j);
        }
    }

    // label을 통해서 내가 빠져나갈 블록을 지정
    out : for (int i = 2; i <= 9; i++) {
        System.out.println(i+"단");
        for (int j = 1; j <= 9; j++) {
            if (j > 5)
                break out;
            System.out.println("%d * %d = %d\n", i, j, i*j);
        }
    }
    ```