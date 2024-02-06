T = int(input())

for tc in range(1, T+1) :
    slst = list(map(str, input()))
    dic = {}
    
    for i in slst :
        dic[i] = 0
    
    clst = list(map(str, input()))
    for j in clst :
        if j in slst :
            dic[j] += 1
    
    val = dic.values()
    vmax = 0
    for k in val :
        if k > vmax :
            vmax = k
    
    print(f'#{tc} {vmax}')