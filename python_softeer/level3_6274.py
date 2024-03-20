# 안전운전을 도와줄 차세대 지능형 교통시스템

# 무조건 신호가 주어진다면 경로가 바뀜
# 완전 탐색으로 생각 -> 이후 길이 막혀있다면 시간을 끝까지 가디릴필요 없음
# 더이상 갈 길이 없다면 break걸고 backtracking
# 셀수 있는 경우에 대해서만 count 및 max function을 이용하여 비교

# 자율 주행 자동차의 시작은 mat[0][0]에서 시작
# 한경로에 대해서의 지나는 교차로 수의 최댓값을 구하는 문제가 아님
# 시간 내에 갈수 있는 모든 경로에 있는 교차로를 check
# 방문 check를 통해서 False -> True로 바뀔 경우에만 check
# 자율주행자동차의 경우 교차로에서 갈수 있는 경로가 있다면 "반드시" 가야한다
# 갈수 없는 경우는 신호가 바뀌어 갈수 있을때까지 대기
# 교차로에 도착하면 바로 방문 check

import sys
input = sys.stdin.readline
from collections import deque

# 신호는 0초부터 시작 즉 1초면 한번 바뀜
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

# time = 출발한 순간으로부터의 시간
# time == t가 되는 순간 break

def bfs() :
    # start_row, start_col, time = 1, 0, 0
    visited[0][0][0] = 1
    q = deque([[0, 0, 0]])
    while q :
        r, c, sec = q.popleft()
        if sec > t :
            continue
        for (i, j) in rgb[mat[r][c][sec%4]]:
            mr = r + i
            mc = c + j
            if 0 <= mr <= n-1 and 0 <= mc <= n-1 and visited[mr][mc][(sec+1)%4] == 0 and sec+1 <= t :
                visited[mr][mc][(sec+1)%4] = 1
                q.append([mr, mc, sec+1])


cnt = 0

if n == 1 :
    print(1)
else : # n != 1
    bfs()
    for i in range(n) :
        for j in range(n) :
            if 1 in visited[i][j] :
                cnt += 1
    print(cnt)