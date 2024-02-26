from collections import deque

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    cards = list(map(str, input().split()))

    first = deque(cards[:(n+1)//2])
    second = deque(cards[(n+1)//2:])
    
    ans = []
    for _ in range(n//2) :
        x = first.popleft()
        ans.append(x)
        y = second.popleft()
        ans.append(y)
    
    if first :
        x = first.pop()
        ans.append(x)
    
    print(f'#{tc} {" ".join(ans)}')