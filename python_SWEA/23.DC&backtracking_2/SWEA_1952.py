# 수영장

import copy

# 3달 이용권을 비교하기 위한 함수
def three(x) :
    global month3, total

    total = min(total, sum(dp))

    if x == 13 :
        return

    for i in range(x, 13) :
        if i < 11 :
            if sum(dp[i:i+3]) > month3 :
                lst = copy.deepcopy(dp[i:i+3])
                dp[i:i+3] = [month3, 0, 0]
                three(i+3)
                dp[i:i+3] = copy.deepcopy(lst)
        else : # x == 11 or x == 12
            if sum(dp[i:13]) > month3 :
                lst = copy.deepcopy(dp[i:13])
                dp[i:13] = [month3] + [0] * (12-i)
                three(13)
                dp[i:13] = copy.deepcopy(lst)


T = int(input())

for tc in range(1, T+1) :
    day, month1, month3, year = map(int, input().split())

    use = [0] + list(map(int, input().split()))

    dp = [0] * 13

    # 모든 달에 일일 이용권과 한달 이용권을 먼저 비교
    for i in range(1, 13) :
        dp[i] = min(month1, use[i] * day)

    total = sum(dp)
    # 세달 이용권 비교
    three(1)

    # 1년 이용권 비교
    if total <= year :
        print(f'#{tc} {total}')
    else : # sum(dp) > year :
        print(f'#{tc} {year}')