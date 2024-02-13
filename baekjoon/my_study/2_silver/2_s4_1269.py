import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = list((A-B)|(B-A))
print(len(C))