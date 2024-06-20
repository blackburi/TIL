# 로봇 청소기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 방문 체크
visited = [[0]*m for _ in range(n)]

# 시작 지점
visited[r][c] = 1
cnt = 1

# 방향전환(반시계방향으로 90도씩) -> d = (d+3)%4
# 북, 동, 남, 서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

while True :
    # 청소 했는지를 확인하는 변수
    flag = 0

    for _ in range(4) :
        d = (d+3) % 4
        mr = r + dr[d]
        mc = c + dc[d]

        # 청소가 가능한 경우
        if 0 <= mr < n-1 and 0 <= mc <= m-1 and mat[mr][mc] == 0 :
            # 청소를 하는 경우
            if visited[mr][mc] == 0 :
                visited[mr][mc] = 1
                cnt += 1
                r, c = mr, mc
                flag = 1
                break

    # 청소를 하지 못하는 경우
    if flag == 0 :
        # 후진했을때 벽이면 stop
        if mat[r-dr[d]][c-dc[d]] == 1 :
            print(cnt)
            break
        # 벽이 아닌경우 위치 갱신
        else :
            r, c = r-dr[d], c-dc[d]