# 최소 신장

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
    v, e = map(int, input().split())

    edges = []
    for _ in range(e) :
        start, end, cost = map(int, input().split())
        edges.append((start, end, cost))

    edges.sort(key = lambda x : x[2])
    parents = [i for i in range(v+1)]

    # 최소 비용
    min_cost = 0
    # MST를 만들었는지 확인하는 변수(v가 된다면 종료 : 총 v+1개 노드)
    cnt = 0

    for start, end, cost in edges :
        # cycle발생
        if find_set(start) == find_set(end) :
            continue

        cnt += 1

        union(start, end)
        min_cost += cost

        if cnt == v :
            break

    print(f'#{tc} {min_cost}')