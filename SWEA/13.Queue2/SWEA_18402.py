T = int(input())

for tc in range(1, T+1) :
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # s : 출발 노드, g : 도착 노드
    s, g = map(int, input().split())
    visited = [0] * (v+1)
    visited[s] = 1
    queue = [s]

    while queue :
        x = queue.pop(0)
        for w in graph[x] :
            if visited[w] == 0 :
                visited[w] = visited[x] + 1
                queue.append(w)

    if visited[g] == 0 :
        print(f'#{tc} 0')
    else :
        print(f'#{tc} {visited[g] - 1}')