# 수고르기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [int(input().rstrip()) for _ in range(n)]
numbers.sort()

left = 0
right = 0

ans = sys.maxsize

while True :
    if numbers[right] - numbers[left] == m :
        ans = m
        break
    elif numbers[right] - numbers[left] > m :
        ans = min(ans, numbers[right] - numbers[left])
        left += 1
    else : # numbers[right] - numbers[left] < m
        right += 1

    if right == n :
        break

print(ans)