# N & M 9

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()

visited = [False] * n
sub = []
ans = []

def dfs() :
    remember = 0
    if len(sub) == m :
        print(*sub)
        return

    for i in range(n) :
        if lst[i] != remember and visited[i] is False :
            visited[i] = True
            sub.append(lst[i])
            remember = lst[i]
            dfs()
            visited[i] = False
            sub.pop()

dfs()