# N & M 3

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

lst = []

def dfs() :
    if len(lst) == m :
        print(*lst)
        return
    
    for i in range(1, n+1) :
        lst.append(i)
        dfs()
        lst.pop()

dfs()