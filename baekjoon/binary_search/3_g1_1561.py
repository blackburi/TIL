# 놀이 공원

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
operations = list(map(int, input().rstrip().split()))

if n < m :
    print(n)
else :
    # 이분 탐색
    left, right = 0, 30*2000000000
    t = 0
    
    while left <= right :
        mid = (left + right) // 2
        cnt = m

        for i in range(m) :
            cnt += mid // operations[i]

        # n명을 태울수 있다면
        if cnt >= n :
            right = mid - 1
            t = mid
        else :
            left = mid + 1

    # t-1 에 탑승한 아이들의 숫자를 계산한다.
    cnt = m
    for i in range(m) :
        cnt += (t - 1) // operations[i]

    # t 탑승한 아이를 계산한다.
    for i in range(m) :
        if t % operations[i] == 0 :
            cnt += 1
        if cnt == n :
            print(i+1)
            break