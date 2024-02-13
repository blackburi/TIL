# 이해를 위한 주석
# 5, 5 4 3 2 1 이 입력되면
# 1, 2, 3, 4, 5를 stack을 이용하여 5 4 3 2 1 을 만들수 있는지
# 만들수 있다면 어떤 순서로 만들어야 하는지
# 만들수 없다면 NO 출력

# idea
# 거꾸로 만들고 (5 4 3 2 1 -> 1 2 3 4 5)
# 나오는 +, - 수열을 reverse 후 +/-를 바꿔주면 된다.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input()) # N부터 나와야 한다.

end = [int(input()) for _ in range(N)]

stack = [] # stack 구조

pm = deque([])

while N > 0 :
    if len(end) != 0 and len(stack) != 0:
        if end[-1] == N :
            end.pop()
            pm.append('+')
            pm.append('-')
            N -= 1
        elif stack[-1] == N :
            stack.pop()
            pm.append('-')
            N -= 1
        else :
            a = end.pop()
            stack.append(a)
            pm.append('+')
    elif len(end) != 0 and len(stack) == 0:
        if end[-1] == N :
            end.pop()
            pm.append('+')
            pm.append('-')
            N -= 1
        else :
            a = end.pop()
            stack.append(a)
            pm.append('+')
    elif len(end) == 0 and len(stack) != 0:
        if stack[-1] == N :
            stack.pop()
            pm.append('-')
            N -= 1
        else :
            print('NO')
            break

if N == 0 :
    pm.reverse()

    for _ in range(len(pm)) :
        a = pm.popleft()
        if a == '+' :
            pm.append('-')
        else :
            pm.append('+')
        
    for j in pm :
        print(j)