# N & M 2

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lst = [i for i in range(1, n+1)]
ans = []
for i in range(1 << n) :
    sub = []
    for j in range(n) :
        if i & (1 << j) :
            sub.append(lst[j])
            if len(sub) > m :
                break
    if len(sub) == m :
        ans.append(sub)

ans.sort()

for k in range(len(ans)) :
    print(*ans[k])