# 두 수의 합

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n, k = map(int, input().split())
    numbers = list(map(int, input().rstrip().split()))
    numbers.sort()

    # 두 수의 합
    m = 200000000

    ans = 0

    for i in range(n) :
        # number[i]와 더하는 수를 찾아야 함 -> i+1부터 시작
        start = i+1
        end = n-1

        if m == k :
            if numbers[i] <= k//2 and ((k-numbers[i]) in numbers) :
                ans += 1

        if numbers[i] > m//2 :
            break

        while start <= end :
            mid = (start+end)//2
            # 모든 경우 check -> start가 아닌 i를 넣어줘야 한다.
            hap = numbers[i] + numbers[mid]


            if abs(k-hap) < m :
                ans = 1
                m = abs(k-hap)
            elif abs(k-hap) == m :
                ans += 1

            if hap > k :
                end = mid - 1
            elif hap < k :
                start = mid + 1
            else : # hap == k
                break

    print(ans)