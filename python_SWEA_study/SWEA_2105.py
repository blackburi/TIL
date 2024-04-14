# 디저트 카페

# 완전 탐색이라고 생각
# 반드시 네번만 턴해야 직사각형 경로가 만들어진다.


# 포함된 디저트 number list, 턴 순서, 턴 횟수(3번 이면 완료)
def dfs(x, y, sub, turn) :
    global i, j, ans

    """ 이렇게 막으면 turn=3인 경우에서 직진하는 경우를 체크하지 못함
    # 3번 턴하고 원래 상태로 돌아온다면
    if turn == 3 :
        if x == i and y == j and len(sub) >= 4 :
            ans = max(ans, len(sub))
        return
    """
    if turn == 3 and x == i and  y == j and len(sub) >= 4 :
        ans = max(ans, len(sub))
        return

    if 0 <= x <= n-1 and 0 <= y <= n-1 and cafe[x][y] not in sub :
        sub.append(cafe[x][y])

        # 직진하는 경우
        mx = x + dx[turn]
        my = y + dy[turn]
        dfs(mx, my, sub, turn)

        # 턴하는 경우
        if turn <= 2 :
            mx = x + dx[turn+1]
            my = y + dy[turn+1]
            dfs(mx, my, sub, turn+1)
        sub.pop()


T = int(input())
for tc in range(1, T+1) :
    n = int(input())

    cafe = [tuple(map(int, input().split())) for _ in range(n)]

    # 순서는 유지되어야 한다.
    # index=0 부터 고정으로 시작해도 되는 이유는
    # index=1 부터 시작되는 경우 또한 다른 점에서 index=0부터 시작하는 경우이기 때문
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    ans = -1
    for i in range(n) :
        for j in range(n) :
            lst = []
            dfs(i, j, lst, 0)

    print(f'#{tc} {ans}')