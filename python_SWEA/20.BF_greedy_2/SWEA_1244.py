T = int(input())

for tc in range(1, T+1) :
    # b는 교환 횟수
    a, b = map(int, input().split())
    
    # lst는 a를 한자리씩 끊어놓은 list
    lst = list(str(a))
    for i in range(len(lst)) :
        lst[i] = int(lst[i])

    max_lst = sorted(lst)
    max_lst.reverse()

    while b :
        if lst == max_lst :
            break

        for i in range(len(lst)) :
            if lst[i] != max_lst[i] :
                a = lst[-1:i:-1].index(max_lst[i])
                lst[i], lst[i+len(lst[i+1:])-a] = lst[i+len(lst[i+1:])-a], lst[i]
                b -= 1

                if b == 0 :
                    break
