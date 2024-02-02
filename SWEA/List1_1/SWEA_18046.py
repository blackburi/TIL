# min max

T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    num = list(map(int, input().split()))

    num_max = num[0]
    num_min = num[0]

    for i in range(N) :
        if num_max < num[i] :
            num_max = num[i]
        elif num_min > num[i] :
            num_min = num[i]

    print(f'#{test_case} {num_max - num_min}')