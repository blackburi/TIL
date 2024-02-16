T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(input()) for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == '2' :
                # start
                x1, y1 = i, j
            if mat[i][j] == '3' :
                # end
                x2, y2,  = i, j
    
    distance = [[-1]*n for _ in range(n)]

    distance[x1][y1] = 0
    mat[x1][y1] = 1
    queue = [[x1, y1]]
    cnt = 0
    while queue :
        a, b = queue.pop(0)
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]] :
            if 0<=a+i<=n-1 and 0<=b+j<=n-1 and mat[a+i][b+j] == '0' :
                mat[a+i][b+j] = '1'
                queue.append([a+i, b+j])
                distance[a+i][b+j] = distance[a][b] + 1
            elif 0<=a+i<=n-1 and 0<=b+j<=n-1 and mat[a+i][b+j] == '3' :
                distance[a+i][b+j] = distance[a][b] + 1
                cnt += 1
                break
        
        if cnt == 1 :
            break
    
    if distance[x2][y2] == -1 :
        print(f'#{tc} 0')
    else :
        print(f'#{tc} {distance[x2][y2] - 1}')