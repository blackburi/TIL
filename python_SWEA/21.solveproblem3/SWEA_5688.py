# 세제곱근을 찾아라

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    p = int(n**(1/3))

    if p**3==n :
        print(f'#{tc} {p}')
    elif (p+1)**3 == n :
        print(f'#{tc} {p+1}')
    else :
        print(f'#{tc} -1')