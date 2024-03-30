# 보호 필름

import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())

# 전체 보석
jewels = []
for _ in range(n) :
    # (보석 무게, 보석 가격)
    heapq.heappush(jewels, tuple(map(int, input().rstrip().split())))

# 가방에 넣은 보석
bags = []
for _ in range(k) :
    bags.append(int(input().rstrip()))

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