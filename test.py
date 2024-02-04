# lst = [8, 5, 3, 1, 4, 7, 9]
# num = len(lst)

# while num > 0 :
#     for i in range(num-1) :
#         if lst[i] > lst[i+1] :
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#     num -= 1

# print(lst)

lst = [8, 5, 3, 1, 4, 7, 9]

for i in range(len(lst)-1) :
    for j in range(0, i) :
        if lst[j] > lst[j+1] :
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)