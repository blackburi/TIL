import sys
from math import sqrt
input = sys.stdin.readline

def prime(x) :
    if x == 0 or x == 1 :
        return False
    for i in range(2, int(sqrt(x)+1)) :
        if x % i == 0 :
            return False
    return True

T = int(input())
for i in range(T) :
    z = int(input())
    while True :
        if prime(z) :
            print(z)
            break
        else :
            z += 1