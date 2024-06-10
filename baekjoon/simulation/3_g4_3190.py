# 뱀

import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
k = int(input())

# 0행 0열이 없기 때문에 index를 맞추기 위해 n+1로 통일
board = [[0]*(n+1) for _ in range(n+1)]
# 사과의 위치를 표시 -> 빈칸 0, 뱀의 위치 -1, 사과의 위치 1
for _ in range(k) :
    x, y = map(int, input().rstrip().split())
    board[x][y] = 1

direction_count = int(input())
directions = {}
for _ in range(direction_count) :
    time, direction = input().rstrip().split()
    directions[int(time)] = direction

# game over가 되지 않고 지속되는 시간
times = 0

# 뱀은 처음 오른쪽으로 이동 시작
# L : 왼쪽으로 돈다(-1), D : 오른쪽으로 돈다(+1)
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
# 시작 방향
dir = 0

# 뱀의 현재 위치
x, y = 1, 1
board[x][y] = -1

# 뱀이 차지하고 있는 좌표
snakes = deque([(1, 1)])

while True :
    mx = x + dx[dir]
    my = y + dy[dir]

    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우
    if mx <= 0 or my <= 0 or mx > n or my > n or ((mx, my) in snakes) :
        break

    # 이동 후 해당 칸에 사과가 없을 경우 -> 꼬리를 제외
    if board[mx][my] != 1 :
        i, j = snakes.popleft()
        board[i][j] = 0

    # 이동
    x, y = mx, my
    board[x][y] = -1
    snakes.append((x, y))
    times += 1

    # 방향 전환 정보가 있는 시간의 경우
    if times in directions.keys() :
        if directions[times] == "D" :
            dir = (dir+1) % 4
        else : # directions[times] == "L"
            # 원래는 (dir-1) % 4, 그러나 dir == 0 인 경우를 위해 모듈로 연산 적용
            dir = (dir+3) % 4

# 게임은 마지막 뱀이 이동하고 끝남 -> +1을 해줘야 한다.
print(times+1)