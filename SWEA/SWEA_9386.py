# 연속한 1의 개수

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    num = list(map(int, input()))
    num.append(0)

    lst = []
    one = 0

    for i in num :
        if i == 1 :
            one += 1
        else :
            lst.append(one)
            one = 0
    
    lst_max = lst[0]
    for j in range(len(lst)) :
        if lst_max < lst[j] :
            lst_max = lst[j]
    
    print(f'#{tc} {lst_max}')