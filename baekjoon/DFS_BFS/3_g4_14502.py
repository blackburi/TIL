# 연구소

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]

# 벽을 세울수 있는 list
walls = []
# virus가 있는 list
q = []

for i in range(n) :
    for j in range(m) :
        if mat[i][j] == '0' :
            walls.append([i, j])

        if mat[i][j] == '2' :
            q.append([i, j])

# 안전한 구역이 가장 넓을때의 변수
safe_area = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def virus(matrix) :
    global safe_area

    tmp_q = deque(copy.deepcopy(q))
    
    while tmp_q :
        x, y = tmp_q.popleft()
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= m-1 and matrix[mx][my] == '0' :
                matrix[mx][my] = '2'
                tmp_q.append([mx, my])

    # 안전구역 면적
    safe = 0
    for i in range(n) :
        safe += matrix[i].count('0')
    safe_area = max(safe_area, safe)


# 벽 3개 선택
for wall in combinations(walls, 3) :
    tmp_mat = copy.deepcopy(mat)
    for x, y in wall :
        tmp_mat[x][y] = '1'
    virus(tmp_mat)

print(safe_area)



########################################################################
# 시간초과
########################################################################


import sys
input = sys.stdin.readline
from collections import deque
import copy


n, m = map(int, input().rstrip().split())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]

# 안전한 구역이 가장 넓을때의 변수
safe_area = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 벽 3개를 선택
def wall(cnt) :
    if cnt == 3 :
        virus()
        return
    
    for i in range(n) :
        for j in range(m) :
            if mat[i][j] == '0' :
                mat[i][j] = '1'
                wall(cnt+1)
                mat[i][j] = '0'

# wall()에서 벽을 세웠으면 virus()로 퍼뜨림
def virus() :
    global safe_area

    q = deque()

    tmp_mat = copy.deepcopy(mat)

    for i in range(n) :
        for j in range(m) :
            if tmp_mat[i][j] == '2' :
                q.append([i, j])

    while q :
        x, y = q.popleft()

        for i in range(4) :
            mx = x+dx[i]
            my = y+dy[i]

            if 0 <= mx <= n-1 and 0 <= my <= m-1 :
                if tmp_mat[mx][my] == '0' :
                    tmp_mat[mx][my] = '2'
                    q.append([mx, my])

    tmp = 0
    for i in range(n) :
        for j in range(m) :
            if tmp_mat[i][j] == '0' :
                tmp += 1
    
    safe_area = max(safe_area, tmp)

wall(0)
print(safe_area)