# 차량 정비소

from collections import deque

T = int(input())

for tc in range(1, T+1) :
    # 접수 창구, 정비창구, 고객수, 접수창구 번호, 정비창구 번호
    n, m, k, a, b = map(int, input().split())

    # 접수창구 n개
    submit = list(map(int, input().split()))
    for i in range(n) :
        # 손님 번호, 이용시간, 필요시간
        submit[i] = [0, 0, submit[i]]
    # 접수창구 손님이 있는지 없는지 확인
    submit_v = [False] * n

    # 정비 창구 m개
    fix = list(map(int, input().split()))
    for i in range(m) :
        # 손님 번호, 이용시간, 필요시간
        fix[i] = [0, 0, fix[i]]
    # 접수창구 손님이 있는지 없는지 확인
    submit_f = [False] * n

    # 고객 방문시간
    time = list(map(int, input().split()))
    time.sort()
    for i in range(k) :
        # 손님 번호, 방문 시간
        time[i] = [i+1, time[i]]

    # a접수창구, b정비창구를 이용한 고객 number
    ans = []

    # 접수 창구 -> 정비 창구를 가는 손님의 list
    waiting = deque([])


    # 손님들이 빠질때까지 전부 