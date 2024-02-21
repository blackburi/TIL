T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    
    # 가로, 우하향 대각선
    r_check = [[] for _ in range(n)]
    # 세로, 좌하향 대각선
    c_check = [[] for _ in range(n)]

    for i in range(n) :
        lst = list(input())
        for j in range(n) :
            if lst[j] == 'o' :
                r_check[j].append(i)
                c_check[i].append(j)
    
    cnt = 0
    for p in range(n-4) :
        if len(r_check(p)) > 0 and len(r_check(p+1)) > 0 and len(r_check(p+2)) > 0 and len(r_check(p+3)) > 0 and len(r_check(p+4)) > 0 :
           cnt += 1
           break
        if r_check :
            for i in r_check :
                if (i+1) in r_check

    if cnt == 1 :
        print(f'#{tc} YES')
        continue

    for p in range(n-4) :
        if len(c_check(p)) > 0 and len(c_check(p+1)) > 0 and len(c_check(p+2)) > 0 and len(c_check(p+3)) > 0 and len(c_check(p+4)) > 0 :
            cnt += 1
            break

    if cnt == 1 :
        print(f'#{tc} YES')
        continue