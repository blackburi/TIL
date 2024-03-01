import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

mat = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 방문체크
# 0은 벽부수기 사용 하기 전, 1은 벽 부수기 사용 후
# 앞은 벽부수기를 사용했는지, 뒤는 이동한 거리
visited = [[0, 0] * m for _ in range(n)]

# [x, y] : 현재 위치, z : 벽을 뚫은 횟수, w : 이동한 거리
def move(x, y, z, w) :
    q = deque([])
    q.append([x, y, z, w])

    while q :
        # [a, b] 현재위치, c 벽을 뚫은 횟수, d 이동거리
        a, b, c, d = q.popleft()

        # 끝에 도착했다면 이동거리 값을 반환
        if a == n-1 and b == m-1 :
            return d
        
        for i in range(4) :
            mx = a + dx[i]
            my = b + dy[i]
            if mx < 0 or my < 0 or mx >= n or my > m :
                continue
                
            # 다음칸으로 이동했을 때 벽이 아닌 경우
            if mat[mx][my] == 1 and visited[mx][my][1] == 0 :
                visited