# 안전 영역

import sys
input = sys.stdin.readline
from collections import deque

# [a, b]는 0이 아닌 구역, h는 잠기는 높이
def bfs(a, b, h) :
    lst = deque([[a, b]])
    visited[a][b] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while lst :
        x, y = lst.popleft()
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= n-1 :
                if mat[mx][my] > h and visited[mx][my] is False :
                    visited[mx][my] = True
                    lst.append([mx, my])


n = int(input())
mat = []
# 최대 높이
hmax = 0
for _ in range(n) :
    sub = list(map(int, input().rstrip().split()))
    if hmax < max(sub) :
        hmax = max(sub)
    mat.append(sub)

# 잠기지 않은 구역 개수의 최댓값
cnt_max = 0

# 잠기는 높이를 hmax-1까지 설정
for i in range(hmax) :
    # 잠기는 높이별로 생기는 지역을 세는 변수
    cnt = 0
    # 방문기록 저장
    visited = [[False] * n for _ in range(n)]
    for p in range(n) :
        for q in range(n) :
            if mat[p][q] > i and visited[p][q] is False :
                bfs(p, q, i)
                cnt += 1
    
    cnt_max = max(cnt_max, cnt)

print(cnt_max)