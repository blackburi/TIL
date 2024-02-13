# 파이썬은 내부적으로 연산과 메모리를 관리하기 때문에
# 파이썬에 내장되어있는 함수들을 적용할수록
# 메모리를 효율적으로 관리할 수 있다고 한다.

import sys

n = int(sys.stdin.readline())

num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)