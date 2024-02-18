###################################################################
# python 시간초과, pypy3 맞음 : 내풀이
###################################################################

import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().rstrip().split())) for _ in range(9)]

# 가로 세로 사각형 check

# a : 행/열의 index, n : 넣으려는 숫자
# 가로
def row(a, n) :
    for i in range(9) :
        if n == sudoku[a][i] :
            return False # 존재하는 경우
    return True # 존재하지 않는 경우

# a : 행/열의 index, n : 넣으려는 숫자
# 세로
def col(a, n) :
    for i in range(9) :
        if n == sudoku[i][a] :
            return False # 존재하는 경우
    return True # 존재하지 않는 경우

# (x, y) : 좌표, n : 넣으려는 숫자
# 사각형
def squ(x, y, n) :
    for i in range(3) :
        for j in range(3) :
            if n == sudoku[x//3*3+i][y//3*3+j] :
                return False # 존재하는 경우
    return True # 존재하지 않는 경우

# backtracking을 이용하여 채워넣기
def fill(n) :
    if n == len(find) :
        for i in range(9) :
            print(*sudoku[i])
        # exit을 넣어야 하는 이유
        # 해당 스도쿠의 모든 답을 출력하는 것을 막기 위해서
        # 답이 여러개인 경우 어러번 출력하는 것을 방지하기 위함
        exit()
    
    for i in range(1, 10) :
        x, y = find[n]
        if row(x, i) and col(y, i) and squ(x, y, i) :
            sudoku[x][y] = i
            fill(n+1)
            sudoku[x][y] = 0

find = [] # 찾아서 넣어야 하는 공간, 문제에서 0으로 입력되는 곳

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            find.append([i, j])

fill(0)