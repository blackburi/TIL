import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001
dp[0] = 1
dp[1] = 1

for i in range(2, 1000001) :
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    if i == n :
        break

print(dp[n])