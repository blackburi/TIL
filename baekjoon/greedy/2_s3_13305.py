# 주유소

T = int(input())


road = list(map(int, input().split())) # 도로의 길이
city = list(map(int, input().split())) # 기름 가격
min_city = city[0]
fee = 0

fee += min_city * road[0]

for i in range(T-2) :
    if min_city <= city[i+1] :
        fee += min_city * road[i+1]
    else :
        min_city = city[i+1]
        fee += min_city * road[i+1]

print(fee)