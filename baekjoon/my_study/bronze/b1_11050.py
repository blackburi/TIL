n, k = map(int, input().split())

ans = 1
for i in range(k) :
    ans = ans * (n-i) // (i+1)

print(ans)