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

# 같은 거리라면 위-> 왼쪽 물고기를 먹어야 하기 때문에
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

cnt = 0

# BFS로 먹을수 있는 가장 가까운 위치를 찾는다.
def bfs(x, y) :
    q = deque()
