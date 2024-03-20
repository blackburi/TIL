# 그룹 나누기

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for i in range(m) :
        graph[lst[2*i]].append(lst[2*i+1])
        graph[lst[2*i+1]].append(lst[2*i])

    # 짝이 없는 사람은 False로 표시
    # n+1개를 만들어서 나중에 답 출력시 -1을 해줘야 한다.
    visited = [False] * (n+1)

    # 그룹의 수
    group = 0

    for i in range(n+1) :
        if visited[i] is False :
            visited[i] = True
            group += 1

            q = [i]
            while q :
                k = q.pop()
                for w in graph[k] :
                    if visited[w] is False :
                        visited[w] = True
                        q.append(w)
    
    print(f'#{tc} {group-1}')