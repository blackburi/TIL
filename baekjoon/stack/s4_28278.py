import sys
input = sys.stdin.readline

N = int(input())

num = []

def stack(x) :  # x : list
    global num
    if x[0] == 1 :
        num.append(x[1])
    elif x[0] == 2 :
        if len(num) == 0 :
            print(-1)
        else :
            a =num.pop()
            print(a)
    elif x[0] == 3 :
        print(len(num))
    elif x[0] == 4 :
        if len(num) == 0 :
            print(1)
        else :
            print(0)
    elif x[0] == 5 :
        if len(num) == 0 :
            print(-1)
        else :
            print(num[-1])

for _ in range(N) :
    stack(list(map(int, input().split())))