# 전기버스2

T = int(input())

for tc in range(1, T+1) :
    # [정류장수, 배터리]
    lst = list(map(int, input().rstrip().split()))

    # 정류장 수
    n = lst.pop(0)

    # dp를 이용하여 최솟값을 비교
    dp = [-1] * n

    # 도착 지점 제외 dp를 돌린다
    for i in range(n-1) :
        if i == 0 :
            dp[i] = 0
            for j in range(0, lst[i]+1) :
                dp[j] = 0
            continue
        
        # 만들어둔 dp의 길이보다 작은 경우
        if i + lst[i] <= n-1 :
            for j in range(i+1, i+lst[i]+1) :
                if dp[j] == -1 :
                    dp[j] = dp[i] + 1
                else : # dp[j] != -1
                    dp[j] = min(dp[j], dp[i]+1)
        else : # i + lst[i] >= n
            for j in range(i+1, n) :
                if dp[j] == -1 :
                    dp[j] = dp[i] + 1
                else : # dp[j] != -1
                    dp[j] = min(dp[j], dp[i] + 1)
    
    print(f'#{tc} {dp[-1]}')