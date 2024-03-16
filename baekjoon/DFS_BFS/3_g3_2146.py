# 다리 만들기

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]

# 방문 체크
visited = [[False] * n for _ in range(n)]
# 섬 넘버링
num = 1
# 다리 길이의 최솟값
ans = sys.maxsize

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 섬을 구분하는 함수
def land(x, y) :
    global num

    q = deque([(x, y)])
    while q :
        x, y = q.popleft()
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= n-1 and visited[mx][my] is False and mat[mx][my] == '1' :
                visited[mx][my] = True
                mat[mx][my] = num
                q.append((mx, my))

# 다리 길이의 최단길이
def distance(v) :
    q = deque()

    # -1로 설정하는 이유는 섬의 가장자리가 아닌 섬의 내부 땅 때문
    # 내부의 땅은 바로 옆까지 거리를 0으로 생각
    dis = [[-1] * n for _ in range(n)]

    # num = v인 섬을 check
    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == v :
                dis[i][j] = 0
                q.append((i, j))

    while q :
        x, y = q.popleft()
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]

            if 0 <= mx <= n-1 and 0 <= my <= n-1 :
                # 다른 섬과 연결될 경우
                if mat[mx][my] != '0' and mat[mx][my] != v :
                    return dis[x][y]
                # 물일 경우
                elif mat[mx][my] == '0' and dis[mx][my] == -1 :
                    dis[mx][my] = dis[x][y] + 1
                    q.append((mx, my))
        
    return sys.maxsize

# 섬을 먼저 구분
for i in range(n) :
    for j in range(n) :
        if mat[i][j] == '1' and visited[i][j] is False :
            visited[i][j] = True
            mat[i][j] = num
            land(i, j)
            num += 1

# 최단 거리
for v in range(1, num+1) :
    ans = min(ans, distance(v))

print(ans)