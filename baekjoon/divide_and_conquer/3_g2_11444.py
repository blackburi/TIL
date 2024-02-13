# 피보나치수열을 행렬로 풀기

# F(n) = F(n-1) + F(n-2)
# [[F(n+2)] = [[1, 1] * [[F(n+1)]
#  [F(n+1)]]   [1, 0]]   [F(n)]]

# 다시 고치면
# [[F(n+1), F(n)] = [[1, 1]  **n
#  [F(n), F(n-1)]]   [1, 0]]

import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

# 행렬의 곱
def gop(a, b) : # a, b 모두 matrix
    tmp = [[0] * 2 for _ in range(2)]
    for i in range(2) :
        for j in range(2) :
            hap = 0
            for k in range(2) :
                hap += a[i][k] * b[k][j]
            tmp[i][j] = hap % p
    return tmp

# 제곱 분할정복
def square(x, y) : # x : matrix, y = 횟수
    if y == 1 :
        return x
    elif y % 2 == 1 :
        return gop(square(x, y-1), x)
    else : # y % 2 == 0
        return square(gop(x, x), y//2)

# 초기 행렬
standard = [[1, 1], [1, 0]]
if n < 3 :
    print(1)
else : # n >= 3
    print(gop(square(standard, n-2), standard)[0][0])