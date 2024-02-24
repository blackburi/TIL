for tc in range(1, 11) :
    n = int(input())
    mat = [list(map(str, input())) for _ in range(8)]

    cnt = 0

    # 가로줄
    for i in range(8) :
        for j in range(9-n) : 
            tmp = 0
            for r in range(n//2) :
                if mat[i][j + r] == mat[i][j+n-1-r] :
                    tmp += 1
                else :
                    break
            if tmp == n //2 :
                cnt += 1
    
    # 세로줄
    for p in range(8) :
        for q in range(9-n) :
            tmp = 0
            for r in range(n//2) :
                if mat[q + r][p] == mat[q+n-1-r][p] :
                    tmp += 1
                else :
                    break
            if tmp == n //2 :
                cnt += 1
    
    print(f'#{tc} {cnt}')