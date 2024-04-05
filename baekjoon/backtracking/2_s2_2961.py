# 도영이가 만든 맛있는 음식

# 신맛은 곱, 쓴맛은 합

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n) :
    lst.append((int, input().rstrip().split()))

ans = float('inf')

def dfs(x, s, b) :
    global ans

    if x == n :
        ans = min(ans, abs(s-b))
        return

    ans = min(ans, abs(s-b))

    for i in range(x, n) :
        s *= lst[i][0]
        b += lst[i][1]
        dfs(i+1, s, b)
        s //= lst[i][0]
        b -= lst[i][1]

for i in range(n) :
    dfs(i, lst[i][0], lst[i][1])