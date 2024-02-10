import sys
input = sys.stdin.readline

n = int(input())
RGB = []
for _ in range(n) :
    a, b, c = map(int, input().split())
    RGB.append([a, b, c])

print(RGB)