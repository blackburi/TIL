import sys
input = sys.stdin.readline

# mat[x][y]는 1인 지점
def dfs(a, b) :
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # area : 그림의 면적
    area = 1
    position = [[a, b]]
    mat[a][b] = 0
    while position :
        x, y = position.pop()
        for i in range(4) :
            mx = dx[i] + x
            my = dy[i] + y
            if 0 <= mx <= n-1 and 0 <= my <= m-1 and mat[mx][my] == 1 :
                position.append([mx, my])
                # 지나간 지점을 0으로 만들어준다.
                mat[mx][my] = 0
                area += 1
    return area

n, m = map(int, input().rstrip().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 그림의 개수
cnt = 0
# 그림의 최대 면적
marea = 0

for i in range(n) :
    for j in range(m) :
        if mat[i][j] == 1 :
            cnt += 1
            marea = max(dfs(i, j), marea)

print(cnt)
print(marea)