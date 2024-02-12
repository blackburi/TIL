import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().rstrip())) for _ in range(n)]

# (x, y)시작점, n : 사이즈
def qt(x, y, n) :
    standard = mat[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if standard != mat[i][j] :
                return f'({qt(x, y, n//2)}{qt(x, y+n//2, n//2)}{qt(x+n//2, y, n//2)}{qt(x+n//2, y+n//2, n//2)})'
    return f'{standard}'

print(qt(0, 0, n))
