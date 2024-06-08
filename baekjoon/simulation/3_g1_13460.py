# 구슬 탈출 2

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

# 방문 처리
visited = []

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 이동 횟수
cnt = 0

# 현재 위치를 찾기
def position() :
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n) :
        for j in range(m) :
            if mat[i][j] == 'R' :
                rx, ry = i, j
            if mat[i][j] == 'B' :
                bx, by = i, j
    return rx, ry, bx, by


# 움직였을때
def move(x, y, dx, dy) : # 현재위치(x, y), 움직이는 방향(dx, dy)
    # 많이 움직인 구슬을 알기 위한 변수
    tmp = 0

    # 이동하는 위치가 벽이 아니고, 구멍에 들어가지 않았다면 반복
    # 갈수 있는 만큼 간다.
    while mat[x+dx][y+dy] != '#' and mat[x][y] != 'O' :
        x += dx
        y += dy
        tmp += 1
    return x, y, tmp


# bfs 탐색
def bfs() :
    rx, ry, bx, by = position()

    # 초기 설정
    q = deque([(rx, ry, bx, by, 1)])
    # 방문 처리
    visited.append((rx, ry, bx, by))

    # 조건을 만족한다면 계속 수행
    while q :
        rx, ry, bx, by, cnt = q.popleft()

        # 움직인 횟수가 10회 초과라면 break
        if cnt > 10 :
            break

        # 그렇지 않다면 이동
        for i in range(4) :
            # 빨간 구슬
            mrx, mry, rcnt = move(rx, ry, dx[i], dy[i])
            # 파란 구슬
            mbx, mby, bcnt = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 들어가는 경우 -> 실패
            if mat[mbx][mby] == 'O' :
                continue

            # 빨간 구슬이 구멍에 들어가는 경우  -> 성공
            # 이후 남은 q를 볼 필요가 없음 -> 최소 횟수이기 때문에
            if mat[mrx][mry] == 'O' :
                print(cnt)
                return

            # 두 구슬이 겹쳐진 경우
            if mrx == mbx and mry == mby :
                # 더 많이 움직인 구슬을 원래의 위치(이동하기 전 위치)로 돌려보낸다
                if rcnt > bcnt :
                    mrx -= dx[i]
                    mry -= dy[i]
                else : # rcnt < bcnt, 같은 거리를 이동할수는 없기 때문에 같은 경우 배제
                    mbx -= dx[i]
                    mby -= dy[i]

            # 방문 처리 -> 파란구슬 빨간구슬을 동시에 해줘야 함
            if (mrx, mry, mbx, mby) not in visited :
                visited.append((mrx, mry, mbx, mby))
                q.append((mrx, mry, mbx, mby, cnt+1))

    # 조건을 만족하지 않는 경우
    print(-1)

bfs()