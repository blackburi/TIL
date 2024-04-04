# 보석 도둑

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

# 전체 보석
jewels = []
for _ in range(n) :
    # (보석 무게, 보석 가격)
    heapq.heappush(jewels, tuple(map(int, input().rstrip().split())))

# 가방에 넣을 수 있는 보석의 최대 무게
bags = []
for _ in range(k) :
    bags.append(int(input().rstrip()))
# 가방을 오름차순으로 정렬
bags.sort()

# 각 가방에 담을 수 있는 모든 보석을 찾을때 최소힙을 사용
# 넣을 수 있는 보석중 가치가 가장 큰 보석을 찾는다

# 보석 가격 총합
total = 0
jewel = []
for bag in bags :
    while jewels and bag >= jewels[0][0] :
        heapq.heappush(jewel, -heapq.heappop(jewels)[1])

    if jewel :
        total -= heapq.heappop(jewel)
    elif not jewels :
        break

print(total)