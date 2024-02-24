T = int(input())

for tc in range(1, T+1) :
    # n명의 사람 m초동안 k개 붕어빵
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))

    boong = [0] * (11111//m + 1)
    for i in lst :
        boong[i//m] += 1
    
    for i in range(1, 11111//m+1) :
        boong[i] += boong[i-1]
    
    cnt = 0
    for j in range(11111//m +1) :
        if j*k < boong[j] :
            break
        else :
            cnt += 1
        
    if cnt == 11111//m + 1 :
        print(f'#{tc} Possible')
    else :
        print(f'#{tc} Impossible')