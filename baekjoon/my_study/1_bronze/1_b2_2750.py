N = int(input())

num_list = []
for _ in range(N) :
    num_list.append(int(input()))

num_list.sort()

for j in num_list :
    print(j)