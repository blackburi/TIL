import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

# 산술평균
hap = 0
for i in num:
    hap += i
if hap / n - hap//n >= 0.5:
    print(hap//n + 1)
else : # hap/n = hap//n < 0.5
    print(hap//n)

# 중앙값
num.sort()
print(num[n//2])

# 최빈값
dic = {}
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1




# 범위
print(num[-1] - num[0])