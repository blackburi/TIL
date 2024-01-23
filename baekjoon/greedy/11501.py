# 주식

""" 처음풀이 -> 시간오버
T = int(input())

for w in range(T) :
    day = int(input())
    stock = list(map(int, input().split()))

    stock_big = list(reversed(sorted(stock)))
    total = 0

    for i in range(day) :
        if stock[0] == stock_big[0] :
            del stock[0]
            stock_big = list(reversed(sorted(stock)))
        else :
            total += stock_big[0] - stock[0]
            del stock[0]
    
    print(total)
"""

T = int(input())
for i in range(T) :
    Day = int(input())
    stock = list(map(int, input().split()))
    stock.reverse()
    Max = stock[0]
    total = 0

    for i in range(1, Day) :
        if Max < stock[i]:
            Max = stock[i]
            continue
        else :
            total += Max - stock[i]

    print(total)