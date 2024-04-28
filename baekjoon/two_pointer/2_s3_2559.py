# 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tem = list(map(int, input().split()))

hap = sum(tem[0:k])
tem_max = hap

for i in range(n-k) :
    hap = hap + tem[i+k] -tem[i]
    if tem_max < hap :
        tem_max = hap

print(tem_max)