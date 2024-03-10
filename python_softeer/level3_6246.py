# 순서대로 방문하기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
mat = []
visited = []
for _ in range(n) :
    sub = list(map(str, input().rstrip().split()))
    mat.append(sub)
    visited_sub = []
    for i in range(n) :
        if sub[i] == '1' :
            visited_sub.append(True)
        else :
            visited_sub.append(False)
    visited.append(visited_sub)

# 방문해야 하는 점의 수
lst = deque([])
for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    lst.append((a-1, b-1))

# 경로의 개수
cnt = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

a, b = lst.popleft()
visited[a][b] = True
c, d = lst[-1]

def dfs(x, y) :
    global cnt

    if x == c and y == d :
        if not lst :
            cnt += 1
        return

    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx <= n-1 and 0 <= my <= n-1 and visited[mx][my] is False :
            visited[mx][my] = True
            if mx == lst[0][0] and my == lst[0][1] :
                lst.popleft()
                dfs(mx, my)
                lst.appendleft((mx, my))
                visited[mx][my] = False
            else :
                dfs(mx, my)
                visited[mx][my] = False
    return

dfs(a, b)
print(cnt)