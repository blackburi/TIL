win = {(1, 2) : 2, (2, 1) : 2,
       (2, 3) : 3, (3, 2) : 3,
       (3, 1) : 1, (1, 3) : 1,
       (1, 1) : 1,
       (2, 2) : 2,
       (3, 3) : 3}

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n) :
        lst[i] = [lst[i], i] # [가위바위보 카드, index]
    
    while lst :
        if n%4 in [0, 3] :
            for i in range(n//2) :
                a = win[(lst[i][0], lst[i+1][0])]
                if a == lst[i][0] :
                    del lst[i+1]
                else : # a == lst[i+1]
                    del lst[i]
        else : # n%4 in [1, 2] :
            k = (n+1)//2
            for i in range(k) :
                a = win[(lst[i][0], lst[i+1][0])]
                if a == lst[i][0] :
                    del lst[i+1]
                else : # a == lst[i+1]
                    del lst[i]
                
                b = win[(lst[k-1][0], lst[k][0])]
                if a == lst[k-1][0] :
                    del lst[k]
                else : # a == lst[i+1]
                    del lst[k-1]

        n = (n+1)//2

        if len(lst) == 1 :
            ans = lst.pop()
    
    print(f'#{tc} {ans[1]+1}')