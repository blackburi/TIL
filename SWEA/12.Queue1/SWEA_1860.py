from collections import deque

for tc in range(1, 11) :
    # n명의 사람 m초동안 k개 붕어빵
    n, m, k = map(int, input().split())
    lst = deque(list(map(int, input().split())))

    minus = [1, 2, 3, 4, 5]
    b = 0
    
    while True :
        a = lst.popleft()
        a -= minus[b%5]

        if a <= 0 :
            lst.append(0)
            break

        lst.append(a)
        b += 1
    
    print(f'#{tc} {"".join(lst)}')