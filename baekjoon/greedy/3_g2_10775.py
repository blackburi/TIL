# 공항

import sys
input = sys.stdin.readline

# 게이트의 수
g = int(input())

# 비행기의 수
p = int(input())

planes = [int(input().rstrip()) for _ in range(p)]

# 게이트 (1~g번 게이트) : 초기에 자기 자신의 값을 갖는다.
gates = [i for i in range(g+1)]

# 도킹 가능한 비행기의 수
ans = 0

# 비행기가 들어왔을때 도킹이 가능한 곳을 큰곳부터 찾는 함수
def find(plane) :
    # gates의 값이 plane과 동일 -> 아직 비어있음
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