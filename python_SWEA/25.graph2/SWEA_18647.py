# 최소 이동 거리

from heapq import heappush, heappop

def find_set(x) :
    if parents[x] == x :
        return x
    
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y) :
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x == y :
        return
    
    if x < y :
        parents[y] = x
    else :
        parents[x] = y


T = int(input())

for tc in range(1, T+1) :
    final, e = map(int, input().split())

    graph = []

    for _ in range(e) :
        start, end, cost = map(int, input().split())
        graph.append((start, end, cost))

    graph.sort(key = lambda x:x[2])
    parents = [i for i in range(final+1)]

    # MST 완성 확인
    cnt = 0

    # 최소 비용
    min_cost = 0

    # 간선들 모두 확인
    for start, end, cost in graph :
        if find_set(start) == find_set(end) :
            continue

        cnt += 1

        # cycle이 없다면 통과
        union(start, end)
        min_cost += cost

        if cnt == final - 1 :
            break
    
    print(f'#{tc} {min_cost}')