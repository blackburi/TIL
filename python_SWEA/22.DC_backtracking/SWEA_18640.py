def binary(num, lst) :
    global cnt, n

    start, end = 0, n-1

    if lst[start] == num or lst[end] == num :
        cnt += 1
        return
    
    if lst[start] > num or lst[end] < num :
        return

    while start <= end :
        middle = (start + end) // 2

        if lst[middle] > num :
            end = middle - 1
        elif lst[middle] < num :
            start = middle + 1
        else : # lst[middle] == num
            cnt += 1
            break
    return

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    lst_a.sort()

    cnt = 0

    for i in lst_b :
        binary(i, lst_a)

    print(f'#{tc} {cnt}')