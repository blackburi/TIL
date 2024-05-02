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

    # 정답(출력값)
    ans = 0

    start = 0
    end = n-1

    while start < end :
        hap = numbers[start] + numbers[end]

        # 차이가 더 작다면
        if m > abs(k-hap) :
            m = abs(k-hap)
            ans = 0

        # 합이 k보다 작음 -> 합을 k에 맞출수 있는지 start += 1을 통해 hap을 크게 만든다.
        if hap < k :
            if abs(k-hap) == m :
                ans += 1
            start += 1
        # 합이 k보다 큼 -> 합을 k에 맞출수 있는지 end -= 1을 통해 hap을 작게 만든다.
        elif hap > k :
            if abs(k-hap) == m :
                ans += 1
            end -= 1
        # 동일하다면 ans+1 동시에 start값을 1개 올려 다시 세어준다.
        else : # hap == k
            ans += 1
            start += 1

    print(ans)