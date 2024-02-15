T = int(input())

for tc in range(1, T+1) :
    # n : 화덕 크기, m : 총 피자수
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(m) :
        lst[i] = [lst[i], i]
    
    grill = lst[:n]
    lst = lst[n:]
    
    while True :
        for i in range(n) :
            grill[i][0] //= 2
            if grill[i][0] == 0 and lst :
                grill[i] = lst.pop(0)
            elif grill[i][0] == 0 and len(lst) == 0 :
                cnt = 1
        
        cnt = 0
        for j in range(n) :
            if grill[j][0] not in [0, 1] :
                break
            else :
                cnt += 1
        
        if cnt == n :
            break
    
    max_pizza = 0
    idx = -1
    for i in range(n) :
        if max_pizza <= grill[i][0] :
            max_pizza = grill[i][0]
            idx = grill[i][1]

    print(f'#{tc} {idx+1}')