from collections import deque

T = int(input())

for tc in range(1, T+1) :
    n, m = map(int, input().split())
    lst = deque(list(map(int, input().split())))

    m = m % n
    for _ in range(m) :
        lst.popleft()
    
    print(f'#{tc} {lst[0]}')