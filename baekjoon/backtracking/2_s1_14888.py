# 연산자 끼워넣기

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
cal = list(map(int, input().split()))

cmax = -1e9
cmin = 1e9

def dfs(cnt, total, plus, minus, multi, divide) :
    global cmax, cmin

    if cnt == n :
        cmax = max(total, cmax)
        cmin = min(total, cmin)
    
    if plus :
        dfs(cnt+1, total + lst[cnt], plus-1, minus, multi, divide)
    if minus :
        dfs(cnt+1, total - lst[cnt], plus, minus-1, multi, divide)
    if multi :
        dfs(cnt+1, total * lst[cnt], plus, minus, multi-1, divide)
    if divide :
        dfs(cnt+1, int(total / lst[cnt]), plus, minus, multi, divide-1)

dfs(1, lst[0], cal[0], cal[1], cal[2], cal[3])
print(cmax)
print(cmin)