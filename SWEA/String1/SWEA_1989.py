T = int(input())

for tc in range(1, T+1) :
    n = list(input())
    m = len(n)
    cnt = 0
    
    for k in range(m//2) :
        if n[k] == n[m-1-k] :
            cnt += 1
    
    if cnt == m//2 :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')