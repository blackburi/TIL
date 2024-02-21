def check() :
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    for i in range(n) :
        for j in range(n) :
            for k in range(4) :
                # a, b로 다시 넣어주는 이유는 while문에서 계속 계산이 되기 때문에 초기화해주는 것
                a = i
                b = j
                cnt = 0
                while 0<=a<=n-1 and 0<=b<=n-1 and mat[a][b] == 'o' :
                    cnt += 1
                    a += dx[k]
                    b += dy[k]
                    
                    if cnt == 5 :
                        break
                
                if cnt == 5 :
                    return 1
    return 0

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    mat = [list(input()) for _ in range(n)]

    ans = check()
    if ans == 1 :
        print(f'#{tc} YES')
    else : # ans == 0
        print(f'#{tc} NO')