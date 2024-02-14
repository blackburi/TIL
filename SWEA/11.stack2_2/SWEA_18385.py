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
        for i in range(n//2) :
            a = win[(lst[i][0], lst[i+1][0])]
            if a == lst[i][0] :
                del lst[i+1]
            else : # a == lst[i+1]
                del lst[i]

        n = (n+1)//2

        if len(lst) == 1 :
            ans = lst.pop()
    
    print(f'#{tc} {ans[1]+1}')