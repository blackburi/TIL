for _ in range(1, 11) :
    tc, e = map(int, input().split())

    lst = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for i in range(e) :
        graph[lst[2*i]].append(lst[2*i+1])

    visited = [False] * 100
    stack = [0]

    while stack :
        p = stack.pop()
        if not visited[p] :
            visited[p] = True
            for w in graph[p] :
                stack.append(w)
    
    if visited[99] is True :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')