for _ in range(1, 11) :
    tc = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    hap = []

    # 가로줄의 합
    for i in range(100) :
        sub_hap = 0
        for j in range(100) :
            sub_hap += mat[i][j]
        hap.append(sub_hap)

    # 세로줄의 합
    for j in range(100) :
        sub_hap = 0
        for i in range(100) :
            sub_hap += mat[i][j]
        hap.append(sub_hap)

    # 대각선의 합
    a = 0
    b = 0
    for k in range(100) :
        a += mat[k][k]
        b += mat[k][99-k]
    hap.append(a)
    hap.append(b)

    hap_max = 0
    for k in hap :
        if hap_max < k :
            hap_max = k

    print(f'#{tc} {hap_max}')