T = int(input())
for tc in range(1, T+1) :
    n = list(input())
    
    lst = []
    for i in n :
        if i in ['(', ')'] :
            lst.append(i)

    if lst[0] == ')' :
        print(f'#{tc} -1')
        continue

    stack = []
    for j in range(len(lst)) :
        stack.append(lst[j])
        if stack[-1] == ')' and stack[-2] == '(' :
            stack.pop()
            stack.pop()
    
    if stack == [] :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} -1')