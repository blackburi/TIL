# 소문난 칠공주

import sys
input = sys.stdin.readline
from collections import deque


mat = [list(input().rstrip()) for _ in range(5)]

dx = [0, 1]
dy = [1, 0]

# 정답 수 출력
ans = 0