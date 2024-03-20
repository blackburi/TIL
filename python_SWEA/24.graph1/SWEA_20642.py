# 연산

from collections import deque

def bfs() :
    global n, m

    dp[n] = 0
    q = deque([n])
    while q :
        k = q.popleft()
        if k+1 <= 2*m+1 and dp[k+1] == -1 :
            dp[k+1] = dp[k]+1
            q.append(k+1)
        if k-1 >= 1 and dp[k-1] == -1 :
            dp[k-1] = dp[k]+1
            q.append(k-1)
        if 2*k <= 2*m+1 and dp[2*k] == -1 :
            dp[2*k] = dp[k]+1
            q.append(2*k)
        if k-10 >= 10 and dp[k-10] == -1 :
            dp[k-10] = dp[k] +1
            q.append(k-10)
        
        if dp[m] != -1 :
            break


T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    # 시행횟수 저장
    dp = [-1] * (2*m+1)
    bfs()

    print(f'#{tc} {dp[m]}')