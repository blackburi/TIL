T = int(input())

for tc in range(1, T+1) :
    r = int(input())
    hap = r
    for i in range(1, r) :
        hap += int((r**2-i**2)**0.5)
    ans = 4*hap + 1
    print(f'#{tc} {ans}')