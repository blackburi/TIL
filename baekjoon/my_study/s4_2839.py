N = int(input())

n = 1
while x + y != n :
    x = (5 * n - N) // 2
    y = (N - 3 * n) // 2
    n += 1

if x >= 0 and y >= 0 and n >= 1 :
    print(n)
else :
    pass