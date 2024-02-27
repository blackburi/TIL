def check(lst) :
    n = len(lst)
    # run, triple
    cnt = [1, 1]
    for i in range(n-1) :
        if lst[i] == lst[i+1] :
            cnt[1] += 1
        elif lst[i] == lst[i+1] - 1 :
            cnt[0] += 1
        else :
            cnt[0] = 1
            cnt[1] = 1
        
        if cnt[1] >= 3 or cnt[0] >= 3 :
            return 1
    return 0


T = int(input())

for tc in range(1, T+1) :
    tmp = 0
    lst = list(map(int, input().split()))

    player1 = []
    player2 = []

    for i in range(12) :
        a = b = 0
        if i % 2 == 0 :
            player1.append(lst[i])
            player1.sort()
            a = check(player1)
        else :
            player2.append(lst[i])
            player2.sort()
            b = check(player2)

        if a > b :
            tmp = 1
            break
        elif a < b :
            tmp = 2
            break

    print(f'#{tc} {tmp}')