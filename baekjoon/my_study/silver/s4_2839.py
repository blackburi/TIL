N = int(input())


a = N // 5
N -= a * 5
k = N % 3

while k != 0 :
    if N != 0 :
        a -= 1
        N += 5
        k = N % 3
    else :
        break

l = N // 3

if a >= 0 and l >= 0 :
    print(a+l)
else :
    print(-1)