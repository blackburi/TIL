# 회전 초밥

import sys
input = sys.stdin.readline

# 접시 수, 초밥 종류수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())

cnt = 1

sushi = [0] * (d+1)
sushi[c] = 1

lst = []
for _ in range(n) :
    lst.append((int(input())))

for i in range(k) :
    sushi[lst[i]] += 1
    if sushi[lst[i]] == 1 :
        cnt += 1

answer = cnt

for i in range(n-1) :
    sushi[lst[i]] -= 1
    if sushi[lst[i]] == 0 :
        cnt -= 1

    sushi[lst(i+k)%n] += 1
    if sushi[lst(i+k)%n] == 1 :
        cnt += 1

    answer = max(answer, cnt)

print(answer)