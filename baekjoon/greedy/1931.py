# 회의실 배정
# 다시 풀어보기

N = int(input())
pair = [list(map(int,input().split())) for _ in range(N)]

pair.sort(key = lambda x : (x[1], x[0]))

num = 1

present = pair[0][1]


for i in pair[1:] :
    if i[0] >= present :
        num += 1
        present = i[1]

print(num)




""" 필요한 회의실의 최소 숫자
N = int(input())

MAX = []
pair = []

for _ in range(N) :
    a, b = list(map(int, input().split()))
    MAX.append(b)
    pair.append([a, b])

length = [[0] * max(MAX) for _ in range(N)]


for i in range(len(pair)) :
    for j in range(pair[i][1] - pair[i][0]) :
        length[i][pair[i][0]+j] = 1

result = []

for k in range(len(MAX)) :
    sum = 0
    for l in range(N) :
        sum += length[l][k]
    result.append(sum)

print(max(result))
"""