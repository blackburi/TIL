# Gaaaaaaaaaarden

import sys
input = sys.stdin.readline
from itertools  import combinations
from collections import deque


# 배양액 색을 배치
def select_color(select, now, gr_list, colors) :
    global ans

    if now == g+r :
        ans = max(ans, bfs(gr_list, select))
        return

    # 초록색 배양
    if colors[0] > 0 :
        colors[0] -= 1
        select[now] = 1
        select_color(select, now+1, gr_list, colors)
        colors[0] += 1

    # 빨강색 배양
    if colors[1] > 0 :
        colors[1] -= 1
        select[now] = -1
        select_color(select, now+1, gr_list, colors)
        colors[1] += 1


# bfs
def bfs(gr_list, select) :
    visited = [[0]*m for _ in range(n)]
    q = deque()

    for idx in range(g+r) :
        x, y = gr_list[idx]
        visited[x][y] = select[idx]
        # x, y, 색
        q.append((x, y, select[idx]))

    flower = 0
    while q :
        # 초록색이면 시간이 흐를수록 +1
        # 빨강색이면 시간이 흐를수록 -1
        x, y, color = q.popleft()

        if visited[x][y] == 1e9 :
            continue

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= mx < n and 0 <= my < m and visited[mx][my] != 1e9 and garden[mx][my] != 0 :
                # 아직 배양액이 퍼지지 않은 곳이라면
                if visited[mx][my] == 0 :
                    if color < 0 :
                        visited[mx][my] = color - 1
                        q.append((mx, my, color-1))
                    else : # color > 0 (color값은 항상 0이 아닌 수를 갖는다)
                        visited[mx][my] = color + 1
                        q.append((mx, my, color+1))
                # 이웃한 두칸에 color값의 부호가 다르고 절댓값이 1차이가 난다면 => 꽃이 핌
                elif abs(visited[mx][my]) == abs(color) + 1 and visited[mx][my]*color < 0 :
                    flower += 1
                    visited[mx][my] = 1e9
    return flower


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, g, r = map(int, input().split())
garden = []
spread = []
for i in range(n) :
    sub = list(map(int, input().rstrip().split()))
    for j in range(m) :
        if sub[j] == 2 :
            spread.append((i, j))
    garden.append(sub)

# 피울수 있는 꽃의 최댓값
ans = 0

select = [0] * (g+r)
for gr_list in combinations(spread, g+r) :
    select_color(select, 0, gr_list, [g, r])
print(ans)