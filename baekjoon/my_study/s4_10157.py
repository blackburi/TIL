c, r = map(int, input().split())

number = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]

if number > c * r :
    print(0)

mat = [[0] * r for _ in range(c)]

while number :
    mat[r-1][0] = 1
    number -= 1
    if 
