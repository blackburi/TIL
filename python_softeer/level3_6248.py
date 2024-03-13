# 출퇴근길

# 문제에서 원하는 경로는 총 네가지
# start -> start
# start -> end
# end -> end
# end -> end
# 시작점에서 출발하여 도착점에 도착하거나 도착점에서 출발하여 시작점에 도착하면 끝
# dfs가 아닌 bfs로 풀어야 하는 문제
# 문제에서 원하는 경로 4가지를 전부 bfs로 탐색
# 


import sys
input = sys.stdin.readline
from collections import deque

# 정점의 수, 간선의 수
n, m = map(int, input().split())

# 출근 graph
graph_go = [[] for _ in range(n+1)]

# 퇴근 graph
graph_back = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph_go[a].append(b)
    graph_go[a].sort()
    graph_back[b].append(a)
    graph_back[b].sort()

s, t = map(int, input().split())


def bfs(start, graph, visited) :
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q :
        move = q.popleft()
        for w in graph[move] :
            if visited[w] is False :
                visited[w] = True
                q.append(w)

# 출근