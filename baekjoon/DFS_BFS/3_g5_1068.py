import sys
input = sys.stdin.readline
 
n = int(input())
tree = list(map(int, input().split())) 
m = int(input())
 
def dfs(t):
    tree[t] = -100 # 방문했음 처리
    for i in range(n):
        if t == tree[i]:
            dfs(i) # 똑같이 제거되는 노드의 자식 노드라면 dfs돌림

dfs(m)
# 리프노드를 구하는 변수
cnt = 0
for i in range(n):
    # 리프트리를 구해서 +1
    if tree[i] != -100 and i not in tree:
        cnt += 1
 
print(cnt)