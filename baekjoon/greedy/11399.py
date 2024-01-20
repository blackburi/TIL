# ATM

T = int(input())

time = list(map(int, input().split()))
time.sort()

ans = 0

for i in range(T) :
    j = (T-i) * time[i]
    ans += j

print(ans)