# 퇴사

import sys
input = sys.stdin.readline

n = int(input())

# 마지막날에 하루만에 끝낼수 있는 일이 있다면 count하기 위해 n+1로 생성
dp = [0] * (n+1)

# 각 날마다 받을수 있는 상담 소요시간과 pay
work = []
for _ in range(n) :
    time, pay = map(int, input().rstrip().split())
    work.append((time, pay))

# 일이 완료 가능하다면 갱신
for i in range(n) :
    for j in range(i+work[i][0], n+1) :
        if dp[j] < dp[i] + work[i][1] :
            dp[j] = dp[i] + work[i][1]

# print(max(dp))
print(dp[-1])