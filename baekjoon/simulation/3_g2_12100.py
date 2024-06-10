# 2048 (Easy)

import sys
input = sys.stdin.readline
from copy import deepcopy

n = int(input())
mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 최대 숫자
answer = 0

# 위로 움직이는 경우
def up(matrix) :
    for i in range(n) :
        # place 초기화 -> 이동할 위치에 있는 수
        place = 0
        for j in range(1, n) :
            # 숫자가 존재하는 경우에만 이동하면 된다.
            if matrix[j][i] :
                tmp = matrix[j][i]
                matrix[j][i] = 0
                # place에 존재하는 수가 0인 경우
                if matrix[place][i] == 0 :
                    matrix[place][i] = tmp
                # place에 존재하는 수 == 현재위치의 수
                elif matrix[place][i] == tmp :
                    matrix[place][i] *= 2
                    place += 1
                # place에 존재하는수 != 현재위치의 수
                else :
                    place += 1
                    matrix[place][i] = tmp
    return matrix


# 아래로 움직이는 경우
def down(matrix) :
    for i in range(n) :
        # place 초기화 -> 이동할 위치에 있는 수
        place = n-1
        for j in range(n-2, -1, -1) :
            # 숫자가 존재하는 경우에만 이동하면 된다.
            if matrix[j][i] :
                tmp = matrix[j][i]
                matrix[j][i] = 0
                # place에 존재하는 수가 0인 경우
                if matrix[place][i] == 0 :
                    matrix[place][i] = tmp
                # place에 존재하는 수 == 현재위치의 수
                elif matrix[place][i] == tmp :
                    matrix[place][i] *= 2
                    place -= 1
                # place에 존재하는수 != 현재위치의 수
                else :
                    place -= 1
                    matrix[place][i] = tmp
    return matrix


# 오른쪽로 움직이는 경우
def right(matrix) :
    for i in range(n) :
        # place 초기화 -> 이동할 위치에 있는 수
        place = n-1
        for j in range(n-2, -1, -1) :
            # 숫자가 존재하는 경우에만 이동하면 된다.
            if matrix[i][j] :
                tmp = matrix[i][j]
                matrix[i][j] = 0
                # place에 존재하는 수가 0인 경우
                if matrix[i][place] == 0 :
                    matrix[i][place] = tmp
                # place에 존재하는 수 == 현재위치의 수
                elif matrix[i][place] == tmp :
                    matrix[i][place] *= 2
                    place -= 1
                # place에 존재하는수 != 현재위치의 수
                else :
                    place -= 1
                    matrix[i][place] = tmp
    return matrix


# 왼쪽으로 움직이는 경우
def left(matrix) :
    for i in range(n) :
        # place 초기화 -> 이동할 위치에 있는 수
        place = 0
        for j in range(1, n) :
            # 숫자가 존재하는 경우에만 이동하면 된다.
            if matrix[i][j] :
                tmp = matrix[i][j]
                matrix[i][j] = 0
                # place에 존재하는 수가 0인 경우
                if matrix[i][place] == 0 :
                    matrix[i][place] = tmp
                # place에 존재하는 수 == 현재위치의 수
                elif matrix[i][place] == tmp :
                    matrix[i][place] *= 2
                    place += 1
                # place에 존재하는수 != 현재위치의 수
                else :
                    place += 1
                    matrix[i][place] = tmp
    return matrix


# dfs로 탐색
# 보드판, 시행횟수
def dfs(matrix, cnt) :
    global answer

    if cnt == 5 :
        for i in range(n) :
            for j in range(n) :
                answer = max(answer, matrix[i][j])
        return

    # 위로 움직이는 경우
    next_matrix = up(deepcopy(matrix))
    dfs(next_matrix, cnt+1)
    # 오른쪽으로 움직이는 경우
    next_matrix = right(deepcopy(matrix))
    dfs(next_matrix, cnt+1)
    # 아래로 움직이는 경우
    next_matrix = down(deepcopy(matrix))
    dfs(next_matrix, cnt+1)
    # 왼쪽으로 움직이는 경우
    next_matrix = left(deepcopy(matrix))
    dfs(next_matrix, cnt+1)


dfs(mat, 0)
print(answer)