# 마트료시카

import sys
input = sys.stdin.readline
import heapq


n = int(input())
lst = list(map(int, input().rstrip().split()))

# 인형 크기를 내림차순으로 정렬
lst.sort(reverse=True)

# 우선순위 큐(dict로 구현)
pq = {i : [] for i in range(1, 100002)}

for x in lst :
    # x+1 크기의 인형이 없으면 x 크기 인형으로 새로운 마트료시카 시작
    if len(pq[x+1]) == 0 :
        # 최댓값을 위해 음수값을 사용 -> python은 최소힙으로 구현되어있음
        heapq.heappush(pq[x], -x)
    else :
        # x+1 크기의 인형이 있으면 그 인형을 현재 크기의 인형으로 변환
        num = -heapq.heappop(pq[x+1])
        heapq.heappush(pq[x], -num)

ans = 0

# 각 크기별로 구성된 마트료시카의 수익 계산
for i in range(1, 100002) :
    while pq[i] :
        node = -heapq.heappop(pq[i])
        ans += node * (node - i + 1)

print(ans)