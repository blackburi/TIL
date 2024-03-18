# 장훈이의 높은 선반

def back(x) :
    global gap, hap, b, n

    if x == n :
        if hap >= b :
            gap = min(gap, hap-b)
            print(hap)
        return

    if hap >= b :
        gap = min(gap, hap-b)
        print(hap)
        return

    for i in range(x, n) :
        hap += heights[i]
        back(x+1)
        hap -= heights[i]


T = int(input())

for tc in range(1, T+1) :
    # n 점원의 수, b 최소 높이
    n, b = map(int, input().split())

    heights = list(map(int, input().split()))

    # 높이의 차(결과값)
    gap = sum(heights)

    for _ in range(n) :
        # 점원 키의합
        hap = 0
        back(0)
    
    print(gap)