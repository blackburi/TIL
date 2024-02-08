v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

lst = list(map(int, input().split()))
for i in range(e) :
    graph[lst[2*i]].append(lst[2*i+1])
    graph[lst[2*i+1]].append(lst[2*i])

for i in range(e) :
    for j in range(len(graph[i])-1) :
        # sort 하기 위해 두번 돌리는게 맞지만
        for k in range(len(graph[i])-1-j) :
            if graph[i][k] > graph[i][k+1] :
                graph[i][k], graph[i][k+1] = graph[i][k+1], graph[i][k]


visited = [False] * (v+1)
ans = []
stack = [1]

while stack :
    a = stack.pop()
    if not visited[a] :
        visited[a] = True
        ans.append(str(a))
        for w in graph[a][::-1] :
            stack.append(w)

print(f'#1 {"-".join(ans)}')