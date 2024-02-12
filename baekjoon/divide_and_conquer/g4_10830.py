import sys
input = sys.stdin.readline

n, b = map(int, input().rstrip().split())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 행렬 연산
def gop(a, b) : # a, b 모두 matrix
    tmp = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                tmp[i][j] = (tmp[i][j] + a[i][k]*b[k][j]) % 1000
    return tmp

# 분할 정복
def square(p, q) : # p는 matrix, q는 곱하는 횟수
    if q == 1 :
        return p
    
    tem = square(p, q//2)

    if q % 2 == 0 :
        return gop(tem, tem)
    else : # q % 2 == 1
        return gop(gop(tem, tem), p)

ans = square(mat, b)
for i in range(n) :
    for j in range(n) :
        ans[i][j] %= 1000

for k in ans :
    print(*k)