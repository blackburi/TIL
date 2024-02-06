import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n) :
    lst.append(input())

ans = 0
im = set()
while lst :
    k = lst.pop(0)
    if k == 'ENTER\n' :
        ans += len(im)
        im = set()
    else :
        im.add(k)


ans += len(im)
print(ans)