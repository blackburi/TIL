# 출퇴근길

import sys
input = sys.stdin.readline

# 정점의 수, 간선의 수
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()

s, t = map(int, input().split())