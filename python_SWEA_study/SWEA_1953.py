# 탈주범 검거


from collections import deque

# 상 하 좌 우
# 1, 4, 2, 3
tunnels = {
    '0' : [],
    '1' : [1, 2, 3, 4],
    '2' : [1, 4],
    '3' : [2, 3],
    '4' : [1, 3],
    '5' : [3, 4],
    '6' : [2, 4],
    '7' : [1, 2]
}

direction = {
    1 : (-1, 0), # 상
    2 : (0, -1), # 좌
    3 : (0, 1), # 우
    4 : (1, 0) # 하
}


T = int(input())
for tc in range(1, T+1) :
    # 세로, 가로, 맨홀x, 맨홀y, 탈출 소요 시간
    n, m, r, c, l = map(int, input().split())

    mat = [list(input().rstrip().split()) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    visited[r][c] = True

    time = 1
    position = deque([(r, c, 1)])
    # 칸의 수
    cnt = 1

    while position :
        now_x, now_y, now_time = position.popleft()

        if now_time >= l :
            continue

        # 현재 있는 곳의 터널 구조물
        k = mat[now_x][now_y]

        for dir in tunnels[k] :
            i, j = direction[dir]
            mx = now_x + i
            my = now_y + j
            if 0 <= mx <= n-1 and 0 <= my <= m-1 and (visited[mx][my] is False) and (5-dir in tunnels[mat[mx][my]]) :
                visited[mx][my] = True
                cnt += 1
                position.append((mx, my, now_time+1))

    print(f'#{tc} {cnt}')