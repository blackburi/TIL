n = int(input())

# space = []
# for i in range(n) :
#     space_n = [' '] * n
#     space.append(space_n)
space = [[' '] * n for i in range(n)]

def star(x, y, z) :
    if z == 3 :
        space[x][y] = '*'
        for p in range(3) :
            space[x][y+p] = '*'
            space[x+p][y] = '*'
            space[x+2][y+p] = '*'
            space[x+p][y+2]= '*'
        space[x+1][y+1] = ' '
        return
    else :
        w = z//3
        star(x, y, w)
        star(x+w, y, w)
        star(x+2*w, y, w)
        star(x, y+w, w)
        star(x+2*w, y+w, w)
        star(x, y+2*w, w)
        star(x+w, y+2*w, w)
        star(x+2*w, y+2*w, w)
        return

star(0, 0, n)

for k in space :
    print(''.join(k))