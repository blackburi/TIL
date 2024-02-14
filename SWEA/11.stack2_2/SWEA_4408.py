T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = [0] * 401
    for i in range(n) :
        a, b = map(int, input().split())
        if a > b :
            a, b = b, a # a는 작은수, b는 큰수
        
        # 작은수가 짝수라면 홀수 방까지 생각
        # 큰수가 홀수라면 짝수 방까지 생각
        a = (a+1)//2 * 2 - 1
        b = (b+1)//2 * 2
        for j in range(a, b+1) :
            lst[j] += 1
    
    M = 0
    for k in lst :
        if M < k :
            M = k
    
    print(f'#{tc} {M}')