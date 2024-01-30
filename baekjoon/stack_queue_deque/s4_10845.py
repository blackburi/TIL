import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque([])

for _ in range(N) :
    x = list(map(str, input().split()))

    if x[0] == 'push' :
        queue.append(x[1])
    elif x[0] == 'pop' :
        if len(queue) == 0 :
            print(-1)
        else :
            a = queue.popleft()
            print(a)
    elif x[0] == 'size' :
        print(len(queue))
    elif x[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif x[0] == 'front' :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
    elif x[0] == 'back' :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])