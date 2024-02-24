# 숫자 배열 회전

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(map(str, input().split())) for _ in range(n)]
    
    print(f'#{tc}')

    sub = []
    for _ in range(3) :
        sub_sub = []
        for i in range(n) :
            line = []

            for j in range(n) :
                line.append(mat[j][i])
            
            line.reverse()
            sub_sub.append(line)
        sub.append(sub_sub)
        mat = sub_sub

    for k in range(n) :
        print(''.join(sub[0][k]), ''.join(sub[1][k]), ''.join(sub[2][k]))