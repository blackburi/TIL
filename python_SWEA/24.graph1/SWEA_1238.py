# contact

from collections import deque

for tc in range(1, 11) :
    length, start = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]

    for i in range(length//2) :
        graph[lst[2*i]].append(lst[2*i+1])

    dp = [-1] * 101
    dp[start] = 0

    q = deque([start])

    while q :
        k = q.popleft()
        for w in graph[k] :
            # 방문한 곳이 아니라면
            if dp[w] == -1 :
                dp[w] = dp[k]+1
                q.append(w)
    
    ans_list = []
    M = max(dp)

    for i in range(101) :
        if dp[i] == M :
            ans_list.append(i)
    
    print(f'#{tc} {max(ans_list)}')

