# bit 풀이
lst = [i for i in range(1, 11)]
n = len(lst)
count = 0
for i in range(1 << n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += lst[j]
            if 10 < total:
                break
    if total == 10:
        count += 1
print(f"#{1} {count}")

# 재귀 풀이
arr = list(map(int,input().split()))
N = len(arr)
c = [0]*N
ans = []
cnt = 0
def powerset(idx):
    global cnt
    s = 0
    if idx == N:
        for i in range(N):
            if c[i]:
                s += arr[i]
            if s>10:
                break
        if s == 10:
            cnt +=1
        return
    c[idx] = 0
    powerset(idx+1)
    c[idx] = 1
    powerset(idx+1)
powerset(0)
print(f'#1 {cnt}')