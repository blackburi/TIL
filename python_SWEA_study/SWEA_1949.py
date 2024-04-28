# 등산로 조정

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cut) :
    global length, visited

    length = max(length, visited[x][y])

    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n and visited[mx][my] == 0 :
            if mat[x][y] > mat[mx][my] :
                visited[mx][my] = visited[x][y] + 1
                dfs(mx, my, cut)
                visited[mx][my] = 0
            elif cut == 0 and mat[mx][my] - k < mat[x][y] :
                tmp = mat[mx][my]
                mat[mx][my] = mat[x][y] - 1
                visited[mx][my] = visited[x][y] + 1
                dfs(mx, my, cut+1)
                visited[mx][my] = 0
                mat[mx][my] = tmp


T = int(input())
for tc in range(1, T+1) :
    n, k = map(int, input().split())

    # 지도
    mat = []

    heights = []
    height = 0
    for i in range(n) :
        sub = list(map(int, input().split()))
        for j in range(n) :
            if sub[j] > height :
                height = sub[j]
                heights = [(i, j)]
            elif sub[j] == height :
                heights.append((i, j))
        mat.append(sub)

    # 최대 길이 등산로
    length = 0
    # 방문처리
    visited = [[0]*n for _ in range(n)]

    for (i, j) in heights :
        visited[i][j] = 1
        dfs(i, j, 0)
        visited[i][j] = 0
    
    print(f'#{tc} {length}')