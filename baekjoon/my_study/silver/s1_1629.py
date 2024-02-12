import sys
input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())

def cal(p, q) :
    global a, c
    if q == 1 :
        return p % c
    else :
        tmp = cal(p, q//2)
        if q % 2 == 0 :
            return (tmp*tmp) % c
        else :
            return (tmp*tmp*a) % c

print(cal(a, b))