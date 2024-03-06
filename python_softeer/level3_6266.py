# 염기서열 커버

import sys
input = sys.stdin.readline

# n 회의실 개수, m 회의 개수
n, m = map(int, input().split())

# 회의실 이름을 담는 list
lst = []
for _ in range(n) :
    lst.append(input().rstrip())