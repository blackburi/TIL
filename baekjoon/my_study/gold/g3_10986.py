import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

# m으로 나눈 나머지가 같은 것끼리 담는 list
rest = [0] * m
hap = 0
for i in range(n) :
    hap += lst[i]
    rest[hap%m] += 1

# m으로 나눈 나머지가 0인 곳
ans = rest[0]

# m으로 나눈 나머지가 같다면 그 두 수를 빼면 m의 배수가 된다.
for j in range(m) :
    ans += rest[j] * (rest[j]-1)//2

print(ans)