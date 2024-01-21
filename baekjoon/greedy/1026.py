# 보물

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0

for i in range(N) :
    total += max(B) * min(A)
    del A[A.index(min(A))]
    del B[B.index(max(B))]

print(total)