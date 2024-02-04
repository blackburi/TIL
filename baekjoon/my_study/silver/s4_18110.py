import sys
input = sys.stdin.readline

n = int(input())
op = [int(input()) for _ in range(n)]

if n == 0 :
    print(0)

else :
    if (n*15/100) - (n*15//100) >= 0.5 :
        los = n*15//100 + 1
    else :
        los = n*15//100

    op.sort()
    hap = 0
    for k in range(los, n-los) :
        hap += op[k]

    if hap/(n - 2*los) - hap//(n - 2*los) >= 0.5 :
        avg = hap//(n - 2*los) + 1
    else :
        avg = hap//(n - 2*los)

    print(avg)