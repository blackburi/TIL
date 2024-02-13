T = int(input())
for _ in range(T) :
    lst = list(input())

    cnt = 0
    for i in range(len(lst)//2) :
        if lst[i] == lst[len(lst)-1-i] :
            cnt += 1
        else :
            break

    if cnt == len(lst)//2 :
        print(1, cnt+1)
    else :
        print(0, cnt+1)