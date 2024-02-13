n, m = map(int, input().split())
lst = {}

for _ in range(n) :
    word = input()

    if len(word) < m :
        continue
    else :
        if word in lst :
            lst[word] += 1
        else :
            lst[word] = 1

lst = sorted(lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for k in lst :
    print(k[0])