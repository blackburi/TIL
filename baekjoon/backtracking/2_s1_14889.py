# 스타트와 링크

import sys
input = sys.stdin.readline

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

flat = 100*n

sub = []
def dfs(x) :
    global flat, hap

    if len(sub) == n//2 :
        # 스타트 팀의 능력치
        stmp = 0
        for p in range(len(sub)) :
            for q in range(p+1, len(sub)) :
                stmp += stat[sub[p]][sub[q]] + stat[sub[q]][sub[p]]
        # 링크 팀의 능력치
        ltmp = 0
        lst = []
        for k in range(n) :
            if k not in sub :
                lst.append(k)
        for p in range(len(lst)) :
            for q in range(p+1, len(lst)) :
                ltmp += stat[lst[p]][lst[q]] + stat[lst[q]][lst[p]]
        
        if flat > abs(stmp - ltmp) :
            flat = abs(stmp - ltmp)
        return

    for i in range(x, n) :
        if len(sub) == 0 and i >= n//2 :
            break
        sub.append(i)
        dfs(i+1)
        sub.pop()

dfs(0)
print(flat)