# 아기 상어

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
mat = []
for i in range(n) :
    sub = list(map(int, input().rstrip().split()))
    for j in range(n) :
        if sub[j] == 9 :
            fx = i
            fy = j
    mat.append(sub)

# 같은 거리라면 위-> 왼쪽 물고기를 먹어야 하기 때문에
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

cnt = 0

# BFS로 먹을수 있는 가장 가까운 위치를 찾는다.
def bfs(x, y) :
    visited = [[0]*n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = 1

    # 가까운 거리 순서, x, y
    candidate = []

    while q :
        a, b = q.popleft()
        for dir in range(4) :
            ma = a + dx[dir]
            mb = b + dy[dir]

            if 0 <= ma < n and 0 <= mb < n and visited[ma][mb] == 0 :
                if mat[x][y] > mat[ma][mb] and mat[ma][mb] != 0 :
                    visited[ma][mb] = visited[a][b] + 1
                    candidate.append((visited[ma][mb]-1, ma, mb))
                elif mat[x][y] == mat[ma][mb] :
                    visited[ma][mb] = visited[a][b] + 1
                    q.append((ma, mb))
                elif mat[ma][mb] == 0 :
                    visited[ma][mb] = visited[a][b] + 1
                    q.append((ma, mb))

    # 거리, 위쪽, 왼쪽 순서대로 중요도  -> 정렬
    return sorted(candidate, key = lambda x : (x[0], x[1], x[2]))

# 물고기 사이즈
size = [2, 0]

while True :
    mat[fx][fy] = size[0]
    candidate = deque(bfs(fx, fy))

    if not candidate :
        break

    # 먹을 물고기를 뽑는다.
    tmp, xx, yy = candidate.popleft()
    # 거리(시간)을 더해준다.
    cnt += tmp
    # 아기상어가 먹은 물고기의 수 + 1
    size[1] += 1

    # 크기가 k인 아기상어는 k마리 물고기를 먹어야 사이즈가 1 증가한다.
    if size[0] == size[1] :
        size[0] += 1
        size[1] = 0

    # 위치 갱신
    mat[fx][fy] = 0
    fx, fy = xx, yy

print(cnt)
