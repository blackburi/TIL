import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    m, n, k = list(map(int, input().split()))

    cabbage = []
    for _ in range(k) :
        a, b = map(int, input().split())
        cabbage.append([a, b])

    cabbage.sort(key = lambda x : (x[0], x[1]))
    
    need = 0
    dum = [] # 붙어있는 배추의 모음
    while cabbage :
        if dum == [] :
            x, y = cabbage.pop(0)
            need += 1
            dum.append([x, y])
        else : # dum != []
            dum.append([x, y])
            for i in dum :
                if [i[0], i[1]+1] in cabbage:
                    dum.append([i[0], i[1]+1])
                    idx = cabbage.index([i[0], i[1]+1])
                    del cabbage[idx]
                elif [i[0]+1, i[1]] in cabbage:
                    dum.append([i[0]+1, i[1]])
                    idx = cabbage.index([i[0]+1, i[1]])
                    del cabbage[idx]
                else :
                    if i == dum[-1] :
                        dum = []
    print(need)