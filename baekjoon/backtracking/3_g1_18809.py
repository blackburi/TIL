# Gaaaaaaaaaarden

import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m, g, r = map(int, input().split())
# 토양
grounds = []
# 배양액을 뿌릴수 있는 곳
possible = []

for i in range(n) :
    sub = tuple(input().rstrip().split())
    for j in range(m) :
        if sub[j] == '2' :
            possible.append((i, j))
    grounds.append(sub)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def plant() :
    q = deque()
    # 핀 꽃의 수
    flower = 0

    for gr in green :
        q.append((gr[0], gr[1], 'g'))
        visited[gr[0]][gr[1]] = True
    for re in red :
        q.append(re[0], re[1], 'r')
        visited[re[0]], [re[1]] = True

    while q :
        x, y, color = q.popleft()

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < m and (grounds[mx][my] == '1' or grounds[mx][my] == '2') and visited[mx][my] is False :
                



# 최대 꽃의 개수
answer = 0

# 방문 처리
visited = [[False]*m for _ in range(n)]

for green in combinations(possible, g) :
    green = list(green)
    rest = possible - green
    for red in combinations(rest, r) :
        red = list(red)
        answer = max(answer, plant())

print(answer)