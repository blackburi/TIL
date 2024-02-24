T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = [0] + list(map(int, input().split()))

    tree = [0] * (n+1)

    for i in range(1, n+1) :
        tree[i] = lst[i]

        while i :
            if tree[i] < tree[i//2] :
                tree[i], tree[i//2] = tree[i//2], tree[i]
            i //= 2

    ans = 0
    while n :
        n //= 2
        ans += tree[n]
    
    print(f'#{tc} {ans}')