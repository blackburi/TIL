# 0 : 통로, 1 : 벽
# 2 : start, 3 : end

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = 0

    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == 2 :
                x1 = i
                y1 = j
            if mat[i][j] == 3 :
                x2 = i
                y2 = j
    
    stack = [[x1, y1]]

    while stack :
        [a, b] = stack.pop()
        mat[a][b] = 1
        if [a, b] == [x2, y2] :
            ans += 1
            break

        if 0 <= a+1 <= n-1 and (mat[a+1][b] in [0, 3]) :
            stack.append([a+1, b])
        if 0 <= a-1 <= n-1 and (mat[a-1][b] in [0, 3]) :
            stack.append([a-1, b])
        if 0 <= b+1 <= n-1 and (mat[a][b+1] in [0, 3]) :
            stack.append([a, b+1])
        if 0 <= b-1 <= n-1 and (mat[a][b-1] in [0, 3]) :
            stack.append([a, b-1])
    
    if ans == 1 :
        print(f'#{tc} 1')
    else : # ans == 0
        print(f'#{tc} 0')