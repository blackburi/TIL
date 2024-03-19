# 최소 생산 비용

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # 임시로 ans 설정
    ans = 0
    for i in range(n) :
        ans += mat[i][i]
    
    # 생산비용
    hap = 0
    # 방문 체크
    visited = [False] * n

    def dfs(i) :
        global hap, ans

        if i == n :
            ans = min(ans, hap)
            return
        
        if hap > ans :
            return

        for j in range(n) :
            if visited[j] is False :
                visited[j] = True
                hap += mat[i][j]
                dfs(i+1)
                hap -= mat[i][j]
                visited[j] = False
    
    dfs(0)
    print(f'#{tc} {ans}')