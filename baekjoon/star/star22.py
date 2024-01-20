from pprint import pprint

n = int(input())

# 가로 4n-3
# 세로 4n-1

space = [[' '] * (4 * n - 3) for dot in range(4 * n -1)]

def star(x, y, z) :
    if z == 1 :
        space[x] = ['*']
        return 
    elif z == 2 :
        for p in range(4*z-3) :
            space[x][y+p] = '*'
        for q in range(4*z-1) :
            space[x+q][y] = '*'
        for r in range(4*z-3) :
            space[x+4*z-2][y+r] = '*'
        for s in range(4*z-3) :
            space[x+2+s][y+4*z-4] = '*'
        for t in range(4*z-5) :
            space[x+2][y+4*z-4-t] = '*'
        for u in range(4*z-5) :
            space[x+2+u][y+2] = '*'
        space[1] = ['*']
        return
    else :
        star(x+2, y+2, z-1)
        for i in range(4*z-3) :
            space[x][y+i] = '*'
            space[x+4*z-2][y+i] = '*'
        for j in range(4*z-1) :
            space[x+j][y] = '*'
        for w in range(4*z-3) :
            space[x+2+w][y+4*z-4] = '*'
        space[x+2][y+4*z-5] = '*'
        return    

star(0, 0, n)

for k in space :
    print(''.join(k))