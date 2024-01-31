from collections import deque

whole = list(map(str, input().split(')')))

cal = ['+', '-', '*', '/']
stack = []
ans = deque([])

if len(whole) == 1 :
    sub = deque(list(map(str, whole[0])))
    
    for _ in range(len(sub)) :
        if sub[0] not in cal :
            a = sub.popleft()
            stack.append(a)
        else :
            b = sub.popleft()
            ans.appendleft(b)
    
    for _ in range(len(stack)) :
        c = stack.pop()
        ans.appendleft(c)
    
    print(''.join(ans))
else :
    for i in range(len(whole)-1, -1, -1) :
        while len(whole[i]) > 0 :
            sub = deque(list(map(str, whole[i])))

            for _ in range(len(sub)) :
                if sub[0] not in cal :
                    a = sub.popleft()
                    stack.append(a)
                else :
                    b = sub.popleft()
                    ans.appendleft(b)
            
            for _ in range(len(stack)) :
                c = stack.pop()
                ans.appendleft(c)
    print(''.join(ans))