import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

def den(x, y) :
    x %= y
    while x > 0 :
        if x < y :
            x, y = y, x
            x %= y
    return y

g = den(a*d + b*c, b*d)

print((a*d + b*c)//g, (b*d)//g)