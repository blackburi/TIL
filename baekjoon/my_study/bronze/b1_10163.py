n = int(input())

# 입력값 : x, y, dy, dx
max_x = 0
max_y = 0
mat = [[0] * 1001 for _ in range(1001)]

for k in range(1, n+1) :
    x, y, dx, dy = list(map(int, input().split()))
    if x+dx-1 > max_x :
        max_x = x + dx - 1 # x axis : max_x까지만 생각해도 됨

    if y+dy-1 > max_y : # y axis : max_y까지만 생각해도 됨
        max_y = y + dy - 1
    
    for i in range(x, x+dx) :
        for j in range(y, y+dy) :
            mat[i][j] = k

dic = {}
for z in range(1, n+1) :
    dic[z] = 0

for i in range(max_x+1) :
    for j in range(max_y+1) :
        if mat[i][j] != 0 :
            s = mat[i][j]
            dic[s] += 1

for k in range(n) :
    print(dic[k+1])