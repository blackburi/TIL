# N & M 10

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [False] * n
sub = []

def dfs(x) :
    remember = 0
    if len(sub) == m :
        print(*sub)
        return
    
    for i in range(x, n) :
        if remember != lst[i] and visited[i] is False :
            sub.append(lst[i])
            remember = lst[i]
            visited[i] = True
            dfs(i+1)
            visited[i] = False
            sub.pop()

dfs(0)