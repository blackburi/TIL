# permutation

* iterable에서 요소의 연속된 길이 r 순열을 반환합니다.

* r이 지정되지 않았거나 None이면, r의 기본값은 iterable의 길이이며 가능한 모든 최대 길이 순열이 생성됩니다.

* The permutation tuples are emitted in lexicographic order according to the order of the input iterable. So, if the input iterable is sorted, the output tuples will be produced in sorted order. -> 정렬되어 들어오면 정렬되어 나온다

* Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeated values within a permutation. -> 입력값에 중복이 없다면 출력값 또한 유일하다.(중복되는 것이 없다)

```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

* `permutations()`의 코드는 반복되는 요소(입력 풀에서 같은 위치에 있는 요소)가 있는 항목을 제외하도록 걸러낸 `product()`의 서브 시퀀스로 표현될 수도 있습니다

```python
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
```

* 반환되는 항목 수는
    * `0 <= r <= n`일 때는 `n! / (n-r)!`
    * `r > n`일 때는 `0`입니다.