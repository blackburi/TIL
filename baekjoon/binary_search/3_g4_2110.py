# 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

house = []
for _ in range(n) :
    house.append(int(input()))
house.sort()

# 공유기 사이의 거리의 최솟값
small = 1
# 공유기 사이의 거리의 최댓값
large = house[-1] - house[0]

answer = 0

while small <= large :
    # 현재 공유기 사이의 거리
    middle = (small + large) // 2

    # 마지막에 설치한 공유기의 위치
    now = house[0]

    # 공유기의 개수
    cnt = 1

    # 공유기가 몇대 설치 가능한지 check
    for i in range(1, n) :
        if house[i] >= now + middle :
            cnt += 1
            now = house[i]

    # 공유기를 설치했을 때 목표 개수보다 크다면 공유기 사이의 거리를 늘린다.
    if cnt >= c :
        small = middle + 1
        answer = middle
    # 공유기를 설치했을 때 목표 개수보다 작다면 공유기 사이의 거리를 줄인다.
    else : # cnt < c
        large = middle - 1

print(answer)