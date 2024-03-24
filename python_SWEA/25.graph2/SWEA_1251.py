# 하나로

def find_set(x) :
    if parents[x] == x :
        return
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y) :
    x = find_set(x)
    y = find_set(y)

    if x == y :
        return
    if x < y :
        parents[y] = x
    else :
        parents[x] = y


T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    rate = float(input())

    position = list(zip(x_lst, y_lst))

    costs = []
    for i in range(n-1) :
        for j in range(i+1, n) :
            start = position[i]
            end = position[j]
            cost = (start[0] - end[0])**2 + (start[1] - end[1])**2
            costs.append((i, j, cost))
    costs.sort(key = lambda x : x[2])
    parents = [i for i in range(n)]

    cnt = 1
    total = 0

    for a, b, cost in costs :
        if find_set(a) == find_set(b) :
            continue
        cnt += 1
        union(a, b)
        total += cost

        if cnt == n :
            break
    print(total)
    print(f'#{tc} {round(total*rate)}')