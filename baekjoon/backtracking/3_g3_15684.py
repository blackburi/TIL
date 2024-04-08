# 사다리 조작


def check(lst) :
    flag = 0
    stack = deque([])
    lst = deque(lst)

    while lst :
        k = lst.popleft()
        if k == 'N' :
            continue

        if stack == deque([]) :
            stack.append(k)
        else : # stack != []
            if stack[-1] == k :
                stack.pop()
            else : # stack[-1] != k
                flag = 1
                break
    if flag == 1 or stack :
        return False
    else :
        return True


# 살펴볼 세로선, 설치한 다리의 개수
def dfs(col, tmp) :
    global cnt

    if tmp > 3 :
        return

    if col == n-1 :
        if check(mat[col]) :
            cnt = min(cnt, tmp)
        return
    
    if check(mat[col]) :
        dfs(col+1, tmp)
    
    for i in range(h) :
        if mat[col][i] == 'N' and mat[col+1][i] == 'N' :
            mat[col][i], mat[col+1][i] = 'R', 'L'
            if check(mat[col]) :
                dfs(col+1, tmp+1)
            mat[col][i], mat[col+1][i] = 'N', 'N'


# 각 세로선에서 연결된 다리를 보았을때
# N을 제외했을때 LRRL처럼 대칭 구조여야 한다.

import sys
input = sys.stdin.readline
from collections import deque

# 세로, 가로선의 개수, 가로
n, m, h = map(int, input().split())

# 각 세로선에 대해 왼쪽(N), 오른쪽(R), 연결되지 않음(N)을 표시
mat = [['N']*h for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    mat[b-1][a-1] == 'L'
    mat[b][a-1] == 'R'

cnt = float('inf')

dfs(0, 0)

if cnt > 3 :
    print(-1)
else :
    print(cnt)