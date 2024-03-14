# GBC

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# (총 이동거리, 제한속도)를 list에 담는다
lst = []
a, b = map(int, input().split())
lst.append((a, b))
for i in range(n-1) :
    a, b = map(int, input().split())
    lst.append((a+lst[-1][0], b))

# 검사 구간
check = deque([])
for _ in range(m) :
    c, d = map(int, input().split())
    check.append((c, d))

# 총 이동거리
distance = 0

# 속도 차이의 최댓값
vmax = 0

# lst에서 거리와 비교할 index 변수
idx = 0

while check :
    if idx >= n :
        idx = n-1

    x, y = check.popleft()
    distance += x

    vmax = max(vmax, y - lst[idx][1])

    while distance > lst[idx][0] :
        idx += 1
        vmax = max(vmax, y - lst[idx][1])

    if distance == lst[idx][0] :
        idx += 1

print(vmax)