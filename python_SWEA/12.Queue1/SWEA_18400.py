T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    m = m % n
    
    print(f'#{tc} {lst[m]}')