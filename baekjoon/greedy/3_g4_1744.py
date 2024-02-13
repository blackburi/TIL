# 수묶기

N = int(input())
num = []

plus = []
minus = []

total = 0

for i in range(N) :
    num = int(input())
    if num > 1 :
        plus.append(num)
    elif num == 1 :
        total += 1
    else :
        minus.append(num)

plus.sort()
plus.reverse()

minus.sort()


if len(plus) == 1 :
    total += plus[0]
else :
    if len(plus) % 2 == 0 :
        for j in range(len(plus)//2) :
            total += plus[0] * plus[1]
            del plus[0], plus[0]
    else :
        total += plus[len(plus)-1]
        for j in range(len(plus)//2) :
            total += plus[0] * plus[1]
            del plus[0], plus[0]


if len(minus) == 1 :
    total += minus[0]
else :
    if len(minus) % 2 == 0 :
        for q in range(len(minus)//2) :
            total += minus[0] * minus[1]
            del minus[0], minus[0]
    else :
        total += minus[len(minus)-1]
        for q in range(len(minus)//2) :
            total += minus[0] * minus[1]
            del minus[0], minus[0]


print(total)