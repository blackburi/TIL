T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(n)]

    ans = []

    for i in range(n) :
        for j in range(n-m+1) :
            cnt = 0
            for k in range(m//2) :
                if lst[i][j+k] == lst[i][j+m-1-k] :
                    cnt += 1
            if cnt == m//2 :
                for p in range(m) :
                    ans.append(lst[i][j+p])
                break
        for j in range(n-m+1) :
            cnt = 0
            for k in range(m//2) :
                if lst[j+k][i] == lst[j+m-1-k][i] :
                    cnt += 1
            if cnt == m//2 :
                for p in range(m) :
                    ans.append(lst[j+p][i])
                break
    
    print(f'#{tc} {"".join(ans)}')
