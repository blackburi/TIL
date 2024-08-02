# 용이 산다

import sys
input = sys.stdin.readline

z = int(input())

for _ in range(z) :
    # 호수, 비가 내리는 날의 수
    n, m = map(int, input().split())
    # 비가 오는 날 / 오지 않는 날을 list로 받기
    rain = list(map(int, input().rstrip().split()))

    # 마시는 물을 저장
    drink = dict()
    # 마셔야 하는 날의 수를 check
    days = 0
    # 불가능한지 가능한지를 체크하는 변수
    flag = 0

    while rain :
        day = rain.pop()

        # 비가 오는 날인 경우
        if day != 0 :
            # 같은 호수에 연속으로 2번 비가 오는경우
            if drink[day] :
                flag = 1
                break
            # 같은 호수에 아직 비가 오지 않은 경우
            else :
                drint[day] = 1
                days += 1
        # 비가 오지 않는 경우
        else : # day == 0
            days -= 1