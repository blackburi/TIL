# 미세먼지 안녕!

import sys
input = sys.stdin.readline


r, c, t = map(int, input().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(r)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dust = [] # 현재 미세먼지들의 위치
cleaner = [] # 공기청정기의 위치

# 미세먼지의 확산 -> 동시에 일어나야 한다.
def spread() :
    while dust :
        x, y, amount = dust.pop()
        # 몇개의 방향으로 확산이 되었는지 count
        cnt = 0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=r or ny < 0 or ny >= c :
                continue
            if (nx, ny) in cleaner :
                continue
            mat[nx][ny] += amount//5
            cnt += 1
        mat[x][y] -= (amount//5) * cnt

# 공기청정기를 돌리는 함수
def clean(a, b) :
    # 위쪽 회전
    x, y = a, 1
    idx = 1 # 우-> 상-> 좌-> 하
    tmp = 0 # 공기청정기에서 나오는 바람

    while True :
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 벽에 닿는 경우
        if nx == -1 or ny == -1 or nx == r or ny == c :
            idx = (idx-1)%4
            continue
        # 공기청정기로 다시 돌아오는 경우
        if x == a and y == 0 :
            break
        mat[x][y], tmp = tmp, mat[x][y]
        x, y = nx, ny

    # 아래로 회전
    x, y = b, 1
    idx = 1 # 우 -> 하 -> 좌 -> 상
    tmp = 0

    while True :
        nx = x + dx[idx]
        ny = y + dy[idx]
        # 벽에 닿는 경우
        if nx == -1 or ny == -1 or nx == r or ny == c :
            idx = (idx+1)%4
            continue
        # 공기청정기로 다시 돌아오는 경우
        if x == b and y == 0 :
            break
        mat[x][y], tmp = tmp, mat[x][y]
        x, y = nx, ny


for i, line in enumerate(mat) :
    for j, amount in enumerate(line) :
        if amount > 0 :
            dust.append((i, j, amount))
        if amount == -1 :
            cleaner.append((i, j))

# 공기청정기 윗부분, 아랫부분
a, b = cleaner[0][0], cleaner[1][0]

for _ in range(t) :
    spread()
    clean(a, b)
    for i, line in enumerate(mat) :
        for j, amount in enumerate(line) :
            if amount > 0 :
                dust.append((i, j, amount))

answer = 0
for _, _, value in dust :
    answer += value
print(answer)