def gaesan(a, b, c) :
    try :
        if cal[a] in ['+', '-', '*', '/'] and cal[c] in ['+', '-', '*', '/'] :
            d, e = graph[a]
            f, g = graph[c]
            return gaesan(gaesan(d, a, e), b, gaesan(f, c, g))
        elif cal[a] in ['+', '-', '*', '/'] :
            d, e = graph[a]
            return gaesan(gaesan(d, a, e), b, c)
        elif cal[c] in ['+', '-', '*', '/'] :
            f, g = graph[c]
            return gaesan(a, b, gaesan(f, c, g))
        else :
            if cal[b] == '+' :
                cal[b] = cal[a]+cal[c]
                return b
            elif cal[b] == '-' :
                cal[b] = cal[a]-cal[c]
                return b
            elif cal[b] == '*' :
                cal[b] = cal[a]*cal[c]
                return b
            elif cal[b] == '/' :
                cal[b] = cal[a]/cal[c]
                return b
    except IndexError :
        print(a, b, c)
        
for tc in range(1, 11) :
    n = int(input())

    # 노드의 연결관계를 보여주는 graph
    graph = [[] for _ in range(n+1)]
    # 노드에 들어가있는 문자 or 숫자를 보여주는 list
    cal = [0] * (n+1)

    for _ in range(n) :
        lst = list(map(str, input().split()))
        if len(lst) == 4 :
            graph[int(lst[0])].append(int(lst[2]))
            graph[int(lst[0])].append(int(lst[3]))
            cal[int(lst[0])] = lst[1]
        else : # len(lst) == 2
            cal[int(lst[0])] = int(lst[1])
    
    a, b = graph[1]
    print(f'#{tc} {int(cal[gaesan(a, 1, b)])}')