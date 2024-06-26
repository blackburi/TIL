# 감시

import sys
input = sys.stdin.readline
import copy

n, m = map(int, input().split())
cctv = []
mat = []
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = sys.maxsize

for i in range(n):
    sub = list(map(int, input().rstrip().split()))
    mat.append(sub)
    for j in range(m):
        if sub[j] in [1, 2, 3, 4, 5]:
            cctv.append([sub[j], i, j])


def watch(mat, mm, x, y):
    for i in mm:
        mx = x
        my = y
        while True:
            mx += dx[i]
            my += dy[i]
            # 범위를 벗어나는 경우
            if mx < 0 or my < 0 or mx >= n or my >= m:
                break

            # 벽에 도달하는 경우
            if mat[mx][my] == 6:
                break
            # 감시가 가능한 경우
            elif mat[mx][my] == 0:
                mat[mx][my] = 7

def dfs(cnt, matrix):
    global answer

    if cnt == len(cctv):
        count = 0
        for i in range(n):
            count += matrix[i].count(0)
        answer = min(answer, count)
        return

    sub_matrix = copy.deepcopy(matrix)
    cctv_num, x, y = cctv[cnt]

    for i in directions[cctv_num]:
        watch(sub_matrix, i, x, y)
        dfs(cnt+1, sub_matrix)
        sub_matrix = copy.deepcopy(matrix)


dfs(0, mat)
print(answer)