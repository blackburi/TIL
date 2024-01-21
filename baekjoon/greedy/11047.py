# 동전

n, m  = list(map(int, input().split()))

value = []
coin = 0

for _ in range(n) :
    value.append(int(input()))

value.reverse()

for i in range(n) :
    coin += m//value[i]
    m %= value[i]

print(coin)

""" 처음풀이 : 시간초과
n, m  = list(map(int, input().split()))

value = []
coin = 0

for _ in range(n) :
    value.append(int(input()))

value.reverse()

while m > 0 :
    for i in range(n-1) :
        if m >= value[i] :
            k = m//value[i]
            m -= k * value[i]
            coin += k
        elif m >= value [i] :
            k = m//value[i+1]
            m -= k * value[i+1]
            coin += k
        else :
            continue

print(coin)
"""