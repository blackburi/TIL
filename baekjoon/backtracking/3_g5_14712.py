# 넴모넴모 (Easy)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nemo = [[0]*(m+1) for _ in range(n+1)]
ans = 0


# cnt는 전체 배열에서 얼만큼 갔는지 count
def dfs(cnt) :
    global ans

    if cnt == n*m :
        ans += 1
        return
    
    x = cnt//m + 1
    y = cnt % m + 1

    if nemo[x-1][y] == 0 or nemo[x-1][y-1] == 0 or nemo[x][y-1] == 0 :
        # 네모를 놓을 수 있는 경우
        nemo[x][y] = 1
        dfs(cnt+1)
        nemo[x][y] = 0
    
    dfs(cnt+1)


dfs(0)
print(ans)