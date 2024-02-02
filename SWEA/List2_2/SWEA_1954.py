# 달팽이 숫자

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [[0]*n for _ in range(n)]
    mat[0][0] = str(1)

    m = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    k = 1
    x = 0
    y = 0
    for i in range(n**2 - 1) :
        if x+dx[m] >= n or y+dy[m] >= n :
            m = (m+1) % 4
            x += dx[m]
            y += dy[m]
            k += 1
            mat[x][y] = str(k)
        elif mat[x+dx[m]][y+dy[m]] == 0 :
            x += dx[m]
            y += dy[m]
            k += 1
            mat[x][y] = str(k)
        else :
            m = (m+1) % 4
            x += dx[m]
            y += dy[m]
            k += 1
            mat[x][y] = str(k)
    
    print(f'#{tc}')
    for i in range(n) :
        print(' '.join(mat[i]))