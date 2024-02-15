# N & M 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = []

def dfs(x) :
    if len(lst) == m :
        print(*lst)
        return

    for i in range(x, n+1) :
        lst.append(i)
        dfs(i)
        lst.pop()

dfs(1)