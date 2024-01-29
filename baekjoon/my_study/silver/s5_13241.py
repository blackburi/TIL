A, B = list(map(int, input().split()))
M = A*B

# 최대공약수 (유클리드 호제법)
while B: # B > 0 이면 계속 돌아간다.
    if A > B:
        A, B = B, A
    B %= A

# 최소공배수
print(M//A)