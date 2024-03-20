# 연산

def dfs(x, tmp) :
    global m, cnt

    if x == m :
        cnt = min(cnt, tmp)
        return

    if tmp >= cnt :
        return

    dfs(x+1, tmp+1)
    dfs(x-1, tmp+1)
    dfs(x-10, tmp+1)
    dfs(x*2, tmp+1)


T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())

    # 시행 횟수 최댓값
    cnt = abs(m-n)
    dfs(n, 0)

    print(f'#{tc} {cnt}')