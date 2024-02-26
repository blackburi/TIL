import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
mat = []
# 탈출하는데 걸리는 최단시간
time = 0

# 지훈이가 지나온 곳
jh = deque([])

# 불이 번지는 곳
fire = deque([])

for i in range(r) :
    sub = list(input().rstrip())
    for j in range(c) :
        if sub[j] == 'J' :
            jh.append([i, j])
        if sub[j] == 'F' :
            fire.append([i, j])
    mat.append(sub)

def bfs() :
    global fire, jh, time

    while True :
        time += 1
        tmp = []
        # 불이 지나가는 곳
        while fire :
            x, y = fire.popleft()
            for i in range(4) :
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx <= r-1 and 0 <= my <= c-1 :
                    # 'x'는 지훈이가 지나간 곳 - 지훈이가 재방문하는것을 방지
                    if mat[mx][my] == '.' or mat[mx][my] == 'x' :
                        tmp.append([mx, my])
        fire = deque(tmp) # tmp는 이미 list

        # 지훈이가 지나가는 곳
        tmp = []
        while jh :
            x, y = jh.popleft()
            # 가장자리에 도착하면 종료
            if x == 0 or y == 0 or x == r-1 or y == c-1 :
                return time

            for i in range(4) :
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx <= r-1 and 0 <= my <= c-1 and mat[mx][my] == '.' :
                    tmp.append([mx, my])
                    mat[x][y] = 'x'
                    mat[mx][my] = 'j'
        jh = deque(tmp) # tmp는 이미 list

        # 지훈이가 없다면 탈출 불가능
        if not jh :
            return False

# 함수 bfs()는 False와 time을 반환
if bfs() :
    print(time)
else :
    print('IMPOSSIBLE')