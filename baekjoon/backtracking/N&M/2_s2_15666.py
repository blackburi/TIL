# N & M 12

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = list(set(lst))
lst.sort()

sub = []

def dfs(x) :
    if len(sub) == m :
        print(*sub)
        return
    
    for i in range(x, len(lst)) : 
        sub.append(lst[i])
        dfs(i)
        sub.pop()

dfs(0)
