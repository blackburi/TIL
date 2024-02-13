import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    deq = deque(list(map(int, input().split())))
    ans = 0

    while deq:
        d_max = max(deq)
        a = deq.popleft()
        k -= 1

        if d_max == a:
            ans += 1
            if k < 0:
                print(ans)
                break
        else:
            deq.append(a)
            if k < 0:
                k = len(deq) - 1