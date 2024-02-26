import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
m = int(input())

# 루트 노드 찾기
for i in range(n) :
    if lst[i] == -1 :
        root = i

# 부모노드 index의 list에 자식 노드를 append
graph = [[] for _ in range(n)]

for i in range(n) :
    graph[lst[i]].append(i)

visited = [False] * n
visited[root] = True
cnt = 0

def dfs(x) :
    global cnt, m
    if graph[x] == [] :
        cnt += 1
        return
    elif x == m :
        return
    else : # graph[x] != [] and x != m
        for w in graph[x] :
            if visited[w] is False :
                visited[w] = True
                dfs(w)

dfs(root)
print(cnt)