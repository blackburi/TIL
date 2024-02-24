for _ in range(1, 11) :
    tc = int(input())
    mat = [list(input()) for _ in range(16)]

    for i in range(16) :
        for j in range(16) :
            if mat[i][j] == '2' :
                # start
                x1, y1 = i, j
            if mat[i][j] == '3' :
                # end
                x2, y2,  = i, j
    
    mat[x1][y1] = 1
    queue = [[x1, y1]]
    cnt = 0
    while queue :
        a, b = queue.pop(0)
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]] :
            if 0<=a+i<=15 and 0<=b+j<=15 and mat[a+i][b+j] == '0' :
                mat[a+i][b+j] = '1'
                queue.append([a+i, b+j])
            elif 0<=a+i<=15 and 0<=b+j<=15 and mat[a+i][b+j] == '3' :
                mat[a+i][b+j] = 4
                cnt += 1
                break
        
        if cnt == 1 :
            break
    
    if mat[x2][y2] == '3' :
        print(f'#{tc} 0')
    else :
        print(f'#{tc} 1')