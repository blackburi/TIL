# 가장 큰 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))

dp = [0] * n
dp[0] = lst[0]

for i in range(1, n) :
    for j in range(i) :
        if lst[i] > lst[j] :
            dp[i] = max(dp[i], dp[j]+lst[i])
        else :
            dp[i] = max(dp[i], lst[i])

print(max(dp))