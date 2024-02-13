import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq = deque([])

for _ in range(N) :
    x = list(map(str, input().split()))

    if x[0] == 'push_front' :
        deq.appendleft(x[1])
    elif x[0] == 'push_back' :
        deq.append(x[1])
    elif x[0] == 'pop_front' :
        if len(deq) == 0 :
            print(-1)
        else :
            a = deq.popleft()
            print(a)
    elif x[0] == 'pop_back' :
        if len(deq) == 0 :
            print(-1)
        else :
            b = deq.pop()
            print(b)
    elif x[0] == 'size' :
        print(len(deq))
    elif x[0] == 'empty' :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    elif x[0] == 'front' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])
    elif x[0] == 'back' :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])