# 전위 순회

v = int(input())
lst = list(map(int, input().rstrip().split()))

graph = [[] for _ in range(v+1)]
for i in range(v-1) :
    graph[lst[2*i]].append(lst[2*i+1])
    graph[lst[2*i]].sort(reverse = True)

ans = []
stack = [1]
visited = [False] * (v+1)
visited[1] = True

while stack :
    k = stack.pop()
    ans.append(k)
    for w in graph[k] :
        if visited[w] is False :
            visited[w] = True
            stack.append(w)

print(*ans)