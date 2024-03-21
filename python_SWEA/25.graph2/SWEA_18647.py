# 최소 이동 거리

from heapq import heappush, heappop


def dijkstra(start) :
    pq = []

    # 시적점의 노드와 cost를 저장
    heappush(pq, (start, 0))

    # 시작 노드 초기화
    distance[start] = 0

    while pq :
        # 최단 거리 노드에 대한 정보
        now, dist = heappop(pq)

        # 더 짧게 온 경우
        if distance[now] < dist :
            continue

        # now에서 인접한 다른 노드 확인
        for go in graph[now] :
            next_dist = go[1]
            next_node = go[0]

            # 누적거리 계산
            new_dist = dist + next_dist

            # 이미 짧은 거리로 방문했다면 
            if new_dist > distance[next_node] :
                continue

            # 누적거리 갱신
            distance[next_node] = new_dist
            # next_node의 인접 노드들을 pq에 추가
            heappush(pq, (next_node, new_dist))


T = int(input())
for tc in range(1, T+1) :
    final, e = map(int, input().split())
    inf = int(1e9)

    # 인접 list
    graph = [[] for _ in range(final+1)]

    # 누적거리 저장
    distance = [inf] * (final+1)

    for _ in range(e) :
        start, end, cost = map(int, input().split())
        graph[start].append([end, cost])

    dijkstra(0)
    print(f'#{tc} {distance[final]}')
