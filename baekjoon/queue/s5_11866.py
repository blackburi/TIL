import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque([i for i in range(1, n+1)])

out_list = []

while len(deq) > 0 :
    for i in range(k-1) :
        a = deq.popleft()
        deq.append(a)
    
    b = deq.popleft()
    out_list.append(str(b))

print(f"<{', '.join(out_list)}>")