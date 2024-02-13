N, M = list(map(int, input().split()))

num_list = list(map(int, input().split()))

sum = 0

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            if num_list[i] + num_list[j] + num_list[k] > M :
                continue
            else :
                sum = max(sum, num_list[i] + num_list[j] + num_list[k])

print(sum)