# 치킨 배달

import sys
input = sys.stdin.readline

# 0은 빈칸, 1은 집, 2는 치킨집

n, m = map(int, input().split())
answer = sys.maxsize

home = []
chickens = []

for i in range(n) :
    sub = list(map(int, input().rstrip().split()))

    for j in range(n) :
        if sub[j] == 1 :
            home.append((i, j))
        elif sub[j] == 2 :
            chickens.append((i, j))

visited = [False] * len(chickens)


# chikens index, 방문한 치킨집 최대 갯수
def dfs(idx, cnt) :
    global answer

    if cnt == m :
        ans = 0
        for i in home :
            distance = sys.maxsize
            for j in range(len(chickens)) :
                if visited[j] :
                    check = abs(i[0] - chickens[j][0]) + abs(i[1] - chickens[j][1])
                    distance = min(distance, check)
            ans += distance
        answer = min(answer, ans)
        return
    
    for i in range(idx, len(chickens)) :
        if not visited[i] :
            visited[i] = True
            dfs(i+1, cnt+1)
            visited[i] = False

dfs(0, 0)
print(answer)