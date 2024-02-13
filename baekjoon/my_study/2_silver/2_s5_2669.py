mat = [[0] * 100 for _ in range(100)]

for _ in range(4) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2) :
        for j in range(y1, y2) :
            mat[i][j] = 1
    
sigma = 0
for k in range(100) :
    sigma += mat[k].count(1)

print(sigma)