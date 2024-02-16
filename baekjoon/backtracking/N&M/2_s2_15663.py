# N & M 9

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()

# index를 뽑아 lst에서 뽑아 쓰기
index = [i for i in range(n)]
idx = []
sub = []

def dfs() :
    if len(set(idx)) == m :
        for i in idx :
            sub.append(lst[i])
        print(*sub)
        return

    for i in idx :
        idx.append(i)
        dfs()
        idx.pop()

dfs()