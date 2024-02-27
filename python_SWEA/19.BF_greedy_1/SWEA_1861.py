T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    sub = [[0] * n for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n) :
        for j in range(n) :
            for k in range(4) :
                if 0 <= i+dx[k] <= n-1 and 0 <= j+dy[k] <= n-1 and mat[i][j] == mat[i+dx[k]][j+dy[k]] - 1 :
                    sub[i+dx[k]][j+dy[k]] = sub[i][j] + 1
    
    maximum = 0

    for i in range(n) :
        for j in range(n) :
            if maximum < sub[i][j] :
                maximum = sub[i][j]
                ans = [i, j]

    print(f'#{tc} {mat[ans[0]][ans[1]]-maximum+1} {maximum}')