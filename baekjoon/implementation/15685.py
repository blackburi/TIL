# 드래곤 커프

# idea - 별찍기와 direction rule
# 전부 0으로 찍어두고 점이 찍히면 그곳을 1로 대체
# 네 꼭짓점의 합이 4인 1 * 1 정사각형을 찾는다

import sys
input = sys.stdin.readline

N = int(input())

mx = [1, 0, -1, 0]
my = [0, -1, 0, 1]

arr = [[0]*101 for _ in range(101)]

# 드래곤 커브의 규칙(rule of direction)
# 이전 시행을 뒤집은 후 전부 + 1 (4이상이면 4로 나눈 나머지)
# 0 1 2 1 : 2세대
# (뒤집으면) 1 2 1 0 -> 2 3 2 1
# 0 1 2 1 / 2 3 2 1 : 3세대
def DC() :
    x, y, d, g = list(map(int, input().split()))

    # DC direction number list
    way = [d]
    for i in range(g) :
        way_sub = list(reversed(way))

        for j in range(len(way_sub)) :
            way_sub[j] = (way_sub[j] + 1) % 4

        way.extend(way_sub)
        
    # 점을 몇개 찍을 것인지
    arr[x][y] = 1 # start point (x, y)
    for i in way :
        x = x + mx[i]
        y = y + my[i]
        arr[x][y] = 1

for _ in range(N) :
    DC()

cnt = 0

for p in range(100) :
    for q in range(100) :
        if arr[p][q] + arr[p+1][q] + arr[p][q+1] + arr[p+1][q+1] == 4 :
            cnt += 1

print(cnt)