T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    pascal = [[0]*i for i in range(1, n+1)]

    for k in range(n) :
        if k == 0 :
            pascal[k] = [1]
        elif k == 1 :
            pascal[k][0] = 1
            pascal[k][-1] = 1
        else : # k > 1
            pascal[k][0] = 1
            pascal[k][-1] = 1
            for j in range(1, k) :
                pascal[k][j] = pascal[k-1][j-1] + pascal[k-1][j]
    
    print(f'#{tc}')
    for p in range(n) :
        print(*pascal[p])