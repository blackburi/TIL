# 소수의 연속합

import sys
input = sys.stdin.readline

n = int(input())

is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[1] = False

prime_num = []

for i in range(2, n+1) :
    if is_prime[i] :
        prime_num.append(i)
        for j in range(2*i, n+1, i) :
            is_prime[j] = False

ans = 0

start = 0
end = 0

while end <= len(prime_num) :
    tmp = sum(prime_num[start:end])
    if tmp == n :
        ans += 1
        end += 1
    elif tmp < n :
        end += 1
    else : # tmp > n
        start += 1

print(ans)