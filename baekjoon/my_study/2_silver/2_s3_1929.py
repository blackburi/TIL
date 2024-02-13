import sys
from math import sqrt
input = sys.stdin.readline

M, N = map(int, input().split())

def prime(x) :
    if x == 1 :
        return False
    elif x == 2 or x == 3 :
        return True
    else :
        for i in range(2, int(sqrt(x)+1)) :
            if x % i == 0 :
                return False
            else :
                pass
        return True
    
prime_list = []
for j in range(M, N+1) :
    if prime(j) is True :
        prime_list.append(j)
    else :
        pass

for k in prime_list :
    print(k)