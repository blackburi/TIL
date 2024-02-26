import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
m = int(input())

cnt = lst.count(-1)
print(n-cnt)