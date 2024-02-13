n, m = map(int, input().split())

cuts = int(input())

row = [] # 행을 자르는 번호
col = [] # 열을 자르는 번호

for cut in range(cuts) :
    a, b = map(int, input().split())
    if a == 0 :
        row.append(b)
    else : # a == 1
        col.append(b)

row.sort()
col.sort()

row.insert(0, 0)
row.append(m)
col.insert(0, 0)
col.append(n)

rlen = []
clen = []

for i in range(len(row)-1) :
    rlen.append(row[i+1]-row[i])
for j in range(len(col)-1) :
    clen.append(col[j+1]-col[j])

print(max(rlen) * max(clen))