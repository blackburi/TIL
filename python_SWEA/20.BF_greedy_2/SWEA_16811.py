T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    # 같은 무게의 당근이 많아 조건을 만족할수 없는경우를 check하는 변수
    check = 0

    for i in range(1, max(lst)+1) :
        if lst.count(i) > n//2 :
            check = 1
            break
        if len(set(lst)) <= 2 :
            check = 1
            break

    # 박스에 들어가는 당근의 개수조건을 만족하지 않으면 이후 동작X
    if check == 1 :
        print(f'#{tc} -1')
        continue

    p = n//3
    q = n % 3

    if q == 0 :
        s = lst[:p]
        m = lst[p:2*p]
        l = lst[2*p:]
    elif  q == 1 :
        s = lst[:p+1]
        m = lst[p+1:2*p+1]
        l = lst[2*p+1:]
    elif q == 2 :
        s = lst[:p+1]
        m = lst[p+1:2*p+2]
        l = lst[2*p+2:]

    if s[-1] == m[0] :
        