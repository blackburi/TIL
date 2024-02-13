import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n) :
    l, h = map(int, input().split())
    lst.append([l, h])

lst.sort(key = lambda x : x[0])

l_list = []
h_list = []

for i in lst :
    l_list.append(i[0])
    h_list.append(i[1])

a = max(h_list)
b = h_list.index(a)

area = 0
height = h_list[0]

for i in range(b) :
    if height < h_list[i+1] :
        area += (l_list[i+1] - l_list[i]) * height
        height = h_list[i+1]
    else :
        area += (l_list[i+1] - l_list[i]) * height

height = h_list[-1]
for j in range(n-b-1) :
    if height < h_list[-2-j] :
        area += (l_list[-1-j] - l_list[-2-j]) * height
        height = h_list[-2-j]
    else :
        area += (l_list[-1-j] - l_list[-2-j]) * height

print(area + a)