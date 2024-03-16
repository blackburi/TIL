# 빵집

import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
mat = [tuple(map(str, input().rstrip())) for _ in range(r)]

# 방문기록 check
visited = [[False] * c for _ in range(r)]

dx = [-1, 0, 1]

def dfs(x, y) :
    if y == c - 1 :
        return True

    for i in range(3) :
        mx = x + dx[i]
        my = y + 1
        if 0 <= mx <= r-1 and 0 <= my <= c-1 :
            if mat[mx][my] == '.' and visited[mx][my] is False :
                visited[mx][my] = True
                if dfs(mx, my) is True :
                    return True
    return False

# 경로의 수
cnt = 0

for i in range(r) :
    if dfs(i, 0) is True :
        cnt += 1

print(cnt)