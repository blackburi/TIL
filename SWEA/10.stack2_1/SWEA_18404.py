lst = list(map(int, input().split()))
cnt = 0

# num : 더할 수의 index, total : 수들의 합
graph = [lst[i+1:10] for i in range(9)]

print(graph)