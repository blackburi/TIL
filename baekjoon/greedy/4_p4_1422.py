# 숫자의 신

import sys
input = sys.stdin.readline

# k개의 수중 n개를 뽑아 사용
k, n = map(int, input().split())

numbers = [int(input()) for _ in range(k)]
numbers.sort(key = lambda x : (x, ))