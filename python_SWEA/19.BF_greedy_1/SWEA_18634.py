def dfs(x) :
    global min_hap, hap, cnt
    if cnt == n :
        if min_hap > hap + mat[x][0] :
            min_hap = hap + + mat[x][0]
        return

    for w in range(n) :
        if visited[w] is False :
            visited[w] = True
            hap += mat[x][w]
            cnt += 1
            dfs(w)
            cnt -= 1
            hap -= mat[x][w]
            visited[w] = False


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    visited[0] = True
    # 배터리 소비량의 최솟값
    min_hap = 100*n
    # 배터리 소비량
    hap = 0
    # 방문한 사무실의 개수
    cnt = 1

    dfs(0)
    print(f'#{tc} {min_hap}')