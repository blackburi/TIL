# 벽 부수고 이동하기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mat = [list(map(str, input().rstrip())) for _ in range(n)]

# [벽을 부수지 않고 간 거리, 벽을 부수고 간 거리]
# 파괴 변수를 통해 파괴를 안했다면 0번, 파괴를 했다면 1번 index사용
dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# [x, y] 위치
def bfs(x, y) :
    # [x, y] 위치, 파괴 유무
    q = deque([[x, y, 0]])
    dp[x][y][0] = 1

    while q :
        # destroy는 0또는 1
        x, y, destroy = q.popleft()

        if x == n-1 and y == m-1 :
            return dp[x][y][destroy]
        
        for i in range(4) :
            mx = x+dx[i]
            my = y+dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= m-1 :
                # 벽을 만나는 경우 -> destroy == 0 이어야 한다.
                if mat[mx][my] == '1' and destroy == 0 and dp[mx][my][1] == 0 :
                    dp[mx][my][1] = dp[x][y][0] + 1
                    q.append([mx, my, 1])
                # 통로를 만나는 경우 -> destroy와 관계 없음
                elif mat[mx][my] == '0' and dp[mx][my][destroy] == 0 :
                    dp[mx][my][destroy] = dp[x][y][destroy] + 1
                    q.append([mx, my, destroy])

    return -1

print(bfs(0, 0))