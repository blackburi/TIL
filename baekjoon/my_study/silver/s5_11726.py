import sys
input = sys.stdin.readline

m = int(input())
S = set()

for _ in range(m) :
    tmp = input().strip().split()

    if len(tmp) == 1 :
        if tmp[0] == 'all' :
            S = set([i for i in range(1, 21)])
        else : # tmp[0] == 'empty'
            S = set()
    else : # len(tmp) == 2
        func, p = tmp[0], tmp[1]
        p = int(p)
        
        if func == 'add' :
            S.add(p)
        elif func == 'remove' :
            S.discard(p)
        elif func == 'check' :
            if p in S :
                print(1)
            else :
                print(0)
        elif func == 'toggle' :
            if p in S :
                S.discard(p)
            else :
                S.add(p)