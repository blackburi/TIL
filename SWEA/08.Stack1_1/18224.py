T = int(input())

for tc in range(1, T+1) :
    n = list(input())
    
    lst = []
    for i in n :
        if i in ['(', ')', '{', '}'] :
            lst.append(i)
    
    stack = []
    for j in range(len(lst)) :
        if j == 0 :
            stack.append(lst[j])
        elif lst[j] == ')' and stack[-1] == '(' :
            stack.pop()
        elif lst[j] == '}' and stack[-1] == '{' :
            stack.pop()
        else :
            stack.append(lst[j])
    
    if stack == [] :
        print(f'#{tc} {1}')
    else :
        print(f'#{tc} {0}')