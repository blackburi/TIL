# BFS 연습

from collections import deque

v, e = map(int, input().split())
lst = list(map(int, input().split()))

graph = [[] for _ in range(v+1)]
for i in range(e) :
    graph[lst[2*i]].append(lst[2*i+1])
    graph[lst[2*i]].sort()
    graph[lst[2*i+1]].append(lst[2*i])
    graph[lst[2*i+1]].sort()
visited = [False] * (v+1)

q = deque([1])
visited[1] = True
ans = []

while q :
    k = q.popleft()
    ans.append(k)
    for w in graph[k] :
        if visited[w] is False :
            visited[w] = True
            q.append(w)

print(f'#1', *ans)