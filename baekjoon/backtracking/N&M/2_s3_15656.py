# N & M 7

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()

sub = []

def dfs() :
    if len(sub) == m :
        print(*sub)
        return
    
    for i in range(n) :
        sub.append(lst[i])
        dfs()
        sub.pop()
    
dfs()