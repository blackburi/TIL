T = int(input())

for tc in range(1, T+1) :
    v, e, a, b = map(int, input().split())
    lst = list(map(int, input().split()))

    graph1 = [0] * (v+1)
    graph2 = [[] for _ in range(v+1)]

    # graph1에서 부모index에 자식node를 넣는 것이 아닌
    # 자식 index에 부모 node를 넣는다.
    for i in range(e) :
        graph1[lst[2*i+1]] = (lst[2*i])
        graph2[lst[2*i]].append(lst[2*i+1])
    
    # 공통조상 찾기
    parent1 = [a]
    parent2 = [b]

    while True :
        x = parent1[-1]
        parent1.append(graph1[x])
        
        if x == 1 :
            break
    
    while True :
        y = parent2[-1]
        parent2.append(graph1[y])
        
        if y == 1 :
            break
    
    for ans in parent1 :
        if ans in parent2 :
            break

    # 서브 트리의 크기
    stack = [ans]
    cnt = 1
    while stack :
        x = stack.pop()
        cnt += len(graph2[x])
        stack.extend(graph2[x])

    print(f'#{tc} {ans} {cnt}')