import sys
input = sys.stdin.readline

n = int(input())
ans = 1

def fac(k) :
    global ans
    if  k == 0 :
        return 1
    elif  k == 1 :
        return ans
    else :
        ans *= k
        fac(k-1)

fac(n)
print(ans)