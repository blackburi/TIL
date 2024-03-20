# 격자판의 숫자 이어 붙이기

T = int(input())

for tc in range(1, T+1) :
    mat = [list(map(str, input().split())) for _ in range(4)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 수들을 보관할 set
    number = set()

    def dfs(x, y) :
        if len(sub) == 7 :
            number.add(''.join(sub))
            return

        for i in range(4) :
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx <= 3 and 0 <= my <= 3 :
                sub.append(mat[mx][my])
                dfs(mx, my)
                sub.pop()


    for i in range(4) :
        for j in range(4) :
            sub = [mat[i][j]]
            dfs(i, j)

    print(f'#{tc} {len(number)}')