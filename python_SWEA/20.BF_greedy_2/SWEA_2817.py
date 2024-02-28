T = int(input())

for tc in range(1, T+1) :
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    # 합이 k가 되는 경우를 센다.
    cnt = 0
    for i in range(1<<n) :
        hap = 0
        for j in range(n) :
            if i & (1<<j) :
                hap += lst[j]
                if hap > k :
                    break
        if hap == k :
            cnt += 1
    
    print(f'#{tc} {cnt}')