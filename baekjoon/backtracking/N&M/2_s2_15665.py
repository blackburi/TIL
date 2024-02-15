# N & M 11

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = list(set(lst))
lst.sort()

sub = []

def dfs() :
    if len(sub) == m :
        print(*sub)
        return
    
    for i in range(len(lst)) :
        sub.append(lst[i])
        dfs()
        sub.pop()

dfs()