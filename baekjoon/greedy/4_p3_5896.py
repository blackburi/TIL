# 효율적으로 소 사기

import sys
input = sys.stdin.readline
import heapq

# 쿠폰을 활용하여 가장 큰 할인을 받으면서 가격이 싼 소들을 많이 사야 한다.

n, k, m = map(int, input().split())
cows =[tuple(map(int, input().rstrip().split())) for _ in range(n)]

# 쿠폰을 썻을때 싼 순서 -> 쿠폰을 썻을때 가격이 동일하다면 원가가 싼 순서
cows.sort(key = lambda x : (x[1], x[0]))

# 지불한 금액
pay = 0
# 산 소의 수
cow = 0

coupons = []

# 쿠폰을 사용하여 싼 소들을 전부 구매
# 가격폭이 큰 순서
for  i in range(k) :
    if cows[i][1] + pay <= m :
        pay += cows[i][1]
        cow += 1
        heapq.heappush(coupons, cows[i][0]-cows[i][1])

for j in range(k, n) :
    # 이전에 쿠폰으로 산 소의 금액 + 소의 비용(쿠폰O) < 소의 비용(쿠폰X)
    # 즉 더 큰 할인을 받을수 있는 경우
    if coupons and coupons[0] + cows[j][1] < cows[j][0] :
        if pay + coupons[0] + cows[j][1] <= m :
            # 금액 갱신
            pay += heapq.heappop(coupons) + cows[j][1]
            # 소 + 1
            cow += 1
            # coupons 갱신
            heapq.heappush(coupons, cows[j][0]-cows[j][1])
    # 더 큰 할인을 받지 못하는 경우
    else :
        if pay + cows[j][0] <= m :
            pay += cows[j][0]
            cow += 1

print(cow)