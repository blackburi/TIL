T = int(input())

for tc in range(1, T+1) :
    d, a, b, f = map(int, input().split())
    print(f'#{tc} {d*f/(a+b)}')