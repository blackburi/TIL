T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    mat = [list(map(str, input().split())) for _ in range(n)]

    # 유적의 최대 길이
    length = 0
    for i in range(n) :
        for j in range(m) :
            if mat[i][j] == '1' :
                # 가로 체크
                if j == 0 or mat[i][j-1] == '0' :
                    cnt = 1
                    for k in range(j+1, m) :
                        if mat[i][k] == '1' :
                            cnt += 1
                        else :
                            break
                    if length < cnt :
                        length = cnt
                # 세로 체크
                if i == 0 or mat[i-1][j] == '0' :
                    cnt = 1
                    for k in range(i+1, n) :
                        if mat[k][j] == '1' :
                            cnt += 1
                        else :
                            break
                    if length < cnt :
                        length = cnt
    print(f'#{tc} {length}')