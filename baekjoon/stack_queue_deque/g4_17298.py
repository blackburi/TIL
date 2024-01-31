import sys
from collections import deque
input = sys.stdin.readline

A = int(input())
sub = list(map(int, input().split()))
sub.reverse()
deq = deque(sub)

stack = [] # put max numbers
ans = [] # answer list

deq.reverse
print(deq)

# if len(deq) == 1 :
#     print(-1)
# else :
#     while len(deq) > 0 or len(stack) > 0 :
#         if deq[0] < deq[1] :
#             deq.pop()
#             ans.append(deq[1])
#         else : # deq[0] > deq[1]
#             if len(stack) == 0 :
#                 k = deq.popleft()
#                 stack.append(k)
#             else : # len(deq) > 0
