# 세로 2**n-1
# 가로 2**(n+1)-3

n = int(input())

if n % 2 == 0 :
    space = [[' ']*(2**(n+1)-3-i) for i in range(2**n-1)]
else :
    space = [[' ']*(2**n-1+i) for i in range(2**n-1)]

def star(x, y, z) :
    if z == 1 :
        space[x][y] = '*'
        return
    else :
        if z % 2 == 0 :
            star(x+1, y+2**(z-1), z-1)
            for p in range(2**(z+1)-3) :
                space[x][y+p] = '*'
            for q in range(2**z-1) :
                space[x+q][y+q] = '*'
                space[x+q][y+2**(z+1)-4-q] = '*'
            return
        else :
            star(x+2**(z-1)-1, y+2**(z-1), z-1)
            for r in range(2**(z+1)-3) :
                space[x+2**z-2][y+r] = '*'
            for s in range(2**z-1) :
                space[x+2**z-2-s][y+s] = '*'
                space[x+2**z-2-s][y+2**(z+1)-4-s] = '*'
            return

star(0, 0, n)

for k in space :
    print(''.join(k))