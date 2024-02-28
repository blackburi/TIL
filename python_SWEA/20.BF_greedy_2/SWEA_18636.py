T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = []
    for _ in range(n) :
        a, b = map(int, input().split())
        lst.append([a, b])

    lst.sort(key = lambda x : (x[1], x[0]))

    cnt = 0
    x = lst[0]
    while True :
        cnt += 1
        for i in lst :
            if x[1] <= i[0] :
                x = i
                break
        else :
            break
    print(f'#{tc} {cnt}')