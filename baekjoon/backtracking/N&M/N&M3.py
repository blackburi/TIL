# N & M 3

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = [i for i in range(1, n+1)]

for _ in range(m) :
    sub = []
    while len(sub) < m :
        