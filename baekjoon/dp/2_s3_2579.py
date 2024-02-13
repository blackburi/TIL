import sys
input = sys.stdin.readline

n = int(input())

# 계단 숫자
lst = [0] * 301 
for i in range(1, n+1) :
    lst[i] = int(input())

dp = [0] * 301
dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
# 계단을 연속해서 3개 밟을수 없기 때문에
dp[3] = max(lst[1] + lst[3], lst[2] + lst[3])

for j in range(4, n+1) :
    dp[j] = max(dp[j-3] + lst[j-1], dp[j-2]) + lst[j]

print(dp[n])