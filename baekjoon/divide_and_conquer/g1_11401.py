# 페르마의 소정리를 이용한 조합공식의 곱셈 형태 변형
# 페르마의 소정리
# p가 소수이면 모든 정수 a에 대해 a**p = a (mod p)
# p가 소수이고 a가 p의 배수가 아니면 a**(p-1) = 1 (mod p)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
c = 1000000007

# 팩토리얼 계산( % c 까지 계산)
def fac(a) :
    re = 1
    for i in range(2, a+1) :
        re = (re*i) % c
    return re

# 거듭제곱 계산( % c 까지 계산)
def square(n, k) :
    if k == 0 :
        return 1 
    elif k == 1 :
        return n
    
    tmp = square(n, k//2)
    if k % 2 :
        return tmp * tmp * n % c
    else :
        return tmp * tmp % c
    
tn = fac(n)
bn = fac(n-k) * fac(k) % c

print(tn * square(bn, c-2) % c)