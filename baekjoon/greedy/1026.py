# 보물



"""시간 초과
N = int(input())

discuss = []

for _ in range(N) :
    a, b = list(map(int, input().split()))
    if len(discuss) < b+1 :
        for _ in range(b+1-len(discuss)) :
            discuss.append(0)
    else :
        pass
    
    for i in range(b+1) :
        if a < i < b :
            discuss[i] += 1

print(max(discuss))
"""