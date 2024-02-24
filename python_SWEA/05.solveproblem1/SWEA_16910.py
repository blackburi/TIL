import sys
input = sys.stdin.readline


T = int(input())

for tc in range(1, T+1) :
    r = int(input()) # r은 반지름

    number = 0

    for k in range(-r, r+1, 1) :
        number += int((r**2 - k**2)**0.5) * 2 + 1

    print(f'#{tc} {number}')
