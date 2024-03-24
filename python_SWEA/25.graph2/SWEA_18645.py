# 최소 비용

from collections import deque

T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    mat= [list(map(int, input().split())) for _ in range(n)]

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque([(0, 0)])
    while q :
        x, y = q.popleft()
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= n-1 :
                # 아직 방문하지 않았다면
                if visited[mx][my] == -1 :
                    # 올라가는 경우
                    if mat[mx][my] > mat[x][y] :
                        visited[mx][my] = visited[x][y] + mat[mx][my] - mat[x][y] + 1
                    # 내려가는 경우
                    else : # mat[mx][my] <= mat[x][y]
                        visited[mx][my] = visited[x][y] + 1
                    q.append((mx, my))
                # 방문한 적이 있다면
                else : # visited[mx][my] != -1
                    # 올라가는 경우
                    a = visited[mx][my]
                    if mat[mx][my] > mat[x][y] :
                        visited[mx][my] = min(visited[mx][my], visited[x][y] + mat[mx][my] - mat[x][y] + 1)
                    # 내려가는 경우
                    else : # mat[mx][my] <= mat[x][y]
                        visited[mx][my] = min(visited[mx][my], visited[x][y] + 1)

                    if a != visited[mx][my] :
                        q.append((mx, my))

    print(f'#{tc} {visited[n-1][n-1]}')