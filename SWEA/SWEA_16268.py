from collections import deque

T = int(input())

for tc in range(1, T+1) :
    N, M = list(map(int, input().split()))
    flower = []
    mat = deque([list(map(int, input().split())) for _ in range(N)])
    mat.appendleft([0]*(M+2))
    mat.append([0]*(M+2))

    for i in range(1, N+1) :
        mat[i].insert(M+1, 0)
        mat[i].insert(0, 0)

    for p in range(1, N+1) :
        for q in range(1, M+1) :
            k = 0
            k += mat[p][q] + mat[p+1][q] + mat[p][q+1] + mat[p-1][q] + mat[p][q-1]
            flower.append(k)

    fmax = 0
    for i in flower :
        if fmax < i :
            fmax = i

    print(f'#{tc} {fmax}')