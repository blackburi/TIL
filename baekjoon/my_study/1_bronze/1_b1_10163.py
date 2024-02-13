n = int(input())

# 입력값 : x, y, dy, dx
mat = [[0] * 1001 for _ in range(1001)]

for k in range(1, n+1) :
    x, y, dx, dy = map(int, input().split())
    
    for i in range(x, x+dx) :
        mat[i][y:y+dy] = [k] * dy

for p in range(1, n+1) :
    ans = 0
    for cnt in range(1001) :
        ans += mat[cnt].count(p)
    print(ans)