import sys

input = sys.stdin.readline

N = int(input())

num = [int(input()) for _ in range(N)]

num.sort()

for i in num :
    print(i)