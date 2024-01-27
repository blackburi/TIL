n, m = list(map(int, input().split()))

g = 1

for i in range(1, min(n, m)+1) :
    if n % i == 0 and m % i == 0 :
        g = i
    else :
        continue

max_num = g
min_num = n * m // g

print(max_num)
print(min_num)
