import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
mat = []
time = 0

# 지훈이와 불난 곳 저장할 곳
fire = deque()
jh = deque()

# 지훈이와 불난곳 찾기
for i in range(r):
    sub = list(input().rstrip())
    for j in range(c):
        if sub[j] == 'J':
            jh.append((i, j))
        if sub[j] == 'F':
            fire.append((i, j))
    mat.append(sub)


def bfs():
    global fire, jh, time

    while True :
        time += 1
        tmp = []
        # 불이 번지는 것
        while fire:
            x, y = fire.popleft()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < r and 0 <= my < c:
                    if mat[mx][my] == '.' or mat[mx][my] == '/':
                        tmp.append((mx, my))
                        mat[mx][my] = 'F'
        fire = deque(tmp)

        tmp = []
        # 지훈이가 도망가는 과정
        while jh:
            x, y = jh.popleft()
            if x == 0 or y == 0 or x == r - 1 or y == c - 1:
                return time

            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < r and 0 <= my < c and mat[mx][my] == '.':
                    tmp.append((mx, my))
                    # '/'는 지훈이가 방문한곳을 방문 처리
                    mat[x][y] = '/'
                    # 지훈이의 현재 위치
                    mat[mx][my] = 'J'

        jh = deque(tmp)
        if not jh:
            return False


if bfs():
    print(time)
else:
    print('IMPOSSIBLE')