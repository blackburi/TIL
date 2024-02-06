# 이진 탐색

T = int(input())

for tc in range(1, T+1) :
    p, a, b = list(map(int, input().split()))

    def half(l, h, j, n) : # h는 높은 쪽수, l은 낮은 쪽수, j는 찾아야 하는 쪽수, n은 횟수
        tmp = (h+l) // 2
        if tmp != h and tmp != l and j > tmp :
            return half(tmp, h, j, n+1)
        elif tmp != h and tmp != l and j < tmp :
            return half(l, tmp, j, n+1)
        else : # tmp = j
            return n+1
    
    anum = half(1, p, a, 0)
    bnum = half(1, p, b, 0)

    if anum > bnum :
        print(f'#{tc} B')
    elif anum < bnum :
        print(f'#{tc} A')
    else :
        print(f'#{tc} 0')