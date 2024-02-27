# 핀볼 게임

# 상1 하2 좌3 우0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 1번~ 5번 block
blocks = [
    [],
    [2, 3, 1, 0],
    [1, 3, 0, 2],
    [3, 2, 0, 1],
    [2, 0, 3, 1],
    [2, 3, 0, 1]
]

def check(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return True
    return False

def get_score(start_x, start_y, start_dir) :
    score = 0
    dx, dy, dir = start_x, start_y, start_dir

    while True :
        dx = dx + directions[dir][0]
        dy = dy + directions[dir][1]
        if check(dx, dy) : # 범위 내에 존재한다면
            # 만약 블록을 만났을 경우
            if data[dx][dy] in range(1, 6) :
                block_type = data[dx][dy]
                # 점수 증가
                score += 1
                dir = blocks[block_type][dir]
                continue
            # 만약 웜홀을 만났을 경우
            elif data[dx][dy] in range(6, 11) :
                hall_type = data[dx][dy]
                if (dx, dy) == wormhole[hall_type][0] :
                    dx, dy = wormhole[hall_type][1]
                else :
                    dx, dy = wormhole[hall_type][0]
                continue
            # 만약 블랙홀을 만났을 경우
            elif data[dx][dy] == -1 :
                return score
            # 시작점으로 도달했을 경우
            elif (dx, dy) == (start_x, start_y) :
                return score
            # 빈 공간일 경우
            else :
                continue
        # 벽을 만났을 경우
        else :
            dir = (dir + 2) % 4 # 반대 방향으로 전환
            score += 1


T = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    # 웜홀 리스트
    wormhole = [[] for _ in range(11)]
    for i in range(n) :
        for j in range(n) :
            value = data[i][j]
            if value in range(6, 11) : # 웜홀일 경우
                wormhole[value].append((i, j)) # 좌표 삽입

    for i in range(n) :
        for j in range(n) :
            if data[i][j] == 0 : # 빈 공간이면
                for k in range(4) : # 네 방향 확인
                    score = get_score(i, j, k)
                    result = max(result, score)

    print('#%d %d' % (tc, result))