# 파리퇴치3

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    mat = []
    for _ in range(m-1) :
        mat.append([0]*(n+2*m-2))
    for _ in range(n) :
        mat.append([0]*(m-1) + list(map(int, input().split())) + [0]*(m-1))
    for _ in range(m-1) :
        mat.append([0]*(n+2*m-2))
    
    pari = 0
    for i in range(m-1, m-1+n) :
        for j in range(m-1, m-1+n) :
            # + 모양
            hap = 0
            for k in range(-m+1, m) :
                hap += mat[i+k][j] + mat[i][j+k]
            hap -= mat[i][j]
            if pari < hap :
                pari = hap

            # X 모양
            hap = 0
            for k in range(-m+1, m) :
                hap += mat[i+k][j+k] + mat[i+k][j-k]
            hap -= mat[i][j]
            if pari < hap :
                pari = hap
    
    print(f'#{tc} {pari}')