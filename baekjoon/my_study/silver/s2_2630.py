import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
w = 0 # white box 개수
b = 0 # black box 개수
# (x, y) : matrix의 시작점, n : 크기
def block(x, y, n) :
    global mat, w, b
    color = mat[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if color != mat[i][j] :
                block(x, y, n//2)
                block(x+n//2, y, n//2)
                block(x, y+n//2, n//2)
                block(x+n//2, y+n//2, n//2)
                return
    if color == 1 :
        b += 1
    else : # color == 0
        w += 1

block(0, 0, n)
print(w)
print(b)