# 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

answer = 0

# ㅗ모양 제외 다른 모양들 전부 dfs로 탐색
# (x, y) 현재 위치, 모양의 합 = total, 칸의 개수 = cnt
def dfs(x, y, total, cnt) :
    global answer

    if cnt == 4 :
        answer = max(answer, total)
        return
    
    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < m and visited[mx][my] is False :
            visited[mx][my] = True
            dfs(mx, my, total+mat[mx][my], cnt+1)
            visited[mx][my] = False

# ㅗ모양 탐색 -> +모양을 만들고 그중 제일 작은 값을 뺀다
# 시작점 (x, y) == +의 중앙 좌표
def fuck(x, y) :
    global answer

    lst = []
    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < m :
            lst.append(mat[mx][my])
    # ㅗ모양이 담긴 경우
    if len(lst) == 3 :
        answer = max(answer, sum(lst) + mat[x][y])
    # +모양이 담긴 경우
    elif len(lst) == 4 :
        lst.sort(reverse=True)
        lst.pop()
        answer = max(answer, sum(lst) + mat[x][y])
    return

for i in range(n) :
    for j in range(m) :
        visited[i][j] = True
        dfs(i, j, mat[i][j], 1)
        fuck(i, j)
        visited[i][j] = False

print(answer)