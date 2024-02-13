T = 10

for tc in range(1, 11) :
    n = int(input())
    lst = list(input())
    stack = []

    for i in lst :
        if i != '+' :
            stack.append(int(i))
    
    ans = 0
    for j in stack :
        ans += j
    
    print(f'#{tc} {ans}')