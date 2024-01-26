N = int(input())

point = []

for _ in range(N) :
    [a, b] = map(int, input().split())
    point.append([a, b])

point.sort()

for i in point :
    print(i[0], i[1])