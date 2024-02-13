import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] + [1] * n

for i in range(2, n+1) :
    for j in range(i) :
        if lst[i] > lst[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))