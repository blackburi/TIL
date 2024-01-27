n, m = list(map(int, input().split()))

S = {input() : 1 for _ in range(n)}

T = [input() for _ in range(m)]

sum = 0

for i in range(m) :
    try :
        sum += S[T[i]]
    except :
        continue

print(sum)