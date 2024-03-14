# 출퇴근길

# 문제에서 원하는 경로는 총 네가지
# start -> start
# start -> end
# end -> end
# end -> end
# 시작점에서 출발하여 도착점에 도착하거나 도착점에서 출발하여 시작점에 도착하면 끝
# dfs가 아닌 bfs로 풀어야 하는 문제
# 문제에서 원하는 경로 4가지를 전부 bfs로 탐색
# 4개가 전부 1이 된다면 정답 


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

# 출근1 s->t
visited_go_end = [False] * (n+1)
visited_go_end[t] = True
bfs(s, graph_go, visited_go_end)

# 출근2 s->s
visited_go_cycle = [False] * (n+1)
bfs(s, graph_back, visited_go_cycle)

# 퇴근1 t->s
visited_back_start = [False] * (n+1)
visited_back_start[s] = True
bfs(t, graph_go, visited_back_start)

# 퇴근2 t->t
visited_back_cycle = [False] * (n+1)
bfs(t, graph_back, visited_back_cycle)

# 출퇴근시 모두 겹치는 노드를 세는 변수
cnt = 0

for i in range(1, n+1) :
    # s, t를 제외해줘야 하기 때문에
    if i == s or i == t :
        continue
    if visited_go_cycle[i] and visited_go_end[i] and visited_back_start[i] and visited_back_cycle[i] :
        cnt += 1

print(cnt)