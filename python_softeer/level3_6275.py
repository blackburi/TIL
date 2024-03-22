# 로봇이 지나간 경로

# 출력형식
# 처음 로봇을 두어야 하는 위치 (a, b)
# 처음 로봇이 바라보는 방향 (>는 동쪽, <는 서쪽, v는 남쪽, ^는 북쪽)
# 명령어출력 (단 명령어의 개수는 최소여야 한다.)


import sys
input = sys.stdin.readline

h, w = map(int, input().split())
mat = [list(input()) for _ in range(h)]

# 시작점 or 도착점이 정해져있는 경우를 check하는 변수
flag = 0

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작점 탐색
for i in range(h) :
    for j in range(w) :
        if mat[i][j] == '#' :
            cnt = 0
            for k in range(4) :
                mx = i + dx[k]
                my = j + dy[k]
                if 0 <= mx < h and 0 <= my < w and mat[mx][my] == '#' :
                    cnt += 1
            
            if cnt == 1 :
                start_x, start_y = i, j
                break

print(start_x+1, start_y+1)

for i in range(4) :
    mx = start_x + dx[i]
    my = start_y + dy[i]
    if 0 <= mx < h and 0 <= my < w and mat[mx][my] == '#' :
        if i == 0 :
            print('^')
        elif i == 1 :
            print('>')
        elif i == 2 :
            print('v')
        else : # i == 3
            print('<')

        direction = i

path = []

# 우회전을 해야 하는 경우 -> 여기에 없다면 반드시 좌회전
right_direction = [(0, 1), (1, 2), (2, 3), (3, 0)]

while True :
    
    for i in range(4) :
        mx = start_x + dx[i]
        my = start_y + dy[i]
        if (direction, i) in [(0, 2), (2, 0), (1, 3), (3, 1)]:\
            continue
        if 0 <= mx < h and 0 <= my < w and mat[mx][my] == '#' :
            if direction == i :
                path.append('A')
            elif (direction, i) in right_direction :
                path.append('RA')
            else :
                path.append('LA')
            direction = i
            start_x += 2*dx[i]
            start_y += 2*dy[i]
            break
    else :
        break

print(''.join(path))