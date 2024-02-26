# 특이한 자석

# 회전시켰을 때의 함수
# number = 회전시키는 자석 번호, direction = 회전 방향
def dfs(number, direction) :
    global visited
    visited[number] = 1
    if number < 3 :
        # N, S극이 다를경우
        if magnetic[number][2] != magnetic[number+1][6] and visited[number+1] == 0 :
            # 다음 톱니 자석을 돌린다, 방향은 반대
            dfs(number+1, -1*direction)

    if number > 0 :
        # N, S극이 다를경우
        if magnetic[number-1][2] != magnetic[number][6] and visited[number-1] == 0 :
            # 다음 톱니 자석을 돌린다, 방향은 반대
            dfs(number-1, -1*direction)

    if direction == 1 :
        magnetic[number] = [magnetic[number][-1]] + magnetic[number][:-1]
    else : # direction == -1
        magnetic[number] = magnetic[number][1:] + [magnetic[number][0]]


T = int(input())

for tc in range(1, T+1) :
    k = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(4)]

    # k번 회전
    for _ in range(k) :
        # 자석 번호, 회전방향
        a, b = map(int, input().split())
        visited = [0] * 4
        dfs(a-1, b)
    
    # 계산할 변수
    ans = 0
    for i in range(4) :
        ans += magnetic[i][0] * (2**i)

    print(f'#{tc} {ans}')