# 50점 짜리 풀이
import sys
input = sys.stdin.readline

s = list(input())
q = int(input())

for _ in range(q) :
    a, l, r = list(map(str, input().split()))
    l = int(l)
    r = int(r)
    cnt = 0
    for i in range(l, r+1) :
        if a == s[i] :
            cnt += 1
    print(cnt)

# 100점 - pypy로 바꿀시
import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
lst = [[0 for _ in range(26)] for _ in range(len(s))]
lst[0][ord(s[0]) - 97] = 1

# 0부터가 아닌 1부터 하는 이유는 i~j번째 까지 중 i == 0인 경우 예외처리를 해줘야 한다.
for i in range(1, len(s)) :
    lst[i][ord(s[i]) - 97] = 1
    for j in range(26):
        lst[i][j] += lst[i-1][j]

for i in range(n) :
    alpha, b, c = list(map(str, input().split()))
    if int(b) > 0:
        res = lst[int(c)][ord(alpha) - 97] - lst[int(b)-1][ord(alpha) - 97]
    else:
        res = lst[int(c)][ord(alpha) - 97]
    
    print(res)

# 100점 - python
import sys
input = sys.stdin.readline

s = input().rstrip()
count = {0 : [0] * 26}

q = int(input().rstrip())
for i, ch in enumerate(s):
    count[i + 1] = count[len(count) - 1][:]
    count[i + 1][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = input().rstrip().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)