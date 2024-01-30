# 최대 최소의 간격

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    num = list(map(int, input().split()))

    num_min = num[0]
    num_max = num[0]
    max_index = []

    for i in range(len(num)) :
        if num_min > num[i] :
            num_min = num[i]
        
        if num_max <= num[i] :
            num_max = num[i]
            max_index.append(i)
            
    a = num.index(num_min)

    index_max = max_index[0]
    for j in range(len(max_index)) :
        if index_max < max_index[j] :
            index_max = max_index[j]

    b = index_max
    
    print(f'#{tc} {abs(a-b)}')