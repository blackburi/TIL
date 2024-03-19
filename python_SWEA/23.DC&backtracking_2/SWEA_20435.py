# 부분집합의 합

lst = list(map(int, input().rstrip().split()))
n = len(lst)

# 정답의 개수
cnt = 0

for i in range(1<<n) :
    hap = 0
    for j in range(n) :
        if i & (1<<j) :
            hap += lst[j]
    if hap == 0 :
        cnt += 1

print(cnt)