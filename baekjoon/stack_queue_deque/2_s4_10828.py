import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N) :
    x = list(map(str, input().split()))
    
    if x[0] == 'push' :
        stack.append(x[1])
    elif x[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            a = stack.pop()
            print(a)
    elif x[0] == 'size' :
        print(len(stack))
    elif x[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif x[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])