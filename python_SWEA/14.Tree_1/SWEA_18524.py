T = int(input())
from collections import deque

for tc in range(1, T+1) :
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [[] for _ in range(e+2)]

    for i in range(e) :
        graph[lst[2*i]].append(lst[2*i+1])

    stack = deque([n])
    cnt = 0

    while stack :
        x = stack.popleft()
        cnt += 1
        stack.extend(graph[x])
    
    print(f'#{tc} {cnt}')