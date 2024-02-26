import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
m = int(input())

sub = []
for i in range(n) :
    if lst[i] != -1 :
        sub.append([i, lst[i]])

for i in sub :
    if m in i :
        del i

print(sub)