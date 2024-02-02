T = int(input())

for tc in range(1, T+1) :

    n, q = map(int, input().split())
    boxes = [0] * n

    for i in range(1, q+1) :
        l, r = map(int, input().split())
        for k in range(l-1, r) :
            boxes[k] = i
    
    print(f'#{tc}', *boxes)
