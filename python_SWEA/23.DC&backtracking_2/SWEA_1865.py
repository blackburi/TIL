# 동철이의 일 분배

T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    mat = []
    for i in range(n) :
        sub = list(map(int, input().split()))
        for j in range(n) :
            sub[j] /= 100
        mat.append(sub)

    # 확률의 최댓값
    answer = 0
    # 방문 check
    visited = [False] * n

    percent = 1

    def dfs(x) :
        global percent, answer

        if x == n :
            answer = max(answer, percent * 100)
            return

        if percent < answer/100 :
            return

        for i in range(n) :
            if visited[i] is False :
                if mat[x][i] == 0 :
                    continue

                visited[i] = True
                percent *= mat[x][i]
                dfs(x+1)
                percent /= mat[x][i]
                visited[i] = False
    
    dfs(0)
    print(f'#{tc} {format(round(answer, 6), ".6f")}')