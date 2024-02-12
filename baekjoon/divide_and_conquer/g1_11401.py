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

"""
문제 해설
이 문제는 페르마 소정리와 모듈로 계산을 이용하여
조합 계산을 거듭제곱 계산으로 바꾸어 페르마 소정리를 이용하는 문제이다.

페르마의 소정리
p가 소수이면 모든 정수 a에 대해 a**p = a (mod p)
p가 소수이고 a가 p의 배수가 아니면 a**(p-1) = 1 (mod p)
                p의 배수라면 당연히 a**(p-1) = 0 (mod p)

이 문제에서 원하는 계산은 
(n!) / ((n-k)! * k!) 이다.

문제에서 주어진 p = 1,000,000,007 이고 소수이다.
n과 ksms 4,000,000 이하의 수이기 때문에 (n-k)! * k!은 p의배수가 될수 없다.
따라서 페르마 소정리를 사용할 수 있다.

페르마의 소정리에 의하여
(n-k)! * k! 은 p의 배수가 아니고 동시에 p가 소수이면
[ (n-k)! * k! ]**(p-1) = 1 (mod p) 가 된다.
p로 나눈 나머지가 1이기 때문에 어떤 식에 곱해도 p로 나눈 나머지가 변하지 않는다.
때문에 우리구 구하려던 (n!) / ((n-k)! * k!) 에 곱해도 무방하다.
기존 구하려던 식에 곱하여 정리를 하면
n! * [ (n-k)! * k! ]**(p-2) 가 된다. 이것을 p로 나눈 나머지를 구해야 하므로
위 풀이에서 tn * square(bn, c-2) % c 처럼 된다.
"""