# 보호 필름

# 필름의 성능 검사
def check(matrix) :
    for col in range(w) :
        tmp = 1
        for row in range(1, d) :
            if matrix[row][col] == matrix[row-1][col] :
                tmp += 1
            else :
                tmp = 1
            
            if tmp >= k :
                break

        # 성능 검사 통과 X
        if tmp < k :
            return False
    # 성능 검사 통과 O
    return True


# 주입 횟수, 막, 목표
def dfs(injection, layer, goal) :
    global ans

    # 주입횟수가 많아지면 break
    if injection >= ans :
        return

    # goal까지 도달했다면 check
    if injection == goal :
        if check(mat) :
            ans = min(ans, injection)
        return

    for i in range(layer, d) :
        for inject in injects :
            mat[i] = inject
            dfs(injection+1, i+1, goal)
            mat[i] = mat_copy[i]



T = int(input())
for tc in range(1, T+1) :
    # 두께, 가로크기, 합격 기준
    d, w, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(d)]
    # mat 복사본
    mat_copy = [sub[:] for sub in mat]

    # 약품을 주입했을때 바뀌는 것 -> delta처럼 생각
    injects = [[0]*w, [1]*w]

    ans = float('inf')

    # 성능검사를 한번에 통과하는 경우
    if check(mat) :
        ans = 0
    # 성능검사를 한번에 통과하지 못해 약품처리 해야 하는 경우
    else : # check(mat) is False
        for goal in range(1, d+1) :
            dfs(0, 0, goal)
            # d의 최댓값이 13 -> injection을 작은 수부터 확인
            # 통과된다면 바로 stop
            if ans < 14 :
                break
    
    print(f'#{tc} {ans}')