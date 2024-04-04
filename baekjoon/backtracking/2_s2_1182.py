# 부분수열의 합

import sys
input = sys.stdin.readline


def dfs(x, total) :
    global ans, s

    if x == n :
        if total == s :
            ans += 1
        return
    
    if total == s :
        ans += 1

    for i in range(x, n) :
        total += lst[i]
        dfs(i+1, total)
        total -= lst[i]


n, s = map(int, input().split())
lst = list(map(int, input().rstrip().split()))

# 정답 수
ans = 0

dfs(0, 0)

# 공집합 제외
if s == 0 :
    print(ans-1)
else :
    print(ans)