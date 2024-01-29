T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    fun = list(map(int, input().split()))

    lst = []
    for i in range(N-M+1) :
        tmp = 0
        for j in range(i, M+i) :
            tmp += fun[j]
        lst.append(tmp)

    num_max = lst[0]
    num_min = lst[0]

    for p in lst :
        if p > num_max :
            num_max = p
        else :
            continue
    
    for q in lst :
        if q < num_min :
            num_min = q
        else :
            continue
    
    print(f'#{tc} {num_max - num_min}')