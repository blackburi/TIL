# 등산로 조정


# 현재 높이, 현재 등산로의 길이, 공사 횟수(max = 1)
# 현재 위치 x, y

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 현재 높이, 등산로 길이, 깎았는지, 현재 위치
def dfs(height, leng, cut, x, y) :
    global length

    length = max(length, leng)

    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n and (visited[mx][my] is False) :
            # 다음 이동이 현재보다 높이가 낮은 경우
            if height > mat[mx][my] :
                visited[mx][my] = True
                dfs(mat[mx][my], leng+1, cut, mx, my)
                visited[mx][my] = False
            
            # 다음 이동이 현재보다 높이가 같거나 높은 경우
            if height <= mat[mx][my] and cut == 0 and mat[mx][my]-k < height :
                visited[mx][my] = True
                dfs(height-1, leng+1, cut+1, mx, my)
                visited[mx][my] = False


T = int(input())
for tc in range(1, T+1) :
    n, k = map(int, input().split())

    # 높이의 최댓값
    max_height = 0
    # 높이가 최대인 지점들의 집합
    start = []

    mat = []
    for i in range(n) :
        sub = list(map(int, input().rstrip().split()))
        for j in range(n) :
            if sub[j] > max_height :
                max_height = sub[j]
                start = [(i, j)]
            elif sub[j] == max_height :
                start.append((i, j))
        mat.append(sub)

    # 최대 길이 등산로
    length = 0
    # 방문체크
    visited = [[False]*n for _ in range(n)]

    for (a, b) in start :
        dfs(max_height, 1, 0, a, b)

    print(f'#{tc} {length}')