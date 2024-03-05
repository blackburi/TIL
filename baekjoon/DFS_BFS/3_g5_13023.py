# ABCDE

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

# 방문기록 check
visited = [False] * n

graph = [[] for _ in range(n)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정답 유무를 판단하는 변수
tmp = 0

def dfs(start, cnt) :
    global tmp
    visited[start] = True
    if cnt == 5 :
        tmp = 1
        return 
    
    for i in graph[start] :
        if visited[i] is False :
            dfs(i, cnt+1)
    visited[start] = False

for i in range(n) :
    dfs(i, 1)
    if tmp == 1 :
        break

if tmp == 1 :
    print(1)
else :
    print(0)