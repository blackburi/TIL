# N & M 9

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()

ans = []
sub = []

def dfs() :
    if len(sub) == m :
        if sub in ans :
            return
        else :
            a = sub
            if a not in ans :
                ans.append(a)
            return
    
    for i in range(n) :
        sub.append(lst[i])
        dfs()
        sub.pop()

dfs()
print(ans)