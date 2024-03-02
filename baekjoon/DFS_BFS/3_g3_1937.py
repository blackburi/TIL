# 욕심쟁이 판다

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 최대 이동 거리를 저장하는 matrix
dp = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y) :
    global cmax

    if dp[x][y] > 0 :
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4) :
        mx = x+dx[i]
        my = y+dy[i]
        if 0 <= mx <= n-1 and 0 <= my <= n-1 and mat[x][y] < mat[mx][my] :
            dp[x][y] = max(dp[x][y], dfs(mx, my) + 1)

    return dp[x][y]

for i in range(n) :
    for j in range(n) :
        if dp[i][j] == 0 :
            dfs(i, j)

# 이동할 수 있는 거리의 최댓값
cmax = 0
for i in range(n) :
    cmax = max(cmax, max(dp[i]))

print(cmax)