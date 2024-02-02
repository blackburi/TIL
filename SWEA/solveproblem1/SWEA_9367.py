T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    carrot = list(map(int, input().split()))
    hap = 0
    hap_list = []

    for i in range(n) :
        if i == 0 :
            hap += 1
        elif carrot[i] > carrot[i-1] :
            hap += 1
        else : # carrot[i] <= carrot[i-1]
            hap_list.append(hap)
            hap = 1
        
        if i == n-1 :
            hap_list.append(hap)
    
    imax = 0
    for i in hap_list :
        if imax < i :
            imax = i
    
    print(f'#{tc} {imax}')