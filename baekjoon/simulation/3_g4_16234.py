# 인구 이동

import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

q = deque()
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

# 연합이 될수 있는지 check -> 될수 있다면 인구수//칸수 값으로 갱신
# 계산이 불가할 때까지 반복
def bfs(x, y) :
    q.append((x, y))
    union = [(x, y)]

    while q :
        a, b = q.popleft()
        for i in range(4) :
            mx = a + dx[i]
            my = b + dy[i]
            if 0 <= mx < n and 0 <= my < n and visited[mx][my] is False :
                if l <= abs(mat[a][b] - mat[mx][my]) <= r :
                    visited[mx][my] = True
                    q.append((mx, my))
                    union.append((mx, my))

    if len(union) <= 1 :
        return 0

    sub = 0
    for (a, b) in union :
        sub += mat[a][b]
    sub //= len(union)

    for (a, b) in union :
        mat[a][b] = sub
    return 1



answer = 0

while True :
    flag = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] is False :
                visited[i][j] = True
                flag += bfs(i, j)
    if flag == 0 :
        break
    answer += 1

print(answer)