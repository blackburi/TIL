# 슈퍼컴퓨터 클러스터

import sys
input = sys.stdin.readline

# 컴퓨터 수, 예산
n, b = map(int, input().split())

# 컴퓨터의 성능
capacity = tuple(map(int, input().rstrip().split()))
k = max(capacity)

# count sort
lst = [0] * (k+1)
for i in capacity :
    lst[i] += 1

# 가장 낮은 컴퓨터의 성능
tmp = 1

# 조건 달성시 멈추게 할 변수
flag = 0

while True :
    # 비용의 총합
    total = 0

    if tmp <= k :
        for i in range(1, tmp) :
            total += ((tmp - i)**2) * lst[i]
            if total > b :
                flag = 1
                break
    else : # tmp > k
        for i in range(1, k+1) :
            total += ((tmp - i)**2) * lst[i]
            if total > b :
                flag = 1
                break

    if flag == 1 :
        tmp -= 1
        break

    if total < b :
        tmp += 1
    elif total > b :
        tmp -= 1
        break
    else : # total == b
        break

print(tmp)