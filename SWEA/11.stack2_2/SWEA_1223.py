for tc in range(1, 11) :
    n = int(input())
    lst = list(input())
    stack = []

    while lst :
        a = lst.pop(0)
        if a == '*' :
            p = stack.pop()
            q = lst.pop(0)
            stack.append(p*int(q))
        elif a == '+' :
            pass
        else : # a = int
            stack.append(int(a))

    ans = 0
    for i in stack :
        ans += i
    
    print(f'#{tc} {ans}')