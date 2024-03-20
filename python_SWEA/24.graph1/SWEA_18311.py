# 그래프 탐색

v, e = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(v+1)]
for i in range(e) :
    graph[lst[2*i]].append(lst[2*i+1])
    graph[lst[2*i+1]].append(lst[2*i])

for i in range(1, v+1) :
    graph[i] = graph[i][::-1]

q = [1]
visited = [False] * (v+1)

# dfs 방문 순서
ans = []

while q :
    k = q.pop()

    if visited[k] is False :
        visited[k] = True
        ans.append(k)

    for w in graph[k] :
        if visited[w] is False :
            q.append(w)

print(f'#1','-'.join(map(str, ans)))