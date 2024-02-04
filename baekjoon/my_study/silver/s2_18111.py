import sys
input = sys.stdin.readline

n, m, b = list(map(int, input().split()))

ground = [list(map(int, input().split())) for _ in range(n)]
height = 0
time = sys.maxsize


# stand : 최종적으로 만들 땅의 높이
for stand in range(257) :
    plus, minus = 0, 0

    for i in range(n) :
        for j in range(m) :

            if ground[i][j] > stand :
                plus += ground[i][j] - stand
            else : # ground[i][j] <= stand
                minus += stand - ground[i][j]
    
    if plus + b >= minus :
        if 2 * plus + minus <= time :
            time = 2 * plus + minus
            height = stand

print(time, height)