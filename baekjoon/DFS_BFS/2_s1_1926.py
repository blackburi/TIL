import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
mat = [list(map(str, input().split()))]

cnt = 0 # 그림의 수
area = 0 # 그림의 최대 넓이
tmp = 0

