# N & M 1

n, m = list(map(int, input().split()))

num = []

def back(x, y) : # x=n, y=m
    if len(num) == y :
        print(' '.join(map(str, num)))
    else :
        for i in range(1, x+1) :
            if i not in num :
                num.append(i)
                back(x, y)
                num.pop()
            else :
                continue

back(n, m)