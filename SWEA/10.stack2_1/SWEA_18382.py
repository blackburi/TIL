T = int(input())
cal = ['+', '-', '*', '/']

for tc in range(1, T+1) :
    lst = list(input().rstrip().split())
    stack = []
    
    while lst :
        a = lst.pop(0)

        if a == '.' :
            ans = stack.pop()
            break

        if a not in cal :
            stack.append(int(a))
        
        else : # a in cal
            if len(stack) < 2 :
                break

            x = stack.pop()
            y = stack.pop()

            if a == '+' :
                stack.append(y+x)
            elif a == '-' :
                stack.append(y-x)
            elif a == '*' :
                stack.append(y*x)
            elif a == '/' :
                stack.append(y//x)
    
    if lst or stack :
        print(f'#{tc} error')
    else :
        print(f'#{tc} {ans}')