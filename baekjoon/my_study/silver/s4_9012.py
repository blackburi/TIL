T = int(input())

for test in range(T) :
    S = list(map(str, input()))
    
    a = 0 # ')'의 개수
    b = 0 # '('의 개수

    for i in range(len(S)) :
        t = S.pop()
        
        if t == ')' :
            a += 1
        else :
            b += 1
        
        if a - b >= 0 :
            continue
        else :
            break
    
    if a - b == 0 :
        print('YES')
    else :
        print('NO')


# idea
# 오른쪽부터 ')'의 개수가 반드시 '('의 개수보다 많아야 한다.