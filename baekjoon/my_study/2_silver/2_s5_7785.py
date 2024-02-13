n = int(input())

list_dict = {}

for i in range(n) :
    x, y = list(map(str, input().split()))
    list_dict[x] = y

name = []

for key in list_dict.keys() :
    if list_dict[key] == 'enter' :
        name.append(key)

name.sort(reverse = True)

for j in name :
    print(j)