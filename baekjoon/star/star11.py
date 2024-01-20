N = int(input())

# space = [[' '] * 2 * N for i in range(N)]
space = []
for i in range(N) :
    tmp = [' '] * 2 * N
    space.append(tmp)

def star(x, y, z) :
    if z == 3 :
        space[x][y] = '*'   # 기준점은 제일 윗줄의 가운데 *
        space[x+1][y+1] = '*'
        space[x+1][y-1] = '*'
        for j in range(2*z-1) :
            space[x+2][y-z+1+j] = '*'
        return
    else : 
        w = z // 2
        star(x, y, w)
        star(x+w, y+w, w)
        star(x+w, y-w, w)
        return

star(0, N-1 , N)

for k in space :
    print(''.join(k))