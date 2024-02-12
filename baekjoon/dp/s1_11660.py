import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = []
for _ in range(n) :
    lst = list(map(int, input().split()))
    for i in range(n-1) :
        lst[i+1] += lst[i]
    mat.append([0]+lst)

for _ in range(m) :
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    for i in range(x1-1, x2) :
        cnt += mat[i][y2] - mat[i][y1-1]

    print(cnt)