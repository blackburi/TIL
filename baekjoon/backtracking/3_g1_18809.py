# Gaaaaaaaaaarden

import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

n, m, g, r = map(int, input().split())
# 토양
grounds = []
# 배양액을 뿌릴수 있는 곳
possible = []

for i in range(n) :
    sub = tuple(input().rstrip().split())
    for j in range(m) :
        if sub[j] == '2' :
            possible.append((i, j))
    grounds.append(sub)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def plant() :
    q = deque()
    # 핀 꽃의 수
    flower = 0

    # 초록 배양액
    for gr in green :
        q.append((gr[0], gr[1]))
        visited[gr[0]][gr[1]] = -1
    # 빨강 배양액
    for re in red :
        q.append((re[0], re[1]))
        visited[re[0]][re[1]] = 1

    while q :
        x, y = q.popleft()

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < m and (grounds[mx][my] == '1' or grounds[mx][my] == '2') :
                if visited[mx][my] == '0' :
                    # 빨간 배양액의 경우
                    if visited[x][y] < 0 :
                        visited[mx][my] = visited[x][y] - 1
                        q.append((mx, my))
                    # 초록 배양액의 경우 - 10000을 두는 이유는 n, m의 범위가 50까지 이기 때문에 여유롭게 10000을 잡는다.
                    elif 0 < visited[x][y] < 10000 :
                        visited[mx][my] = visited[x][y] + 1
                        q.append((mx, my))
            
            # q에 초록 배양액을 먼저 넣었기 때문에 초록 배양액이 먼저 배치된다.
            # 이웃한 칸의 절대값이 1차이가 나면 같은 시간에 같은 칸 도달 불가능
            if 0 <= mx < n and 0 <= my < m and visited[mx][my]*visited[x][y] < 0 and visited[mx][my] + visited[x][y] + 1 == 0 :
                visited[mx][my] = 10000
                flower += 1
    return flower


# 최대 꽃의 개수
answer = 0

# 방문 처리 - 합이 0이 되는 것과 구분하기 위해 문자열로 배치
# '0' : 방문X, 0 : 같은 시간에 배양액이 만나 꽃을 피움 -> 'f'
# 양수 : 빨간 배양액, 음수 : 초록 배양액
visited = [['0']*m for _ in range(n)]

for green in combinations(possible, g) :
    green = list(green)
    rest = list(set(possible) - set(green))
    for red in combinations(rest, r) :
        red = list(red)
        answer = max(answer, plant())

print(answer)