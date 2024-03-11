# 자동차 테스트

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
efficiency = list(map(int, input().rstrip().split()))
efficiency.sort()

for _ in range(q) :
    m = int(input())
    
    if m not in efficiency :
        print(0)
        continue

    k = efficiency.index(m)
    
    if k == 0 or k == n-1 :
        print(0)
        continue
    
    print(k*(n-k-1))