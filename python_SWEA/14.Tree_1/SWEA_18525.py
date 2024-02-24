T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    lst = [0] * (n+1)

    def number(x) :
        global cnt
        if x > n :
            return
        number(2*x)
        lst[x] = cnt
        cnt += 1
        number(2*x+1)
    
    cnt = 1
    number(1)

    print(f'#{tc} {lst[1]} {lst[n//2]}')