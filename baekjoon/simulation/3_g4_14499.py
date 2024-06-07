# 주사위 굴리기

# 동1, 서2, 북3, 남4

import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

# 지도
mat = []

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

# 윗면, 뒷면, 오른쪽면, 앞면, 왼쪽면, 바닥면
dice = [0, 0, 0, 0, 0, 0]

# 주사위가 움직였을때 -> 주사위 면을 갱신
def move(dir) :
    global dice
    top, back, right, front, left, bottom = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if dir == 1 : # 동1
        dice = [left, back, top, front, bottom, right]
    elif dir == 2 : # 서2
        dice = [right, back, bottom, front, top, left]
    elif dir == 3 : # 북3
        dice = [front, top, right, bottom, left, back]
    else : # dir == 4, 남4
        dice = [back, bottom, right, top, left, front]

# 지도 완성
for _ in range(n) :
    mat.append(list(map(int, input().rstrip().split())))

commands = list(map(int, input().rstrip().split()))

for i in commands :
    x += dx[i-1]
    y += dy[i-1]

    # 지도 밖으로 벗어나는 경우
    if x < 0 or x >= n or y < 0 or y >= m :
        x -= dx[i-1]
        y -= dy[i-1]
        continue

    move(i)

    # 지도의 숫자가 0인 경우
    if mat[x][y] == 0 :
        # 주사위의 바닥면을 지도에 복사
        mat[x][y] = dice[-1]
    # 지도의 숫자가 0이 아닌 경우
    else :
        # 지도의 숫자를 주사위 바닥면에 복사
        dice[-1] = mat[x][y]
        # 지도의 숫자를 0으로 갱신
        mat[x][y] = 0

    print(dice[0])