for tc in range(1, 11) :
    n, sub = list(map(str, input().split()))
    
    lst = list(sub)
    stack = []
    
    while lst :
        if stack == [] or lst[-1] != stack[-1] :
            stack.append(lst.pop())
        else : 
            lst.pop()
            stack.pop()
    
    stack.reverse()
    print(f'#{tc} {"".join(stack)}')