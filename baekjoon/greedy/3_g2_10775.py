# 공항

import sys
input = sys.stdin.readline

# 게이트의 수
g = int(input())
gate = [0]*g
# 비행기의 수
p = int(input())

# 도킹할 수 있는 비행기를 넣는 곳
maxplane = set()

for _ in range(p) :
    k = int(input())
    if k not in maxplane :
        maxplane.add(k)
        continue
    # k in maxplane
    while k > 0 :
        k -= 1
        if k == 0 :
            break
        if k not in maxplane :
            maxplane.add(k)
            break
    
    if k == 0 :
        break

print(len(maxplane))

# 시간 초과 // 60분