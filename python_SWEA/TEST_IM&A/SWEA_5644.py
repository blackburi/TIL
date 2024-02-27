# 무선 충전

# 이동방향과 숫자
direction = {
    0 : [0, 0],
    1 : [-1, 0],
    2 : [0, 1],
    3 : [1, 0],
    4 : [0, -1]
}

T = int(input())

for tc in range(1, T+1) :
    # 3중 list
    mat = [[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]] for _ in range(10)]
    # m은 시간, a는 bc의 개수
    m, a = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))

    # A의 위치
    A = [0, 0]
    # B의 위치
    B = [9, 9]

    # 충전소 list
    bc = [0]
    for i in range(1, a+1) :
        # 중심 [x, y], 범위 z, recharge : e
        x, y, z, e = map(int, input().split())
        x, y = y, x
        for p in range(-z, z+1) :
            for q in range(-z, z+1) :
                if 0<=x-1+p<=9 and 0<=y-1+q<=9 and abs(p)+abs(q) <= z :
                    mat[x-1+p][y-1+q].append(i)
        bc.append(e)

    # A, B가 지나간 곳에 bc가 있다면 넣어준다.
    path_A = [mat[0][0]]
    path_B = [mat[9][9]]

    # 경과된 시간
    time = 0

    while time < m :
        A[0] += direction[move_a[time]][0]
        A[1] += direction[move_a[time]][1]

        B[0] += direction[move_b[time]][0]
        B[1] += direction[move_b[time]][1]

        path_A.append(mat[A[0]][A[1]])
        path_B.append(mat[B[0]][B[1]])

        time += 1

    # A, B 충전의 총량
    ans = 0

    for i in range(m+1) :
        # path_A와 path_B를 합쳐서 최대값에 해당하는 2개의 값을 더하면 된다.
        bc_set_list = set(path_A[i] + path_B[i])
        bc_list = list(bc_set_list)
        recharge = []
        for i in bc_list :
            recharge.append(bc[i])
        
        recharge.sort()

        if len(recharge) == 1 :
            ans += recharge[-1]
        else :
            ans += recharge[-1] + recharge[-2]

    print(f'#{tc} {ans}')