import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

up = [1] * n
down = [1] * n

for i in range(n-1) :
    if lst[i] > lst[i+1] :
        up[i+1] += up[i]
    elif lst[i] < lst[i+1] :
        down[i+1] += down[i]
    else : # lst[i] == lst[i+1]
        up[i+1] += up[i]
        down[i+1] += down[i]

umax = max(up)
dmax = max(down)

print(max(umax, dmax))