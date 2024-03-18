def binary() :



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