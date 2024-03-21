# 진정한 효도

import sys
input = sys.stdin.readline

mat = [list(map(int, input().rstrip().split())) for _ in range(3)]

# 최소 비용
min_cost = 27

for i in range(3) :
    for k in range(1, 4) :
        row = 0
        col = 0
        for j in range(3) :
            # row확인
            row += abs(k-mat[i][j])
            col += abs(k-mat[j][i])
        min_cost = min(min_cost, row, col)

print(min_cost)