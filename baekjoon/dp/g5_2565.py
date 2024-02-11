# A의 전깃줄 번호를 작은 순서대로 정렬
# 각 A와 연결된 B의 숫자들은 순차적으로 커져야 한다.

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 같은 위치에는 두개 이상의 전깃줄이 연결될수 없음 - 문제 조건
# lst.sort(key = lambda x : (x[0], x[1]))로 두번 정렬할 필요 없다.
lst.sort()

dp = [1] * n

for i in range(1, n) :
    for j in range(i) :
        if lst[j][1] < lst[i][1] :
            dp[i] = max(dp[i], dp[j] + 1)


print(n - max(dp))