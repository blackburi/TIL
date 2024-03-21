# 최소 비용

from heapq import heappush, heappop


def prim(start) :
    pq = []
    visited = [0] * (n**2)

    # 최소 비용
    min_cost = 0

    # (cost, node)형태로 집어넣음
    heappush(pq, (0, start))

    while pq :
        cost, now = heappop(pq)

        # 이미 기존에 더 짧은 거리로 방문했다면 continue
        if visited[now] :
            continue

        # 방문처리
        visited[now] = 1
        # 누적합 추가
        min_cost += cost

        # 갈수 있는 노드들을 보면서
        for go in 




T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    graph = [[] for _ in range(n**2)]
    for i in range(n**2) :
        if i == 0 :
            graph[i] = (i+1, i+n)
        elif i < n-1 :
            graph[i]