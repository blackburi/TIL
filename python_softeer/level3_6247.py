# 자동차 테스트

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

efficiency = list(map(int, input().rstrip().split()))

for _ in range(q) :
    m = int(input())
    
    # m과 같은 수가 있는지 보는 것
    tmp = 0
    # m보다 작은수 개수 저장
    a = 0
    # m보다 큰수 개수 저장
    b = 0

    for i in efficiency :
        if i > m :
            a += 1
        elif i < m :
            b += 1
        else : # i == m
            tmp += 1
    
    if tmp == 0 :
        print(0)
        continue
    else :
        print(a*b)