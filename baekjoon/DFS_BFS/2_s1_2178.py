# 미로 탐색

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

mat = [list(map(str, input())) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
distance[0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque([(0, 0)])

while q :
    x, y = q.popleft()
    for i in range(4) :
        if 0 <= x+dx[i] <= n-1 and 0 <= y+dy[i] <= m-1 and mat[x+dx[i]][y+dy[i]] == '1':
            if distance[x+dx[i]][y+dy[i]] == 0 :
                distance[x+dx[i]][y+dy[i]] = distance[x][y] + 1
                q.append((x+dx[i], y+dy[i]))

print(distance[n-1][m-1])