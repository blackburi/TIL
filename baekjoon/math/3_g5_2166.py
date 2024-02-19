# 신발끈 정리

import sys
input = sys.stdin.readline

x = []
y = []
n = int(input())
for _ in range(n) :
    a, b = map(int, input().rstrip().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

plus = 0
minus = 0

for i in range(n) :
    plus += x[i]*y[i+1]
    minus += x[i+1]*y[i]

print(round(abs(plus-minus)/2, 1))