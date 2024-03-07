# 카드 놓기

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
first = deque([]) # 위-아래
lst = deque([i for i in range(1, n+1)]) # 위-아래

def re(k) :
    if k == 1 :
        a = lst.popleft()
        first.appendleft(a)
    elif k == 2 :
        a = lst.popleft()
        k = first.popleft()
        first.appendleft(a)
        first.appendleft(k)
    else : # k == 3
        a = lst.popleft()
        first.append(a)

way = list(map(int, input().rstrip().split()))

while way :
    k = way.pop()
    re(k)

print(*first)