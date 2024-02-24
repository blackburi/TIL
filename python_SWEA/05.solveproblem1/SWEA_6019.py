T = int(input())


for tc in range(1, T+1) :
    D, A, B, F = list(map(int, input().split()))

    length = (D / (A+B) ) * F

    print(f'#{tc} {length}')