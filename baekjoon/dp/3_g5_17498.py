# 폴짝 게임

import sys
input = sys.stdin.readline

n, m, d = map(int, input().split())

mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
score = [[-float('inf')]*m for _ in range(n)]

for i in range(m) :
    score[0][i] = mat[0][i]

for j in range(1, n):
    tmp_dp = [-float('inf')] * m
    