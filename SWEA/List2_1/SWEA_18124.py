T = int(input())

for tc in range(1, T+1) :
    arr = list(map(int, input().split()))
    sigma = []
    n = 10  # 원소의 개수
    ans = 0 # 결과값

    sigma = []

    for i in range(1 <<10):  # 1<<n : 부분집합의 개수
        num = 0
        for j in range(10):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i의 j번 비트가 1인경우
                num += arr[j]

            if j == 9 :
                sigma.append(num)

    sigma.pop(0)

    if 0 in sigma :
        ans += 1
    else :
        pass

    print(f'#{tc} {ans}')
