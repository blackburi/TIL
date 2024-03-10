# 자두 나무

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
lst = [0] + [int(input().rstrip()) for _ in range(t)]

# [[첨프 0~w번 했을때 받은 자두의 수] * 총 떨어지는 자두의 횟수 t]
dp = [[0] * (w+1) for _ in range(t+1)]

for i in range(1, t+1) :
    # 1이 나온경우
    if lst[i] == 1 :
        dp[i][0] = dp[i-1][0] + 1
    # 2가 나온 경우
    else : # lst[i] == 2
        dp[i][0] = dp[i-1][0]

    # j는 움직인 횟수를 나타냄(홀수번-> 2번나무, 짝수번-> 1번나무)
    for j in range(1, w+1) :
        # 움직이지 않아도 자두를 받는 경우
        if (lst[i] == 1 and j % 2 == 0) or (lst[i] == 2 and j % 2 == 1) :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        # 움직여야 자두를 받을 수 있는 경우
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[t]))