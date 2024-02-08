import sys
input = sys.stdin.readline

n = int(input())

lst = [0] * 1001
lst[0] = 1
lst[1] = 1

for i in range(2, 1001) :
    lst[i] = lst[i-1] + 2 * lst[i-2]

print(lst[n]%10007)