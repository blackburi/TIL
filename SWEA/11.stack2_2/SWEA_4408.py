T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    stack = []
    
    while lst :
        a, b = lst.pop()
        if a > b :
                a, b = b, a # a는 작은수, b는 큰수

        for i in lst :
            if ((a-1)//2)*2+1 <= i[0] <= ((b+1)//2)*2 or ((a-1)//2)*2+1 <= i[1] <= ((b+1)//2)*2 :
                pass
            else : 
                idx = lst.index(i)
                lst.pop(idx)
        
        cnt += 1
    
    print(f'#{tc} {cnt}')