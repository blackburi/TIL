# 적록색약

import sys
input = sys.stdin.readline
from collections import deque


# delta
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 같은 색의 영역을 count해주는 함수
# mat[x][y] = color
def area(x, y, color) :
    global cnt
    cnt += 1
    q = deque([[x, y]])
    visited[x][y] = True
    while q :
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4) :
            if 0 <= x+dx[i] <= n-1 and 0 <= y+dy[i] <= n-1 :
                if mat[x+dx[i]][y+dy[i]] == color and visited[x+dx[i]][y+dy[i]] is False :
                    visited[x+dx[i]][y+dy[i]] = True
                    q.append([x+dx[i], y+dy[i]])

    for p in range(n) :
        for q in range(n) :
            if visited[p][q] is False :
                area(p, q, mat[p][q])

    return


n = int(input())
mat = [list(map(str, input().rstrip())) for _ in range(n)]

## 일반사람이 본 경우
# 방문기록 저장
visited = [[False] * n for _ in range(n)]
# 영역의 수
cnt = 0
area(0, 0, mat[0][0])
a = cnt

## 적록색약인 사람이 본 경우 (R == G)
for i in range(n) :
    for j in range(n) :
        if mat[i][j] == 'G' :
            mat[i][j] = 'R'
# 방문기록 저장 (이전 기록 초기화)
visited = [[False] * n for _ in range(n)]
# 영역의 수

area(0, 0, mat[0][0])
b = cnt

print(a, b-a)