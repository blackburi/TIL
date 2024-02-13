N = int(input())

num = []

while N > 10 :
    num.append(str(N%10))
    N//=10

num.append(str(N))

num.sort(reverse=True)

print(*num, sep='')

