# 진우의 민트초코우유

import sys
input = sys.stdin.readline
from collections import deque

n, m, h = map(int, input().split())

# 우유가 있는 집
houses = deque()

for i in range(n) :
    sub = list(input().rstrip().split())
    for j in range(n) :
        # 진우의 집
        if sub[j] == '1' :
            start = (i, j)
            houses.appendleft((i, j))
        # 우유가 있는 집
        if sub[j] == '2' :
            houses.append((i, j))

# 방문 처리 / index=0 최종 도착지(진우집)
visited = {}
for i in range(len(houses)) :
    visited[i] = False

# 진우가 먹는 우유의 최대 개수
cnt = 0


# 현재 위치, 먹은 우유의 개수, 남은 체력
def dfs(x, y, milk, stamina) :
    global cnt

    if milk != 0 and (x, y) == start :
        cnt = max(cnt, milk-1)
        return

    for i in range(len(visited)) :
        if (visited[i] is False) and (stamina >= abs(x-houses[i][0])+abs(y-houses[i][1])) :
            visited[i] = True
            dfs(houses[i][0], houses[i][1], milk+1, stamina-(abs(x-houses[i][0])+abs(y-houses[i][1]))+h)
            visited[i] = False


dfs(start[0], start[1], 0, m)

print(cnt)