# 시험 감독

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
b, c = map(int, input().split())

total = 0

for i in lst :
    total += 1
    i -= b

    if i > 0 :
        if i % c == 0 :
            total += i//c
        else :
            total += i//c + 1

print(total)