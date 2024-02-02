mat = [[0]*100 for _ in range(100)]

papers = int(input())

for paper in range(papers) :
    a, b = map(int, input().split())

    for i in range(a, a+10) :
        for j in range(b, b+10) :
            mat[i][j] = 1

hap = 0
for k in range(100) :
    hap += sum(mat[k])

print(hap)