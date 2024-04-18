# 숫자의 신

import sys
input = sys.stdin.readline

# k개의 수중 n개를 뽑아 사용
k, n = map(int, input().split())

# 모든수를 1번 이상 사용
# 추가로 더 사용하는 수는 무조건 1개

# str(x)*10 으로 배열하는 이유
# 자릿수가 많은 순서 > 동일하다면 큰 순서, 10**9까지
# 즉 큰 숫자만 추가로 사용

numbers = [int(input().rstrip()) for _ in range(k)]

answer = ''
M = max(numbers)

for _ in range(n-k) :
    numbers.append(M)

numbers.sort(key = lambda x : str(x)*10, reverse = True)

for i in range(len(numbers)) :
    numbers[i] = str(numbers[i])

print(int(''.join(numbers)))