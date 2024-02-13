import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0] + lst

for i in range(n) :
    lst[i+1] += lst[i]
    
for _ in range(m) :
    a, b = map(int, input().split())
    print(lst[b] - lst[a-1])