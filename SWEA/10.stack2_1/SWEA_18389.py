T = int(input())

lst = list(map(str, input().rstrip()))
num_lst = [str(i) for i in range(10)]
stack = []
ans = []

while lst :
    a = lst.pop(0)
    if a in num_lst :
        ans.append(a)
    else :
        stack.append(a)
    
while stack :
    a = stack.pop()
    ans.append(a)

print(f'#{T} {"".join(ans)}')