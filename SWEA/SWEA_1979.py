from collections import deque

T = int(input())

for tc in range(1, T+1) :
    N, K = list(map(int, input().split()))

    mat = deque([list(map(int, input().split())) for _ in range(N)])
    mat.appendleft([0] * (N + 2))
    mat.append([0] * (N + 2))

    for i in range(1, N+1) :
        mat[i].insert(0, 0)
        mat[i].insert(N+1, 0)

    cnt = 0
    word = [0] + [1] * K + [0]

    # 가로줄
    for i in range(N+2) :
        for j in range(N-K+1) :
            if mat[i][j:(j+K+2)] == word :
                cnt += 1

    # 세로줄
    for j in range(N+2):
        for i in range(N-K+1) :
            sub_word = []
            for k in range(K+2) :
                sub_word.append(mat[i+k][j])
            if sub_word == word :
                cnt += 1

    print(f'#{tc} {cnt}')