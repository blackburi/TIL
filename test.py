"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

from heapq import heappush, heappop

def prime(start) :
    pq = []
    visited = [0] * v

    # 최소 비용
    sum_cost = 0

    # 시작점 추가
    # 기존 bfs에서는 노드 번호만 관리
    # prime에서는 우선 순위가 가중치에 따라 정렬 되어야 한다
    # 관리해야할 데이터 : 가중치, 노드 번호 (두 가지)
    # -> 1. class로 관리 , 2. tuple로 관리
    # 두개까지는 tuple로 관리하는것이 용이, but 3개 이상부턴 class 관리가 효율적이다.
    heappush(pq, (0, start))

    while pq :
        cost, now = heappop(pq)

        # 이미 기존에 더 짧은 거리로 방문했다면 continue
        if visited[now] :
            continue

        # 방문처리
        visited[now] = 1
        # 누적합 추가
        sum_cost += cost

        # 갈수 있는 노드들을 보면서
        for to in range(v) :
            # 갈수 없다면, 이미 방문했다면 pass
            if graph[now][to] == 0 or visited[to] :
                continue

            heappush(pq, (graph[now][to], to))
    
    print(f'최소비용 : {sum_cost}')


v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]

# 인접 행렬로 저장
# 가중치 그래프로 저장
for _ in range(e) :
    start, end, cost = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

prime(0)


#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################


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


v, e = map(int, input().split())
edges = [] #  간선 정보들을 모두 저장
for _ in range(e) :
    start, end, cost = map(int, input().split())
    edges.append([start, end, cost])
edges.sort(key = lambda x: x[2]) # 가중치를 기준으로 정렬
parents = [i for i in range(v)] # 대표자 배열 (자기자신을 바라봄)

# MST를 완성했는지 확인하는 변수 -> 간선의 수가 v-1이 되는 경우
cnt = 0

sum_cost = 0

# 간선들을 모두 확인
for start, end, cost in edges :
    # cycle이 발생하면 pass
    # -> 이미 같은 집합에 속해 있다면 pass
    if find_set(start) == find_set(end) :
        continue

    cnt += 1

    # cycle이 없다면 통과
    union(start, end)
    sum_cost += cost

    if cnt == v-1 # MST완성
        break

print(f'최소비용 : {sum_cost}')