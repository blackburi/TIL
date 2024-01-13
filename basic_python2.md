# 제어 구조

## 반복문

### while 반복문

```python
num = 1   # num에 1을 저장한다
while num <=100:   # num이 100보다 작거나 같다면
    print(num)   # num을 출력해라
    num = num + 1   # num에 1을 더해서
    ## 마지막 줄은 num += 1 로 써도 무방하다.
```
* 위의 code를 실행하면 `num = 100`이 될때 while 반복문이 멈추고 1~100이 출력되는 것을 알 수 있다.
* 이때 조심해야 할 부분은 code를 위에서부터 있는 그대로 인식해야한다.
    * 다음 경우는 `num`을 출력한 이후에 `num += 1`을 수행하는 것이다. 따라서 1~100까지 출력이 된다.
    ```python
    num = 1
    while num <=100:
        print(num)
        num += 1
    ``` 

    * 다음 경우는 `num += 1`을 수행하고 `num`을 출력한다. 따라서 1~101까지 출력이 된다.
    ```python
    num = 1
    while num <=100:
        num += 1
        print(num)
    ```
* while 반복문 사용시 while을 사용하는 줄 제일 마지막에는 `:`를 붙여줘야 한다.

### for 반복문
* `for`반복문은 `for (요소) in sequence`로 이루어진다.
    * `for` : `for`반복문의 시작을 나타낸다.
    * 요소 : sequence에서 어떤 것을 쓸 것인지를 말해준다.
        * 예시를 몇개 들어본다면 `for letter in word` : `word`라는 sequence에서 `letter`이라는 요소를 사용한다는 의미이다.
        ```python
        word = 'alphabet'
        for letter in word:
            print(letter)
        # a l p h a b e t이 각각 한줄에 한 글자씩 출력된다.
        ```
* `range()` : 특정 범위의 정수를 return하는 것
    * `range(a)` : 0부터 a미만의 정수를 return한다.
        * `range(0)`의 경우 0부터 0미만의 정수가 없기 때문에 emtpy(`[]`)를 return한다.
        ```python
        >>> list(range(0))
        []   # 왼쪽처럼 출력되는 것을 empty라고 한다.
        ```
    * 다음의 경우는 조심해야 한다.
    ```python
    num = int(input())   # 입력한 값을 num애 저장한다.
    for i in range(num):   # i가 0~(num-1)까지 받는다 즉 num번 loop가 반복된다.
        print('', num)   # (space)num이 출력된다.
    # n을 입력하면 n이 n번 출력된다.
    ```
    * `range(a, b)` : a 이상 b 미만의 정수를 return한다.
        ```python
       for i in range(2,7):
            print(i)
        # 2 3 4 5 6이 줄당 1개씩 출력된다.
        ```
    * `range(a, b, c)` : a부터 b까지 c의 간격으로 return한다.
        ```python
        >>> list(range(-1, -9, -2))
        [-1, -3, -5, -7. -9]   # 출력값
        ```
         * 보통 음수 값을 출력하기 위해 이 경우를 사용한다.
* `match-case`문
    * `match-case`문은 보통 `match`뒤에 조건이 붙고 `case`뒤에 조건에 따른 유형이 붙는다.
    ```python
    for n in range(1, 101):   # n을 1~100까지 정수로 return
    match (n % 3, n % 5):   # match조건 : (n을 3으로 나눈나머지, n을 5로 나눈 나머지)
        case (0, 0):   # case1 : 3과 5로 나눈 나머지가 모두 0인경우
            print("FizzBuzz")
        case (0, _):   # case2 : 3으로 나눈 나머지만 0인경우
            print("Fizz")
        case (_, 0):   # case3 : 5로 나눈 나머지만 0인경우
            print("Buzz")
        case _:   # case4 : 3과 5로 나눈 나머지가 모두 0이 아닌 경우
            print(n)
    ```
    * 위의 code에서 조건에 0이 아닌 경우가 필요한 경우 공백(space)로 놔두면 error가 뜬다. 0이 아닌 다른 수는 `_`(under bar)를 이용하면 된다.

## 조건문 (if-elif-else)
* `if` : 먄약 `if`뒤의 조건을 만족한다면 `if`에 해당하는 code 실행
* `elif` : `if`와 동일한 조건이다.
    * `elif`는 `if`에 넣을 조건이 여러 가지일 경우 사용한다.
* `else` : `if`와 `elif`의 경우를 제외한 모든 경우를 의미한다.
* `if`와 `elif`
* 마찬가지로 `if`, `elif`, `else`를 사용하는 줄의 마지막엔 `:`를 붙여야 한다.
```python
c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else:
    print('I don\'t know')   
# 결과값으로 'c is equal to d'가 출력된다.
```
* `if`반복문을 끝내는 또 다른 방법은 `break`를 사용하는 방법이다.
    ```python
    max = 10
    while True:
        num = int(input())
        if num > max:
            print(num, 'is too big!')
            break
    # 이때 10 이하의 정수를 입력하면 계속 돌아가지만 10 초과의 정수를 입력하면 멈추게 된다.
    ```
* `if-elif-else` 반복문에서 특정 조건에서 아무일도 일어나지 않게 만들기 위해서는 `pass`를 사용하면 된다.
* 조건문에 `and/or`또한 사용할 수 있다.
    ```python
    s = 'banana'
    if 'a' in s:
        if 'b' in 'banana':
            print('banana에는 a도 있고 b도 있어요!')
    ```
    ```python
    s = 'banana'
    if 'a' in s and 'b' in 'banana':
        print('banana에는 a도 있고 b도 있어요!')
    ```
    * 두 code는 모두 같은 결과값을 출력한다.
    * python에서는 `and/or`의 왼쪽항부터 차례대로 평가를 하기 때문에 같은 뜻의 code를 입력해도 결과값이 다르게 나온다.
    ```python
    a = 3
    b = 0
    (a * b) > 0 and (a / b) > 0
    # False가 출력된다
    # (a * b) > 0 이 이미 False이기 때문에 오른쯕항은 평가 자체를 하지 않는다.
    ```
    ```python
    a = 3
    b = 0
    (a / b) > 0 and (a * b) > 0
    # ZeroDivisionError가 발생한다.
    # (a / b) > 0에서 계산이 불가하기 때문이다.
    ```

## `for-else`문

[공부해야하는 링크](https://wikidocs.net/190098)


## `while-else`문