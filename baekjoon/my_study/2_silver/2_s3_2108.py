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
for i in num :
    if i in dic:
        dic[i] += 1
    else : # i not in dic
        dic[i] = 1
mx = max(dic.values()) # 제일 작은 최빈값

mx_lst = [] # 최빈값들을 저장할 배열

for i in dic :
    if mx == dic[i] :
        mx_lst.append(i)

if len(mx_lst) >= 2 :
    print(mx_lst[1])
else : # len(mx_lst) == 1
    print(mx_lst[0])


# 범위
print(num[-1] - num[0])