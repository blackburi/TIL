T = int(input())

for tc in range(1, T+1) :
    sen, s = list(map(str, input().split()))
    s = list(s)
    sen = list(sen)

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
    
    ans = m - cnt * n + cnt
    print(f'#{tc} {ans}')