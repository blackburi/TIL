# 장애물 인식 프로그램

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
mat = []
visited = []

for _ in range(n) :
    lst = list(map(str, input().rstrip()))
    mat.append(lst)

    boolean = []
    for i in range(n) :
        if lst[i] == '0' :
            boolean.append(True)
        else : # lst[i] == '1'
            boolean.append(False)
    
    visited.append(boolean)

# 블록의 수
block = 0

# block의 크기를 담는 list
sizes = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# mat[x][y] == '1', visitied[x][y] is False 인 경우 실행
def find(x, y) :
    global block

    block += 1
    size = 0

    q = deque([(x, y)])

    while q :
        x, y = q.popleft()
        visited[x][y] = True
        size += 1

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= n-1 and 0 <= my <= n-1 :
                if mat[mx][my] == '1' and visited[mx][my] is False :
                    visited[mx][my] = True
                    q.append((mx, my))
    
    sizes.append(size)
    return


for i in range(n) :
    for j in range(n) :
        if mat[i][j] == '1' and visited[i][j] is False :
            find(i, j)

sizes.sort()

print(block)

for size in sizes :
    print(size)