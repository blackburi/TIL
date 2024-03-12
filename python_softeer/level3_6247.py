# 자동차 테스트

import sys
input = sys.stdin.readline

# n 연비의 개수
n, q = map(int, input().split())

efficiency = list(map(int, input().rstrip().split()))
efficiency.sort()

for _ in range(q) :
    m = int(input())

    if m == efficiency[0] or  m == efficiency[-1] :
        print(0)
        continue

    # index
    start = 0
    end = n-1 

    # 값이 존재하는지를 check하는 변수
    check = -1

    while start < end :
        tmp = (start + end)//2


        if m > efficiency[tmp] :
            start = tmp+1
        elif m < efficiency[tmp] :
            end = tmp
        else : # m == efficiency[tmp]
            check = tmp
            break
    
    if check == -1 or check == 0 or check == n-1 :
        print(0)
    else : # check != 0
        print(tmp*(n-tmp-1))