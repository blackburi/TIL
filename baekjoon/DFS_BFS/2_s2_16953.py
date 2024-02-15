import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 0

while a < b :
    if b % 10 == 1 :
        b = (b-1)//10
        cnt += 1
    elif b % 2 == 0 :
        b //= 2
        cnt += 1
    else :
        break

    if a == b :
        break

if a == b :
    print(cnt+1)
else :
    print(-1)
