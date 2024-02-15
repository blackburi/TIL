# N & M 8

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()

sub = []

def dfs(x) :
    if len(sub) == m :
        print(*sub)
        return
    
    for i in range(x, n) :
        sub.append(lst[i])
        dfs(i)
        sub.pop()

dfs(0)