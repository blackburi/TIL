import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque([i for i in range(1, n+1)])

while len(deq) > 1 :
    deq.popleft()
    k = deq.popleft()
    deq.append(k)

print(*deq)