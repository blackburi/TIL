# 특별한 정렬

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1) :
    num = list(map(int, input().split()))

    for i in range(len(num)-1) :
        for j in range(i+1, len(num)-1) :
            if 