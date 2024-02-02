c, r = map(int, input().split())

number = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]
m = 0

if number > c * r :
    print(0)

mat = [[0] * (r+2) for _ in range(c+2)]

x = r
y = 1
mat[r][1] = 1
number -= 1

while number :
    if 1 <= x <= r and mat[x][y] == 0 :