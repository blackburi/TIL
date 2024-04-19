# 등산로 조정


# 현재 높이, 현재 등산로의 길이, 공사 횟수(max = 1)
# 현재 위치 x, y
def dfs(height, leng, cut, x, y) :
    global length, k

    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n and (visited[mx][my] is False) :
            visited[my][my] = True
            if height > mat[mx][my] :
                dfs(mat[mx][my], leng+1, cut, mx, my)

            if cut == 0 and k >= mat[mx][my] - height :
                for j in range(1, k+1) :
                    dfs(mat[mx][my]-j, leng+1, cut+1, mx, my)
                    visited[mx][my] = False




dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


T = int(input())
for tc in range(1, T+1) :
    n, k = map(int, input().split())

    # 최대 높이
    max_height = 0
    # 최대 높이를 담아두는 list
    start = []
    # 등산로의 최대 길이
    length = 0

    mat = []
    for i in range(n) :
        sub = list(map(int, input().split()))
        for j in range(n) :
            if max_height < sub[j] :
                start = [(i, j)]
            elif max_height == sub[j] :
                start.append((i, j))
        mat.append(sub)

    visited = [[False]*n for _ in range(n)]

