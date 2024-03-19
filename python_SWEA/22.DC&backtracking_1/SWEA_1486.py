# 장훈이의 높은 선반

def dfs(x) :
    global n, b, hap, ans
    if hap >= b :
        ans = min(ans, hap - b)
        return

    for i in range(x, n) :
        hap += heights[i]
        dfs(i+1)
        hap -= heights[i]
    
    return


T = int(input())

for tc in range(1, T+1) :
    # 점원의 수, 선반의 높이
    n, b = map(int, input().split())

    heights = list(map(int, input().split()))

    # 점원들의 키의 합
    hap = 0
    # 정답
    ans = sum(heights)

    dfs(0)

    print(f'#{tc} {ans}')