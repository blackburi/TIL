T = int(input())

for tc in range(1, T+1) :
    n = int(input())

    line = []
    for _ in range(n) :
        a, b = map(int, input().split())
        line.append([a, b])

    line.sort(key = lambda x : x[0])
    
    cnt = 0

    for i in range(n) :
        for j in range(i+1, n) :
            if line[i][1] > line[j][1] :
                cnt += 1

    print(f'#{tc} {cnt}')