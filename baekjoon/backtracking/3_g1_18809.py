# Gaaaaaaaaaarden

import sys
input = sys.stdin.readline
from itertools  import combinations
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    flower = 0

    while q :
        x, y, xlast, ylast, time, color = q.popleft()
        # 전에 꽃이 폈으면
        if visited[xlast][ylast] == 1 : 
            continue
        if visited[x][y] :
            if visited[x][y] == (time, -color) :
                # 꽃이 피는 경우
                visited[x][y] = 1
                flower += 1
            continue

        visited[x][y] = (time, color)

        for i in range(4) :
            mx = x+dx[i]
            my = y+dy[i]
            if 0 <= mx < n and 0 <= my < m and garden[mx][my] :
                q.append((mx, my, x, y, time+1, color))

    return flower


n, m, g, r = map(int, input().split())

# garden
garden = []
# 배양액을 뿌릴수 있는 곳
spread = []
for i in range(n) :
    sub = list(map(int, input().rstrip().split()))
    for j in range(m) :
        if sub[j] == 2 :
            spread.append((i, j))
    garden.append(sub)
# 피울수 있는 꽃의 최댓값
result = 0

for grlist in combinations(spread, g+r) :
    for glist in combinations(grlist, g) :
        visited = [[0]*m for _ in range(n)]
        q = deque()

        # 초록색 배양
        for x, y in glist :
            visited[x][y] = 1
            # x, y, xlast, ylast, time, color
            q.append((x, y, x, y, 1, 1))

        # 빨강색 배양
        for x, y in grlist :
            if visited[x][y] :
                continue
            # x, y, xlast, ylast, time, color
            q.append((x, y, x, y, 1, -1))
            result = max(result, bfs())

print(result)