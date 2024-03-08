# 퇴사

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

# 각 날마다 받을수 있는 상담 소요시간과 pay
work = [(0, 0)]
for _ in range(n) :
    time, pay = map(int, input().rstrip().split())
    work.append((time, pay))

for i in range(n+1) :
    if i + work[i][0] - 1 <= n :
        dp[i + work[i][0]-1] = max(dp[i + work[i][0]-2], dp[i] + work[i][1])