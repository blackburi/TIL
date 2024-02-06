import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    n, m = map(int, input().split())

    ans = 1
    for i in range(n) :
        ans *= m-i
        ans //= i+1
    
    print(ans)
