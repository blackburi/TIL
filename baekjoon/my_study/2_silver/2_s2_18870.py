# 시간 초과

import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num_2 = sorted(list(set(num)))

num_dict = {num_2[i] : i for i in range(len(num_2))}

for p in num :
    print(num_dict[p], end = ' ')