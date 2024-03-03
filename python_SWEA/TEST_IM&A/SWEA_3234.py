# 준환이의 양팔 저울

# 반드시 왼쪽이 오른쪽보다 크거나 같아야 한다.
# 무게추를 배열(올리는 순서로)후 무게추를 조건에 맞게 저울에 올리기

# 무게추를 배열 하는 방법
def dfs(x) :
    if x == n :
        on(0, 0, 0)
        return

    for i in range(n) :
        if w[i] not in sub :
            sub.append(w[i])
            dfs(x+1)
            sub.pop()

# 조건에 맞게 저울에 올리는 방법
def on(cnt, left, right) :
    global n, ans
    # 추를 배치 완료한 경우
    if cnt == n :
        ans += 1
        return

    # 왼쪽이 전체 추의 합 절반 이상이면 그 이상 생각 X
    if left >= (sum(w)+1)//2 :
        # 남은 추를 좌우, 순서 랜덤으로 배치
        ans += 2**(n-cnt)
        return

    # 추를 모두 배치하거나 왼쪽이 전체의 절반이 되지 않은 나머지 경우
    # 추를 배치하고 있는 경우 - 좌측에 올리는 경우
    on(cnt+1, left+sub[cnt], right)
    # 추를 배치하고 있는 경우 - 우측에 올리는 경우
    if left >= right + sub[cnt] :
        on(cnt+1, left, right+sub[cnt])


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    w = list(map(int, input().split()))

    # 정답
    ans = 0

    # w를 배열할 list
    sub = []

    dfs(0)

    print(f'#{tc} {ans}')