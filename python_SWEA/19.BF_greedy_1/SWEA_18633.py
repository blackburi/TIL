# 최소합

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-1) :
        mat[i+1][0] += mat[i][0]
        mat[0][i+1] += mat[0][i]
    
    for i in range(1, n) :
        for j in range(1, n) :
            mat[i][j] += min(mat[i-1][j], mat[i][j-1])
    
    print(f'#{tc} {mat[n-1][n-1]}')