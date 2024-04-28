# 부분합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().rstrip().split()))

left = 0
right = 0
total = 0
length=1e9

while True:
    if total >= s:
        length = min(length, right-left)
        total -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        total += nums[right]
        right+=1

if length == 1e9:
    print(0)
else:
    print(length)