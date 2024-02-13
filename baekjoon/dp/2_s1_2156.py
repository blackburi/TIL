import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)


dp[1] = lst[1]

if n >= 2 :
    dp[2] = lst[1] + lst[2]

if n >= 3 :
    dp[3] = max(lst[1]+lst[2], lst[2]+lst[3], lst[1]+lst[3])

if n >= 4 :
    for i in range(4, n+1) :
        dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i], dp[i-1])

print(dp[n])