_ = int(input())
_ = int(input())
lst = []
for _ in range(7) :
    lst.extend(list(map(int, input().strip())))

ans = []
for i in range(10) :
    tmp = 0
    for j in range(7) :
        tmp += lst[7*i+j] * (2**(6-j))
    ans.append(tmp)
print('#1', *ans)