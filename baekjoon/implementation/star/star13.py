n = int(input())

for i in range(1, n):
    print('*'*i)

for i in range(1, n+1):
    print('*'*(n-i+1))