T = int(input())

for tc in range(1, T+1) :
    lst = list(input())

    stack = []

    while lst :
        for _ in lst :
            if stack == [] :
                a = lst.pop(0)
                stack.append(a)
            elif stack[-1] == lst[0] :
                stack.pop()
                lst.pop(0)
            else :
                a = lst.pop(0)
                stack.append(a)
    
    print(f'#{tc} {len(stack)}')