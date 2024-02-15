from collections import deque

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst = deque(list(map(int, input().split())))

    while m :
        x = lst.popleft()
        lst.append(x)
        m -= 1
    
    print(f'#{tc} {lst[0]}')