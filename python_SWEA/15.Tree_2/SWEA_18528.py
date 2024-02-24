T = int(input())

for tc in range(1, T+1) :
    # 노드의 개수, 리프노드의 개수, 출력할 노드 번호
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for i in range(m) :
        a, b = map(int, input().split())
        tree[a] = b
    
    for i in range(n, 0, -1) :
        if tree[i] == 0 :
            if n >= 2*i + 1 :
                tree[i] = tree[2*i] + tree[2*i + 1]
            else : # n < 2*i + 1
                tree[i] = tree[2*i]
        
        if i == l :
            break
    
    print(f'#{tc} {tree[l]}')