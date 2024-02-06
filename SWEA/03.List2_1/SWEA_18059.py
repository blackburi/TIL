T = int(input())

for tc in range(1, T+1) :
    mat = [[0] * 10 for _ in range(10)]

    n = int(input())

    for _ in range(n) :
        x1, y1, x2, y2, color = list(map(int, input().split()))

        if color == 1 :
            for i in range(x1, x2 + 1) :
                for j in range(y1, y2 + 1) :
                    mat[i][j] += 1
        else : # color == 2
            for i in range(x1, x2 + 1) :
                for j in range(y1, y2 + 1) :
                    mat[i][j] += 2

    cnt = 0
    for p in range(10) :
        for q in range(10) :
            if mat[p][q] == 3 :
                cnt += 1

    print(f'#{tc} {cnt}')