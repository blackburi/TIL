# DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1) :
    graph[i].sort()

# DFS
def dfs(start) :
    visited_dfs = []
    stack = [start]
    while stack :
        k = stack.pop()
        if k not in visited_dfs :
            visited_dfs.append(k)
            for w in graph[k][::-1] :
                stack.append(w)
    return visited_dfs

print(*dfs(v))

# BFS
visited_bfs = [False] * (n+1)
ans = []

def bfs(graph, start, visited) :
    ans.append(start)
    queue = deque([start])
    visited[start] = True

    while queue :
        z = queue.popleft()
        for j in graph[z] :
            if not visited[j] :
                ans.append(j)
                queue.append(j)
                visited[j] = True

bfs(graph, v, visited_bfs)
print(*ans)
