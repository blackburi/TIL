K = int(input())

num = []

def stack(x) :
    if x != 0 :
        num.append(x)
    else :
        num.pop()

for i in range(K) :
    stack(int(input()))

print(sum(num))