# 다리 만들기

import sys
input = sys.stdin.readline
from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
mat = [list(map(str, input().rstrip().split())) for _ in range(n)]

