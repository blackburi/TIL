# 문자열 2개의 부분 수열이 되는 것중 가장 긴것
# 문자를 순서대로 하나하나 비교
# 문자열 X, Y가 있다고 하고
# X의 i번째, Y의 j번째 문자열까지의 정답을 ans(X(i), Y(j))라고 하자
# if X[i] == Y[j] :
#     ans(X(i), Y(j)) = ans(X(i-1), Y(j-1)) + 1
# else : # X[i] != Y[j]
#     # i-1, j-1을 동시에 하지 않는 이유는 Y(j) == X(i-1) 또는 Y(j-1) == X(i)일수 있기 때문에
#     ans(X(i), Y(j)) = max(ans(X(i-1), Y(j)), ans(X(i), Y(j-1)))

import sys
input = sys.stdin.readline

# 이중 for문의 indexerror를 막기 위해서 앞에 빈공백을 넣어준다.
lst_1 = [' '] + list(input().rstrip())
lst_2 = [' '] + list(input().rstrip())

dp = [[0] * len(lst_2) for _ in range(len(lst_1))]



for i in range(1, len(lst_1)) :
    for j in range(1, len(lst_2)) :
        if lst_1[i] == lst_2[j] :
            dp[i][j] = dp[i-1][j-1] + 1
        else : # lst_1[i] != lst_2[j]
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])