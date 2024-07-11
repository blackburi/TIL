# 나무 재테크

# pypy로 확인된 풀이
import sys
input = sys.stdin.readline
from collections import deque


n, m, k = map(int, input().split(' '))

mat = [list(map(int, input().split())) for _ in range(n)]
first = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead = [[list() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

dx = (1, 1, 1, 0, 0, -1, -1, -1)
dy = (1, 0, -1, 1, -1, 1, 0, -1)


# 봄, 여름 함수
def ss():
    for i in range(n):
        for j in range(n):
            length = len(trees[i][j])
            for k in range(length):
                if first[i][j] < trees[i][j][k]:
                    for _ in range(k, length):
                        dead[i][j].append(trees[i][j].pop())
                    break
                else:
                    first[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead[i][j]:
                first[i][j] += dead[i][j].pop() // 2


# 가을, 겨울 함수
def fw():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)

            first[i][j] += mat[i][j]


for i in range(k):
    ss()
    fw()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)