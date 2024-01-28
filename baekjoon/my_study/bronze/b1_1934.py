T = int(input())

for _ in range(T) :
    a, b = list(map(int, input().split()))
    share = []
    for i in range(1, min(a, b)+1) :
        if a % i == 0 and b % i == 0 :
            share.append(i)
    G = max(share)
    print(a * b // G)