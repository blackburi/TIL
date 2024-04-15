# 소문난 칠공주

import sys
input = sys.stdin.readline


# 7명의 좌표, 이다솜파('S'), 임도연파('Y')
def solve(seats, t, f) :
    global ans

    # 임도연파가 4명이상이면 return
    if f >= 4 :
        return

    if len(seats) == 7 :
        seats = tuple(sorted(seats))
        if seats not in positions :
            positions.add(seats)
            ans += 1
        return

    for seat in seats :
        x = seat[0]
        y = seat[1]
        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= 4 and 0 <= my <= 4 and ((mx, my) not in seats) :
                if mat[mx][my] == 'S' :
                    solve(seats+[(mx, my)], t+1, f)
                else : # mat[mx][my] == 'Y'
                    solve(seats+[(mx, my)], t, f+1)



mat = [list(input().rstrip()) for _ in range(5)]

# 정답의 경우
ans = 0
# 정답이 되는 경우의 7명의 자리 배치
positions = set()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(5) :
    for j in range(5) :
        lst = [(i, j)]
        if mat[i][j] == 'S' :
            solve(lst, 1, 0)
        else :
            solve(lst, 0, 1)
print(ans)