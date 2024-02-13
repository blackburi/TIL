## 태완풀이
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

## 광영 풀이 - 수정 필요
def dfs(idx: int, total: int) -> None:
    global result
 
    if total + nums[idx] > 10 :
        return
    elif total + nums[idx] == 10 :
        result += 1
        return
 
    for i in range(idx + 1, 10) :
        dfs(i, total + nums[idx])

nums = list(range(1, 11))
result = 0
dfs(0, 0)
print(f'#1 {result}')