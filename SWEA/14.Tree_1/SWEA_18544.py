from collections import deque

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
stack = deque([1])
while stack :
    a = stack.popleft()
    