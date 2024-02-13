# 입력값(x, y) -> 코드값(y-1, x-1)

def turn_r(a, b, c) :
    global n
    stack = [[a, b]]
    # 가로 오른쪽 확인
    while True :
        if 0 <= b+1 <= n-1 and mat[a][b+1] == 3-c :
            stack.append([a, b+1])
            b += 1
        elif 0 <= b+1 <= n-1 and mat[a][b+1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_l(a, b, c) :
    global n
    stack = [[a, b]]
    # 가로 왼쪽 확인
    while True :
        if 0 <= b-1 <= n-1 and mat[a][b-1] == 3-c :
            stack.append([a, b-1])
            b -= 1
        elif 0 <= b-1 <= n-1 and mat[a][b-1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_u(a, b, c) :
    global n
    stack = [[a, b]]
    # 세로 위 확인
    while True :
        if 0 <= a-1 <= n-1 and mat[a-1][b] == 3-c :
            stack.append([a-1, b])
            a -= 1
        elif 0 <= a-1 <= n-1 and mat[a-1][b] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_d(a, b, c) :
    global n
    stack = [[a, b]]
    # 세로 아래 확인
    while True :
        if 0 <= a+1 <= n-1 and mat[a+1][b] == 3-c :
            stack.append([a+1, b])
            a += 1
        elif 0 <= a+1 <= n-1 and mat[a+1][b] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_lu(a, b, c) :
    global n
    stack = [[a, b]]
    # 왼쪽 위 대각선 확인
    while True :
        if 0 <= a-1 <= n-1 and 0 <= b-1 <= n-1 and mat[a-1][b-1] == 3-c :
            stack.append([a-1, b-1])
            a -= 1
            b -= 1
        elif 0 <= a-1 <= n-1 and 0 <= b-1 <= n-1 and mat[a-1][b-1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_ru(a, b, c) :
    global n
    stack = [[a, b]]
    # 오른쪽 위 대각선 확인
    while True :
        if 0 <= a-1 <= n-1 and 0 <= b+1 <= n-1 and mat[a-1][b+1] == 3-c :
            stack.append([a-1, b+1])
            a -= 1
            b += 1
        elif 0 <= a-1 <= n-1 and 0 <= b+1 <= n-1 and mat[a-1][b+1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_ld(a, b, c) :
    global n
    stack = [[a, b]]
    # 왼쪽 아래 대각선 확인
    while True :
        if 0 <= a+1 <= n-1 and 0 <= b-1 <= n-1 and mat[a+1][b-1] == 3-c :
            stack.append([a+1, b-1])
            a += 1
            b -= 1
        elif 0 <= a+1 <= n-1 and 0 <= b-1 <= n-1 and mat[a+1][b-1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break

def turn_rd(a, b, c) :
    global n
    stack = [[a, b]]
    # 오른쪽 아래 대각선 확인
    while True :
        if 0 <= a+1 <= n-1 and 0 <= b+1 <= n-1 and mat[a+1][b+1] == 3-c :
            stack.append([a+1, b+1])
            a += 1
            b += 1
        elif 0 <= a+1 <= n-1 and 0 <= b+1 <= n-1 and mat[a+1][b+1] == c :
            for i in stack :
                mat[i[0]][i[1]] = c
            break
        else :
            break


T = int(input())
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    mat = [[0]*n for _ in range(n)]

    mat[n//2][n//2] = 2
    mat[n//2-1][n//2-1] = 2
    mat[n//2-1][n//2] = 1
    mat[n//2][n//2-1] = 1

    for _ in range(m) :
        a, b, c = map(int, input().split())
        turn_r(b-1, a-1, c)
        turn_l(b-1, a-1, c)
        turn_u(b-1, a-1, c)
        turn_d(b-1, a-1, c)
        turn_ru(b-1, a-1, c)
        turn_rd(b-1, a-1, c)
        turn_lu(b-1, a-1, c)
        turn_ld(b-1, a-1, c)

    p = 0 # 흑돌
    q = 0 # 백돌

    for i in range(n) :
        for j in range(n) :
            if mat[i][j] == 1 :
                p += 1
            elif mat[i][j] == 2 :
                q += 1

    print(f'#{tc} {p} {q}')