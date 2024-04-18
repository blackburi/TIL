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
        return plane
    
    # 동일하지 않음 -> 차있음 -> 앞쪽에서 찾아야함
    gates[plane] = find(gates[plane])
    return gates[plane]

for plane in planes :
    # gate가 가득차서 도킹이 불가능한 경우
    if find(plane) == 0 :
        break
            
    # gate가 남아서 도킹이 가능한 경우
    gates[find(plane)] = gates[find(plane)-1]
    ans += 1

print(ans)