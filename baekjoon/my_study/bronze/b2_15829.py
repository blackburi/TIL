import sys
input = sys.stdin.readline

l = int(input())
alp = list(map(str, input()))
alp.pop()

hap = 0
for i in range(len(alp)) :
    hap += (ord(alp[i])-96) * (31**i)

print(hap%1234567891)