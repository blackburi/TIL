# 치즈

import sys
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())

# 치즈판
mat = []
# 치즈 수
cnt = 0
# 치즈가 다 녹기 전 치즈의 수
memory = 0

for _ in range(n) :
    lst = list(map(int, input().rstrip().split()))
    cnt += sum(lst)
    mat.append(lst)

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

# 시간
t = 0

def melt() :
    q = deque([(0, 0)])
    visited[0][0] = 1
    # 치즈 수
    cnt = 0
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                # 공기인 경우
                if mat[nx][ny] == 0 :
                    # 치즈가 아닌부분 check -> 0인부분은 모두 치즈
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 치즈인 경우
                elif mat[nx][ny] == 1 :
                    mat[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt

while True :
    t += 1
    visited = [[0]*m for _ in range(n)]
    cnt = melt()
    if cnt == 0 :
        break
    else :
        memory = cnt

print(t-1)
print(memory)