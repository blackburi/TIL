T = int(input())

def isprime(x) :
    for i in range(3, int(x**0.5+2)) :
        if x == 1 :
            return False
        else :
            if x % i == 0 :
                return False
            return True

for t in range(T) :
    n = int(input())
    cnt = 0
    for j in range(3, int(n**0.5+2)) :
        if isprime(j) is True :
            if isprime(n-j) is True :
                cnt += 1
    print(cnt)