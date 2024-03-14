# 지도 자동 구축

import sys
input = sys.stdin.readline

n = int(input())

# 초기값
start = 2

while n :
    start = 2 * start - 1
    n -= 1

print(start ** 2)