for _ in range(1, 11) :
    tc = int(input())
    s = list(input())
    sen = list(input())

    cnt = 0
    
    n = len(s) # lenght of pattern
    m = len(sen)
    
    p = 0 # index of s
    q = 0 # index of sen

    while q < m-n+1 :
        if s[p] == sen[q] :
            tmp = 0
            for i in range(n) :
                if s[p+i] == sen[q+i] :
                    tmp += 1
                else :
                    break
            if tmp == n :
                cnt += 1
                p = 0
                q += n
            else : # tmp != n
                p = 0
                q += tmp
        else : # s[p] != sen[q]
            q += 1
    
    print(f'#{tc} {cnt}')