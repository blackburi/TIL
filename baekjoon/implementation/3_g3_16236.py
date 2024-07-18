# 아기 상어

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
mat = []
for i in range(n) :
    sub = list(map(int, input().rstrip().split()))
    for j in range(n) :
        if sub[j] == 9 :
            fx = i
            fy = j
    mat.append(sub)

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

cnt = 0

