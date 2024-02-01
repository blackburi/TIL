import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 학생수
line = deque(list(map(int, input().split())))
deq = []

for i in range(len(line)) :
    a = line.popleft()
    deq.insert(a, i+1)

deq.reverse()

print(*deq)