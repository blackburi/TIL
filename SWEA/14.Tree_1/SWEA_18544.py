v = int(input())
c1 = [0] * (v+1)
c2 = [0] * (v+1)

lst = list(map(int, input().split()))
for i in range(v-1) :
    if c1[lst[2*i]] == 0 :
        c1[lst[2*i]] = lst[2*i+1]
    else :
        c2[lst[2*i]] = lst[2*i+1]

ans = []
visited = [False] * (v+1)

def dfs(x) :
    ans.append(x)
    visited[x] = True
    if c1[x] != 0 :
        dfs(c1[x])
    if c2[x] != 0 :
        dfs(c2[x])

dfs(1)
print(*ans)