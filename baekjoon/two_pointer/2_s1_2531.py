# 회전 초밥

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

plates = [int(input().rstrip()) for _ in range(n)]

ans = 0

for i in range(n) :
    if i+k <= n :
        sub = set(plates[i:i+k])
    else : # i+k > n
        sub = set(plates[i:]) | set(plates[:(i+k)%n])

    sub.add(c)
    ans = max(ans, len(sub))

print(ans)