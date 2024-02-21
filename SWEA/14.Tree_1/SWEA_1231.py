for tc in range(1, 11) :
    n = int(input())
    graph = [[] for _ in range(n+1)]
    word = [0] * (n+1)

    for _ in range(n) :
        lst = list(map(str, input().split()))
        
        if len(lst) == 4 :
            graph[int(lst[0])].append(int(lst[2]))
            graph[int(lst[0])].append(int(lst[3]))
            word[int(lst[0])] = lst[1]
        else : # len(lst) == 2 :
            word[int(lst[0])] = lst[1]

    def read(i) :
        if i > n :
            return
        read(2*i)
        ans.append(word[i])
        read(2*i+1)

    ans = []
    read(1)
    print(f'#{tc} {"".join(ans)}')