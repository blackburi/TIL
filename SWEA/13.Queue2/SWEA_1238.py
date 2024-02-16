for tc in range(1, 11) :
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]

    lst = list(map(int, input().split()))

    for i in range(n//2) :
        graph[lst[2*i]].append(lst[2*i+1])

    visited = [-1] * 101
    visited[start] = 0
    queue = [start]

    while queue :
        x = queue.pop(0)
        for w in graph[x] :
            if visited[w] == -1 :
                visited[w] = visited[x] + 1
                queue.append(w)

    last = []
    call_max = 0

    for i in range(1, 101) :
        if call_max < visited[i] :
            call_max = visited[i]
            last = [i]
        elif call_max == visited[i] :
            last.append(i)
    
    print(f'#{tc} {last[-1]}')