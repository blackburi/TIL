T = int(input())

for tc in range(1, T+1) :
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())

    visited = [False] * (v+1)
    stack = [s]
    while stack :
        p = stack.pop()
        if not visited[p] :
            visited[p] = True
            for w in graph[p] :
                stack.append(w)
    
    if visited[g] is True :
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')