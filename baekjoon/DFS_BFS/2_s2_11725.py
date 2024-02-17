import sys
input = sys.stdin.readline

n = int(input()) # 노드의 개수

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
queue = [1]
visited[1] = 1

while queue :
    x = queue.pop(0)
    for w in graph[x] :
        if visited[w] == 0 :
            visited[w] = visited[x] + 1
            queue.append(w)

for i in range(2, n+1) :
    for w in graph[i] :
        if visited[w] == visited[i] - 1 :
            print(w)
            break
