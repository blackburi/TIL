import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq_num = deque(list(map(int, input().split())))
deq_index = deque([i for i in range(1, N+1)])

bomb_list = []

a = deq_num.popleft()
b = deq_index.popleft()
bomb_list.append(b)

while len(deq_index) > 0 :
    if a > 0 :
        for _ in range(a-1) :
            n = deq_num.popleft()
            deq_num.append(n)

            i = deq_index.popleft()
            deq_index.append(i)
        
        a = deq_num.popleft()
        b = deq_index.popleft()
        bomb_list.append(b)
    else : # a < 0
        for _ in range(abs(a)-1) :
            n = deq_num.pop()
            deq_num.appendleft(n)

            i = deq_index.pop()
            deq_index.appendleft(i)
        
        a = deq_num.pop()
        b = deq_index.pop()
        bomb_list.append(b)

print(*bomb_list)