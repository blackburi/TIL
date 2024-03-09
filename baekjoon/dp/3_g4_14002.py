# 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline
import copy

n = int(input())
lst = list(map(int, input().rstrip().split()))

dp = [1] * n

# 가장 긴 증가하는 부분 수열의 길이
for i in range(n) :
    for j in range(i) :
        if lst[i] > lst[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 가장 긴 증가하는 부분 수열을 찾기
length = max(dp)
for i in range(n) :
    if length == dp[i] :
        idx = i

# 수열을 필요한 부분까지 자름
# reverse를 하는 이유는 length에 맞춰서 숫자를 뽑기 위해
# (작은수부터 뽑으면 꼬일수 있음)
sub = lst[:idx+1]
sub.reverse()
# dp또한 필요한 부분까지 자름
dp = dp[:idx+1]
dp.reverse()

ans = []

# 조건에 맞으면 length를 1씩 줄여가며 동일한 경우 수를 ans에 넣어준다
for i in range(idx+1) :
    if length == dp[i] :
        length -= 1
        ans.append(sub[i])

ans.reverse()

print(*ans)