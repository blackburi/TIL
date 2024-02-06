# View

T = 10

for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))
    cnt = 0
    for i in range(2, len(height)-2):
        lst = []
        for j in [-2, -1, 1, 2]:
            if height[i] - height[i+j] > 0:
                lst.append(height[i] - height[i+j])
        if len(lst) == 4:
            lst_min = lst[0]
            for k in lst:
                if lst_min > k:
                    lst_min = k
            cnt += lst_min
    print(f'#{test_case} {cnt}')