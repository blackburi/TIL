# 바이러스

import sys
input = sys.stdin.readline

# 초기 바이러스 수, 증가율, 총 시간
k, p, n = map(int, input().split())
c = 1000000007

# a**b % c를 계산하는 과정
def square(a, b) :
    global c

    if b == 0 :
        return 1
    if b == 1 :
        return a % c
    
    tmp = square(a, b//2)
    if b % 2 == 0 :
        return tmp * tmp % c
    else : # b % 2 == 1
        return tmp * tmp * a % c

print(k * square(p, n) % c)