from sys import stdin
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
board = []
time = 0

# 지훈이와 불난 곳 저장할 곳
F = deque()
J = deque()

# 지훈이와 불난곳 찾기
for i in range(r):
    sub = list(stdin.readline().rstrip())
    for j in range(c):
        if sub[j] == 'J':
            J.append((i, j))
        if sub[j] == 'F':
            F.append((i, j))
    board.append(sub)


def bfs():
    global F, J, time

    while True :
        time += 1
        tmp = []
        while F:
            x, y = F.popleft()
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if -1 < mx < r and -1 < my < c:
                    if board[mx][my] == '.' or board[mx][my] == '$':
                        tmp.append((mx, my))
                        board[mx][my] = 'F'
        F = deque(tmp)

        tmp = []
        while J:
            x, y = J.popleft()
            if x == 0 or y == 0 or x == r - 1 or y == c - 1:
                return time

            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < r and 0 <= my < c and board[nx][ny] == '.':
                    tmp.append((nx, ny))
                    board[x][y] = '$'
                    board[nx][ny] = 'J'

        J = deque(tmp)
        if not J:
            return False


if bfs():
    print(time)
else:
    print('IMPOSSIBLE')