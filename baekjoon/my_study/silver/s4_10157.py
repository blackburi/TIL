import sys
input = sys.stdin.readline

c, r = map(int, input().split())

number = int(input())

if number > r * c :
    print(0)
else :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    m = 0

    mat = [[0] * c for _ in range(r)]

    x = r-1
    y = 0
    mat[x][y] = 1
    number -= 1

    while number :
        if 0 <= x+dx[m] <= r-1 and 0 <= y+dy[m] <= c-1 :
            if mat[x+dx[m]][y+dy[m]] == 0 :
                x += dx[m]
                y += dy[m]
                mat[x][y] = 1
                number -= 1
            else : # mat[x+dx[m]][y+dy[m]] != 0
                m = (m+1) % 4
                x += dx[m]
                y += dy[m]
                mat[x][y] = 1
                number -= 1
        else :
            m = (m+1) % 4

    print(y+1, r-x)