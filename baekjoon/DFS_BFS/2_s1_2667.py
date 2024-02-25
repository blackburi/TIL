import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(str, input().rstrip())) for _ in range(n)]

# 넓이를 넣어둘 list
area = []
# 개수
cnt = 0

# [x, y]는 1이 있는 위치
def dfs(x, y) :
    global cnt
    cnt += 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    mat[x][y] = '0'
    lst = [[x, y]]
    # 넓이를 측정할 변수
    tmp = 1

    while lst :
        x, y = lst.pop()
        a = x
        b = y
        for i in range(4) :
            if 0 <= a+dx[i] <= n-1 and 0 <= b+dy[i] <= n-1 and mat[a+dx[i]][b+dy[i]] == '1' :
                lst.append([a+dx[i], b+dy[i]])
                mat[a+dx[i]][b+dy[i]] = '0'
                tmp += 1

    area.append(tmp)
    return

for i in range(n) :
    for j in range(n) :
        if mat[i][j] == '1' :
            dfs(i, j)
area.sort()

print(cnt)
for i in range(cnt) :
    print(area[i])