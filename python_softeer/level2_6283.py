# 8단 변속기

import sys
input = sys.stdin.readline

lst = list(map(int, input().rstrip().split()))

if lst == [1, 2, 3, 4, 5, 6, 7, 8] :
    print('ascending')
elif lst == [8, 7, 6, 5, 4, 3, 2, 1] :
    print('descending')
else :
    print('mixed')