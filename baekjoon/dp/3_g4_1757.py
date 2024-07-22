# 달려달려

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [0] + [int(input().rstrip()) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1) :
    # 1초전 달린 거리 + 1초 달린 거리
    for j in range(1, m+1) :
        dp[i][j] = dp[i-1][j-1] + lst[i]
    # 반드시 달린 시간 >= 쉰 시간이어야 최대 거리가 된다
    for k in range(1, m+1) :
        if i-k < 0 :
            break
        # i초 달린거리의 최대
        # dp[i][0], k초만큼 쉰 사람, 다 쉰사람
        dp[i][0] = max(dp[i][0], dp[i-k][k], dp[i-k][0])

print(dp[n][0])