import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq = deque([])

for _ in range(N) :
    x = list(map(str, input().split()))
    if x[0] == '1' :
        deq.appendleft(x[1])
    if x[0] == '2' :
        deq.append(x[1])
    if x[0] == '3' :
        if len(deq) == 0 :
            print(-1)
        else :
            a = deq.popleft()
            print(a)
    if x[0] == '4' :
        if len(deq) == 0 :
            print(-1)
        else :
            b = deq.pop()
            print(b)
    if x[0] == '5' :
        print(len(deq))
    if x[0] == '6' :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    if x[0] == '7' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])
    if x[0] == '8' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])