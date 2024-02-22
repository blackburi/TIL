import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

cnt = 0 # 그림의 수
area = 0 # 그림의 최대 넓이

stack = deque([])
for i in range(n) :
    for j in range(m) :
        if mat[i][j] == 1 :
            stack.append([i, j])

while stack :
    a, b = stack.popleft()
    cnt += 1
    tmp = 0
    sub = deque([[a, b]])
    while sub :
        x, y = sub.popleft()
        tmp += 1
        for p, q in [[1, 0], [0, 1], [-1, 0], [0, -1]] :
            if [x+p, y+q] in stack :
                stack.remove([x+p, y+q])
                sub.append([x+p, y+q])
    
    if area < tmp :
        area = tmp

print(cnt)
print(area)