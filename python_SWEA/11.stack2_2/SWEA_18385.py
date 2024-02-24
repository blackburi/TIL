win = {(1, 2) : 2, (2, 1) : 2,
       (2, 3) : 3, (3, 2) : 3,
       (3, 1) : 1, (1, 3) : 1,
       (1, 1) : 1,
       (2, 2) : 2,
       (3, 3) : 3}

def rsp(p) : # p : 가위바위보 하는 인원의 카드 list
    if len(p) == 1 :
        return p.pop()
    elif len(p) == 2 :
        a = win[p[0][0], p[1][0]]
        if a == p[0][0] :
            return p[0]
        else :
            return p[1]
    else : # len(p) > 2
        q = len(p)
        if len(p) % 2 == 0 :
            return rsp([rsp(p[0:q//2]), rsp(p[q//2:q])])
        else : # len(p) % 2 == 1
            return rsp([rsp(p[0:q//2+1]), rsp(p[q//2+1:q])])


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n) :
        lst[i] = [lst[i], i] # [가위바위보 카드, index]
    
    ans = rsp(lst)
    
    print(f'#{tc} {ans[1]+1}')