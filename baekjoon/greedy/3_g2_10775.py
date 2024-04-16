# 공항

import sys
input = sys.stdin.readline

# 게이트의 수
g = int(input())
gate = [0]*g
# 비행기의 수
p = int(input())

for _ in range(p) :
    k = int(input().rstrip())
    if gate[k] == 0 :
        gate[k] == 1
    else : # gate[k] == 1
        while True :
            