# combinations
* 입력 iterable에서 요소의 길이 r 서브 시퀀스들을 반환합니다.

* The combination tuples are emitted in lexicographic ordering according to the order of the input iterable. So, if the input iterable is sorted, the output tuples will be produced in sorted order.

* Elements are treated as unique based on their position, not on their value. So if the input elements are unique, there will be no repeated values in each combination.

```python
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
```