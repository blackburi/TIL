# 안전운전을 도와줄 차세대 지능형 교통시스템

# 무조건 신호가 주어진다면 경로 또한 정해짐
# 완전 탐색으로 생각 -> 이후 길이 막혀있다면 시간을 끝까지 기다릴 필요 없음

# 자율 주행 자동차의 시작은 mat[0][0]에서 시작
# 자율주행자동차의 경우 교차로에서 갈수 있는 경로가 있다면 "반드시" 가야한다
# 교차로에 도착하면(신호가 맞다면) 바로 방문 check

import sys
input = sys.stdin.readline
from collections import deque

# 신호는 0초부터 시작 즉 1초면 한번 바뀜
# dictionary 원소 => 신호 number : (자동차가 들어오는 방향, dx, dy, 자동차가 나가는 방향)
rgb = {1 : [(-1, 0), (0, 1), (1, 0)],
       2 : [(0, -1), (-1, 0), (0, 1)],
       3 : [(-1, 0), (0, -1), (1, 0)],
       4 : [(0, -1), (1, 0), (0, 1)],
       5 : [(-1, 0), (0, 1)],
       6 : [(0, -1), (-1, 0)],
       7 : [(1, 0), (0, -1)],
       8 : [(1, 0), (0, 1)],
       9 : [(0, 1), (1, 0)],
       10 : [(-1, 0), (0, 1)],
       11 : [(-1, 0), (0, -1)],
       12 : [(0, -1), (1, 0)]
       }

# 들어오는 자동차의 방향 (신호 number : 자동차가 들어와야 하는 방향)
directions_in = {1 : 'r',
                 2 : 'u',
                 3 : 'l',
                 4 : 'd',
                 5 : 'r',
                 6 : 'u',
                 7 : 'l',
                 8 : 'd',
                 9 : 'r',
                 10 : 'u',
                 11 : 'l',
                 12 : 'd'
                 }

# 바뀌는 자동차 방향
def direction(x, y) :
    if x == -1 and y == 0 :
        return 'u'
    elif x == 0 and y == 1 :
        return 'r'
    elif x == 1 and y == 0 :
        return 'd'
    elif x == 0 and y == -1 :
        return 'l'

# n, 시간
n, t = map(int, input().split())

# 신호들의 집합
mat = [[0] * n for _ in range(n)]
for i in range(n**2) :
    mat[i//n][i%n] = tuple(map(int, input().rstrip().split()))

# 방문 체크
# 한 교차로를 4개의 방문체크를 두는 이유는
# 4초마다 모든 교차로가 cycle (bfs로 돌리기 때문)
# -> 같은 신호에 들어온경우 이전에 check했다면 또다시 check할 필요 X "backtracking"
visited = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]

# 차가 들어오는 방향도 신경을 써야한다
# directions // u(위), d(아래), l(좌), r(우)

# time = 출발한 순간으로부터의 시간
# time == t+1이 되는 순간 break

def bfs() :
    # start_row, start_col, time, start_direction = 0, 0, 0, 'u'
    visited[0][0][0] = 1
    q = deque([[0, 0, 0, 'u']])
    while q :
        # out_dir = 자동차의 마지막 이동 방향
        r, c, sec, out_dir = q.popleft()

        for (i, j) in rgb[mat[r][c][sec%4]]:
            in_dir = directions_in[mat[r][c][sec%4]]
            mr = r + i
            mc = c + j
            if 0 <= mr <= n-1 and 0 <= mc <= n-1 and in_dir == out_dir and visited[mr][mc][(sec+1)%4] == 0 and sec+1 <= t :
                # 방문check
                visited[mr][mc][(sec+1)%4] = 1
                # 자동차 진행방향 최신화(out_dir -> in_dir)
                q.append([mr, mc, sec+1, direction(i, j)])


cnt = 0

if 'u' == directions_in[mat[0][0][0]] :
    visited[0][0][0] = 1

bfs()
for i in range(n) :
    for j in range(n) :
        if 1 in visited[i][j] :
            cnt += 1
print(cnt)