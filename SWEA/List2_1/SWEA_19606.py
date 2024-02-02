T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    hap = 0
    for i in range(n) :
        hap += mat[i][i]
        hap += mat[i][n-1-i]

    if n % 2 == 1 :
        hap -= mat[(n-1)//2][(n-1)//2]

    print(f'#{tc} {hap}')