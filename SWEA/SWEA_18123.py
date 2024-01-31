from collections import deque

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = deque(list(map(int, input().split())) for _ in range(5))
    mat.appendleft([0, 0, 0, 0, 0, 0, 0])
    mat.append([0, 0, 0, 0, 0, 0, 0])

    for i in range(1, 6) :
        mat[i].insert(0, 0)
        mat[i].insert(6, 0)

    sigma = 0

    for p in range(1, 6) :
        for q in range(1, 6) :
            sigma += abs(mat[p][q] - mat[p - 1][q])
            sigma += abs(mat[p][q] - mat[p + 1][q])
            sigma += abs(mat[p][q] - mat[p][q + 1])
            sigma += abs(mat[p][q] - mat[p][q - 1])

    for p in [1, 5] :
        for q in range(1, 6) :
            sigma -= mat[p][q]

    for q in [1, 5] :
        for p in range(1, 6) :
            sigma -= mat[p][q]

    print(f'#{tc} {sigma}')