import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

ears = {input().rstrip() for _ in range(N)}
eyes = {input().rstrip() for _ in range(M)}

shares = list(ears & eyes)
shares.sort()

print(len(shares))
for share in shares :
    print(share)