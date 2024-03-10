# 염기서열 커버

import sys
input = sys.stdin.readline
from collections import deque
import copy

# 개수, 길이
n, m = map(int, input().split())

# 염기서열을 담는 list
sequence = []
for _ in range(n) :
    sequence.append(list(input().rstrip()))

# 염기서열을 합친 후에 넣어둘 list
after = [[] for _ in range(2**n)]

# 2의 거듭제곱 index에 염기서열을 넣어둔다
for i in range(n) :
    after[2**i] = copy.deepcopy(sequence[i])

# 염기서열 2개를 합칠수 있다면 합친 것을, 아니라면 빈 list를 return
def combine(dna1, dna2) :
    dna = []
    if dna1 == [] or dna2 == [] :
        return dna
    
    for i in range(m) :
        if dna1[i] == '.' :
            dna.append(dna2[i])
        elif dna2[i] == '.' :
            dna.append(dna1[i])
        elif dna1[i] == dna2[i] :
            dna.append(dna1[i])
        else :
            dna = []
            return dna
    return dna

# 하나의 정수는 2의 거듭제곱의 합으로 표현하는 방법이 유일하다
# 3 = 1 + 2로 유일하고 index = 3 인 곳에는
# index=1, index=2 인 염기서열을 combine한 것을 넣어둔다.
# 마찬가지로 7 = 1 + 2 + 4
for i in range(1<<n) :
    if i == 0 :
        continue
    if after[i] == [] :
        lst = deque([])
        for j in range(n) :
            if i & (1<<j) :
                lst.append(sequence[j])

        while len(lst) > 1 :
            dna1 = lst.popleft()
            dna2 = lst.popleft()
            lst.append(combine(dna1, dna2))
    
        after[i] = lst[-1]

# 최소 염기서열 개수
cnt = n

# after에서 빈list가 아닌경우의 index를 담는다
idx = []
for i in range(2**n) :
    if after[i] != [] :
        idx.append(i)

for i in range(1<<len(idx)) :
    hap = 0
    tmp = 0
    for j in range(len(idx)) :
        if i & (1<<j) :
            hap += idx[j]
            tmp += 1
            if hap > 2**n-1 :
                break
    if hap == 2**n-1 :
        cnt = min(cnt, tmp)

print(cnt)