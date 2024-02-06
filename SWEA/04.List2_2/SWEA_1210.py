#Ladder 1

for tc in range(1, 11) :
    n = int(input())
    mat = [input().split() for _ in range(100)]

    x = 98
    y = mat[99].index(2) # 2의 위치는 mat[99][k]

    while x > 0 :
        mat[x][y] = 0
        if y-1>=0 and mat[x][y-1] == 1 :
            y -= 1
        elif y+1<=99 and mat[x][y+1] == 1 :
            y += 1
        elif mat[x-1][y] == 1 :
            x -= 1
    
    print(f'#{tc} {y}')