import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

# 0 == queue, 1 == stack
sep = deque(list(map(int, input().split())))

# data
queuestack = deque(list(map(int, input().split())))

# 삽입할 수열의 길이
M = int(input())

# 삽입할 수열
C = list(map(int, input().split()))


# sep에서 1이라면 삽입된 data가 그대로 나온다.
# 즉 stack은 영향을 주지 않아 삭제한다
for i in range(N) :
    a = sep.popleft()
    b = queuestack.popleft()
    if a == 0 :
        queuestack.append(b)

ans = []
# C의 원소가 들어가면 queuestack의 마지막 원소가 출력된다.
for i in C :
    queuestack.appendleft(i)
    k = queuestack.pop()
    ans.append(k)

print(*ans)