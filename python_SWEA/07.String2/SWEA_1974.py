T = int(input())

for tc in range(1, T+1) :
    mat = [list(map(int, input().split())) for _ in range(9)]

    cset = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    cnt = 0

    # 가로줄
    for i in range(9) :
        if set(mat[i]) == cset :
            cnt += 1
        else :
            break

    if cnt != 9 :
        print(f'#{tc} 0')
        continue
    
    # 세로줄
    for i in range(9) :
        if set(mat[j][i] for j in range(9)) == cset :
            cnt += 1
        else :
            break
    
    if cnt != 18 :
        print(f'#{tc} 0')
        continue

    # 박스 안
    xlst = [0, 3, 6]
    ylst = [0, 3, 6]
    for x in xlst :
        for y in ylst :
            lst = []
            for i in [0, 1, 2] :
                for j in [0, 1, 2] :
                    lst.append(mat[x+i][y+j])
            if set(lst) == cset :
                cnt += 1
            else :
                break
    
    if cnt == 27 :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')