# 공항


import sys
input = sys.stdin.readline

# 게이트의 수
g = int(input())

# 비행기의 수
p = int(input())

planes = []
for _ in range(p) :
    planes.append(int(input().rstrip()))

# 게이트 (1~g번 게이트)
gates = [i for i in range(g+1)]

for plane in planes :
    # i번 비행기가 들어올때 i번 게이트가 비어있는 경우
    if gates[plane] == plane :
        
    # i번 비행기가 들어올때 i번 게이트가 차있는 경우
    else :
        gates[plane] = gates[plane - 1]
















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