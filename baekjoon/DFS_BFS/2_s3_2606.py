import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(e) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
stack = deque([1])

cnt = 0
def bfs() :
    global cnt
    while stack :
        x = stack.popleft()
        if visited[x] is False :
            visited[x] = True
            cnt += 1
            stack.extend(graph[x])

bfs()
print(cnt-1)