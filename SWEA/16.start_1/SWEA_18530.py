T = int(input())

for tc in range(1, T+1) :
    n = float(input())
    p = -1
    ans = []
    while n :
        if 2**p <= n :
            n -= 2**p
            ans.append('1')
        else : # 2**p > n
            ans.append('0')
        p -= 1

        if len(ans) >= 13 :
            break
    
    if len(ans) <= 12 :
        print(f'#{tc} {"".join(ans)}')
    else :
        print(f'#{tc} overflow')