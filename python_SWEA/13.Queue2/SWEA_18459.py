v, e = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(v+1)]

for i in range(e) :
    graph[lst[2*i]].append(lst[2*i+1])
    graph[lst[2*i+1]].append(lst[2*i])

ans = ['1']
visited = [False] * (v+1)
stack = [1]
visited[1] = True

while stack :
    a = stack.pop(0)
    for w in graph[a] :
        if visited[w] is False :
            stack.append(w)
            ans.append(str(w))
            visited[w] = True

print(f'#1 {" ".join(ans)}')