for tc in range(1, 11) :
    _ = int(input())
    mat = [list(map(str, input().split())) for _ in range(100)]

    cnt = 0 # 교착상태의 수
    for i in range(100) :
        for j in range(100) :
            if mat[i][j] == '1' :
                a = i+1
                while 0<=a<=99 :
                    if mat[a][j] == '0' :
                        pass
                    # 1을 만나면 교차 X
                    elif mat[a][j] == '1' :
                        break
                    # 2를 만나면 교착 상태 발생
                    else : # mat[a][j] == '2'
                        cnt += 1
                        break
                    a += 1
    
    print(f'#{tc} {cnt}')