import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

move_cnt = [-1] * (10**5+1)
move_cnt[n] = 0

def bfs(n, k) :
    global move_cnt
    queue = deque([n])
    
    while queue :
        a = queue.popleft()

        if a == k :
            print(move_cnt[a])
            break

        for b in (a-1, a+1, 2*a) :
            if 0 <= b <= 10**5 and move_cnt[b] == -1 :
                move_cnt[b] = move_cnt[a] + 1
                queue.append(b)

bfs(n, k)