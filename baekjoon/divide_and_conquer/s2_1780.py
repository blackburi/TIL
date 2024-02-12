import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

a = 0 # -1 box
b = 0 # 0 box
c = 0 # 1 box


# (x, y)시작점 , n은 사이즈
def dc(x, y, n) :
    global a, b, c
    num = mat[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if num != mat[i][j] :
                dc(x, y, n//3)
                dc(x+n//3, y, n//3)
                dc(x+2*n//3, y, n//3)
                dc(x, y+n//3, n//3)
                dc(x, y+2*n//3, n//3)
                dc(x+n//3, y+n//3, n//3)
                dc(x+n//3, y+2*n//3, n//3)
                dc(x+2*n//3, y+n//3, n//3)
                dc(x+2*n//3, y+2*n//3, n//3)
                return
    
    if num == -1 :
        a += 1
    elif num == 0 :
        b += 1
    else : # num == 1
        c += 1

dc(0, 0, n)
print(a)
print(b)
print(c)