T = int(input())

for tc in range(1, T+1) :
    N, M = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for _ in range(N)]

    hap = []
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            k = 0
            for p in range(M) :
                for q in range(M) :
                    k += mat[i + p][j + q]
            hap.append(k)

    hmax = 0
    for r in hap :
        if hmax < r :
            hmax = r

    print(f'#{tc} {hmax}')