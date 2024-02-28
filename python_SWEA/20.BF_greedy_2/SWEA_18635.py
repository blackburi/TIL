T = int(input())

for tc in range(1, T+1) :
    # 컨테이너수, 트럭수
    n, m = map(int, input().split())
    # 화물(컨테이너)의 무게
    n_lst = list(map(int, input().split()))
    # 트럭의 적재용량
    w_lst = list(map(int, input().split()))

    n_lst.sort()
    n_lst.reverse()
    w_lst.sort()
    w_lst.reverse()

    # 총 운반량
    hap = 0

    for i in w_lst :
        for j in n_lst :
            if i >= j :
                hap += j
                n_lst.remove(j)
                break
    print(f'#{tc} {hap}')